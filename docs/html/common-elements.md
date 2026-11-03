# De vanligaste elementen

Jag kommer inte kunna gå igenom alla element som finns och därför väljer jag väldigt specifika exempel för olika typer av innehåll. Du får gärna kika på externa resurser för att få en översikt över flera HTML-element. Testa mina exempel genom att kopiera och klistra in koden i en HTML-fil.

---

## Text

Du har redan sett `<p>` som står för paragraph eller textstycke och `<br>` som används för radbrytning.

Ytterligare några element är listor, till exempel `<ol>` eller `<ul>`. Varje element i en lista ska representeras av `<li>`.

För att skapa länkar används `<a>` (anchor) och platsen som länken ska leda till anges i attributet `href`.

Det finns sex rubriknivåer, från `<h1>` till `<h6>` (heading 1–heading 6).

^^^^ Exempel
```html
<h1>Text</h1>

<h2>Listor</h2>

<h3>Ordnad lista</h3>
<ol>
    <li>Punkt 1</li>
    <li>Punkt 2</li>
    <li>Punkt 3</li>
</ol>

<h3>Oordnad lista</h3>
<ul>
    <li>Punkt 1</li>
    <li>Punkt 2</li>
    <li>Punkt 3</li>
</ul>

<h2>Länkar</h2>
<a href="https://www.miun.se/">Klicka här för att gå till MIUN:s hemsida</a>
<br>
<a href="other.html">Skapa filen med namnet <code>other.html</code> i samma katalog och klicka på den här länken</a>
```

Resultatet kan du se här:
<iframe style="border: medium none currentcolor;" src="../../demo/html/common-text-elements.html" width="100%" height="450"></iframe>

[Eller öppna som en separat sida](../../demo/html/common-text-elements.html)
^^^^

---

## Block

Man kan bifoga bilder med `<img>`.

Alternativt kan man bädda in övriga typer av multimedia, till exempel `<video>` eller `<audio>`.

Man kan även visa tabeller med `<table>` som då har `<tr>` för rader och `<td>` för celler. För kolumnnamn kan man använda `<thead>` och `<th>`.

^^^^ Exempel
```html
<h1>Block</h1>

<h2>Bilder</h2>
<img src="https://images.pexels.com/photos/37842711/pexels-photo-37842711.jpeg" alt="Den här texten visas om bilden inte kunde laddas. Man vill alltid ha en bildbeskrivning här" width="100%">

<h2>Tabeller</h2>
<table>
    <thead>
    <tr>
        <th>Kurskod</th>
        <th>Kursnamn</th>
    </tr>
    </thead>
    <tr>
        <td>DV043G</td>
        <td>Programvaruteknik, introduktionskurs</td>
    </tr>
    <tr>
        <td>DV044G</td>
        <td>Programmeringens grunder</td>
    </tr>
    <tr>
        <td>DV045G</td>
        <td>Webbutveckling med inriktning frontend</td>
    </tr>
</table>
```
Resultatet kan du se här:
<iframe style="border: medium none currentcolor;" src="../../demo/html/common-block-elements.html" width="100%" height="750"></iframe>

[Eller öppna som en separat sida](../../demo/html/common-block-elements.html)
^^^^

---

## Formulär

Formulär stöter man på mycket ofta på webbsidor, och dessa skapas med hjälp av `<form>` med flera `<input>`-element. För `<input>` brukar man ange typen för att få det att fungera som det ska, till exempel `<input type="number">`, `<input type="text">` eller `<input type="email">` m.m.

Man kan även inkludera knappar med `<button>`.

```html
<h1>Annat</h1>
<form action="#">
    <label for="username">Användarnamn</label>
    <input type="text" name="username" id="username" placeholder="Användarnamn">
    <!--  Använd inte <br> för att utforma layouten. Här används det bara för att illustrera exemplet-->
    <br> 
    <label for="email">E-post</label>
    <input type="email" name="email" id="email" placeholder="e-post">
    <br>
    <label for="birthDate">Födelsedatum</label>
    <input type="date" name="birthDate" id="birthDate" placeholder="2000-01-01">
    <br>
    <label for="password">Lösenord</label>
    <input type="password" name="password" id="password">
    <br>
    <button>Klicka på mig!</button>
</form>
```

^^^^Titta på hur det ser ut
<iframe style="border: medium none currentcolor;" src="../../demo/html/common-forms.html" width="100%" height="200"></iframe>

[Eller öppna som en separat sida](../../demo/html/common-forms.html)
^^^^

---

## Generiska element

Det finns en del generiska element som fungerar som behållare, till exempel `<div>` eller `<span>`. De har ingen visuell representation, men är väldigt användbara vid styling när man behöver ändra en specifik grupp av andra element.

---

## Externa resurser

> [HTML Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) `MDN`  
> [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms) `MDN`  