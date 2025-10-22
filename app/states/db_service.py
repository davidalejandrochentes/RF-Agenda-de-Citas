import reflex as rx
import sqlite3
import os
from typing import TypedDict, List, Optional
import uuid
import datetime


class Appointment(TypedDict):
    id: str
    name: str
    last_name: str
    phone: str
    date: str
    time: str
    services: List[str]  # Changed from service: str
    barber: str
    booking_code: str


class Barber(TypedDict):
    id: str
    name: str


class Service(TypedDict):
    id: str
    name: str
    price: int


def get_db_path() -> str:
    return "app/states/app.db"


def get_db_connection() -> sqlite3.Connection:
    """Establishes a connection to the SQLite database."""
    db_path = get_db_path()
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    # Drop service column from appointments if it exists (for migration)
    try:
        cursor.execute("ALTER TABLE appointments DROP COLUMN service")
    except sqlite3.OperationalError:
        # Column doesn't exist, which is fine for new setups
        pass
    
    # Add last_name column if it doesn't exist (for migration)
    try:
        cursor.execute("ALTER TABLE appointments ADD COLUMN last_name TEXT NOT NULL DEFAULT ''")
    except sqlite3.OperationalError:
        # Column already exists
        pass


    # Add booking_code column if it doesn't exist (for migration)
    try:
        cursor.execute("ALTER TABLE appointments ADD COLUMN booking_code TEXT NOT NULL DEFAULT ''")
    except sqlite3.OperationalError:
        # Column already exists
        pass

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS appointments (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            barber TEXT NOT NULL,
            booking_code TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS barbers (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS services (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS barber_availability (
            id TEXT PRIMARY KEY,
            barber_id TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (barber_id) REFERENCES barbers (id) ON DELETE CASCADE,
            UNIQUE (barber_id, date, time)
        )
        """
    )
    # New table for many-to-many relationship between appointments and services
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS appointment_services (
            id TEXT PRIMARY KEY,
            appointment_id TEXT NOT NULL,
            service_name TEXT NOT NULL,
            FOREIGN KEY (appointment_id) REFERENCES appointments (id) ON DELETE CASCADE
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_appointments() -> list[Appointment]:
    conn = get_db_connection()
    cursor = conn.cursor()
    # Get all appointments
    cursor.execute("SELECT * FROM appointments")
    appointments_rows = cursor.fetchall()
    
    appointments_dict = {row["id"]: dict(row) for row in appointments_rows}
    for app_id in appointments_dict:
        appointments_dict[app_id]['services'] = []

    # Get all service associations
    cursor.execute("""
        SELECT appointment_id, service_name 
        FROM appointment_services
    """)
    services_rows = cursor.fetchall()
    
    for row in services_rows:
        app_id = row['appointment_id']
        if app_id in appointments_dict:
            appointments_dict[app_id]['services'].append(row['service_name'])

    conn.close()
    return [Appointment(**app_data) for app_data in appointments_dict.values()]


def add_appointment_db(appointment: Appointment):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN")
        # Insert into appointments table
        cursor.execute(
            "INSERT INTO appointments (id, name, last_name, phone, date, time, barber, booking_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                appointment["id"],
                appointment["name"],
                appointment["last_name"],
                appointment["phone"],
                appointment["date"],
                appointment["time"],
                appointment["barber"],
                appointment["booking_code"],
            ),
        )
        # Insert into appointment_services table for each service
        for service_name in appointment["services"]:
            cursor.execute(
                "INSERT INTO appointment_services (id, appointment_id, service_name) VALUES (?, ?, ?)",
                (str(uuid.uuid4()), appointment["id"], service_name),
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Database error in add_appointment_db: {e}")
    finally:
        conn.close()


def delete_appointment_db(appointment_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    # The ON DELETE CASCADE foreign key will handle deleting from appointment_services
    cursor.execute(
        "DELETE FROM appointments WHERE id = ?",
        (appointment_id,),
    )
    conn.commit()
    conn.close()


def get_appointment_by_code(code: str) -> Optional[Appointment]:
    """Fetches a single appointment by its unique booking code."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE booking_code = ?", (code,))
    appointment_row = cursor.fetchone()

    if not appointment_row:
        conn.close()
        return None

    appointment_dict = dict(appointment_row)
    appointment_dict['services'] = []

    # Get associated services
    cursor.execute(
        "SELECT service_name FROM appointment_services WHERE appointment_id = ?",
        (appointment_dict["id"],),
    )
    services_rows = cursor.fetchall()
    for row in services_rows:
        appointment_dict['services'].append(row['service_name'])

    conn.close()
    return Appointment(**appointment_dict)


def get_all_barbers() -> list[Barber]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barbers ORDER BY name")
    rows = cursor.fetchall()
    conn.close()
    return [Barber(**dict(row)) for row in rows]


def add_barber_db(barber: Barber):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO barbers (id, name) VALUES (?, ?)",
        (barber["id"], barber["name"]),
    )
    conn.commit()
    conn.close()


def update_barber_db(barber_id: str, new_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE barbers SET name = ? WHERE id = ?",
        (new_name, barber_id),
    )
    conn.commit()
    conn.close()


def delete_barber_db(barber_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM barbers WHERE id = ?", (barber_id,)
    )
    conn.commit()
    conn.close()


def get_all_services() -> list[Service]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM services ORDER BY name")
    rows = cursor.fetchall()
    conn.close()
    return [Service(**dict(row)) for row in rows]


def add_service_db(service: Service):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO services (id, name, price) VALUES (?, ?, ?)",
        (service["id"], service["name"], service["price"]),
    )
    conn.commit()
    conn.close()


def update_service_db(
    service_id: str, new_name: str, new_price: int
):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE services SET name = ?, price = ? WHERE id = ?",
        (new_name, new_price, service_id),
    )
    conn.commit()
    conn.close()


def delete_service_db(service_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM services WHERE id = ?", (service_id,)
    )
    conn.commit()
    conn.close()


def get_availability_for_barber(
    barber_id: str, date: str
) -> list[str]:
    """Fetches the available time slots for a specific barber on a specific date."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT time FROM barber_availability WHERE barber_id = ? AND date = ? ORDER BY time",
        (barber_id, date),
    )
    rows = cursor.fetchall()
    conn.close()
    return [row["time"] for row in rows]


def set_availability_for_barber(
    barber_id: str, date: str, times: list[str]
):
    """Sets the available time slots for a barber on a date, overwriting existing ones."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN")
        cursor.execute(
            "DELETE FROM barber_availability WHERE barber_id = ? AND date = ?",
            (barber_id, date),
        )
        for time in times:
            cursor.execute(
                "INSERT INTO barber_availability (id, barber_id, date, time) VALUES (?, ?, ?, ?)",
                (str(uuid.uuid4()), barber_id, date, time),
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Database error: {e}")
    finally:
        conn.close()

def get_all_available_dates() -> list[str]:
    """Fetches all unique dates that have at least one availability slot."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT date FROM barber_availability")
    rows = cursor.fetchall()
    conn.close()
    return [row["date"] for row in rows]


def delete_past_availability_db():
    """Deletes barber availability records for dates that have already passed."""
    conn = get_db_connection()
    cursor = conn.cursor()
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    try:
        cursor.execute(
            "DELETE FROM barber_availability WHERE date < ?", (today_str,)
        )
        conn.commit()
    except Exception as e:
        print(f"Database error in delete_past_availability_db: {e}")
    finally:
        conn.close()
