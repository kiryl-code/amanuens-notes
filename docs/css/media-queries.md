# Media queries

CSS tillhandahåller funktionalitet för att anpassa webbsidans utseende beroende på vilken enhet som används och därmed uppnå responsivitet. Det finns tre mediatyper som man kan anpassa sidan för:

- `all` - alla mediatyper. All CSS som man skriver på en HTML-sida eller i en kopplad `.css`-fil tillämpas på den här nivån som standard om man inte anger något annat.
- `screen` - enheter med skärm.
- `print` - utskrifter, dvs hur sidan ska se ut om den skrivs ut. Klickar man på `ctrl+p` (eller `cmd+p` på Mac) i webbläsaren ser man en förhandsgranskning som använder just den här typen.

***Media queries*** ger oss möjlighet att anpassa CSS efter mediatyper och villkor. I CSS ser det ut så här: 

```css
@media print {
    /* Vad som behöver ändras vid utskriften */
}
```

När det kommer till `screen` brukar man kombinera det med villkor såsom `width` (som refererar då till *viewportens* bredd) för att skriva regler för specifika skärmstorlekar:

```css
@media screen and (width <= 400px) {
    /* Vad som behöver ändras för mindre skärmar */
}

@media screen and (width > 400px) and (width <= 1028px) {
    /* Vad som behöver ändras för mellanstora skärmar */
}
```

Om man så vill kan man dra en analogi med programmeringsspråk och `if`-satser:

```
OM mediatypen är "screen" OCH viewportens bredd är högst 400px:
    ANVÄND CSS-reglerna här

OM mediatypen är "screen" OCH viewportens bredd är större än 400px OCH högst 1028px:
    ANVÄND CSS-reglerna här
```

---

## Externa resurser

> [CSS @media Rule](https://www.w3schools.com/cssref/atrule_media.php) `w3school`