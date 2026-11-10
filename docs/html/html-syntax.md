# HTML syntax

## HTML taggar

HTML syntax består av taggar som representerar olika HTML element. Det finns två typer av taggar i HTML:

- `<p>` - öppnande tagg
- `</p>` - stängande tagg

Skillnaden är just `/` som skrivs innan elementnamnet i den stängande taggen. Innehållet av HTML elementet skrivs då mellan öppnande och stängande tagg som tillhör detta element. `<p>` är en textstycke (paragraf) så ett komplett exempel med öppnande tagg, innehåll och stängande tagg kan se ut så här:

```html
<p>
    Hello world!
</p>
```

Det finns dock några element som inte har någon innehåll och behöver därför ingen separat öppnande eller stängande tagg. Dessa är **självstängande** eller **void** element. Till exempel elementet `<br>` som används för radbrytning:

```html
<p>
    Hello <br> world!
</p>
```

I flera kodbaser kan du möta självstängande taggar som har formen `<br/>`. Detta är ett helt korrekt alternativ och båda variant funkar, men moderna validators rekommenderar att inte inkludera den "onödiga" snedstrecket i självstängande taggar och lämna de precis som vanliga öppnande taggar, det vill säga bara `<br>`.

---

## HTML element

Skillnaden mellan ett HTML element och en HTML tagg är att taggen är bara en syntax (med andra ord endast det man skriver inom `<>` och själva `<`, `>`, `/`), medan **element** är ett bredare begrepp som omfattar öppnande och stängande taggar, innehåll, utseende samt alla egenskaper och beteende hos HTMLs "bitar". 

I HTML finns mycket riktigt enorm mängd olika element och jag ska inte gå igenom de alla, men jag länkar till en bra resurs där du kan alltid kolla upp de olika element och hur de används. 

Alla element är förkortning (eller ett helt ord) av det de faktiskt betyder. Till exempel har du redan sett **p** som är **paragraf** och **br** som är **break**.

----

## Attribut

För att ange ytterligare instruktioner för olika element, möjliggöra styling och interaktivitet samt göra flera andra spännande saker används en del av HTML syntax som kallas **attribut**. Ett exempel som ändrar färgen på texten i ett textstycke:

```html
<p style="color: red">
    Hello world!
</p>
```

Principen är enkel. I den öppnande taggen (eller i den enda taggen för självstängande element) skriver man attribut på formatet `nyckel="värde"`. Olika element har olika attribut, men det finns även ett antal globala attribut som kan användas för vilket som helst element (till exempel `class`). Du kommer att lära dig de olika attribut allt eftersom och kan alltid vända dig till sidan under externa resurser för att se en lista av de attribut som stöds för ett specifikt element.

---

## Externa resurser

> [HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference) `MDN`

---

## Quiz

Ta ett snabbt quiz för att testa dina kunskaper! [Eller öppna som en separat sida](../../exercises/html/html-syntax.html)

<iframe style="border: medium none currentcolor;" src="../../exercises/html/html-syntax.html" width="100%" height="500px"></iframe>
