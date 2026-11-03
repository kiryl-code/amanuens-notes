# Flexbox

I modern webbutveckling används ofta flexbox-modellen för att skapa layouter. Den förenklar positionering av element som tidigare krävde krångliga omvägar eller hårdkodade värden. För att förstå flexbox behöver vi först definiera ett viktigt begrepp. **En behållare (container)** är ett element som omsluter andra element. Det är grunden i flexbox, eftersom all positionering anges på behållaren och styr de element som ligger direkt inuti den.

!!!! warning
Det bästa sättet att förstå flexbox är att se hur det fungerar i praktiken. Vi rekommenderar starkt att du öppnar din kodeditor och skapar en enkel `sandbox.html` där du lägger till exempelkod och gör ändringarna som föreslås i texten nedan.
!!!!

^^^^Flexbox, startkod
```html
<div class="container">
    <div class="rectangle red"></div>
    <div class="rectangle green"></div>
    <div class="rectangle blue"></div>
</div>
```

```css
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

.container {
    height: 100vh;
    width: 100vw;
}

.rectangle {
    width: 100px;
    height: 50px;
}

.red {
    background-color: red;
}

.green {
    background-color: green;
}

.blue {
    background-color: blue;
}
```
^^^^

Som du ser i koden ligger tre rektanglar inuti ett `<div class="container">`. Det är detta `<div>` som kommer att vara en behållare, och det är där vi ska ange hur elementen inuti den ska placeras. Vi börjar med att göra behållaren till en flexbehållare genom att lägga till `display: flex;`:

```css
.container {
    height: 100vh;
    width: 100vw;
    display: flex; /* <- nu är .container en flex-behållare */
}
```

---

## `justify-content`

Det första som du kanske redan märker är att rektanglarna nu placeras bredvid varandra. Detta är standardbeteendet för flexbox. Alla element som ligger direkt i en flexbehållare placeras efter varandra i en rad som standard. Om det inte finns tillräckligt med utrymme försöker flexelementen normalt krympa för att få plats istället för att automatiskt flyttas till en ny rad.

Nu finns det följande alternativ för hur vi kan placera elementen längs **huvudaxeln (main axis)**. I det här fallet är huvudaxeln _X_-led, alltså horisontell. Det är egenskapen `justify-content` som ansvarar för hur elementen placeras längs _huvudaxeln_:

| Beskrivning                                                                                          | Värde på `justify-content` |
|:-----------------------------------------------------------------------------------------------------|----------------------------|
| Placera elementen med jämnt mellanrum **mellan varandra**, utan extra utrymme vid behållarens kanter | `space-between`            |
| Placera elementen med jämnt mellanrum **mellan varandra och vid behållarens kanter**                 | `space-evenly`             |
| Placera elementen med jämnt utrymme **runt varje element**                                           | `space-around`             |
| Centrera elementen längs huvudaxeln                                                                  | `center`                   |
| Placera elementen bredvid varandra med början från huvudaxelns startkant                             | `flex-start`               |
| Placera elementen bredvid varandra med början från huvudaxelns slutkant                              | `flex-end`                 |

^^^^Kolla på hur det ser ut
<iframe style="border: medium none currentcolor;" src="https://studenter.miun.se/~kiya2400/dv045g/course_material/flexbox/justify-content-demo.html" width="100%" height="850" name="flexbox-justify-content-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](https://studenter.miun.se/~kiya2400/dv045g/course_material/flexbox/justify-content-demo.html)
^^^^

## `align-items`

Man kan även styra hur elementen placeras längs den sekundära axeln, alltså **tväraxeln (cross axis)**. Som standard är den _Y_-led, och det är `align-items` som ansvarar för detta. Här finns bland annat följande värden:

| Beskrivning                                                                              | Värde på `align-items` |
|------------------------------------------------------------------------------------------|------------------------|
| Placera elementen vid tväraxelns startkant                                               | `flex-start`           |
| Centrera elementen längs tväraxeln                                                       | `center`               |
| Placera elementen vid tväraxelns slutkant                                                | `flex-end`             |
| Sträck ut elementen så att de fyller behållarens tillgängliga utrymme längs tväraxeln(*) | `stretch` (standard)   |
| Justera elementen efter deras textbaslinje                                               | `baseline`             |

(*) Det är viktigt att notera att det endast gäller för element med `height: auto;`. Har elementet ett fast höjd, till exempel `height: 25px;` kommer det inte påverkas.

