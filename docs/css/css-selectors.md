# CSS-selectors

För att kunna styla olika element behöver vi kunna komma åt dem från vår CSS-kod. Som vanligt kan man använda lite olika metoder, beroende på vilka element man vill manipulera.

---

## Element

Den mest grundläggande selektorn väljer alla element utifrån deras namn. Då anger man bara elementets namn, till exempel:

```css
p {
    color: green;
}
```

Den här koden kommer att färga all text som ligger inuti alla `<p>`-element i ::green | grön::. Detta påverkar alltså samtliga element av den angivna typen.

---

## Id

Vill man endast ändra ett specifikt element utan att de andra påverkas kan man ge elementet ett `id` (`id="menu"`) och välja det på följande sätt:

```css
#menu {
    background-color: yellow;
}
```

Det är alltså `#` följt av samma `id` som man skriver som HTML-attribut som väljer ett element och tillämpar stilar på det. Eftersom det endast får finnas ett element med samma `id` kommer bara ett element att påverkas.

---

## Class

Man kan även välja alla element med samma `class`-attribut. Till exempel kan man använda följande syntax om man vill att vissa texter ska bli fetmarkerade (och använda `class="text-bold"` på dem i HTML):

```css
.text-bold {
    font-weight: bold;
}
```

---

Dessa tre selektorer kommer du att använda mest, eftersom de ger möjlighet att styla både enskilda element och grupper av element.

---

## Barnselektorer

Man kan även använda relationer mellan HTML-element för att komma åt specifika element i en specifik struktur. Om du till exempel vill ändra `text-decoration` för alla numrerade listor utan att påverka punktlistor kan du använda följande selektor:

```css
ol > li {
    text-decoration: underline;
}
```

Eftersom `<li>` är ett barn till `<ol>` kommer alla `<li>` som ligger direkt inuti `<ol>` att påverkas. De `<li>`-element som tillhör `<ul>` kommer däremot inte att påverkas, eftersom de inte ligger inuti `<ol>`.

`>` väljer endast direkta barn. Om liststrukturen innehåller en nästlad lista kommer selektorn inte att välja alla `<li>` i den nästlade listan genom samma relation. Om du i stället använder ett mellanslag väljs alla `<li>`-element som ligger inuti `<ol>`, även de som ligger djupare i strukturen:

```css
ol li {
    text-decoration: underline;
}
```

---

## Attributselektorer
Ibland vill man styla element med specifika attribut. Detta är särskilt användbart när man skriver stilar för ett formulär. Då skriver man attributet och dess värde inuti `[]`. Om attributet saknar ett värde (till exempel `required`) skriver man bara attributets namn. Till exempel:

```css
input[type="text"] {
    border-radius: 16px;
}

input[required] {
    border-color: red;
}

button[disabled] {
    display: none;
}
```

---

## Universell selektor
En universell selektor används för att tillämpa vissa stilar på samtliga element. Den används oftast för att exempelvis nollställa webbläsarens standardinställningar, såsom mellanrum. Man använder helt enkelt `*`:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: sans-serif;
}
```

---

## Prioritering (specificity)

När det finns så här många olika sätt att använda CSS-selektorer kan man börja fundera på vad som händer när flera regler krockar med varandra. Till exempel, vad händer om man ändrar textfärgen till grön för alla `<a>`, men vill sätta textfärgen till gul för alla `<a class="yellowLink">`? Det kanske dessutom finns ytterligare ett element: `<a class="yellowLink" id="uniquePurpleLink" style="color: red;">`. Hur fungerar det här då?

I CSS finns det strikta regler för hur stilarna tillämpas. För regler med samma specificitet och vikt gäller att de som kommer längst ner i samma CSS-dokument prioriteras över de som kommer högre upp. Till exempel:

```css
a {
    color: green;
}

.yellowLink {
    color: yellow;
}
```

Den här koden kommer att ändra textfärgen för alla `<a>`-element till ::green | grönt::. För alla element med `class="yellowLink"` kommer textfärgen istället att ändras till ::#FFC000 | gult::, till och med för `<a class="yellowLink">`.

När CSS anges på flera ställen gäller följande prioriteringsregler i vanliga fall (från lägre till högre prioritet):

- Universell selektor `*`
- Elementselektor, exempelvis `p`
- Klass-, attribut- eller pseudoklassselektor, exempelvis `.class_name` eller `[type="text"]`
- ID-selektor, exempelvis `#id_name`
- Inline-stilar, exempelvis `<ELEMENT style="...">`

### `!important`

`!important` kan användas efter ett CSS-egenskapsvärde för att ge deklarationen högre prioritet. Om vi tar det tidigare exemplet och lägger till `!important`:

```css
a {
    color: green !important;
}

.yellowLink {
    color: yellow;
}
```

Då kommer det inte att spela någon roll att ett `<a>`-element har klassen `yellowLink`. Texten kommer ändå vara grön. I generiska stilmallar rekommenderas det att undvika `!important` för att inte skapa en massa konflikter, men det finns vissa situationer där `!important` kan behövas.

---

## Externa resurser

> [Introduction to CSS syntax: declarations, rulesets, and statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction) `MDN`  
> [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties) `MDN`  
> [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity) `MDN`  

---

## Quiz

Testa dina kunskaper om du vill! [Eller öppna som en separat sida](../../exercises/css/selectors.html)

<iframe style="border: medium none currentcolor;" src="../../exercises/css/selectors.html" width="100%" height="600"></iframe>