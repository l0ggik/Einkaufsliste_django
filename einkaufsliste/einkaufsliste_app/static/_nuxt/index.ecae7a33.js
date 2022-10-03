import{p as R,q as O,s as E,e as H,v as L,u as y,x as S,y as W,k as P,z as B,b as V,r as c,o as g,f as M,h as o,w as r,m as D,t as i,l as v,F as I,i as N,c as U,j as q,a as K,A as Q,B as J}from"./entry.7bd964ca.js";const Z=()=>null;function G(...u){var d,p,x,k,F,_,Y,A,T;const a=typeof u[u.length-1]=="string"?u.pop():void 0;typeof u[0]!="string"&&u.unshift(a);let[n,l,e={}]=u;if(typeof n!="string")throw new TypeError("[nuxt] [asyncData] key must be a string.");if(typeof l!="function")throw new TypeError("[nuxt] [asyncData] handler must be a function.");e.server=(d=e.server)!=null?d:!0,e.default=(p=e.default)!=null?p:Z,e.defer&&console.warn("[useAsyncData] `defer` has been renamed to `lazy`. Support for `defer` will be removed in RC."),e.lazy=(k=(x=e.lazy)!=null?x:e.defer)!=null?k:!1,e.initialCache=(F=e.initialCache)!=null?F:!0,e.immediate=(_=e.immediate)!=null?_:!0;const t=R(),f=()=>(t.isHydrating||e.initialCache)&&t.payload.data[n]!==void 0;t._asyncData[n]||(t._asyncData[n]={data:O(f()?t.payload.data[n]:(A=(Y=e.default)==null?void 0:Y.call(e))!=null?A:null),pending:O(!f()),error:O((T=t.payload._errors[n])!=null?T:null)});const s={...t._asyncData[n]};s.refresh=s.execute=($={})=>t._asyncDataPromises[n]?t._asyncDataPromises[n]:$._initial&&f()?t.payload.data[n]:(s.pending.value=!0,t._asyncDataPromises[n]=new Promise((C,w)=>{try{C(l(t))}catch(j){w(j)}}).then(C=>{e.transform&&(C=e.transform(C)),e.pick&&(C=X(C,e.pick)),s.data.value=C,s.error.value=null}).catch(C=>{var w,j;s.error.value=C,s.data.value=y((j=(w=e.default)==null?void 0:w.call(e))!=null?j:null)}).finally(()=>{s.pending.value=!1,t.payload.data[n]=s.data.value,s.error.value&&(t.payload._errors[n]=!0),delete t._asyncDataPromises[n]}),t._asyncDataPromises[n]);const h=()=>s.refresh({_initial:!0}),m=e.server!==!1&&t.payload.serverRendered;{const $=S();if($&&!$._nuxtOnBeforeMountCbs){$._nuxtOnBeforeMountCbs=[];const w=$._nuxtOnBeforeMountCbs;$&&(E(()=>{w.forEach(j=>{j()}),w.splice(0,w.length)}),H(()=>w.splice(0,w.length)))}m&&t.isHydrating&&n in t.payload.data?s.pending.value=!1:$&&(t.payload.serverRendered&&t.isHydrating||e.lazy)&&e.immediate?$._nuxtOnBeforeMountCbs.push(h):e.immediate&&h(),e.watch&&L(e.watch,()=>s.refresh());const C=t.hook("app:data:refresh",w=>{if(!w||w.includes(n))return s.refresh()});$&&H(C)}const b=Promise.resolve(t._asyncDataPromises[n]).then(()=>s);return Object.assign(b,s),b}function X(u,a){const n={};for(const l of a)n[l]=u[l];return n}function z(u,a,n){const[l={},e]=typeof a=="string"?[{},a]:[a,n],t=l.key||e;if(!t||typeof t!="string")throw new TypeError("[nuxt] [useFetch] key must be a string: "+t);if(!u)throw new Error("[nuxt] [useFetch] request is missing.");const f="$f"+t,s=W(()=>{let T=u;return typeof T=="function"&&(T=T()),P(T)?T.value:T}),{server:h,lazy:m,default:b,transform:d,pick:p,watch:x,initialCache:k,...F}=l,_={...F,cache:typeof l.cache=="boolean"?void 0:l.cache},Y={server:h,lazy:m,default:b,transform:d,pick:p,initialCache:k,watch:[s,...x||[]]};return G(f,()=>$fetch(s.value,_),Y)}const ee={__name:"weatherCard",async setup(u){let a,n;const l="https://loggik.pythonanywhere.com/api/",{data:e,pending:t,refresh:f,error:s}=([a,n]=B(()=>z(l+"wetter/","$t8CiJ3sCbM")),a=await a,n(),a);V(async()=>{await h()});async function h(){setInterval(async function(){await f()},6e4)}return(m,b)=>{const d=c("v-card-title"),p=c("v-card-text"),x=c("v-card");return g(),M("div",null,[o(x,{elevation:"0","max-height":"400",class:"overflow-auto"},{default:r(()=>[o(d,null,{default:r(()=>[D(i(m.$dayjs(y(e).weather_date).format("dddd, DD.MM.YYYY")),1)]),_:1}),o(p,null,{default:r(()=>[v("p",null,[v("strong",null,i(y(e).description)+",",1),D(" Temperatur: "+i((y(e).temperature-273.15).toFixed(1))+"\xB0C, Min: "+i((y(e).temperature_max-273.15).toFixed(1))+"\xB0C / Max: "+i((y(e).temperature_min-273.15).toFixed(1))+"\xB0C, Bew\xF6lkung: "+i(y(e).clouds)+"%",1)])]),_:1})]),_:1})])}}},te={key:0},ne={__name:"weatherForecastTomorrow",async setup(u){let a,n;const l="https://loggik.pythonanywhere.com/api/",{data:e,pending:t,refresh:f,error:s}=([a,n]=B(()=>z(l+"wetter/wetter_morgen/","$NZL2StQsmI")),a=await a,n(),a);V(async()=>{await h()});async function h(){setInterval(async function(){await f()},6e4)}return(m,b)=>{const d=c("v-card-title"),p=c("v-timeline-item"),x=c("v-timeline"),k=c("v-card-text"),F=c("v-card");return g(),M("div",null,[y(e).length>0?(g(),M("div",te,[o(F,{elevation:"0"},{default:r(()=>[o(d,null,{default:r(()=>[D(i(m.$dayjs(y(e)[0].weather_date).format("dddd, DD.MM.YYYY")),1)]),_:1}),o(k,null,{default:r(()=>[o(x,{direction:"vertical",side:"end"},{default:r(()=>[(g(!0),M(I,null,N(y(e).slice(2,7),_=>(g(),U(p,{size:"x-small","dot-color":"grey-lighten-2","fill-dot":"",icon:"mdi-check"},{opposite:r(()=>[v("h3",null,i(m.$dayjs.utc(_.weather_date).format("HH:mm")),1)]),default:r(()=>[v("h3",null,i(_.description),1),v("h4",null,i((_.temperature-273.15).toFixed(1))+"\xB0C",1),v("p",null,[v("strong",null,i((_.temperature_max-273.15).toFixed(1))+"\xB0C",1),D(" / "+i((_.temperature_min-273.15).toFixed(1))+"\xB0C ",1)]),v("p",null,"Regen "+i((_.probability_of_rain*100).toFixed(0))+"%",1)]),_:2},1024))),256))]),_:1})]),_:1})]),_:1})])):q("",!0)])}}},ae={__name:"weatherForecastDayAfterTomorrow",async setup(u){let a,n;const l="https://loggik.pythonanywhere.com/api/",{data:e,pending:t,refresh:f,error:s}=([a,n]=B(()=>z(l+"wetter/wetter_uebermorgen/","$ziqIi59MUy")),a=await a,n(),a);V(async()=>{await h()});async function h(){setInterval(async function(){await f()},6e4)}return(m,b)=>{const d=c("v-card-title"),p=c("v-timeline-item"),x=c("v-timeline"),k=c("v-card-text"),F=c("v-card");return g(),M("div",null,[o(F,{elevation:"0"},{default:r(()=>[o(d,null,{default:r(()=>[D(i(m.$dayjs(y(e)[0].weather_date).format("dddd, DD.MM.YYYY")),1)]),_:1}),o(k,null,{default:r(()=>[o(x,{direction:"vertical",side:"end"},{default:r(()=>[(g(!0),M(I,null,N(y(e).slice(2,7),_=>(g(),U(p,{size:"x-small","dot-color":"grey-lighten-2","fill-dot":"",icon:"mdi-check"},{opposite:r(()=>[v("h3",null,i(m.$dayjs.utc(_.weather_date).format("HH:mm")),1)]),default:r(()=>[v("h3",null,i(_.description),1),v("h4",null,i((_.temperature-273.15).toFixed(1))+"\xB0C",1),v("p",null,[v("strong",null,i((_.temperature_max-273.15).toFixed(1))+"\xB0C",1),D(" / "+i((_.temperature_min-273.15).toFixed(1))+"\xB0C ",1)]),v("p",null,"Regen "+i((_.probability_of_rain*100).toFixed(0))+"%",1)]),_:2},1024))),256))]),_:1})]),_:1})]),_:1})])}}},oe=D("Morgen"),re=D("\xDCbermorgen"),se={__name:"WeatherForecastCard",setup(u){const a=K("tab",()=>"tomorrow");return(n,l)=>{const e=c("v-tab"),t=c("v-tabs"),f=ne,s=c("v-window-item"),h=ae,m=c("v-window"),b=c("v-card-text"),d=c("v-card");return g(),M("div",null,[o(d,{height:"450",class:"overflow-auto",elevation:"0"},{default:r(()=>[o(t,{modelValue:y(a),"onUpdate:modelValue":l[0]||(l[0]=p=>P(a)?a.value=p:null)},{default:r(()=>[o(e,{value:"tomorrow"},{default:r(()=>[oe]),_:1}),o(e,{value:"dayAfterTomorrow"},{default:r(()=>[re]),_:1})]),_:1},8,["modelValue"]),o(b,null,{default:r(()=>[o(m,{modelValue:y(a),"onUpdate:modelValue":l[1]||(l[1]=p=>P(a)?a.value=p:null)},{default:r(()=>[o(s,{value:"tomorrow"},{default:r(()=>[o(f)]),_:1}),o(s,{value:"dayAfterTomorrow"},{default:r(()=>[o(h)]),_:1})]),_:1},8,["modelValue"])]),_:1})]),_:1})])}}},ce=D(" N\xE4chste M\xFClltermine "),le=v("br",null,null,-1),ie={__name:"wasteEventsCard",async setup(u){let a,n;const l="https://loggik.pythonanywhere.com/api/",{data:e,pending:t,refresh:f,error:s}=([a,n]=B(()=>z(l+"muell/","$vKjeImFmQa")),a=await a,n(),a);V(async()=>{await h()});async function h(){setInterval(async function(){await f()},6e4)}function m(d,p){return d.diff(p,"day")<1}function b(d){switch(d){case"Restabfall 40L-240L(2-w\xF6chentlich)":return"grey-darken-1";case"Wertstoff/LVP(2-w\xF6chentlich)":return"yellow-darken-2";case"Bioabfall(2-w\xF6chentlich)":return"brown-darken-1";default:return"light-blue-darken-2"}}return(d,p)=>{const x=c("v-card-title"),k=c("v-icon"),F=c("v-card-text"),_=c("v-card");return g(),M("div",null,[o(_,{"max-width":"300px",elevation:"0",height:"450",class:"overflow-auto"},{default:r(()=>[o(x,null,{default:r(()=>[ce]),_:1}),(g(!0),M(I,null,N(y(e),Y=>(g(),U(F,null,{default:r(()=>[v("p",{class:Q(m(d.$dayjs(Y.event_date),d.$dayjs())?"bg-green-lighten-3":"")},[o(k,{icon:"mdi-delete",color:b(Y.name),large:""},null,8,["color"]),D(" "+i(d.$dayjs(Y.event_date).format("dddd, DD.MM.YYYY")),1),le,D(" "+i(Y.name),1)],2)]),_:2},1024))),256))]),_:1})])}}},de={};function _e(u,a){const n=ee,l=c("v-card-text"),e=c("v-card"),t=c("v-col"),f=se,s=ie,h=c("v-row"),m=c("v-container");return g(),M("div",null,[o(e,{elevation:"0"},{default:r(()=>[o(l,null,{default:r(()=>[o(n)]),_:1})]),_:1}),o(m,{"background-color":"green-lighten-5"},{default:r(()=>[o(h,null,{default:r(()=>[o(t,{cols:"12",md:"3"}),o(t,{cols:"12",md:"3"},{default:r(()=>[o(f)]),_:1}),o(t,{cols:"12",md:"3"}),o(t,{cols:"12",md:"3"},{default:r(()=>[o(s)]),_:1})]),_:1})]),_:1})])}const fe=J(de,[["render",_e]]);export{fe as default};