/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useEffect, useRef } from "react"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getRefValue, getRefValues, isTrue, refs } from "$/utils/state"
import { Scissors as LucideScissors } from "lucide-react"
import dynamic from "next/dynamic"
import { Button_6a57e89901a48b4d802108bdfb9233d9, Button_70a48297308ae33ca05188f23feac1ce, H3_08c94965a27fedb77161ab9bac7c626a } from "$/utils/stateful_components"
import NextHead from "next/head"
import { jsx } from "@emotion/react"

const Moment = dynamic(() => import('react-moment'), { ssr: false });


export function Form_947475c16c2f1bcad0584eb47b16e17b () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  
    const handleSubmit_080fb55a1df69d4eb75550ec4a8ad961 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({ ["service"] : getRefValue(refs["ref_service"]), ["name"] : getRefValue(refs["ref_name"]), ["phone"] : getRefValue(refs["ref_phone"]) })};

        (((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.prepare_appointment", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))(ev));

        if (false) {
            $form.reset()
        }
    })
    




  
  return (
    jsx(
"form",
{className:"w-full",onSubmit:handleSubmit_080fb55a1df69d4eb75550ec4a8ad961},
jsx(
"div",
{className:"flex flex-col items-center gap-4"},
jsx(
"div",
{className:"flex flex-col items-center gap-4 w-full"},
jsx(
"div",
{className:"w-full"},
jsx(
"div",
{className:"flex items-center justify-between mb-4"},
jsx(Button_70a48297308ae33ca05188f23feac1ce,{},)
,jsx(H3_08c94965a27fedb77161ab9bac7c626a,{},)
,jsx(Button_6a57e89901a48b4d802108bdfb9233d9,{},)
,),jsx(Div_0072e4fa7138b7927d6fdfa3dc22d569,{},)
,jsx(Div_f6452c0de795713433d89c19ead44429,{},)
,),jsx(Fragment_16f25570cb608cb95df76df26c5d52f4,{},)
,jsx(Fragment_0efb89bdb9c73df4b99f135c7c50ad00,{},)
,),jsx(Fragment_02a4e52655751d9e0076cbb2fec4bee4,{},)
,),)
  )
}

export function Div_d2e486d82860f014cc592457f74d5e41 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_dcc1792dd4de10b5282c28ad24a9a3f5 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.cancel_confirmation", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx("div",{className:"fixed inset-0 z-40 bg-black/60 backdrop-blur-sm",onClick:on_click_dcc1792dd4de10b5282c28ad24a9a3f5},)

  )
}

export function P_54d5acd980c8ad364bfb31e9b7eff274 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Fecha: "
,),reflex___state____state__app___states___state____barber_state.selected_date
,)
  )
}

export function P_9c2917450345670fdbc01395723cbed1 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Servicio: "
,),(isTrue(reflex___state____state__app___states___state____barber_state.pending_appointment_data["service"]) ? reflex___state____state__app___states___state____barber_state.pending_appointment_data["service"] : "")
,)
  )
}

export function P_814e44555c2acaf525fcf967e74d5641 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Nombre: "
,),(isTrue(reflex___state____state__app___states___state____barber_state.pending_appointment_data["name"]) ? reflex___state____state__app___states___state____barber_state.pending_appointment_data["name"] : "")
,)
  )
}

export function Button_769511a1f448185b2b51f0ac8ce0dbdb () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_dcc1792dd4de10b5282c28ad24a9a3f5 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.cancel_confirmation", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
"button",
{className:"w-full sm:w-auto px-6 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 font-medium transition-colors",onClick:on_click_dcc1792dd4de10b5282c28ad24a9a3f5,type:"button"},
"Cancelar"
,)
  )
}