^^^^Kolla på hur det ser ut
<iframe style="border: medium none currentcolor;" src="https://studenter.miun.se/~kiya2400/dv045g/course_material/flexbox/align-items-demo.html" width="100%" height="900" name="flexbox-align-items-demo" sandbox="allow-scripts allow-same-origin allow-forms" loading="lazy" allowfullscreen="allowfullscreen" scrolling="yes"></iframe>

[Klicka här för att öppna som en separat sida](https://studenter.miun.se/~kiya2400/dv045g/course_material/flexbox/align-items-demo.html)
^^^^

Man kan såklart kombinera `justify-content` med `align-items` för att bestämma hur elementen placeras både vertikalt och horisontellt.

---

## Huvudaxel och tväraxel

I texten ovan nämnde vi _huvudaxeln_ och _tväraxeln_ några gånger. Det är ytterligare två viktiga begrepp inom flexbox. Som standard är huvudaxeln X-led och då beskriver `justify-content` hur elementen placeras horisontellt. Tväraxeln är som standard Y-led och styrs av `align-items`. Men det behöver inte alltid vara så här så vi försöker att undvika formuleringar med "horisontellt" och "vertikalt".

Vill man placera elementen under varandra istället för bredvid varandra och behålla alla fördelar med flexbox kan man byta riktning på axlarna så att Y-axeln blir huvudaxel. Man anger då `flex-direction: column;`. Nu ansvarar `justify-content` för vertikal positionering (samma värden används, men tillämpas nu längs Y-axeln) och `align-items` ansvarar för horisontell positionering (samma värden används, men tillämpas nu längs X-axeln). Därmed kan vi ändra vilken axel `justify-content` och `align-items` arbetar längs.

Man kan alltså säga att `justify-content` bestämmer hur elementen placeras längs huvudaxeln, medan `align-items` bestämmer hur de placeras längs tväraxeln. Testa att lägga till `flex-direction: column;` till något av våra exempel och se vad som händer.

---

## Hur centrerar man ett `<div>`?

^^^^Hur centrerar man ett `<div>`?
Hur man centrerar ett `<div>` är ett skämt inom webbutveckling, eftersom det finns så många sätt att göra det, men när man väl behöver göra det visar det sig att ingen kan göra det. Med flexbox är det ganska enkelt och du kanske redan nu förstår hur man kan kombinera `justify-content` med `align-items` för att uppnå detta. Hur som helst, här är ett exempel.

Vi använder en väldigt enkel struktur för HTML:

```html
<body>
    <div></div>
</body>
```

Och lite CSS. Vi lägger till `border` för att visa var `<div>` faktiskt ligger och "bevisa" att det är centrerat. Vi nollställer `margin` och `padding` för att slippa scrollbars. Vi låter `body` ta hela fönstrets bredd och höjd samt sätter dimensionerna för `<div>` för att kunna se elementet.

```css
div, body {
    margin: 0;
    padding: 0;
}

body {
    min-height: 100vh;
    width: 100vw;
    /* the magic is here */
    display: flex;
    justify-content: center;
    align-items: center;
}

div {
    width: 150px;
    height: 150px;
    border: 1px solid black;
}
```

Klart! [Se resultatet här](https://studenter.miun.se/~kiya2400/dv045g/course_material/flexbox/center-a-div.html).
^^^^

---

!!!! warning
Det är viktigt att komma ihåg att flexbox endast gäller för elementen som ligger direkt inuti behållaren. Element som ligger djupare i HTML-strukturen blir **_inte_** automatiskt flexelement.

Det måste även finnas ledigt utrymme för att egenskaper som `justify-content` och `align-items` ska kunna fördela eller flytta elementen på ett synligt sätt. Som standard anpassas behållarens höjd efter dess innehåll. Vill du centrera vertikalt med `align-items` måste behållaren ha en tillräcklig höjd (exempelvis `height: 100vh`). När det gäller `width` brukar den automatiskt ta upp hela den tillgängliga bredden för ett blockelement, men om elementen tillsammans fyller ut hela bredden finns det inget ledigt utrymme kvar för `justify-content` att fördela.
!!!!

---

## Gap

Man kan även sätta ett eget värde på hur mycket utrymme det ska finnas mellan elementen som ligger i behållaren. För att göra detta använder man `gap`. Resultatet blir att det skapas ett bestämt mellanrum mellan elementen. Till skillnad från `justify-content: space-between` anger man alltså ett fast avstånd istället för att låta flexbox fördela det lediga utrymmet mellan elementen. Testa följande ändring:

```css
.container {
    height: 100vh;
    width: 100vw;
    display: flex;
    gap: 32px; /* <- lek med det här värdet */
}
```
