# Hur kommer man åt HTML-element från JavaScript?

Till att börja med är det värt att nämna att hela HTML-dokumentet representeras av ett DOM-element, där DOM står för _document object model_. Man kan komma åt det här elementet genom ett globalt objekt `document` i JavaScript. Objektet innehåller en massa egenskaper och metoder som kan vara användbara för att komma åt saker på sidan. Beroende på vad man behöver komma åt och vilka metoder man vill använda kan man välja olika tillvägagångssätt.

---

## `getElementsByTagName`

Precis som det låter returnerar metoden en lista av noder av ett specificerat element. Till exempel, om man vill välja alla bilder som finns på sidan:

```js
const imgElements = document.getElementsByTagName("img");
```

!!!!warning
***OBS!*** Den här metoden returnerar **en lista**, oavsett hur många sådana element faktiskt finns på en sida. Du kan alltså inte skriva `imgElements.alt`, detta kommer att returnera `undefined`. Vill du komma åt alla alternativa texter måste du loopa igenom alla bilder.
!!!!

---

## `getElementsByClassName`

Precis som i CSS kan man välja alla element som har en specifik klass:

```js
const containers = document.getElementsByClassName("container");
```

!!!!warning
***OBS!*** Den här metoden returnerar **en lista**, oavsett hur många sådana element faktiskt finns på en sida. Jag kommer att upprepa informationen om returvärdet för samtliga metoder, eftersom det brukar skapa massa problem och förvirring innan man blir van vid hur de funkar.
!!!!

---

## `getElementById`

Den här metoden, till skillnad från de andra, returnerar _bara ett enda element_ som har ett specifikt id:

```js
const actionButton = document.getElementById("action-button");
```

---

## `querySelector` & `querySelectorAll`

De två metoderna är mina personliga favoriter, eftersom de helt ersätter de tre alternativ som presenterades ovan. Med `querySelector` och `querySelectorAll` använder man dessutom samma selectors som i CSS, vilket jag tycker är smidigt.

!!!!warning
`querySelector` returnerar **ett enda element**. Väljer man elementen efter deras elementnamn eller klass kommer bara den första träffen att returneras.

`querySelectorAll` returnerar **en lista** av element som matchar dina selectors.
!!!!

```javascript
const imgElements = document.querySelectorAll("img");
const containers = document.querySelectorAll(".container");
const actionButton = document.querySelector("#action-button");
```

---

## Välja element i subträd

`document` är inte det enda objektet som används för att välja andra element. Man kan välja element som ligger i subträd, till exempel om man har följande struktur:

```html
<body>
    <div class="container">
        ...
    </div>
    <form action="">
        <div class="container">
            ...
        </div>
    </form>
</body>
```

kan vi enkelt koppla JavaScript-kod som endast jobbar mot `<form>` och dess `.container`, men som inte har någon effekt på det `div.container` som är direkt barn till `<body>`:

```javascript
const form = document.querySelector("form");
const formContainer = form.querySelector(".container");
//                    ^ inte document, utan ett annat element
```
