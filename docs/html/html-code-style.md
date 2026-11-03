# Kodstil

HTML är väldigt förlåtande i syntaxen. Inga felmeddelande kommer att visas om du glömmer att stänga någon tagg, felstavar ett attribut eller inte följer den grundläggande strukturen. Det värsta som kan hända är att vissa element kan se lite konstigt ut. Men det är viktigt att följa de etablerade konventionerna för att hålla koden tydligt, lätläst, rent och förståeligt.

---

Uppenbarligen ska du alltid stänga taggar som behöver stängas och hålla dig till den grundläggande strukturen. Förutom detta har jag samlat ytterligare några principer som webbutvecklare följer och som kan mycket riktigt räknas som krav till HTML koden.

---

Du kanske redan märkte att nästlade element (när ett element ligger inuti ett annat element) indenteras ett steg för varje indenteringsnivå. 1 indrag brukar motsvara antingen 2 eller 4 mellanslag. Detta värde ska vara samma för hela dokumentet.

^^^^Exempel

!!!! success
Översikt över de element som används i exemplet:

- `<nav>`: ett block med navigationsmeny
- `<ul>`: en punktlista (oordnad). *Ul* i sig är förkortning från eng. unordered list
- `<li>`: ett element i listan

!!!!

```html
<!DOCTYPE html>
<html>
    <head>
    </head>

    <body>
        <nav>
            <ul>
                <li>Punkt 1</li>
                <li>Punkt 2</li>
                <li>Punkt 3</li>
            </ul>
        </nav>
    </body>
</html>
```
^^^^

---

Ytterligare en konvention är användning av gemener (små bokstaver) för taggar och attribut. För HTML och webbläsare spelar det ingen roll om man skriver `<hr>` eller `<HR>` eller till och med `<hR>`. Men för bättre läsbarhet har man kommit överens om att använda gemener. Ett undantag är `<!DOCTYPE html>` där *DOCTYPE* oftast skrivs med versaler.

---

Tänk på att använda en extra radbrytning för att separera större block och uppdela koden så att det är enkelt att navigera i den visuellt och håll dig till samma stil genom hela filen. Du kan även använda kommentarer för att förtydliga vissa delar eller ge korta rubriker för de som läser koden.

^^^^Exempel

Även kommentarer skrivs inom taggar i HTML. En öppnande tagg för en kommentar är `<!--` och en stängande tagg är `-->`.

```html
<!DOCTYPE html>
<html>
    <head>
    </head>

    <body>
        <nav>
            <!-- navigationslänkar -->
            <ul>
                <li><a href="index.html">Hem</a></li>
                <li><a href="about_us.html">Om oss</a></li>
                <li><a href="contact_us.html">Kontakta oss</a></li>
            </ul>

            <!-- profil-knappar -->
            <button>Logga in</button>
            <button>Logga ut</button>
            <button>Min profil</button>
        </nav>
    </body>
</html>
```
^^^^