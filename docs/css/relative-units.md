# Relativa enheter

Ett av de enklaste sätten att bidra till webbsidans responsivitet är att använda relativa enheter där det passar. Det kan exempelvis vara procentuell storlek på vissa element, automatisk anpassning av textstorlek och annat. Det är därför viktigt att känna till olika relativa enheter som kan användas i CSS.

---

## `%`

Med procent anger man, precis som det låter, ett värde i procentenheter istället för ett hårt antal pixlar. Man kan fråga då vad `5%` betyder? `5%` av vad? Svaret beror på vilken CSS-egenskap det handlar om. Exempelvis för `width` och `height` används motsvarande dimensioner av föräldrarelementet. `border-radius` använder elementets egna dimensioner. Om man sätter `border-radius: 50%` på en kvadrat kommer man få en cirkel. Det beror alltså på.

---

## `rem`

`rem` har med textstorlek att göra och `1rem` motsvarar en standardtextstorlek (den som anges för `<html>`-elementet). Ofta är det `16px`, men det kan skilja sig beroende på webbläsarinställningar och `font-size` som man anger för `<html>`-elementet.

Om vi har följande CSS:

```css
html {
    font-size: 12px;
}
```

Då kommer `1rem` att vara lika med `12px`. `0.5rem` motsvarar då `6px` och `2rem` blir lika med `24px`. 

Fördelen med `rem` är att det räcker att ändra `font-size` på ett `<html>` och samtliga storlekar, mellanrum m.m. som använder `rem` kommer att anpassas automatiskt.

---

## `em`

`em` är ungefär samma sak som `rem`, men den har ett annorlunda scope. `em` används relativt till elementets egen `font-size` istället för `<html>`s `font-size`.

```css
html {
    font-size: 12px;
}

p {
    font-size: 1.5rem; /* =18px */
    line-height: 1em; /* =18px */
}
```

I exemplet ovan sätter vi textstorleken till `1.5rem`, vilket motsvarar `18px` och säger att `line-height`, dvs en textrads höjd, ska vara `1em`. Eftersom `em` beror på elementets egen `font-size` kommer det vara lika med `18px`.

Vad händer då om man sätter `font-size` på ett element till ett värde med `em`-enheten? I så fall kommer förälderns `font-size` att användas som en referens:

```html
<div class="container">
    <p>En smalare text</p>
</div>
```

```css
.container {
    font-size: 18px;
}

.container p {
    font-size: 0.5em; /* =9px */
}
```

---

## `vw`

`1vw` motsvarar `1%` av webbläsarfönstrets bredd. Om webbläsarens fönster är `100px` kommer `1vw` vara lika med `1px`. Det här är särskilt användbart när man vill att ett visst element ska täcka hela fönstrets bredd:

```css
body {
    width: 100vw;
}
```

Exemplet är väldigt illustrativt och opraktiskt, eftersom de flesta blockelement (och `<body>` är en av dem) brukar ofta ta hela den tillgängliga bredden automatiskt.

---

## `vh`

Precis som `vw`, men handlar om fönstrets höjd istället. Också användbart om ett element ska täcka ett utrymme som är lika med webbläsarefönstrets höjd:

```css  
body {
    min-height: 100vh;
}
```

---

## Externa resurser

> [CSS Units](https://www.w3schools.com/cssref/css_units.php) `w3school`
> [CSS values and units (endast Numbers, lengths, and percentages)](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units#numbers_lengths_and_percentages) `MDN`

---

## Quiz

Testa dina kunskaper om du vill! [Eller öppna som en separat sida](../../exercises/css/relative-units.html)

<iframe style="border: medium none currentcolor;" src="../../exercises/css/relative-units.html" width="100%" height="600"></iframe>