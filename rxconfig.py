import reflex as rx
import reflex.plugins

config = rx.Config(
    app_name="app",
    show_built_with_reflex=False,
    tailwind={
        "theme": {
            "extend": {
                "keyframes": {
                    "fade-in-up": {
                        "0%": {
                            "opacity": "0",
                            "transform": "translateY(10px)",
                        },
                        "100%": {
                            "opacity": "1",
                            "transform": "translateY(0)",
                        },
                    },
                },
                "animation": {
                    "fade-in-up": "fade-in-up 0.5s ease-out",
                },
            },
        },
    },
    plugins=[
        rx.plugins.TailwindV3Plugin(),
    ],
)
