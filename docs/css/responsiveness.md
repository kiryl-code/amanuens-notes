# Responsivitet

När man skapar webbsidor och webbapplikationer vill man oftast att de ska fungera bra på olika enheter, från stora datorskärmar till små mobilskärmar. Innehållet ska vara lätt att läsa och använda oavsett hur mycket utrymme som finns tillgängligt. En responsiv webbsida anpassar sin layout och sitt innehåll efter skärmens eller webbläsarfönstrets storlek.

Det finns olika sätt att tänka när man utvecklar en responsiv webbsida:

- **Desktop-first** innebär att man först utformar sidan för större datorskärmar och sedan anpassar det för smalare skärmar.
- **Mobile-first** gör tvärtom och utformar sidan först för telefoner och andra enheter med små skärmar och sedan anpassar resultatet för större datorskärmar.
- **Responsive by design** innebär att man bygger layouten så att den anpassar sig naturligt. _Flexbox_, _Grid_ och _relativa enheter_ kan hjälpa till med det. Man kan fortfarande behöva göra anpassningar, men man försöker undvika det så mycket som möjligt.

## Viewport

Det väldigt viktigt att definiera hur sidans *viewport* (den synliga ytan i webbläsaren) ska skalas för att responsiv anpassning ska fungera som tänkt på mobila enheter. Det görs genom att lägga till följande `<meta>`-element inuti `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

!!!!warning
Om du glömmer den här raden kommer mobila webbläsare oftast att simulera en bred datorskärm och zooma ut hela sidan så att innehållet blir orimligt litet. Då kommer inte heller dina media queries att fungera som förväntat på små skärmar.
!!!!