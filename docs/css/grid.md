# Grid

Grid är ytterligare en modern teknik som används för att positionera element på sidan. Precis som namnet antyder använder grid ett rutnät och placerar elementen i "celler" i rutnätet.

---

## Startkod och layoutsbeskrivning

Precis som med Flexbox behöver vi göra en behållare till en grid-behållare. Vi gör det direkt i startkoden.

^^^^Grid, startkod
```html
<body>
    <header></header>
    <nav></nav>
    <main></main>
    <footer></footer>
</body>
```

```css
* {
    /* 
    I stort sett behövs inte, men jag använder
    detta för att kunna visa den renderade exempel 
    utan några onödiga scrollbars som följer med
    när jag sätter <body>s dimensioner till hela fönstret
    */
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    width: 100vw;

    display: grid;
}

header, nav, main, footer {
    border: 1px solid black;
}
```

Vi markerar alla element med `border` för att kunna se var de faktiskt ligger.

<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-initial.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-initial.html)
^^^^

Nu kan vi börja sätta layouten för vårt rutnät. I det här fallet vill jag att `<header>` ska finnas längst upp, `<footer>` längst ner och att navigationsmenyn ska ligga till vänster om huvudinnehållet. Säg att menyn ska ta 1/4 av behållarens bredd. Då översätter vi detta till grid.

## Kolumner

Det första steget är att sätta `grid-template-columns` som beskriver hur sidan ska delas upp i X-led:

```css
body {
    height: 100vh;
    width: 100vw;
    display: grid;
    
    grid-template-columns: 1fr 3fr;
}
```

Man kan tänka på `fr` som "delar". Totalt har vi 4 jämna delar av det tillgängliga utrymmet, eftersom `1+3=4`. Den första kolumnen tar då 1/4 av det utrymmet (1 del) och den andra kolumnen tar 3/4 (3 delar).

Det är viktigt att `fr` handlar om det utrymme som finns tillgängligt i grid-behållaren. Om man sätter `width=100px` blir alltså `1fr = 25px`.

^^^^Flera exempel
Det är egentligen inget mer än enkel matematik som ligger bakom `fr`.

```css
grid-template-columns: 5fr 2fr;
```

Den här koden kommer att dela upp behållaren i 7 jämna delar, varav de första 5 utgör den första kolumnen och de resterande 2 utgör den andra kolumnen.

```css
grid-template-columns: 1fr 1fr 1fr;
```

Totalt tre kolumner. Varje kolumn tar exakt 1/3 av det tillgängliga utrymmet.

```css
grid-template-columns: 1fr 1fr;
```

Båda kolumnerna tar exakt hälften av det tillgängliga utrymmet.
^^^^

^^^^Så här ser det ut nu
<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-template-columns.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-template-columns.html)
^^^^

Som du kan se när du skapar en sådan kod hamnar nu `<header>` och `<main>` i den första kolumnen, medan `<nav>` och `<footer>` hamnar i den andra kolumnen. Det beror på att grid automatiskt placerar elementen ett efter ett i rutnätet i den ordning de förekommer i HTML-koden.

---

## Sträcka element med `span`

Vi kan enkelt fixa detta genom att säga till både `<header>` och `<footer>` att sträcka sig över båda kolumnerna så att de hamnar på sina platser högst upp respektive längst ner. Vi använder `grid-column: span X;` för att få ett element att sträcka sig över `X` kolumner:

```css
header, footer {
    grid-column: span 2;
}
```

^^^^Så här ser det ut

<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-template-columns-span.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-template-columns-span.html)

---

Om du vill ha en lite tydligare version, där jag har lagt till lite CSS och HTML för att visa vilka block som motsvarar vilka element:

<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-column-span-with-labels.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-column-span-with-labels.html)

^^^^

## Rader

Man kanske vill bygga vidare på det här exemplet och göra så att `<header>` och `<footer>` tar något mindre plats. Då kan man ändra storleken på raderna istället. Principen är densamma, men man sätter `grid-template-rows` istället. Vi kan alltså göra så här:

```css
body {
    height: 100vh;
    width: 100vw;
    display: grid;
    grid-template-columns: 1fr 3fr;

    grid-template-rows: auto 1fr auto;
}
```

`auto` innebär att storleken på raden anpassas efter innehållet och andra faktorer som påverkar radens storlek. `<main>` ska nu placeras mellan `<header>` och `<footer>` och kommer att ta upp hela återstående tillgängliga utrymmet, medan `<header>` och `<footer>` endast tar så mycket höjd som de behöver för att göra sitt innehåll synligt.

^^^^Så här ser det ut
<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-template-rows-labeled.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-template-rows-labeled.html)
^^^^

---

## Mellanrum med `gap`

På samma sätt som i flexbox kan vi manuellt ange mellanrum mellan elementen i rutnätet med `gap`:

```css
body {
    height: 100vh;
    width: 100vw;
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-template-rows: auto 1fr auto;
    
    gap: 16px;
}
```

^^^^Så här ser det ut
<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-gap.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-gap.html)
^^^^

---

## TL;DR

Sammanfattningsvis definierar man med hjälp av grid ett rutnät:

- `grid-template-columns` - kolumner
- `grid-template-rows` - rader

Därefter placeras elementen ett efter ett i rutnätet. Man kan sträcka ett element över flera kolumner eller rader (eller både rader och kolumner) med hjälp av:

- `grid-column: span X;`
- `grid-row: span X;`

Där `X` är antalet kolumner eller rader som elementet ska sträcka sig över.

Mellanrum mellan cellerna i rutnätet kan sättas med `gap`.

---

## Ett extra exempel

Innan du kollar på koden, tänk på hur man kan skapa följande layout:

<iframe style="border: medium none currentcolor;" src="../../demo/grid/grid-extra-example.html" width="100%" height="400" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](../../demo/grid/grid-extra-example.html)

^^^^Facit

Här är det viktigt att förstå hur grid hanterar automatisk placering. När `<nav>` sträcker sig över tre rader upptar det även utrymme i rader där andra element ska placeras. Grid försöker då hitta lediga platser för återstående elementen och kan vid behov skapa "implicita" rader eller kolumner. Det innebär att det faktiska resultatet inte alltid blir som man först tänkt sig. Därför är det bra att kontrollera hur elementen placeras när man använder `<span>`.

```html
<body>
    <header></header>
    <nav></nav>
    <main></main>
    <footer></footer>
</body>
```

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    width: 100vw;
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-template-rows: auto 1fr auto;
}

header, nav, main, footer {
    border: 1px solid black;
}

nav {
    /* Det är den här raden som gör magin */
    grid-row: span 3;
}
```
^^^^

---

## Externa resurser

> Det är en lång video, men den går igenom allt i detalj och tar upp några saker som inte nämns på den här sidan. Rekommenderar starkt om du verkligen vill lära dig grid.  
> [CSS Grid Crash Course](https://www.youtube.com/watch?v=0xMQfnTU6oo) `YouTube`  
> [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout) `MDN`  
> [CSS Grid Layout](https://www.w3schools.com/css/css_grid.asp) `W3School`