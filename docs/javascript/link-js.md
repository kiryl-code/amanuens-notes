# Att koppla JavaScript till HTML

Kopplingen mellan JavaScript och HTML fungerar på ett liknande sätt som kopplingen mellan CSS och HTML. Man har alltså flera tillvägagångssätt.

---

## `<script>`

Ett sätt att skriva JavaScript-kod är att göra det direkt inuti `<script>`-elementet:

```html
<script>
    console.log("Hello World!");
</script>
```

Ibland kan det vara användbart, men av skalbarhetsskäl rekommenderas det att du inte gör det.

---

## Externa `.js`-filer

Precis som CSS ska JavaScript skrivas i externa filer. De filerna kan enkelt kopplas till en HTML-sida genom att ange `src` för ett `<script>`:

```html
<script src="js/main.js"></script>
```

Man brukar vanligtvis koppla in scripts i dokumentets `<head>`.

---

!!!!warning
När en HTML-sida laddas i en webbläsare sker laddningen uppifrån och ner. Eftersom man brukar koppla alla skript i `<head>` kan det enkelt hända att JavaScript-kod försöker komma åt ett element som ännu inte har hunnit laddas. Detta kommer att resultera i en runtime exception och krascha hela skriptet (inte webbsidan, utan logiken i `.js`). Det är därför viktigt att implementera mekanismer som säkerställer att HTML laddas innan koden körs. 

Ett exempel på en sådan mekanism är attributet `defer`. Det förhindrar att skriptet exekveras förrän HTML-innehållet har parsats av webbläsaren:

```html
<script src="js/main.js" defer></script>
```

Ett annat sätt är att lyssna på `DOMContentLoaded`-händelsen. Den körs precis efter `defer`. Koden nedan kan vara lite svår att förstå innan du går igenom JavaScripts syntax, callbacks och events, men det finns inget som förhindrar dig från att komma tillbaka sedan när du har läst om dessa koncept =)

```javascript
function main(e) {
    // Här skriver du din kod
}

document.addEventListener("DOMContentLoaded", main);
```
!!!!