# Variabler i CSS

När vi jobbar med programmeringsspråk vill vi vanligtvis undvika hårdkodade värden för att öka skalbarheten och läsbarheten. På samma sätt kan vi använda variabler i CSS för att slippa hårdkoda färger, mått och andra värden. 

Oftast skapar man globala variabler som kan användas i hela projektet, eftersom webbsidor vanligtvis har gemensamma stilregler för hela webbplatsen. Därför definieras de i `:root`. Det enklaste sättet att demonstrera hur man skapar och använder variabler är kanske att visa ett exempel:

```css
:root {
    /* Så här definierar man en variabel: */
    --accent-color: #3A53BB;
}

.actionButton {
    /* Så här använder man en variabel: */
    background-color: var(--accent-color);
}
```

Det här är ett väldigt smidigt sätt att slippa skriva olika värden manuellt. Jag rekommenderar verkligen att använda det för att dels förenkla livet för sig själv och dels hålla sig till en konsekvent design genom hela sidan.
