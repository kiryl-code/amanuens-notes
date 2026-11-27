# Events

För att göra sidan reaktiv och interaktiv, alltså reagera på användarens handlingar, kan man använda **events** som kan ske på olika element. Precis som det ofta brukar vara med frontend är det väldigt många olika event man kan lyssna på på olika element, så jag kommer att nämna bara några. För fler exempel och fullständig dokumentation, kika på MDN.

## DOMContentLoaded & allmän syntax

På sidan om hur man kopplar JavaScript har jag redan visat det här eventet. Vi använder samma kod för att se hur vi registrerar olika events:

```js
function callback(e) {
    // gör någonting...
}

document.addEventListener("DOMContentLoaded", callback)
```

Det är metoden `.addEventListener()` som används för att lyssna på events. Metoden kan anropas på vilket som helst element som du plockar med `.querySelector()` eller `.getElementBy...()`. Den första parametern som skickas är ett namn på eventet och den andra parametern är funktionen som ska köras när eventet inträffar. JavaScript kommer att skicka `Event`-objektet som första parametern i callbacken. Om man vet att man inte kommer behöva information om eventet, kan man skippa argumentet. Objektet innehåller ofta en referens till elementet som orsakade eventet och några standardmetoder. Man kan såklart även använda anonyma funktioner:

///tab | Anonym funktion
```js
document.addEventListener("DOMContentLoaded", function(e) {
   // gör någonting... 
});
```
```js
document.addEventListener("DOMContentLoaded", function() {
   // gör någonting... 
});
```
/// 

///tab | Lambda

```js
document.addEventListener("DOMContentLoaded", e => {
    // gör någonting
});
```
```js
document.addEventListener("DOMContentLoaded", () => {
    // gör någonting
});
```
///

---

## Andra events

| Event    | Förklaring                                                                                                                                                                                                         | Exempel                                                                                             |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| `click`  | Inträffar när användaren klickar på elementet. Förresten, det behöver inte vara `<button>` eller ett annat klickbart element. Eventet kan registreras även för ett `<div>` och för vilket annat element som helst. | `document.querySelector("#clickable").addEventListener("click", e => {});`                          |
| `input`  | Inträffar när `value` på `input`, `select` eller `textarea` ändras.                                                                                                                                                | `document.querySelector("#email").addEventListener("input", e => {});`                              |
| `submit` | Inträffas när ett formuläret skickas. `preventDefault()` används ofta för att hinna göra något innan själva förfrågningen med formulärdatan skickas.                                                               | `document.querySelector("form").addEventListener("submit", e => {e. preventDefault(); /* ... */});` |
| `reset`  | Inträffas när användare återstället formuläret, exempelvis genom att klicka på `<button type="reset">`.                                                                                                            | `document.querySelector("form").addEventListener("reset", e => {});`                                |