export function Fragment_02a4e52655751d9e0076cbb2fec4bee4 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)
  const ref_name = useRef(null); refs["ref_name"] = ref_name;
  const ref_phone = useRef(null); refs["ref_phone"] = ref_phone;





  
  return (
    jsx(
Fragment,
{},
(!((reflex___state____state__app___states___state____barber_state.selected_time === "")) ? (jsx(
Fragment,
{},
jsx(
"div",
{className:"flex flex-col items-center gap-4 w-full"},
jsx("div",{className:"w-full border-t border-gray-200 my-6"},)
,jsx(
"div",
{className:"w-full"},
jsx(
"label",
{className:"block text-sm font-medium text-gray-700 mb-1",htmlFor:"name"},
"Nombre Completo"
,),jsx("input",{className:"w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors",id:"name",name:"name",placeholder:"Ej: Juan P\u00e9rez",ref:ref_name,required:true,type:"text"},)
,),jsx(
"div",
{className:"w-full"},
jsx(
"label",
{className:"block text-sm font-medium text-gray-700 mb-1",htmlFor:"phone"},
"N\u00famero de Tel\u00e9fono"
,),jsx("input",{className:"w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors",id:"phone",name:"phone",placeholder:"Ej: 55 1234 5678",ref:ref_phone,required:true,type:"tel"},)
,),jsx(
"div",
{className:"w-full"},
jsx(
"label",
{className:"block text-sm font-medium text-gray-700 mb-1",htmlFor:"service"},
"Servicio"
,),jsx(Select_6f70bacbcef8cc0e95f57d8d3367477a,{},)
,),jsx(
"button",
{className:"w-full mt-4 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-all duration-200 shadow-md hover:shadow-lg",type:"submit"},
"Agendar Cita"
,),),)) : (jsx(
Fragment,
{},
jsx("div",{},)
,))),)
  )
}

export function Select_bd4fc43e270e8d05b25567de0e8c4ea5 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_2e534a2a815c0cdc92f62a874cb81338 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.select_barber", ({ ["barber"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(
"select",
{className:"w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors appearance-none bg-white",onChange:on_change_2e534a2a815c0cdc92f62a874cb81338,value:reflex___state____state__app___states___state____barber_state.selected_barber},
jsx(
"option",
{disabled:true,value:""},
"Seleccione un barbero"
,),reflex___state____state__app___states___state____barber_state.barber_names.map((barber,index_64f308f653c72d07)=>(jsx(
"option",
{key:index_64f308f653c72d07,value:barber},
barber
,))),)
  )
}

export function Fragment_0efb89bdb9c73df4b99f135c7c50ad00 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
Fragment,
{},
((!((reflex___state____state__app___states___state____barber_state.selected_date === "")) && !((reflex___state____state__app___states___state____barber_state.selected_barber === ""))) ? (jsx(
Fragment,
{},
jsx(
"div",
{className:"w-full mt-6"},
jsx(H4_0933c81deb74f5d9071d8c05eac30e3c,{},)
,jsx(Fragment_4b500c48a4d4fd4049414ec387cc7c5e,{},)
,),)) : (jsx(Fragment,{},)
)),)
  )
}

export function Fragment_16f25570cb608cb95df76df26c5d52f4 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
Fragment,
{},
((!((reflex___state____state__app___states___state____barber_state.selected_date === "")) && (reflex___state____state__app___states___state____barber_state.barbers.length > 0)) ? (jsx(
Fragment,
{},
jsx(
"div",
{className:"w-full mt-6"},
jsx(H4_e9256af9d5b93f9ab19e8cc332d5511a,{},)
,jsx(Select_bd4fc43e270e8d05b25567de0e8c4ea5,{},)
,),)) : (jsx(Fragment,{},)
)),)
  )
}

export function H4_0933c81deb74f5d9071d8c05eac30e3c () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"h4",
{className:"font-semibold mb-4 text-center text-gray-700"},
("Horas disponibles para "+reflex___state____state__app___states___state____barber_state.selected_barber+" el "+reflex___state____state__app___states___state____barber_state.selected_date)
,)
  )
}

export function Fragment_4b500c48a4d4fd4049414ec387cc7c5e () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
Fragment,
{},
((reflex___state____state__app___states___state____barber_state.available_times_for_selected_date_and_barber.length > 0) ? (jsx(
Fragment,
{},
jsx(Div_1d80c3ba44564d801ce31837bca91238,{},)
,)) : (jsx(
Fragment,
{},
jsx(
"p",
{className:"text-center text-gray-500 py-4"},
"No hay horas disponibles para este barbero en este d\u00eda."
,),))),)
  )
}

export function Moment_23fe52bfdb221d5a61736ac9175a03ab () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
Moment,
{format:"hh:mm A",parse:"HH:mm"},
reflex___state____state__app___states___state____barber_state.selected_time
,)
  )
}

