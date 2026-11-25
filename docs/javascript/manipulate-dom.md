# Manipulera DOM med JavaScript

I DOM (Document Object Model) kopplas olika noder (element) till varandra genom förälder-, barn- och syskonrelationer. Titta på följande exempel:

```html
<body>
    <header></header>
    <main></main>
    <footer></footer>
</body>
```

Vi kan säga att `<body>` har tre barnnoder: `<header>`, `<main>` och `<footer>`. Dessa tre är förresten syskon till varandra och `<body>` är deras förälder. Nu när vi förstår hur relationerna fungerar i DOM kan vi börja manipulera element genom att ta bort dem eller skapa och klistra in nya element.

---

## Ta bort ett element från DOM

Att ta bort ett element från DOM är egentligen ganska enkelt. Som vanligt plockar man elementet med någon av metoderna som motsvarar `querySelector` eller `getElementBy...`. Därefter kör man metoden `.remove()`:

```js
document.querySelector("header").remove();
```

---

## Skapa ett nytt element

Man kan göra lite olika beroende på hur man vill hantera det. Man kan såklart klistra in en sträng som `innerHTML`, men jag har redan skrivit att `innerHTML` kan innebära en säkerhetsrisk. Vi kan därför använda ett lite mer "programmistiskt" sätt:

/// tab | JavaScript

```js
const headingElement = document.createElement("h1");
headingElement.textContent = "Hello World!";
// här kan vi lägga till attribut, klasser osv
// på samma sätt som om vi skulle arbeta med ett
// befintligt element

document.querySelector("main").appendChild(headingElement);
```

///
/// tab | Resultat i HTML

```html
<body>
    <header></header>
    <main>
        <h1>Hello World!</h1>
    </main>
    <footer></footer>
</body>
```

///

Som du ser använder vi oss huvudsakligen av två metoder: `.createElement()` som skapar ett element i minnet, men lägger inte till det i DOM-trädet; och `.appendChild()` som faktiskt klistrar in elementet sist inuti föräldrarelementet och därmed inkluderar det i DOM-trädet.

---

## Andra metoder som kan vara användbara

Det finns en del. Jag kan nämna följande:

- `.cloneNode()` - skapar en kopia av en nod  
- `.hasChildNodes()` - returnerar `true` om noden har några barn, annars returnerar `false`  
- `.removeChild()` - tar bort en specifik barn-nod  
- `.replaceChild()` - ersätter en barnnod med en annan

Mer information finns i följande extern resurs:

> [Node - Instance methods](https://developer.mozilla.org/en-US/docs/Web/API/Node#instance_methods) `MDN`  
