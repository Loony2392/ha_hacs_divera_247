function t(t,e,i,s){var r,o=arguments.length,n=o<3?e:null===s?s=Object.getOwnPropertyDescriptor(e,i):s;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)n=Reflect.decorate(t,e,i,s);else for(var a=t.length-1;a>=0;a--)(r=t[a])&&(n=(o<3?r(n):o>3?r(e,i,n):r(e,i))||n);return o>3&&n&&Object.defineProperty(e,i,n),n}"function"==typeof SuppressedError&&SuppressedError;const e=globalThis,i=e.ShadowRoot&&(void 0===e.ShadyCSS||e.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,s=Symbol(),r=new WeakMap;let o=class{constructor(t,e,i){if(this._$cssResult$=!0,i!==s)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=t,this.t=e}get styleSheet(){let t=this.o;const e=this.t;if(i&&void 0===t){const i=void 0!==e&&1===e.length;i&&(t=r.get(e)),void 0===t&&((this.o=t=new CSSStyleSheet).replaceSync(this.cssText),i&&r.set(e,t))}return t}toString(){return this.cssText}};const n=(t,...e)=>{const i=1===t.length?t[0]:e.reduce(((e,i,s)=>e+(t=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(i)+t[s+1]),t[0]);return new o(i,t,s)},a=i?t=>t:t=>t instanceof CSSStyleSheet?(t=>{let e="";for(const i of t.cssRules)e+=i.cssText;return(t=>new o("string"==typeof t?t:t+"",void 0,s))(e)})(t):t,{is:l,defineProperty:d,getOwnPropertyDescriptor:c,getOwnPropertyNames:h,getOwnPropertySymbols:p,getPrototypeOf:u}=Object,m=globalThis,v=m.trustedTypes,f=v?v.emptyScript:"",g=m.reactiveElementPolyfillSupport,y=(t,e)=>t,b={toAttribute(t,e){switch(e){case Boolean:t=t?f:null;break;case Object:case Array:t=null==t?t:JSON.stringify(t)}return t},fromAttribute(t,e){let i=t;switch(e){case Boolean:i=null!==t;break;case Number:i=null===t?null:Number(t);break;case Object:case Array:try{i=JSON.parse(t)}catch(t){i=null}}return i}},x=(t,e)=>!l(t,e),_={attribute:!0,type:String,converter:b,reflect:!1,hasChanged:x};Symbol.metadata??(Symbol.metadata=Symbol("metadata")),m.litPropertyMetadata??(m.litPropertyMetadata=new WeakMap);let $=class extends HTMLElement{static addInitializer(t){this._$Ei(),(this.l??(this.l=[])).push(t)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(t,e=_){if(e.state&&(e.attribute=!1),this._$Ei(),this.elementProperties.set(t,e),!e.noAccessor){const i=Symbol(),s=this.getPropertyDescriptor(t,i,e);void 0!==s&&d(this.prototype,t,s)}}static getPropertyDescriptor(t,e,i){const{get:s,set:r}=c(this.prototype,t)??{get(){return this[e]},set(t){this[e]=t}};return{get(){return null==s?void 0:s.call(this)},set(e){const o=null==s?void 0:s.call(this);r.call(this,e),this.requestUpdate(t,o,i)},configurable:!0,enumerable:!0}}static getPropertyOptions(t){return this.elementProperties.get(t)??_}static _$Ei(){if(this.hasOwnProperty(y("elementProperties")))return;const t=u(this);t.finalize(),void 0!==t.l&&(this.l=[...t.l]),this.elementProperties=new Map(t.elementProperties)}static finalize(){if(this.hasOwnProperty(y("finalized")))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(y("properties"))){const t=this.properties,e=[...h(t),...p(t)];for(const i of e)this.createProperty(i,t[i])}const t=this[Symbol.metadata];if(null!==t){const e=litPropertyMetadata.get(t);if(void 0!==e)for(const[t,i]of e)this.elementProperties.set(t,i)}this._$Eh=new Map;for(const[t,e]of this.elementProperties){const i=this._$Eu(t,e);void 0!==i&&this._$Eh.set(i,t)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(t){const e=[];if(Array.isArray(t)){const i=new Set(t.flat(1/0).reverse());for(const t of i)e.unshift(a(t))}else void 0!==t&&e.push(a(t));return e}static _$Eu(t,e){const i=e.attribute;return!1===i?void 0:"string"==typeof i?i:"string"==typeof t?t.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){var t;this._$ES=new Promise((t=>this.enableUpdating=t)),this._$AL=new Map,this._$E_(),this.requestUpdate(),null===(t=this.constructor.l)||void 0===t||t.forEach((t=>t(this)))}addController(t){var e;(this._$EO??(this._$EO=new Set)).add(t),void 0!==this.renderRoot&&this.isConnected&&(null===(e=t.hostConnected)||void 0===e||e.call(t))}removeController(t){var e;null===(e=this._$EO)||void 0===e||e.delete(t)}_$E_(){const t=new Map,e=this.constructor.elementProperties;for(const i of e.keys())this.hasOwnProperty(i)&&(t.set(i,this[i]),delete this[i]);t.size>0&&(this._$Ep=t)}createRenderRoot(){const t=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return((t,s)=>{if(i)t.adoptedStyleSheets=s.map((t=>t instanceof CSSStyleSheet?t:t.styleSheet));else for(const i of s){const s=document.createElement("style"),r=e.litNonce;void 0!==r&&s.setAttribute("nonce",r),s.textContent=i.cssText,t.appendChild(s)}})(t,this.constructor.elementStyles),t}connectedCallback(){var t;this.renderRoot??(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null===(t=this._$EO)||void 0===t||t.forEach((t=>{var e;return null===(e=t.hostConnected)||void 0===e?void 0:e.call(t)}))}enableUpdating(t){}disconnectedCallback(){var t;null===(t=this._$EO)||void 0===t||t.forEach((t=>{var e;return null===(e=t.hostDisconnected)||void 0===e?void 0:e.call(t)}))}attributeChangedCallback(t,e,i){this._$AK(t,i)}_$EC(t,e){const i=this.constructor.elementProperties.get(t),s=this.constructor._$Eu(t,i);if(void 0!==s&&!0===i.reflect){var r;const o=(void 0!==(null===(r=i.converter)||void 0===r?void 0:r.toAttribute)?i.converter:b).toAttribute(e,i.type);this._$Em=t,null==o?this.removeAttribute(s):this.setAttribute(s,o),this._$Em=null}}_$AK(t,e){const i=this.constructor,s=i._$Eh.get(t);if(void 0!==s&&this._$Em!==s){var r;const t=i.getPropertyOptions(s),o="function"==typeof t.converter?{fromAttribute:t.converter}:void 0!==(null===(r=t.converter)||void 0===r?void 0:r.fromAttribute)?t.converter:b;this._$Em=s,this[s]=o.fromAttribute(e,t.type),this._$Em=null}}requestUpdate(t,e,i){if(void 0!==t){if(i??(i=this.constructor.getPropertyOptions(t)),!(i.hasChanged??x)(this[t],e))return;this.P(t,e,i)}!1===this.isUpdatePending&&(this._$ES=this._$ET())}P(t,e,i){this._$AL.has(t)||this._$AL.set(t,e),!0===i.reflect&&this._$Em!==t&&(this._$Ej??(this._$Ej=new Set)).add(t)}async _$ET(){this.isUpdatePending=!0;try{await this._$ES}catch(t){Promise.reject(t)}const t=this.scheduleUpdate();return null!=t&&await t,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??(this.renderRoot=this.createRenderRoot()),this._$Ep){for(const[t,e]of this._$Ep)this[t]=e;this._$Ep=void 0}const t=this.constructor.elementProperties;if(t.size>0)for(const[e,i]of t)!0!==i.wrapped||this._$AL.has(e)||void 0===this[e]||this.P(e,this[e],i)}let t=!1;const e=this._$AL;try{var i;t=this.shouldUpdate(e),t?(this.willUpdate(e),null!==(i=this._$EO)&&void 0!==i&&i.forEach((t=>{var e;return null===(e=t.hostUpdate)||void 0===e?void 0:e.call(t)})),this.update(e)):this._$EU()}catch(e){throw t=!1,this._$EU(),e}t&&this._$AE(e)}willUpdate(t){}_$AE(t){var e;null!==(e=this._$EO)&&void 0!==e&&e.forEach((t=>{var e;return null===(e=t.hostUpdated)||void 0===e?void 0:e.call(t)})),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(t)),this.updated(t)}_$EU(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(t){return!0}update(t){this._$Ej&&(this._$Ej=this._$Ej.forEach((t=>this._$EC(t,this[t])))),this._$EU()}updated(t){}firstUpdated(t){}};$.elementStyles=[],$.shadowRootOptions={mode:"open"},$[y("elementProperties")]=new Map,$[y("finalized")]=new Map,null!=g&&g({ReactiveElement:$}),(m.reactiveElementVersions??(m.reactiveElementVersions=[])).push("2.0.4");const w=globalThis,A=w.trustedTypes,C=A?A.createPolicy("lit-html",{createHTML:t=>t}):void 0,E="$lit$",S=`lit$${(Math.random()+"").slice(9)}$`,R="?"+S,I=`<${R}>`,P=document,k=()=>P.createComment(""),T=t=>null===t||"object"!=typeof t&&"function"!=typeof t,L=Array.isArray,N="[ \t\n\f\r]",z=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,M=/-->/g,U=/>/g,O=RegExp(`>|${N}(?:([^\\s"'>=/]+)(${N}*=${N}*(?:[^ \t\n\f\r"'\`<>=]|("|')|))|$)`,"g"),H=/'/g,D=/"/g,B=/^(?:script|style|textarea|title)$/i,V=t=>(e,...i)=>({_$litType$:t,strings:e,values:i}),F=V(1),j=V(2),q=Symbol.for("lit-noChange"),K=Symbol.for("lit-nothing"),W=new WeakMap,G=P.createTreeWalker(P,129);function Z(t,e){if(!Array.isArray(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return void 0!==C?C.createHTML(e):e}const Y=(t,e)=>{const i=t.length-1,s=[];let r,o=2===e?"<svg>":"",n=z;for(let e=0;e<i;e++){const i=t[e];let a,l,d=-1,c=0;for(;c<i.length&&(n.lastIndex=c,l=n.exec(i),null!==l);)c=n.lastIndex,n===z?"!--"===l[1]?n=M:void 0!==l[1]?n=U:void 0!==l[2]?(B.test(l[2])&&(r=RegExp("</"+l[2],"g")),n=O):void 0!==l[3]&&(n=O):n===O?">"===l[0]?(n=r??z,d=-1):void 0===l[1]?d=-2:(d=n.lastIndex-l[2].length,a=l[1],n=void 0===l[3]?O:'"'===l[3]?D:H):n===D||n===H?n=O:n===M||n===U?n=z:(n=O,r=void 0);const h=n===O&&t[e+1].startsWith("/>")?" ":"";o+=n===z?i+I:d>=0?(s.push(a),i.slice(0,d)+E+i.slice(d)+S+h):i+S+(-2===d?e:h)}return[Z(t,o+(t[i]||"<?>")+(2===e?"</svg>":"")),s]};class J{constructor({strings:t,_$litType$:e},i){let s;this.parts=[];let r=0,o=0;const n=t.length-1,a=this.parts,[l,d]=Y(t,e);if(this.el=J.createElement(l,i),G.currentNode=this.el.content,2===e){const t=this.el.content.firstChild;t.replaceWith(...t.childNodes)}for(;null!==(s=G.nextNode())&&a.length<n;){if(1===s.nodeType){if(s.hasAttributes())for(const t of s.getAttributeNames())if(t.endsWith(E)){const e=d[o++],i=s.getAttribute(t).split(S),n=/([.?@])?(.*)/.exec(e);a.push({type:1,index:r,name:n[2],strings:i,ctor:"."===n[1]?it:"?"===n[1]?st:"@"===n[1]?rt:et}),s.removeAttribute(t)}else t.startsWith(S)&&(a.push({type:6,index:r}),s.removeAttribute(t));if(B.test(s.tagName)){const t=s.textContent.split(S),e=t.length-1;if(e>0){s.textContent=A?A.emptyScript:"";for(let i=0;i<e;i++)s.append(t[i],k()),G.nextNode(),a.push({type:2,index:++r});s.append(t[e],k())}}}else if(8===s.nodeType)if(s.data===R)a.push({type:2,index:r});else{let t=-1;for(;-1!==(t=s.data.indexOf(S,t+1));)a.push({type:7,index:r}),t+=S.length-1}r++}}static createElement(t,e){const i=P.createElement("template");return i.innerHTML=t,i}}function X(t,e,i=t,s){var r,o,n,a;if(e===q)return e;let l=void 0!==s?null===(r=i._$Co)||void 0===r?void 0:r[s]:i._$Cl;const d=T(e)?void 0:e._$litDirective$;return(null===(o=l)||void 0===o?void 0:o.constructor)!==d&&(null!==(n=l)&&void 0!==n&&null!==(a=n._$AO)&&void 0!==a&&a.call(n,!1),void 0===d?l=void 0:(l=new d(t),l._$AT(t,i,s)),void 0!==s?(i._$Co??(i._$Co=[]))[s]=l:i._$Cl=l),void 0!==l&&(e=X(t,l._$AS(t,e.values),l,s)),e}class Q{constructor(t,e){this._$AV=[],this._$AN=void 0,this._$AD=t,this._$AM=e}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(t){const{el:{content:e},parts:i}=this._$AD,s=((null==t?void 0:t.creationScope)??P).importNode(e,!0);G.currentNode=s;let r=G.nextNode(),o=0,n=0,a=i[0];for(;void 0!==a;){var l;if(o===a.index){let e;2===a.type?e=new tt(r,r.nextSibling,this,t):1===a.type?e=new a.ctor(r,a.name,a.strings,this,t):6===a.type&&(e=new ot(r,this,t)),this._$AV.push(e),a=i[++n]}o!==(null===(l=a)||void 0===l?void 0:l.index)&&(r=G.nextNode(),o++)}return G.currentNode=P,s}p(t){let e=0;for(const i of this._$AV)void 0!==i&&(void 0!==i.strings?(i._$AI(t,i,e),e+=i.strings.length-2):i._$AI(t[e])),e++}}class tt{get _$AU(){var t;return(null===(t=this._$AM)||void 0===t?void 0:t._$AU)??this._$Cv}constructor(t,e,i,s){this.type=2,this._$AH=K,this._$AN=void 0,this._$AA=t,this._$AB=e,this._$AM=i,this.options=s,this._$Cv=(null==s?void 0:s.isConnected)??!0}get parentNode(){var t;let e=this._$AA.parentNode;const i=this._$AM;return void 0!==i&&11===(null===(t=e)||void 0===t?void 0:t.nodeType)&&(e=i.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(t,e=this){t=X(this,t,e),T(t)?t===K||null==t||""===t?(this._$AH!==K&&this._$AR(),this._$AH=K):t!==this._$AH&&t!==q&&this._(t):void 0!==t._$litType$?this.$(t):void 0!==t.nodeType?this.T(t):(t=>L(t)||"function"==typeof(null==t?void 0:t[Symbol.iterator]))(t)?this.k(t):this._(t)}S(t){return this._$AA.parentNode.insertBefore(t,this._$AB)}T(t){this._$AH!==t&&(this._$AR(),this._$AH=this.S(t))}_(t){this._$AH!==K&&T(this._$AH)?this._$AA.nextSibling.data=t:this.T(P.createTextNode(t)),this._$AH=t}$(t){var e;const{values:i,_$litType$:s}=t,r="number"==typeof s?this._$AC(t):(void 0===s.el&&(s.el=J.createElement(Z(s.h,s.h[0]),this.options)),s);if((null===(e=this._$AH)||void 0===e?void 0:e._$AD)===r)this._$AH.p(i);else{const t=new Q(r,this),e=t.u(this.options);t.p(i),this.T(e),this._$AH=t}}_$AC(t){let e=W.get(t.strings);return void 0===e&&W.set(t.strings,e=new J(t)),e}k(t){L(this._$AH)||(this._$AH=[],this._$AR());const e=this._$AH;let i,s=0;for(const r of t)s===e.length?e.push(i=new tt(this.S(k()),this.S(k()),this,this.options)):i=e[s],i._$AI(r),s++;s<e.length&&(this._$AR(i&&i._$AB.nextSibling,s),e.length=s)}_$AR(t=this._$AA.nextSibling,e){for(null===(i=this._$AP)||void 0===i||i.call(this,!1,!0,e);t&&t!==this._$AB;){var i;const e=t.nextSibling;t.remove(),t=e}}setConnected(t){var e;void 0===this._$AM&&(this._$Cv=t,null===(e=this._$AP)||void 0===e||e.call(this,t))}}class et{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(t,e,i,s,r){this.type=1,this._$AH=K,this._$AN=void 0,this.element=t,this.name=e,this._$AM=s,this.options=r,i.length>2||""!==i[0]||""!==i[1]?(this._$AH=Array(i.length-1).fill(new String),this.strings=i):this._$AH=K}_$AI(t,e=this,i,s){const r=this.strings;let o=!1;if(void 0===r)t=X(this,t,e,0),o=!T(t)||t!==this._$AH&&t!==q,o&&(this._$AH=t);else{const s=t;let n,a;for(t=r[0],n=0;n<r.length-1;n++)a=X(this,s[i+n],e,n),a===q&&(a=this._$AH[n]),o||(o=!T(a)||a!==this._$AH[n]),a===K?t=K:t!==K&&(t+=(a??"")+r[n+1]),this._$AH[n]=a}o&&!s&&this.j(t)}j(t){t===K?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,t??"")}}class it extends et{constructor(){super(...arguments),this.type=3}j(t){this.element[this.name]=t===K?void 0:t}}class st extends et{constructor(){super(...arguments),this.type=4}j(t){this.element.toggleAttribute(this.name,!!t&&t!==K)}}class rt extends et{constructor(t,e,i,s,r){super(t,e,i,s,r),this.type=5}_$AI(t,e=this){if((t=X(this,t,e,0)??K)===q)return;const i=this._$AH,s=t===K&&i!==K||t.capture!==i.capture||t.once!==i.once||t.passive!==i.passive,r=t!==K&&(i===K||s);s&&this.element.removeEventListener(this.name,this,i),r&&this.element.addEventListener(this.name,this,t),this._$AH=t}handleEvent(t){var e;"function"==typeof this._$AH?this._$AH.call((null===(e=this.options)||void 0===e?void 0:e.host)??this.element,t):this._$AH.handleEvent(t)}}class ot{constructor(t,e,i){this.element=t,this.type=6,this._$AN=void 0,this._$AM=e,this.options=i}get _$AU(){return this._$AM._$AU}_$AI(t){X(this,t)}}const nt=w.litHtmlPolyfillSupport;null!=nt&&nt(J,tt),(w.litHtmlVersions??(w.litHtmlVersions=[])).push("3.1.2");var at;let lt=class extends ${constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var t;const e=super.createRenderRoot();return(t=this.renderOptions).renderBefore??(t.renderBefore=e.firstChild),e}update(t){const e=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(t),this._$Do=((t,e,i)=>{const s=(null==i?void 0:i.renderBefore)??e;let r=s._$litPart$;if(void 0===r){const t=(null==i?void 0:i.renderBefore)??null;s._$litPart$=r=new tt(e.insertBefore(k(),t),t,void 0,i??{})}return r._$AI(t),r})(e,this.renderRoot,this.renderOptions)}connectedCallback(){var t;super.connectedCallback(),null===(t=this._$Do)||void 0===t||t.setConnected(!0)}disconnectedCallback(){var t;super.disconnectedCallback(),null===(t=this._$Do)||void 0===t||t.setConnected(!1)}render(){return q}};lt._$litElement$=!0,lt.finalized=!0,null===(at=globalThis.litElementHydrateSupport)||void 0===at||at.call(globalThis,{LitElement:lt});const dt=globalThis.litElementPolyfillSupport;null==dt||dt({LitElement:lt}),(globalThis.litElementVersions??(globalThis.litElementVersions=[])).push("4.0.4");const ct=t=>(e,i)=>{void 0!==i?i.addInitializer((()=>{customElements.define(t,e)})):customElements.define(t,e)},ht={attribute:!0,type:String,converter:b,reflect:!1,hasChanged:x},pt=(t=ht,e,i)=>{const{kind:s,metadata:r}=i;let o=globalThis.litPropertyMetadata.get(r);if(void 0===o&&globalThis.litPropertyMetadata.set(r,o=new Map),o.set(i.name,t),"accessor"===s){const{name:s}=i;return{set(i){const r=e.get.call(this);e.set.call(this,i),this.requestUpdate(s,r,t)},init(e){return void 0!==e&&this.P(s,void 0,t),e}}}if("setter"===s){const{name:s}=i;return function(i){const r=this[s];e.call(this,i),this.requestUpdate(s,r,t)}}throw Error("Unsupported decorator location: "+s)};function ut(t){return(e,i)=>"object"==typeof i?pt(t,e,i):((t,e,i)=>{const s=e.hasOwnProperty(i);return e.constructor.createProperty(i,s?{...t,wrapped:!0}:t),s?Object.getOwnPropertyDescriptor(e,i):void 0})(t,e,i)}function mt(t){return ut({...t,state:!0,attribute:!1})}const vt=(t,e,i)=>(i.configurable=!0,i.enumerable=!0,Reflect.decorate&&"object"!=typeof e&&Object.defineProperty(t,e,i),i);function ft(t,e){return(i,s,r)=>{const o=e=>{var i;return(null===(i=e.renderRoot)||void 0===i?void 0:i.querySelector(t))??null};if(e){const{get:t,set:e}="object"==typeof s?i:r??(()=>{const t=Symbol();return{get(){return this[t]},set(e){this[t]=e}}})();return vt(i,s,{get(){let i=t.call(this);return void 0===i&&(i=o(this),(null!==i||this.hasUpdated)&&e.call(this,i)),i}})}return vt(i,s,{get(){return o(this)}})}}let gt;function yt(t){return(e,i)=>{const{slot:s,selector:r}=t??{},o="slot"+(s?`[name=${s}]`:":not([name])");return vt(e,i,{get(){var e;const i=null===(e=this.renderRoot)||void 0===e?void 0:e.querySelector(o),s=(null==i?void 0:i.assignedElements(t))??[];return void 0===r?s:s.filter((t=>t.matches(r)))}})}}const bt=Symbol("attachableController");let xt;xt=new MutationObserver((t=>{for(const i of t){var e;null===(e=i.target[bt])||void 0===e||e.hostConnected()}}));class _t{get htmlFor(){return this.host.getAttribute("for")}set htmlFor(t){null===t?this.host.removeAttribute("for"):this.host.setAttribute("for",t)}get control(){return this.host.hasAttribute("for")?this.htmlFor&&this.host.isConnected?this.host.getRootNode().querySelector(`#${this.htmlFor}`):null:this.currentControl||this.host.parentElement}set control(t){t?this.attach(t):this.detach()}constructor(t,e){var i;this.host=t,this.onControlChange=e,this.currentControl=null,t.addController(this),t[bt]=this,null===(i=xt)||void 0===i||i.observe(t,{attributeFilter:["for"]})}attach(t){t!==this.currentControl&&(this.setCurrentControl(t),this.host.removeAttribute("for"))}detach(){this.setCurrentControl(null),this.host.setAttribute("for","")}hostConnected(){this.setCurrentControl(this.control)}hostDisconnected(){this.setCurrentControl(null)}setCurrentControl(t){this.onControlChange(this.currentControl,t),this.currentControl=t}}const $t=["focusin","focusout","pointerdown"];class wt extends lt{constructor(){super(...arguments),this.visible=!1,this.inward=!1,this.attachableController=new _t(this,this.onControlChange.bind(this))}get htmlFor(){return this.attachableController.htmlFor}set htmlFor(t){this.attachableController.htmlFor=t}get control(){return this.attachableController.control}set control(t){this.attachableController.control=t}attach(t){this.attachableController.attach(t)}detach(){this.attachableController.detach()}connectedCallback(){super.connectedCallback(),this.setAttribute("aria-hidden","true")}handleEvent(t){var e;if(!t[At]){switch(t.type){default:return;case"focusin":this.visible=(null===(e=this.control)||void 0===e?void 0:e.matches(":focus-visible"))??!1;break;case"focusout":case"pointerdown":this.visible=!1}t[At]=!0}}onControlChange(t,e){for(const i of $t)null==t||t.removeEventListener(i,this),null==e||e.addEventListener(i,this)}update(t){t.has("visible")&&this.dispatchEvent(new Event("visibility-changed")),super.update(t)}}t([ut({type:Boolean,reflect:!0})],wt.prototype,"visible",void 0),t([ut({type:Boolean,reflect:!0})],wt.prototype,"inward",void 0);const At=Symbol("handledByFocusRing"),Ct=n`:host{animation-delay:0s,calc(var(--md-focus-ring-duration, 600ms)*.25);animation-duration:calc(var(--md-focus-ring-duration, 600ms)*.25),calc(var(--md-focus-ring-duration, 600ms)*.75);animation-timing-function:cubic-bezier(0.2, 0, 0, 1);box-sizing:border-box;color:var(--md-focus-ring-color, var(--md-sys-color-secondary, #625b71));display:none;pointer-events:none;position:absolute}:host([visible]){display:flex}:host(:not([inward])){animation-name:outward-grow,outward-shrink;border-end-end-radius:calc(var(--md-focus-ring-shape-end-end, var(--md-focus-ring-shape, 9999px)) + var(--md-focus-ring-outward-offset, 2px));border-end-start-radius:calc(var(--md-focus-ring-shape-end-start, var(--md-focus-ring-shape, 9999px)) + var(--md-focus-ring-outward-offset, 2px));border-start-end-radius:calc(var(--md-focus-ring-shape-start-end, var(--md-focus-ring-shape, 9999px)) + var(--md-focus-ring-outward-offset, 2px));border-start-start-radius:calc(var(--md-focus-ring-shape-start-start, var(--md-focus-ring-shape, 9999px)) + var(--md-focus-ring-outward-offset, 2px));inset:calc(-1*var(--md-focus-ring-outward-offset, 2px));outline:var(--md-focus-ring-width, 3px) solid currentColor}:host([inward]){animation-name:inward-grow,inward-shrink;border-end-end-radius:calc(var(--md-focus-ring-shape-end-end, var(--md-focus-ring-shape, 9999px)) - var(--md-focus-ring-inward-offset, 0px));border-end-start-radius:calc(var(--md-focus-ring-shape-end-start, var(--md-focus-ring-shape, 9999px)) - var(--md-focus-ring-inward-offset, 0px));border-start-end-radius:calc(var(--md-focus-ring-shape-start-end, var(--md-focus-ring-shape, 9999px)) - var(--md-focus-ring-inward-offset, 0px));border-start-start-radius:calc(var(--md-focus-ring-shape-start-start, var(--md-focus-ring-shape, 9999px)) - var(--md-focus-ring-inward-offset, 0px));border:var(--md-focus-ring-width, 3px) solid currentColor;inset:var(--md-focus-ring-inward-offset, 0px)}@keyframes outward-grow{from{outline-width:0}to{outline-width:var(--md-focus-ring-active-width, 8px)}}@keyframes outward-shrink{from{outline-width:var(--md-focus-ring-active-width, 8px)}}@keyframes inward-grow{from{border-width:0}to{border-width:var(--md-focus-ring-active-width, 8px)}}@keyframes inward-shrink{from{border-width:var(--md-focus-ring-active-width, 8px)}}@media(prefers-reduced-motion){:host{animation:none}}/*# sourceMappingURL=focus-ring-styles.css.map */
`;let Et=class extends wt{};Et.styles=[Ct],Et=t([ct("md-focus-ring")],Et);const St=1;class Rt{constructor(t){}get _$AU(){return this._$AM._$AU}_$AT(t,e,i){this._$Ct=t,this._$AM=e,this._$Ci=i}_$AS(t,e){return this.update(t,e)}update(t,e){return this.render(...e)}}const It=(t=>(...e)=>({_$litDirective$:t,values:e}))(class extends Rt{constructor(t){var e;if(super(t),t.type!==St||"class"!==t.name||(null===(e=t.strings)||void 0===e?void 0:e.length)>2)throw Error("`classMap()` can only be used in the `class` attribute and must be the only part in the attribute.")}render(t){return" "+Object.keys(t).filter((e=>t[e])).join(" ")+" "}update(t,[e]){if(void 0===this.st){this.st=new Set,void 0!==t.strings&&(this.nt=new Set(t.strings.join(" ").split(/\s/).filter((t=>""!==t))));for(const t in e){var i;e[t]&&(null===(i=this.nt)||void 0===i||!i.has(t))&&this.st.add(t)}return this.render(e)}const s=t.element.classList;for(const t of this.st)t in e||(s.remove(t),this.st.delete(t));for(const t in e){var r;const i=!!e[t];i===this.st.has(t)||(null===(r=this.nt)||void 0===r?void 0:r.has(t))||(i?(s.add(t),this.st.add(t)):(s.remove(t),this.st.delete(t)))}return q}}),Pt={STANDARD:"cubic-bezier(0.2, 0, 0, 1)",STANDARD_ACCELERATE:"cubic-bezier(.3,0,1,1)",STANDARD_DECELERATE:"cubic-bezier(0,0,0,1)",EMPHASIZED:"cubic-bezier(.3,0,0,1)",EMPHASIZED_ACCELERATE:"cubic-bezier(.3,0,.8,.15)",EMPHASIZED_DECELERATE:"cubic-bezier(.05,.7,.1,1)"};var kt;!function(t){t[t.INACTIVE=0]="INACTIVE",t[t.TOUCH_DELAY=1]="TOUCH_DELAY",t[t.HOLDING=2]="HOLDING",t[t.WAITING_FOR_CLICK=3]="WAITING_FOR_CLICK"}(kt||(kt={}));const Tt=["click","contextmenu","pointercancel","pointerdown","pointerenter","pointerleave","pointerup"],Lt=window.matchMedia("(forced-colors: active)");class Nt extends lt{constructor(){super(...arguments),this.disabled=!1,this.hovered=!1,this.pressed=!1,this.rippleSize="",this.rippleScale="",this.initialSize=0,this.state=kt.INACTIVE,this.checkBoundsAfterContextMenu=!1,this.attachableController=new _t(this,this.onControlChange.bind(this))}get htmlFor(){return this.attachableController.htmlFor}set htmlFor(t){this.attachableController.htmlFor=t}get control(){return this.attachableController.control}set control(t){this.attachableController.control=t}attach(t){this.attachableController.attach(t)}detach(){this.attachableController.detach()}connectedCallback(){super.connectedCallback(),this.setAttribute("aria-hidden","true")}render(){const t={hovered:this.hovered,pressed:this.pressed};return F`<div class="surface ${It(t)}"></div>`}update(t){t.has("disabled")&&this.disabled&&(this.hovered=!1,this.pressed=!1),super.update(t)}handlePointerenter(t){this.shouldReactToEvent(t)&&(this.hovered=!0)}handlePointerleave(t){this.shouldReactToEvent(t)&&(this.hovered=!1,this.state!==kt.INACTIVE&&this.endPressAnimation())}handlePointerup(t){if(this.shouldReactToEvent(t)){if(this.state!==kt.HOLDING)return this.state===kt.TOUCH_DELAY?(this.state=kt.WAITING_FOR_CLICK,void this.startPressAnimation(this.rippleStartEvent)):void 0;this.state=kt.WAITING_FOR_CLICK}}async handlePointerdown(t){if(this.shouldReactToEvent(t)){if(this.rippleStartEvent=t,!this.isTouch(t))return this.state=kt.WAITING_FOR_CLICK,void this.startPressAnimation(t);this.checkBoundsAfterContextMenu&&!this.inBounds(t)||(this.checkBoundsAfterContextMenu=!1,this.state=kt.TOUCH_DELAY,await new Promise((t=>{setTimeout(t,150)})),this.state===kt.TOUCH_DELAY&&(this.state=kt.HOLDING,this.startPressAnimation(t)))}}handleClick(){this.disabled||(this.state!==kt.WAITING_FOR_CLICK?this.state===kt.INACTIVE&&(this.startPressAnimation(),this.endPressAnimation()):this.endPressAnimation())}handlePointercancel(t){this.shouldReactToEvent(t)&&this.endPressAnimation()}handleContextmenu(){this.disabled||(this.checkBoundsAfterContextMenu=!0,this.endPressAnimation())}determineRippleSize(){const{height:t,width:e}=this.getBoundingClientRect(),i=Math.max(t,e),s=Math.max(.35*i,75),r=Math.floor(.2*i),o=Math.sqrt(e**2+t**2)+10;this.initialSize=r,this.rippleScale=""+(o+s)/r,this.rippleSize=`${r}px`}getNormalizedPointerEventCoords(t){const{scrollX:e,scrollY:i}=window,{left:s,top:r}=this.getBoundingClientRect(),o=e+s,n=i+r,{pageX:a,pageY:l}=t;return{x:a-o,y:l-n}}getTranslationCoordinates(t){const{height:e,width:i}=this.getBoundingClientRect(),s={x:(i-this.initialSize)/2,y:(e-this.initialSize)/2};let r;return r=t instanceof PointerEvent?this.getNormalizedPointerEventCoords(t):{x:i/2,y:e/2},r={x:r.x-this.initialSize/2,y:r.y-this.initialSize/2},{startPoint:r,endPoint:s}}startPressAnimation(t){var e;if(!this.mdRoot)return;this.pressed=!0,null===(e=this.growAnimation)||void 0===e||e.cancel(),this.determineRippleSize();const{startPoint:i,endPoint:s}=this.getTranslationCoordinates(t),r=`${i.x}px, ${i.y}px`,o=`${s.x}px, ${s.y}px`;this.growAnimation=this.mdRoot.animate({top:[0,0],left:[0,0],height:[this.rippleSize,this.rippleSize],width:[this.rippleSize,this.rippleSize],transform:[`translate(${r}) scale(1)`,`translate(${o}) scale(${this.rippleScale})`]},{pseudoElement:"::after",duration:450,easing:Pt.STANDARD,fill:"forwards"})}async endPressAnimation(){this.rippleStartEvent=void 0,this.state=kt.INACTIVE;const t=this.growAnimation;let e=1/0;"number"==typeof(null==t?void 0:t.currentTime)?e=t.currentTime:null!=t&&t.currentTime&&(e=t.currentTime.to("ms").value),e>=225?this.pressed=!1:(await new Promise((t=>{setTimeout(t,225-e)})),this.growAnimation===t&&(this.pressed=!1))}shouldReactToEvent(t){if(this.disabled||!t.isPrimary)return!1;if(this.rippleStartEvent&&this.rippleStartEvent.pointerId!==t.pointerId)return!1;if("pointerenter"===t.type||"pointerleave"===t.type)return!this.isTouch(t);const e=1===t.buttons;return this.isTouch(t)||e}inBounds({x:t,y:e}){const{top:i,left:s,bottom:r,right:o}=this.getBoundingClientRect();return t>=s&&t<=o&&e>=i&&e<=r}isTouch({pointerType:t}){return"touch"===t}async handleEvent(t){if(null==Lt||!Lt.matches)switch(t.type){case"click":this.handleClick();break;case"contextmenu":this.handleContextmenu();break;case"pointercancel":this.handlePointercancel(t);break;case"pointerdown":await this.handlePointerdown(t);break;case"pointerenter":this.handlePointerenter(t);break;case"pointerleave":this.handlePointerleave(t);break;case"pointerup":this.handlePointerup(t)}}onControlChange(t,e){for(const i of Tt)null==t||t.removeEventListener(i,this),null==e||e.addEventListener(i,this)}}t([ut({type:Boolean,reflect:!0})],Nt.prototype,"disabled",void 0),t([mt()],Nt.prototype,"hovered",void 0),t([mt()],Nt.prototype,"pressed",void 0),t([ft(".surface")],Nt.prototype,"mdRoot",void 0);const zt=n`:host{display:flex;margin:auto;pointer-events:none}:host([disabled]){display:none}@media(forced-colors: active){:host{display:none}}:host,.surface{border-radius:inherit;position:absolute;inset:0;overflow:hidden}.surface{-webkit-tap-highlight-color:rgba(0,0,0,0)}.surface::before,.surface::after{content:"";opacity:0;position:absolute}.surface::before{background-color:var(--md-ripple-hover-color, var(--md-sys-color-on-surface, #1d1b20));inset:0;transition:opacity 15ms linear,background-color 15ms linear}.surface::after{background:radial-gradient(closest-side, var(--md-ripple-pressed-color, var(--md-sys-color-on-surface, #1d1b20)) max(100% - 70px, 65%), transparent 100%);transform-origin:center center;transition:opacity 375ms linear}.hovered::before{background-color:var(--md-ripple-hover-color, var(--md-sys-color-on-surface, #1d1b20));opacity:var(--md-ripple-hover-opacity, 0.08)}.pressed::after{opacity:var(--md-ripple-pressed-opacity, 0.12);transition-duration:105ms}/*# sourceMappingURL=ripple-styles.css.map */
`;let Mt=class extends Nt{};Mt.styles=[zt],Mt=t([ct("md-ripple")],Mt);const Ut=Symbol.for(""),Ot=t=>{if((null==t?void 0:t.r)===Ut)return null==t?void 0:t._$litStatic$},Ht=(t,...e)=>({_$litStatic$:e.reduce(((e,i,s)=>e+(t=>{if(void 0!==t._$litStatic$)return t._$litStatic$;throw Error(`Value passed to 'literal' function must be a 'literal' result: ${t}. Use 'unsafeStatic' to pass non-literal values, but\n            take care to ensure page security.`)})(i)+t[s+1]),t[0]),r:Ut}),Dt=new Map,Bt=(t=>(e,...i)=>{const s=i.length;let r,o;const n=[],a=[];let l,d=0,c=!1;for(;d<s;){for(l=e[d];d<s&&void 0!==(o=i[d],r=Ot(o));)l+=r+e[++d],c=!0;d!==s&&a.push(o),n.push(l),d++}if(d===s&&n.push(e[s]),c){const t=n.join("$$lit$$");void 0===(e=Dt.get(t))&&(n.raw=n,Dt.set(t,e=n)),i=a}return t(e,...i)})(F),Vt=["ariaAtomic","ariaAutoComplete","ariaBusy","ariaChecked","ariaColCount","ariaColIndex","ariaColSpan","ariaCurrent","ariaDisabled","ariaExpanded","ariaHasPopup","ariaHidden","ariaInvalid","ariaKeyShortcuts","ariaLabel","ariaLevel","ariaLive","ariaModal","ariaMultiLine","ariaMultiSelectable","ariaOrientation","ariaPlaceholder","ariaPosInSet","ariaPressed","ariaReadOnly","ariaRequired","ariaRoleDescription","ariaRowCount","ariaRowIndex","ariaRowSpan","ariaSelected","ariaSetSize","ariaSort","ariaValueMax","ariaValueMin","ariaValueNow","ariaValueText"];function Ft(t){return t.replace("aria","aria-").replace(/Elements?/g,"").toLowerCase()}function jt(t){for(const e of Vt)t.createProperty(e,{attribute:Ft(e),reflect:!0});t.addInitializer((t=>{const e={hostConnected(){t.setAttribute("role","presentation")}};t.addController(e)}))}Vt.map(Ft);const qt=Symbol("internals"),Kt=Symbol("privateInternals");function Wt(t){return class extends t{get[qt](){return this[Kt]||(this[Kt]=this.attachInternals()),this[Kt]}}}function Gt(t){t.addInitializer((t=>{const e=t;e.addEventListener("click",(async t=>{const{type:i,[qt]:s}=e,{form:r}=s;r&&"button"!==i&&(await new Promise((t=>{setTimeout(t)})),t.defaultPrevented||("reset"!==i?(r.addEventListener("submit",(t=>{Object.defineProperty(t,"submitter",{configurable:!0,enumerable:!0,get:()=>e})}),{capture:!0,once:!0}),s.setFormValue(e.value),r.requestSubmit()):r.reset()))}))}))}function Zt(t,e=!0){return e&&"rtl"===getComputedStyle(t).getPropertyValue("direction").trim()}const Yt=Wt(lt);class Jt extends Yt{constructor(){super(...arguments),this.disabled=!1,this.flipIconInRtl=!1,this.href="",this.target="",this.ariaLabelSelected="",this.toggle=!1,this.selected=!1,this.type="submit",this.value="",this.flipIcon=Zt(this,this.flipIconInRtl)}get name(){return this.getAttribute("name")??""}set name(t){this.setAttribute("name",t)}get form(){return this[qt].form}get labels(){return this[qt].labels}willUpdate(){this.href&&(this.disabled=!1)}render(){const t=this.href?Ht`div`:Ht`button`,{ariaLabel:e,ariaHasPopup:i,ariaExpanded:s}=this,r=e&&this.ariaLabelSelected,o=this.toggle?this.selected:K;let n=K;return this.href||(n=r&&this.selected?this.ariaLabelSelected:e),Bt`<${t}
        class="icon-button ${It(this.getRenderClasses())}"
        id="button"
        aria-label="${n||K}"
        aria-haspopup="${!this.href&&i||K}"
        aria-expanded="${!this.href&&s||K}"
        aria-pressed="${o}"
        ?disabled="${!this.href&&this.disabled}"
        @click="${this.handleClick}">
        ${this.renderFocusRing()}
        ${this.renderRipple()}
        ${this.selected?K:this.renderIcon()}
        ${this.selected?this.renderSelectedIcon():K}
        ${this.renderTouchTarget()}
        ${this.href&&this.renderLink()}
  </${t}>`}renderLink(){const{ariaLabel:t}=this;return F`
      <a
        class="link"
        id="link"
        href="${this.href}"
        target="${this.target||K}"
        aria-label="${t||K}"></a>
    `}getRenderClasses(){return{"flip-icon":this.flipIcon,selected:this.toggle&&this.selected}}renderIcon(){return F`<span class="icon"><slot></slot></span>`}renderSelectedIcon(){return F`<span class="icon icon--selected"
      ><slot name="selected"><slot></slot></slot
    ></span>`}renderTouchTarget(){return F`<span class="touch"></span>`}renderFocusRing(){return F`<md-focus-ring
      part="focus-ring"
      for=${this.href?"link":"button"}></md-focus-ring>`}renderRipple(){return F`<md-ripple
      for=${this.href?"link":K}
      ?disabled="${!this.href&&this.disabled}"></md-ripple>`}connectedCallback(){this.flipIcon=Zt(this,this.flipIconInRtl),super.connectedCallback()}async handleClick(t){await 0,!this.toggle||this.disabled||t.defaultPrevented||(this.selected=!this.selected,this.dispatchEvent(new InputEvent("input",{bubbles:!0,composed:!0})),this.dispatchEvent(new Event("change",{bubbles:!0})))}}jt(Jt),Gt(Jt),Jt.formAssociated=!0,Jt.shadowRootOptions={mode:"open",delegatesFocus:!0},t([ut({type:Boolean,reflect:!0})],Jt.prototype,"disabled",void 0),t([ut({type:Boolean,attribute:"flip-icon-in-rtl"})],Jt.prototype,"flipIconInRtl",void 0),t([ut()],Jt.prototype,"href",void 0),t([ut()],Jt.prototype,"target",void 0),t([ut({attribute:"aria-label-selected"})],Jt.prototype,"ariaLabelSelected",void 0),t([ut({type:Boolean})],Jt.prototype,"toggle",void 0),t([ut({type:Boolean,reflect:!0})],Jt.prototype,"selected",void 0),t([ut()],Jt.prototype,"type",void 0),t([ut({reflect:!0})],Jt.prototype,"value",void 0),t([mt()],Jt.prototype,"flipIcon",void 0);const Xt=n`:host{display:inline-flex;outline:none;-webkit-tap-highlight-color:rgba(0,0,0,0);height:var(--_container-height);width:var(--_container-width);justify-content:center}:host([touch-target=wrapper]){margin:max(0px,(48px - var(--_container-height))/2) max(0px,(48px - var(--_container-width))/2)}md-focus-ring{--md-focus-ring-shape-start-start: var(--_container-shape-start-start);--md-focus-ring-shape-start-end: var(--_container-shape-start-end);--md-focus-ring-shape-end-end: var(--_container-shape-end-end);--md-focus-ring-shape-end-start: var(--_container-shape-end-start)}:host([disabled]){pointer-events:none}.icon-button{place-items:center;background:none;border:none;box-sizing:border-box;cursor:pointer;display:flex;place-content:center;outline:none;padding:0;position:relative;text-decoration:none;user-select:none;z-index:0;flex:1;border-start-start-radius:var(--_container-shape-start-start);border-start-end-radius:var(--_container-shape-start-end);border-end-start-radius:var(--_container-shape-end-start);border-end-end-radius:var(--_container-shape-end-end)}.icon ::slotted(*){font-size:var(--_icon-size);height:var(--_icon-size);width:var(--_icon-size);font-weight:inherit}md-ripple{z-index:-1;border-start-start-radius:var(--_container-shape-start-start);border-start-end-radius:var(--_container-shape-start-end);border-end-start-radius:var(--_container-shape-end-start);border-end-end-radius:var(--_container-shape-end-end)}.flip-icon .icon{transform:scaleX(-1)}.icon{display:inline-flex}.link{height:100%;outline:none;position:absolute;width:100%}.touch{position:absolute;height:max(48px,100%);width:max(48px,100%)}:host([touch-target=none]) .touch{display:none}@media(forced-colors: active){:host([disabled]){--_disabled-icon-opacity: 1}}/*# sourceMappingURL=shared-styles.css.map */
`,Qt=n`:host{--_disabled-icon-color: var(--md-icon-button-disabled-icon-color, var(--md-sys-color-on-surface, #1d1b20));--_disabled-icon-opacity: var(--md-icon-button-disabled-icon-opacity, 0.38);--_icon-size: var(--md-icon-button-icon-size, 24px);--_selected-focus-icon-color: var(--md-icon-button-selected-focus-icon-color, var(--md-sys-color-primary, #6750a4));--_selected-hover-icon-color: var(--md-icon-button-selected-hover-icon-color, var(--md-sys-color-primary, #6750a4));--_selected-hover-state-layer-color: var(--md-icon-button-selected-hover-state-layer-color, var(--md-sys-color-primary, #6750a4));--_selected-hover-state-layer-opacity: var(--md-icon-button-selected-hover-state-layer-opacity, 0.08);--_selected-icon-color: var(--md-icon-button-selected-icon-color, var(--md-sys-color-primary, #6750a4));--_selected-pressed-icon-color: var(--md-icon-button-selected-pressed-icon-color, var(--md-sys-color-primary, #6750a4));--_selected-pressed-state-layer-color: var(--md-icon-button-selected-pressed-state-layer-color, var(--md-sys-color-primary, #6750a4));--_selected-pressed-state-layer-opacity: var(--md-icon-button-selected-pressed-state-layer-opacity, 0.12);--_state-layer-height: var(--md-icon-button-state-layer-height, 40px);--_state-layer-shape: var(--md-icon-button-state-layer-shape, 9999px);--_state-layer-width: var(--md-icon-button-state-layer-width, 40px);--_focus-icon-color: var(--md-icon-button-focus-icon-color, var(--md-sys-color-on-surface-variant, #49454f));--_hover-icon-color: var(--md-icon-button-hover-icon-color, var(--md-sys-color-on-surface-variant, #49454f));--_hover-state-layer-color: var(--md-icon-button-hover-state-layer-color, var(--md-sys-color-on-surface-variant, #49454f));--_hover-state-layer-opacity: var(--md-icon-button-hover-state-layer-opacity, 0.08);--_icon-color: var(--md-icon-button-icon-color, var(--md-sys-color-on-surface-variant, #49454f));--_pressed-icon-color: var(--md-icon-button-pressed-icon-color, var(--md-sys-color-on-surface-variant, #49454f));--_pressed-state-layer-color: var(--md-icon-button-pressed-state-layer-color, var(--md-sys-color-on-surface-variant, #49454f));--_pressed-state-layer-opacity: var(--md-icon-button-pressed-state-layer-opacity, 0.12);--_container-shape-start-start: 0;--_container-shape-start-end: 0;--_container-shape-end-end: 0;--_container-shape-end-start: 0;--_container-height: 0;--_container-width: 0;height:var(--_state-layer-height);width:var(--_state-layer-width)}:host([touch-target=wrapper]){margin:max(0px,(48px - var(--_state-layer-height))/2) max(0px,(48px - var(--_state-layer-width))/2)}md-focus-ring{--md-focus-ring-shape-start-start: var(--_state-layer-shape);--md-focus-ring-shape-start-end: var(--_state-layer-shape);--md-focus-ring-shape-end-end: var(--_state-layer-shape);--md-focus-ring-shape-end-start: var(--_state-layer-shape)}.standard{background-color:rgba(0,0,0,0);color:var(--_icon-color);--md-ripple-hover-color: var(--_hover-state-layer-color);--md-ripple-hover-opacity: var(--_hover-state-layer-opacity);--md-ripple-pressed-color: var(--_pressed-state-layer-color);--md-ripple-pressed-opacity: var(--_pressed-state-layer-opacity)}.standard:hover{color:var(--_hover-icon-color)}.standard:focus{color:var(--_focus-icon-color)}.standard:active{color:var(--_pressed-icon-color)}.standard:disabled{color:var(--_disabled-icon-color)}md-ripple{border-radius:var(--_state-layer-shape)}.standard:disabled .icon{opacity:var(--_disabled-icon-opacity)}.selected{--md-ripple-hover-color: var(--_selected-hover-state-layer-color);--md-ripple-hover-opacity: var(--_selected-hover-state-layer-opacity);--md-ripple-pressed-color: var(--_selected-pressed-state-layer-color);--md-ripple-pressed-opacity: var(--_selected-pressed-state-layer-opacity)}.selected:not(:disabled){color:var(--_selected-icon-color)}.selected:not(:disabled):hover{color:var(--_selected-hover-icon-color)}.selected:not(:disabled):focus{color:var(--_selected-focus-icon-color)}.selected:not(:disabled):active{color:var(--_selected-pressed-icon-color)}/*# sourceMappingURL=standard-styles.css.map */
`;let te=class extends Jt{getRenderClasses(){return{...super.getRenderClasses(),standard:!0}}};te.styles=[Xt,Qt],te=t([ct("md-icon-button")],te);class ee extends lt{constructor(){super(...arguments),this.inset=!1,this.insetStart=!1,this.insetEnd=!1}}t([ut({type:Boolean,reflect:!0})],ee.prototype,"inset",void 0),t([ut({type:Boolean,reflect:!0,attribute:"inset-start"})],ee.prototype,"insetStart",void 0),t([ut({type:Boolean,reflect:!0,attribute:"inset-end"})],ee.prototype,"insetEnd",void 0);const ie=n`:host{box-sizing:border-box;color:var(--md-divider-color, var(--md-sys-color-outline-variant, #cac4d0));display:flex;height:var(--md-divider-thickness, 1px);width:100%}:host([inset]),:host([inset-start]){padding-inline-start:16px}:host([inset]),:host([inset-end]){padding-inline-end:16px}:host::before{background:currentColor;content:"";height:100%;width:100%}@media(forced-colors: active){:host::before{background:CanvasText}}/*# sourceMappingURL=divider-styles.css.map */
`;let se=class extends ee{};function re(t,e=ce){const i=ae(t,e);return i&&(i.tabIndex=0,i.focus()),i}function oe(t,e=ce){const i=function(t,e=ce){for(let i=t.length-1;i>=0;i--){const s=t[i];if(e(s))return s}return null}(t,e);return i&&(i.tabIndex=0,i.focus()),i}function ne(t,e=ce){for(let i=0;i<t.length;i++){const s=t[i];if(0===s.tabIndex&&e(s))return{item:s,index:i}}return null}function ae(t,e=ce){for(const i of t)if(e(i))return i;return null}function le(t,e,i=ce){if(e){const s=function(t,e,i=ce){for(let s=1;s<t.length;s++){const r=t[(s+e)%t.length];if(i(r))return r}return t[e]?t[e]:null}(t,e.index,i);return s&&(s.tabIndex=0,s.focus()),s}return re(t,i)}function de(t,e,i=ce){if(e){const s=function(t,e,i=ce){for(let s=1;s<t.length;s++){const r=t[(e-s+t.length)%t.length];if(i(r))return r}return t[e]?t[e]:null}(t,e.index,i);return s&&(s.tabIndex=0,s.focus()),s}return oe(t,i)}function ce(t){return!t.disabled}se.styles=[ie],se=t([ct("md-divider")],se);const he={ArrowDown:"ArrowDown",ArrowLeft:"ArrowLeft",ArrowUp:"ArrowUp",ArrowRight:"ArrowRight",Home:"Home",End:"End"};class pe{constructor(t){this.handleKeydown=t=>{const e=t.key;if(t.defaultPrevented||!this.isNavigableKey(e))return;const i=this.items;if(!i.length)return;const s=ne(i,this.isActivatable);s&&(s.item.tabIndex=-1),t.preventDefault();const r=this.isRtl();switch(e){case he.ArrowDown:case r?he.ArrowLeft:he.ArrowRight:le(i,s,this.isActivatable);break;case he.ArrowUp:case r?he.ArrowRight:he.ArrowLeft:de(i,s,this.isActivatable);break;case he.Home:re(i,this.isActivatable);break;case he.End:oe(i,this.isActivatable)}},this.onDeactivateItems=()=>{const t=this.items;for(const e of t)this.deactivateItem(e)},this.onRequestActivation=t=>{this.onDeactivateItems();const e=t.target;this.activateItem(e),e.focus()},this.onSlotchange=()=>{const t=this.items;let e=!1;for(const i of t){!(!i.disabled&&i.tabIndex>-1)||e?i.tabIndex=-1:(e=!0,i.tabIndex=0)}if(e)return;const i=ae(t,this.isActivatable);i&&(i.tabIndex=0)};const{isItem:e,getPossibleItems:i,isRtl:s,deactivateItem:r,activateItem:o,isNavigableKey:n,isActivatable:a}=t;this.isItem=e,this.getPossibleItems=i,this.isRtl=s,this.deactivateItem=r,this.activateItem=o,this.isNavigableKey=n,this.isActivatable=a}get items(){const t=this.getPossibleItems(),e=[];for(const i of t){if(this.isItem(i)){e.push(i);continue}const t=i.item;t&&this.isItem(t)&&e.push(t)}return e}activateNextItem(){const t=this.items,e=ne(t,this.isActivatable);return e&&(e.item.tabIndex=-1),le(t,e,this.isActivatable)}activatePreviousItem(){const t=this.items,e=ne(t,this.isActivatable);return e&&(e.item.tabIndex=-1),de(t,e,this.isActivatable)}}const ue=new Set(Object.values(he));class me extends lt{get items(){return this.listController.items}constructor(){super(),this.listController=new pe({isItem:t=>t.hasAttribute("md-list-item"),getPossibleItems:()=>this.slotItems,isRtl:()=>"rtl"===getComputedStyle(this).direction,deactivateItem:t=>{t.tabIndex=-1},activateItem:t=>{t.tabIndex=0},isNavigableKey:t=>ue.has(t),isActivatable:t=>!t.disabled&&"text"!==t.type}),this.internals=this.attachInternals(),this.internals.role="list",this.addEventListener("keydown",this.listController.handleKeydown)}render(){return F`
      <slot
        @deactivate-items=${this.listController.onDeactivateItems}
        @request-activation=${this.listController.onRequestActivation}
        @slotchange=${this.listController.onSlotchange}>
      </slot>
    `}activateNextItem(){return this.listController.activateNextItem()}activatePreviousItem(){return this.listController.activatePreviousItem()}}t([yt({flatten:!0})],me.prototype,"slotItems",void 0);const ve=n`:host{background:var(--md-list-container-color, var(--md-sys-color-surface, #fef7ff));color:unset;display:flex;flex-direction:column;outline:none;padding:8px 0;position:relative}/*# sourceMappingURL=list-styles.css.map */
`;let fe=class extends me{};fe.styles=[ve],fe=t([ct("md-list")],fe);class ge extends lt{constructor(){super(...arguments),this.multiline=!1}render(){return F`
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline" @slotchange=${this.handleTextSlotChange}></slot>
        <slot
          class="default-slot"
          @slotchange=${this.handleTextSlotChange}></slot>
        <slot name="headline" @slotchange=${this.handleTextSlotChange}></slot>
        <slot
          name="supporting-text"
          @slotchange=${this.handleTextSlotChange}></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    `}handleTextSlotChange(){let t=!1,e=0;for(const i of this.textSlots)if(ye(i)&&(e+=1),e>1){t=!0;break}this.multiline=t}}function ye(t){for(const i of t.assignedNodes({flatten:!0})){var e;const t=i.nodeType===Node.ELEMENT_NODE,s=i.nodeType===Node.TEXT_NODE&&(null===(e=i.textContent)||void 0===e?void 0:e.match(/\S/));if(t||s)return!0}return!1}t([ut({type:Boolean,reflect:!0})],ge.prototype,"multiline",void 0),t([function(t){return(e,i)=>vt(e,i,{get(){return(this.renderRoot??gt??(gt=document.createDocumentFragment())).querySelectorAll(t)}})}(".text slot")],ge.prototype,"textSlots",void 0);const be=n`:host{color:var(--md-sys-color-on-surface, #1d1b20);font-family:var(--md-sys-typescale-body-large-font, var(--md-ref-typeface-plain, Roboto));font-size:var(--md-sys-typescale-body-large-size, 1rem);font-weight:var(--md-sys-typescale-body-large-weight, var(--md-ref-typeface-weight-regular, 400));line-height:var(--md-sys-typescale-body-large-line-height, 1.5rem);align-items:center;box-sizing:border-box;display:flex;gap:16px;min-height:56px;overflow:hidden;padding:12px 16px;position:relative;text-overflow:ellipsis}:host([multiline]){min-height:72px}[name=overline]{color:var(--md-sys-color-on-surface-variant, #49454f);font-family:var(--md-sys-typescale-label-small-font, var(--md-ref-typeface-plain, Roboto));font-size:var(--md-sys-typescale-label-small-size, 0.6875rem);font-weight:var(--md-sys-typescale-label-small-weight, var(--md-ref-typeface-weight-medium, 500));line-height:var(--md-sys-typescale-label-small-line-height, 1rem)}[name=supporting-text]{color:var(--md-sys-color-on-surface-variant, #49454f);font-family:var(--md-sys-typescale-body-medium-font, var(--md-ref-typeface-plain, Roboto));font-size:var(--md-sys-typescale-body-medium-size, 0.875rem);font-weight:var(--md-sys-typescale-body-medium-weight, var(--md-ref-typeface-weight-regular, 400));line-height:var(--md-sys-typescale-body-medium-line-height, 1.25rem)}[name=trailing-supporting-text]{color:var(--md-sys-color-on-surface-variant, #49454f);font-family:var(--md-sys-typescale-label-small-font, var(--md-ref-typeface-plain, Roboto));font-size:var(--md-sys-typescale-label-small-size, 0.6875rem);font-weight:var(--md-sys-typescale-label-small-weight, var(--md-ref-typeface-weight-medium, 500));line-height:var(--md-sys-typescale-label-small-line-height, 1rem)}[name=container]::slotted(*){inset:0;position:absolute}.default-slot{display:inline}.default-slot,.text ::slotted(*){overflow:hidden;text-overflow:ellipsis}.text{display:flex;flex:1;flex-direction:column;overflow:hidden}/*# sourceMappingURL=item-styles.css.map */
`;let xe=class extends ge{};xe.styles=[be],xe=t([ct("md-item")],xe);class _e extends lt{constructor(){super(...arguments),this.disabled=!1,this.type="text",this.isListItem=!0,this.href="",this.target=""}get isDisabled(){return this.disabled&&"link"!==this.type}willUpdate(t){this.href&&(this.type="link"),super.willUpdate(t)}render(){return this.renderListItem(F`
      <md-item>
        <div slot="container">
          ${this.renderRipple()} ${this.renderFocusRing()}
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        ${this.renderBody()}
      </md-item>
    `)}renderListItem(t){const e="link"===this.type;let i;switch(this.type){case"link":i=Ht`a`;break;case"button":i=Ht`button`;break;default:i=Ht`li`}const s="text"!==this.type,r=e&&this.target?this.target:K;return Bt`
      <${i}
        id="item"
        tabindex="${this.isDisabled||!s?-1:0}"
        ?disabled=${this.isDisabled}
        role="listitem"
        aria-selected=${this.ariaSelected||K}
        aria-checked=${this.ariaChecked||K}
        aria-expanded=${this.ariaExpanded||K}
        aria-haspopup=${this.ariaHasPopup||K}
        class="list-item ${It(this.getRenderClasses())}"
        href=${this.href||K}
        target=${r}
        @focus=${this.onFocus}
      >${t}</${i}>
    `}renderRipple(){return"text"===this.type?K:F` <md-ripple
      part="ripple"
      for="item"
      ?disabled=${this.isDisabled}></md-ripple>`}renderFocusRing(){return"text"===this.type?K:F` <md-focus-ring
      @visibility-changed=${this.onFocusRingVisibilityChanged}
      part="focus-ring"
      for="item"
      inward></md-focus-ring>`}onFocusRingVisibilityChanged(t){}getRenderClasses(){return{disabled:this.isDisabled}}renderBody(){return F`
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot
        name="trailing-supporting-text"
        slot="trailing-supporting-text"></slot>
    `}onFocus(){-1===this.tabIndex&&this.dispatchEvent(new Event("request-activation",{bubbles:!0,composed:!0}))}focus(){var t;null===(t=this.listItemRoot)||void 0===t||t.focus()}}jt(_e),_e.shadowRootOptions={...lt.shadowRootOptions,delegatesFocus:!0},t([ut({type:Boolean,reflect:!0})],_e.prototype,"disabled",void 0),t([ut({reflect:!0})],_e.prototype,"type",void 0),t([ut({type:Boolean,attribute:"md-list-item",reflect:!0})],_e.prototype,"isListItem",void 0),t([ut()],_e.prototype,"href",void 0),t([ut()],_e.prototype,"target",void 0),t([ft(".list-item")],_e.prototype,"listItemRoot",void 0);const $e=n`:host{display:flex;-webkit-tap-highlight-color:rgba(0,0,0,0);--md-ripple-hover-color: var(--md-list-item-hover-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--md-ripple-hover-opacity: var(--md-list-item-hover-state-layer-opacity, 0.08);--md-ripple-pressed-color: var(--md-list-item-pressed-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--md-ripple-pressed-opacity: var(--md-list-item-pressed-state-layer-opacity, 0.12)}:host(:is([type=button]:not([disabled]),[type=link])){cursor:pointer}md-focus-ring{z-index:1;--md-focus-ring-shape: 8px}a,button,li{background:none;border:none;cursor:inherit;padding:0;margin:0;text-align:unset;text-decoration:none}.list-item{border-radius:inherit;display:flex;flex:1;max-width:inherit;min-width:inherit;outline:none;-webkit-tap-highlight-color:rgba(0,0,0,0);width:100%}.list-item.interactive{cursor:pointer}.list-item.disabled{opacity:var(--md-list-item-disabled-opacity, 0.3);pointer-events:none}[slot=container]{pointer-events:none}md-ripple{border-radius:inherit}md-item{border-radius:inherit;flex:1;height:100%;color:var(--md-list-item-label-text-color, var(--md-sys-color-on-surface, #1d1b20));font-family:var(--md-list-item-label-text-font, var(--md-sys-typescale-body-large-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-list-item-label-text-size, var(--md-sys-typescale-body-large-size, 1rem));line-height:var(--md-list-item-label-text-line-height, var(--md-sys-typescale-body-large-line-height, 1.5rem));font-weight:var(--md-list-item-label-text-weight, var(--md-sys-typescale-body-large-weight, var(--md-ref-typeface-weight-regular, 400)));min-height:var(--md-list-item-one-line-container-height, 56px);padding-top:var(--md-list-item-top-space, 12px);padding-bottom:var(--md-list-item-bottom-space, 12px);padding-inline-start:var(--md-list-item-leading-space, 16px);padding-inline-end:var(--md-list-item-trailing-space, 16px)}md-item[multiline]{min-height:var(--md-list-item-two-line-container-height, 72px)}[slot=supporting-text]{color:var(--md-list-item-supporting-text-color, var(--md-sys-color-on-surface-variant, #49454f));font-family:var(--md-list-item-supporting-text-font, var(--md-sys-typescale-body-medium-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-list-item-supporting-text-size, var(--md-sys-typescale-body-medium-size, 0.875rem));line-height:var(--md-list-item-supporting-text-line-height, var(--md-sys-typescale-body-medium-line-height, 1.25rem));font-weight:var(--md-list-item-supporting-text-weight, var(--md-sys-typescale-body-medium-weight, var(--md-ref-typeface-weight-regular, 400)))}[slot=trailing-supporting-text]{color:var(--md-list-item-trailing-supporting-text-color, var(--md-sys-color-on-surface-variant, #49454f));font-family:var(--md-list-item-trailing-supporting-text-font, var(--md-sys-typescale-label-small-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-list-item-trailing-supporting-text-size, var(--md-sys-typescale-label-small-size, 0.6875rem));line-height:var(--md-list-item-trailing-supporting-text-line-height, var(--md-sys-typescale-label-small-line-height, 1rem));font-weight:var(--md-list-item-trailing-supporting-text-weight, var(--md-sys-typescale-label-small-weight, var(--md-ref-typeface-weight-medium, 500)))}:is([slot=start],[slot=end])::slotted(*){fill:currentColor}[slot=start]{color:var(--md-list-item-leading-icon-color, var(--md-sys-color-on-surface-variant, #49454f))}[slot=end]{color:var(--md-list-item-trailing-icon-color, var(--md-sys-color-on-surface-variant, #49454f))}@media(forced-colors: active){.disabled slot{color:GrayText}.list-item.disabled{color:GrayText;opacity:1}}/*# sourceMappingURL=list-item-styles.css.map */
`;let we=class extends _e{};we.styles=[$e],we=t([ct("md-list-item")],we);let Ae=class extends lt{render(){return j`
    <svg
      viewBox=${this.viewBox||"0 0 24 24"}
      preserveAspectRatio="xMidYMid meet"
      focusable="false"
      role="img"
      aria-hidden="true"
    >
      <g>
        ${this.path?j`<path class="primary-path" d=${this.path}></path>`:K}
        ${this.secondaryPath?j`<path class="secondary-path" d=${this.secondaryPath}></path>`:K}
      </g>
    </svg>`}static get styles(){return n`
      :host {
        display: var(--ha-icon-display, inline-flex);
        align-items: center;
        justify-content: center;
        position: relative;
        vertical-align: middle;
        fill: var(--icon-primary-color, currentcolor);
        width: var(--mdc-icon-size, 24px);
        height: var(--mdc-icon-size, 24px);
      }
      svg {
        width: 100%;
        height: 100%;
        pointer-events: none;
        display: block;
      }
      path.primary-path {
        opacity: var(--icon-primary-opactity, 1);
      }
      path.secondary-path {
        fill: var(--icon-secondary-color, currentcolor);
        opacity: var(--icon-secondary-opactity, 0.5);
      }
    `}};t([ut()],Ae.prototype,"path",void 0),t([ut()],Ae.prototype,"secondaryPath",void 0),t([ut()],Ae.prototype,"viewBox",void 0),Ae=t([ct("ha-svg-icon")],Ae);var Ce="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z",Ee="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z",Se=Number.isNaN||function(t){return"number"==typeof t&&t!=t};function Re(t,e){if(t.length!==e.length)return!1;for(var i=0;i<t.length;i++)if(s=t[i],r=e[i],!(s===r||Se(s)&&Se(r)))return!1;var s,r;return!0}let Ie=class extends lt{constructor(){super(...arguments),this.nodeEntries=function(t,e){void 0===e&&(e=Re);var i=null;function s(){for(var s=[],r=0;r<arguments.length;r++)s[r]=arguments[r];if(i&&i.lastThis===this&&e(s,i.lastArgs))return i.lastResult;var o=t.apply(this,s);return i={lastResult:o,lastArgs:s,lastThis:this},o}return s.clear=function(){i=null},s}((t=>Object.entries(t)))}render(){const t=this.nodeEntries(this.nodes),e=location.href.includes(":5580");return F`
      <div class="header">
        <div>Python Matter Server</div>
        <div class="actions">
        ${e?"":F`
          <md-icon-button @click=${this._disconnect}>
            <ha-svg-icon .path=${"M17 7L15.59 8.41L18.17 11H8V13H18.17L15.59 15.58L17 17L22 12M4 5H12V3H4C2.9 3 2 3.9 2 5V19C2 20.1 2.9 21 4 21H12V19H4V5Z"}></ha-svg-icon>
          </md-icon-button>
          `}
        </div>
      </div>
      <div class="container">
        <md-list>
          <md-list-item type="link" href=${"#server"}>
            <span slot="start"></span>
            <div slot="headline">Matter Server</div>
            <div slot="supporting-text">
              ${this.client.serverInfo.sdk_version}
            </div>
            <ha-svg-icon slot="end" .path=${Ee}></ha-svg-icon>
          </md-list-item>
          <md-divider></md-divider>
          ${t.map((([t,e])=>F`
              <md-list-item type="link" href=${`#node/${e.node_id}`}>
                <span slot="start">${e.node_id}</span>
                <div slot="headline">
                  ${e.vendorName} ${e.productName}
                  ${e.available?"":F`<span class="status">OFFLINE</span>`}
                </div>
                <div slot="supporting-text">${e.serialNumber}</div>
                <ha-svg-icon slot="end" .path=${Ee}></ha-svg-icon>
              </md-list-item>
            `))}
        </md-list>
      </div>
      <div class="footer">
        Python Matter Server is a project by Nabu Casa.
        <a href="https://www.nabucasa.com">Fund development</a>
      </div>
    `}_disconnect(){localStorage.removeItem("matterURL"),location.reload()}};function Pe(t,e,i){return import("./dialog-box-3QS-wG6x.js"),new Promise((t=>{const s=document.createElement("dialox-box");s.params=i,s.dialogResult=t,s.type=e,document.body.appendChild(s)}))}Ie.styles=n`
    :host {
      display: flex;
      background-color: var(--md-sys-color-background);
      box-sizing: border-box;
      flex-direction: column;
      min-height: 100vh;
    }

    .header {
      background-color: var(--md-sys-color-primary);
      color: var(--md-sys-color-on-primary);
      --icon-primary-color: var(--md-sys-color-on-primary);
      font-weight: 400;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-left: 16px;
      padding-right: 8px;
      height: 48px;
    }

    .container {
      padding: 16px;
      max-width: 600px;
      margin: 0 auto;
      flex: 1;
      width: 100%;
    }

    @media (max-width: 600px) {
      .container {
        padding: 16px 0;
      }
    }

    span[slot="start"] {
      width: 40px;
      text-align: center;
    }

    .status {
      color: var(--danger-color);
      font-weight: bold;
      font-size: 0.8em;
    }

    .footer {
      padding: 16px;
      text-align: center;
      font-size: 0.8em;
      color: var(--md-sys-color-on-surface);
    }

    .footer a {
      color: var(--md-sys-color-on-surface);
    }
  `,t([ut()],Ie.prototype,"nodes",void 0),Ie=t([ct("matter-dashboard")],Ie);const ke=(t,e)=>Pe(0,"alert",e);let Te=class extends lt{render(){return this.node?F`
      <div class="header">
        <a href="#">
          <md-icon-button>
            <ha-svg-icon .path=${Ce}></ha-svg-icon>
          </md-icon-button>
        </a>

        <div>Node ${this.node.node_id}</div>
        <div class="flex"></div>
        <div class="actions">
          <md-icon-button @click=${this._reinterview} title="Reinterview node">
            <ha-svg-icon .path=${"M12,3C17.5,3 22,6.58 22,11C22,15.42 17.5,19 12,19C10.76,19 9.57,18.82 8.47,18.5C5.55,21 2,21 2,21C4.33,18.67 4.7,17.1 4.75,16.5C3.05,15.07 2,13.13 2,11C2,6.58 6.5,3 12,3M17,12V10H15V12H17M13,12V10H11V12H13M9,12V10H7V12H9Z"}></ha-svg-icon>
          </md-icon-button>
        </div>
      </div>
      <div class="container">
        <pre>${JSON.stringify(this.node.data,void 0,2)}</pre>
      </div>
    `:F`
        <p>Node not found!</p>
        <button
          @click=${()=>{history.back()}}
        >
          Back
        </button>
      `}async _reinterview(){var t;if(await(t={title:"Reinterview",text:"Are you sure you want to reinterview this node?",confirmText:"Reinterview"},Pe(0,"prompt",t)))try{await this.client.interviewNode(this.node.node_id),ke(0,{title:"Reinterview node",text:"Success!"})}catch(t){ke(0,{title:"Failed to reinterview node",text:t.message})}}};Te.styles=n`
    :host {
      display: block;
      background-color: var(--md-sys-color-background);
    }

    .header {
      background-color: var(--md-sys-color-primary);
      color: var(--md-sys-color-on-primary);
      --icon-primary-color: var(--md-sys-color-on-primary);
      font-weight: 400;
      display: flex;
      align-items: center;
      padding-right: 8px;
      height: 48px;
    }

    md-icon-button {
      margin-right: 8px;
    }

    .flex {
      flex: 1;
    }

    .container {
      padding: 16px;
      max-width: 600px;
      margin: 0 auto;
    }
  `,t([ut()],Te.prototype,"node",void 0),Te=t([ct("matter-node-view")],Te);let Le=class extends lt{render(){return F`
      <div class="header">
        <a href="#">
          <md-icon-button>
            <ha-svg-icon .path=${Ce}></ha-svg-icon>
          </md-icon-button>
        </a>

        <div>Matter Server</div>
        <div class="flex"></div>
        <div class="actions"></div>
      </div>
      <div class="container">
        <pre>${JSON.stringify(this.client.serverInfo,void 0,2)}</pre>
      </div>
    `}};Le.styles=n`
    :host {
      display: flex;
      background-color: var(--md-sys-color-background);
      box-sizing: border-box;
      flex-direction: column;
      min-height: 100vh;
    }

    .header {
      background-color: var(--md-sys-color-primary);
      color: var(--md-sys-color-on-primary);
      --icon-primary-color: var(--md-sys-color-on-primary);
      font-weight: 400;
      display: flex;
      align-items: center;
      padding-right: 8px;
      height: 48px;
    }

    md-icon-button {
      margin-right: 8px;
    }

    .flex {
      flex: 1;
    }

    .container {
      padding: 16px;
      max-width: 600px;
      margin: 0 auto;
      flex: 1;
    }
  `,Le=t([ct("matter-server-view")],Le);let Ne=class extends lt{constructor(){super(...arguments),this._route={prefix:"",path:""},this._state="connecting"}firstUpdated(t){super.firstUpdated(t),this.client.startListening().then((()=>{this._state="connected",this.client.addEventListener("nodes_changed",(()=>this.requestUpdate()))}),(t=>{this._state="error",this._error=t.message}));const e=()=>{let[t,e]=location.hash.substring(1).split("/",2);void 0===e&&(e=t,t=""),this._route={prefix:t,path:e}};window.addEventListener("hashchange",e),e()}render(){return"connecting"===this._state?F`<p>Connecting...</p>`:"error"===this._state?F`
        <p>Error: ${this._error}</p>
        <button @click=${this._clearLocalStorage}>Clear stored URL</button>
      `:"node"===this._route.prefix?F`
        <matter-node-view
          .client=${this.client}
          .node=${this.client.nodes[parseInt(this._route.path,10)]}
        ></matter-node-view>
      `:"server"===this._route.path?F`
        <matter-server-view .client=${this.client}></matter-server-view>
      `:F`<matter-dashboard
      .client=${this.client}
      .nodes=${this.client.nodes}
      .route=${this._route}
    ></matter-dashboard>`}_clearLocalStorage(){localStorage.removeItem("matterURL"),location.reload()}};t([mt()],Ne.prototype,"_route",void 0),t([mt()],Ne.prototype,"_state",void 0),Ne=t([ct("matter-dashboard-app")],Ne);var ze=Object.freeze({__proto__:null});export{Pt as E,K as T,t as _,mt as a,It as b,Gt as c,qt as d,ft as e,ze as f,n as i,Wt as m,ut as n,yt as o,jt as r,lt as s,ct as t,F as x};