export function P_429a745b4f63ac9aec7fd69d06b7c16d () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Barbero: "
,),reflex___state____state__app___states___state____barber_state.selected_barber
,)
  )
}

export function Fragment_8c7d8c8828b78424b344dec021c42149 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__app___states___state____barber_state.show_confirm_dialog ? (jsx(
Fragment,
{},
jsx(
"div",
{},
jsx(
"div",
{className:"fixed inset-0 z-50 flex items-center justify-center p-4"},
jsx(
"div",
{className:"bg-white p-8 rounded-2xl shadow-2xl max-w-md w-full m-4"},
jsx(
"h3",
{className:"text-xl font-semibold text-gray-900"},
"Confirmar Cita"
,),jsx(
"p",
{className:"text-sm text-gray-500 mt-1"},
"Por favor, revise los detalles de su cita antes de confirmar."
,),jsx("div",{className:"my-4 border-t border-gray-200"},)
,jsx(
"div",
{className:"flex flex-col gap-2 my-4 text-base text-gray-700"},
jsx(P_814e44555c2acaf525fcf967e74d5641,{},)
,jsx(P_89827b1f1fa89224ea6c6856c35b8b6f,{},)
,jsx(P_9c2917450345670fdbc01395723cbed1,{},)
,jsx(P_429a745b4f63ac9aec7fd69d06b7c16d,{},)
,jsx(P_54d5acd980c8ad364bfb31e9b7eff274,{},)
,jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Hora: "
,),jsx(Moment_23fe52bfdb221d5a61736ac9175a03ab,{},)
,),),jsx(
"div",
{className:"flex flex-col sm:flex-row justify-end gap-3 mt-6"},
jsx(Button_769511a1f448185b2b51f0ac8ce0dbdb,{},)
,jsx(Button_5ad5e9158de854a0556d292f1405e701,{},)
,),),),jsx(Div_d2e486d82860f014cc592457f74d5e41,{},)
,),)) : (jsx(Fragment,{},)
)),)
  )
}

export function P_89827b1f1fa89224ea6c6856c35b8b6f () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"p",
{},
jsx(
"span",
{className:"font-semibold"},
"Tel\u00e9fono: "
,),(isTrue(reflex___state____state__app___states___state____barber_state.pending_appointment_data["phone"]) ? reflex___state____state__app___states___state____barber_state.pending_appointment_data["phone"] : "")
,)
  )
}

export function Main_6fa438345f7fb4260817e924d3da2fe9 () {
  
  
                useEffect(() => {
                    ((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.load_data", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    jsx(
"main",
{className:"min-h-screen bg-gray-50 font-['Inter']"},
jsx(
"div",
{className:"container mx-auto flex flex-col items-center p-4 md:p-8"},
jsx(
"div",
{className:"text-center mb-10"},
jsx(
"div",
{className:"flex items-center gap-4"},
jsx(LucideScissors,{className:"h-10 w-10 text-blue-600"},)
,jsx(
"h1",
{className:"text-4xl font-extrabold tracking-tight text-gray-800"},
"Chentes Barber"
,),),jsx(
"p",
{className:"text-lg text-gray-600 mt-2"},
"Agenda tu cita de forma r\u00e1pida y sencilla."
,),),jsx(
"div",
{className:"bg-white p-8 rounded-2xl shadow-lg border border-gray-100 w-full max-w-lg"},
jsx(Fragment_8c7d8c8828b78424b344dec021c42149,{},)
,jsx(
"h2",
{className:"text-2xl font-bold text-gray-800 mb-6 text-center"},
"Agendar Nueva Cita"
,),jsx(Form_947475c16c2f1bcad0584eb47b16e17b,{},)
,),jsx(
"div",
{className:"w-full max-w-3xl mt-8 text-center"},
jsx(
"p",
{className:"text-sm text-gray-500"},
"Para cancelaciones, contactar a 54214040"
,),),),)
  )
}

export function Div_f6452c0de795713433d89c19ead44429 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    jsx(
"div",
{className:"flex flex-col gap-2"},
reflex___state____state__app___states___state____barber_state.calendar_weeks.map((week,index_45b6d23e4a4b8137)=>(jsx(
"div",
{className:"grid grid-cols-7 gap-2",key:index_45b6d23e4a4b8137},
week.map((day_data,index_e8ad7448170be962)=>(jsx(
Fragment,
{key:index_e8ad7448170be962},
(isTrue(day_data["is_in_month"]) ? (jsx(
Fragment,
{},
jsx(
"button",
{className:(isTrue(day_data["is_disabled"]) ? "p-2 rounded-full w-10 h-10 flex items-center justify-center text-gray-300 cursor-not-allowed" : (isTrue(day_data["is_selected"]) ? "p-2 rounded-full bg-blue-600 text-white w-10 h-10 flex items-center justify-center font-bold shadow-lg" : (isTrue(day_data["is_today"]) ? "p-2 rounded-full bg-blue-100 text-blue-600 w-10 h-10 flex items-center justify-center font-semibold" : "p-2 rounded-full hover:bg-gray-100 w-10 h-10 flex items-center justify-center transition-colors"))),disabled:day_data["is_disabled"],onClick:((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.select_date", ({ ["date_str"] : day_data["date_str"] }), ({  })))], args, ({  })))),type:"button"},
day_data["day"]
,),)) : (jsx(
Fragment,
{},
jsx("div",{className:"p-2 w-10 h-10"},)
,))),))),))),)
  )
}

export function Div_0072e4fa7138b7927d6fdfa3dc22d569 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"div",
{className:"grid grid-cols-7 gap-2 mb-2"},
reflex___state____state__app___states___state____barber_state.week_days.map((day,index_0a500f136e0987ee)=>(jsx(
"div",
{className:"text-center font-medium text-sm text-gray-500",key:index_0a500f136e0987ee},
day
,))),)
  )
}

