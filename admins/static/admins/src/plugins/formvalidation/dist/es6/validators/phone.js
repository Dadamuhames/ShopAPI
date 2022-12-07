import s from"../utils/format";export default function e(){const e=["AE","BG","BR","CN","CZ","DE","DK","ES","FR","GB","IN","MA","NL","PK","RO","RU","SK","TH","US","VE"];return{validate(t){if(t.value===""){return{valid:true}}const a=Object.assign({},{message:""},t.options);const d=t.value.trim();let r=d.substr(0,2);if("function"===typeof a.country){r=a.country.call(this)}else{r=a.country}if(!r||e.indexOf(r.toUpperCase())===-1){return{valid:true}}let c=true;switch(r.toUpperCase()){case"AE":c=/^(((\+|00)?971[\s.-]?(\(0\)[\s.-]?)?|0)(\(5(0|2|5|6)\)|5(0|2|5|6)|2|3|4|6|7|9)|60)([\s.-]?[0-9]){7}$/.test(d);break;case"BG":c=/^(0|359|00)(((700|900)[0-9]{5}|((800)[0-9]{5}|(800)[0-9]{4}))|(87|88|89)([0-9]{7})|((2[0-9]{7})|(([3-9][0-9])(([0-9]{6})|([0-9]{5})))))$/.test(d.replace(/\+|\s|-|\/|\(|\)/gi,""));break;case"BR":c=/^(([\d]{4}[-.\s]{1}[\d]{2,3}[-.\s]{1}[\d]{2}[-.\s]{1}[\d]{2})|([\d]{4}[-.\s]{1}[\d]{3}[-.\s]{1}[\d]{4})|((\(?\+?[0-9]{2}\)?\s?)?(\(?\d{2}\)?\s?)?\d{4,5}[-.\s]?\d{4}))$/.test(d);break;case"CN":c=/^((00|\+)?(86(?:-| )))?((\d{11})|(\d{3}[- ]{1}\d{4}[- ]{1}\d{4})|((\d{2,4}[- ]){1}(\d{7,8}|(\d{3,4}[- ]{1}\d{4}))([- ]{1}\d{1,4})?))$/.test(d);break;case"CZ":c=/^(((00)([- ]?)|\+)(420)([- ]?))?((\d{3})([- ]?)){2}(\d{3})$/.test(d);break;case"DE":c=/^(((((((00|\+)49[ \-/]?)|0)[1-9][0-9]{1,4})[ \-/]?)|((((00|\+)49\()|\(0)[1-9][0-9]{1,4}\)[ \-/]?))[0-9]{1,7}([ \-/]?[0-9]{1,5})?)$/.test(d);break;case"DK":c=/^(\+45|0045|\(45\))?\s?[2-9](\s?\d){7}$/.test(d);break;case"ES":c=/^(?:(?:(?:\+|00)34\D?))?(?:5|6|7|8|9)(?:\d\D?){8}$/.test(d);break;case"FR":c=/^(?:(?:(?:\+|00)33[ ]?(?:\(0\)[ ]?)?)|0){1}[1-9]{1}([ .-]?)(?:\d{2}\1?){3}\d{2}$/.test(d);break;case"GB":c=/^\(?(?:(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?\(?(?:0\)?[\s-]?\(?)?|0)(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}|\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4}|\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3})|\d{5}\)?[\s-]?\d{4,5}|8(?:00[\s-]?11[\s-]?11|45[\s-]?46[\s-]?4\d))(?:(?:[\s-]?(?:x|ext\.?\s?|#)\d+)?)$/.test(d);break;case"IN":c=/((\+?)((0[ -]+)*|(91 )*)(\d{12}|\d{10}))|\d{5}([- ]*)\d{6}/.test(d);break;case"MA":c=/^(?:(?:(?:\+|00)212[\s]?(?:[\s]?\(0\)[\s]?)?)|0){1}(?:5[\s.-]?[2-3]|6[\s.-]?[13-9]){1}[0-9]{1}(?:[\s.-]?\d{2}){3}$/.test(d);break;case"NL":c=/^((\+|00(\s|\s?-\s?)?)31(\s|\s?-\s?)?(\(0\)[-\s]?)?|0)[1-9]((\s|\s?-\s?)?[0-9])((\s|\s?-\s?)?[0-9])((\s|\s?-\s?)?[0-9])\s?[0-9]\s?[0-9]\s?[0-9]\s?[0-9]\s?[0-9]$/gm.test(d);break;case"PK":c=/^0?3[0-9]{2}[0-9]{7}$/.test(d);break;case"RO":c=/^(\+4|)?(07[0-8]{1}[0-9]{1}|02[0-9]{2}|03[0-9]{2}){1}?(\s|\.|-)?([0-9]{3}(\s|\.|-|)){2}$/g.test(d);break;case"RU":c=/^((8|\+7|007)[-./ ]?)?([(/.]?\d{3}[)/.]?[-./ ]?)?[\d\-./ ]{7,10}$/g.test(d);break;case"SK":c=/^(((00)([- ]?)|\+)(421)([- ]?))?((\d{3})([- ]?)){2}(\d{3})$/.test(d);break;case"TH":c=/^0\(?([6|8-9]{2})*-([0-9]{3})*-([0-9]{4})$/.test(d);break;case"VE":c=/^0(?:2(?:12|4[0-9]|5[1-9]|6[0-9]|7[0-8]|8[1-35-8]|9[1-5]|3[45789])|4(?:1[246]|2[46]))\d{7}$/.test(d);break;case"US":default:c=/^(?:(1-?)|(\+1 ?))?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$/.test(d);break}return{message:s(t.l10n&&t.l10n.phone?a.message||t.l10n.phone.country:a.message,t.l10n&&t.l10n.phone&&t.l10n.phone.countries?t.l10n.phone.countries[r]:r),valid:c}}}}