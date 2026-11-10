# Emmet

!!!!message
Du kanske vill läsa lite om HTML och CSS grundläggande syntax först, eftersom emmet berör båda.
!!!!

Emmet är ett verktyg som finns inbyggt i både _VSCode_ och _WebStorm_, men kan även installeras för andra IDE. Verktyget används för att snabba upp utvecklingsprocessen genom att använda förkortningar som sedan automatiskt expanderas till riktiga HTML- och CSS-strukturer.

---

## Emmet i HTML

Säg att vi vill skapa en lista med 3 element:

```html
<ul>
    <li>Element 1</li>
    <li>Element 2</li>
    <li>Element 3</li>
</ul>
```

Att skriva in alla `<li>`-element kan ta lite tid. Med emmet räcker det att du skriver `ul>li*3` och trycker på `tab`.

Med en enkel deduktion kan du klura ut att `>` används för barnelement och `*X` används för att deklarera hur många sådana element som ska skapas. Nedan kommer en lite mer utförlig lista med olika modifierare.

^^^^Emmet i HTML, exempel

`>` - barnrelationen, till exempel `p>span`:

```html
<p><span></span></p>
```

`*` - multiplikation, till exempel: `div*2`

```html
<div></div>
<div></div>
```

`+` - syskon, till exempel: `p+button`

```html
<p></p>
<button></button>
```

`#` - id-attribut, till exempel: `a#uniqueLink`. Om man inte anger elementet (`#someRandomId`) kommer ett `<div>` att skapas.

```html
<a href="" id="uniqueLink"></a>
<div id="someRandomId"></div>
```

`.` - class-attribut, till exempel: `a.navLink`. Om man inte anger elementet (`.someRandomClass`) kommer ett `<div>` att skapas.

```html
<a href="" class="navLink"></a>
<div class="someRandomClass"></div>
```

Det finns många fler som inte nämns här. Kika på externa resurser (särskilt cheatsheet) för fler exempel.

---

Här är ett exempel på en ganska omfattande struktur som enkelt kan skapas på bara några sekunder tack vare emmet:

`header>nav>a*5^h1+p+.actions_container>button*2`

```html
<header>
    <nav>
        <a href=""></a>
        <a href=""></a>
        <a href=""></a>
        <a href=""></a>
        <a href=""></a>
    </nav>
    <h1></h1>
    <p></p>
    <div class="actions_container">
        <button></button>
        <button></button>
    </div>
</header>
```
^^^^

---

## Emmet i CSS

På ett liknande sätt kan man skriva förkortningar i CSS som expanderas till egenskap-värde-par. Det finns extremt många förkortningar, så jag ger bara två exempel här:

- `ta:c` motsvarar `text-align: center`
- `d:n` motsvarar `display: none`

Principen här är att man använder de första bokstäverna i en egenskap och dess värde för att slippa skriva hela uttrycket. Det är inte alltid sant, men den här algoritmen räcker ganska långt. Återigen, kika på cheatsheets under externa resurser för fler exempel.

---

## Externa resurser

> [Emmet](https://www.emmet.io/) `Emmet`  
> [Emmet cheat sheet](https://docs.emmet.io/cheat-sheet/) `Emmet`

---

## Quiz

Testa dina kunskaper! [Öppna som en separat sida](../../exercises/tools-and-techniques/emmet.html)

<iframe style="border: medium none currentcolor;" src="../../exercises/tools-and-techniques/emmet.html" width="100%" height="600px"></iframe>

