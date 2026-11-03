# Att koppla CSS till HTML

Det finns flera tillvägagångssätt för att skriva CSS-stilar för olika HTML-element. Två av dem kräver att man skriver CSS direkt i HTML-dokumentet och den tredje använder en separat CSS-fil som kopplas till hela HTML-dokumentet. Vi börjar med de första två.

---

## Style attribut

Samtliga HTML-element har ett attribut som heter `style`. Värdet man anger för det här attributet är CSS-kod för elementet, till exempel:

```html
<a href="#" style="color: green; font-size: 24px;">Klicka på mig!</a>
```

Den här metoden kan användas ibland, men den har flera brister, framför allt när det gäller skalbarhet. Har man en stor HTML-fil där flera länkar måste formateras på samma sätt kan det snabbt bli många oläsbara upprepningar i koden. 

---

## Style element

Man skriva all CSS inuti `<style>`-elementet (som vanligtvis placeras i `<head>`).

---

## Extern `.css`-fil

Men tänk att du vill tillämpa samma stilmall på alla HTML-dokument. Då är det smidigt att använda en separat CSS-fil. Det följer också principen om ansvarsfördelning: HTML-dokumentet hanterar HTML-koden och CSS-filen hanterar stilarna. Skriver man CSS i ett separat dokument ska man koppla det till HTML med hjälp av följande syntax:

```html
<link rel="stylesheet" href="...">
```

Där `href` är filsökvägen till CSS-filen. Det behöver inte vara en lokal fil, utan det kan även vara en CSS-fil från nätet. Det är bara att ange rätt sökväg. Man brukar vanligtvis länka till CSS-dokument i `<head>`.

!!!! success
Det är främst den sista metoden, med en extern fil, som du ska använda mest.
!!!!