export function Button_5ad5e9158de854a0556d292f1405e701 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_2a8647827e3769f51c5c739cde744ad4 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.confirm_appointment", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
"button",
{className:"w-full sm:w-auto px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors",onClick:on_click_2a8647827e3769f51c5c739cde744ad4,type:"button"},
"Confirmar Cita"
,)
  )
}

export function H4_e9256af9d5b93f9ab19e8cc332d5511a () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"h4",
{className:"font-semibold mb-4 text-center text-gray-700"},
("Seleccione un barbero para "+reflex___state____state__app___states___state____barber_state.selected_date)
,)
  )
}

export function Select_6f70bacbcef8cc0e95f57d8d3367477a () {
  
  const ref_service = useRef(null); refs["ref_service"] = ref_service;
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)





  
  return (
    jsx(
"select",
{className:"w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors appearance-none bg-white",id:"service",name:"service",ref:ref_service,required:true},
reflex___state____state__app___states___state____barber_state.services.map((service,index_dfbaf238706d1704)=>(jsx(
"option",
{key:index_dfbaf238706d1704,value:service["name"]},
(service["name"]+" - $"+service["price"])
,))),)
  )
}

export function Div_1d80c3ba44564d801ce31837bca91238 () {
  
  const reflex___state____state__app___states___state____barber_state = useContext(StateContexts.reflex___state____state__app___states___state____barber_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    jsx(
"div",
{className:"grid grid-cols-3 sm:grid-cols-4 gap-3"},
reflex___state____state__app___states___state____barber_state.available_times_for_selected_date_and_barber.map((time,index_0d959a9b3eeccda4)=>(jsx(
"button",
{className:((reflex___state____state__app___states___state____barber_state.selected_time === time) ? "w-full py-2 px-4 rounded-lg bg-blue-600 text-white font-semibold shadow-md" : "w-full py-2 px-4 rounded-lg bg-gray-100 hover:bg-blue-100 text-gray-800 font-medium transition-colors"),key:index_0d959a9b3eeccda4,onClick:((...args) => (addEvents([(Event("reflex___state____state.app___states___state____barber_state.select_time", ({ ["time_str"] : time }), ({  })))], args, ({  })))),type:"button"},
jsx(
Moment,
{format:"hh:mm A",parse:"HH:mm"},
time
,),))),)
  )
}

export default function Component() {
    




  return (
    jsx(
Fragment,
{},
jsx(Main_6fa438345f7fb4260817e924d3da2fe9,{},)
,jsx(
NextHead,
{},
jsx(
"title",
{},
"Chentes Barber"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,),)
  )
}
