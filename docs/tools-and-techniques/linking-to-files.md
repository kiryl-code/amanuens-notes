# Att koppla externa filer

!!!!message
Du kanske vill läsa lite om HTML och CSS grundläggande syntax först.
!!!!

Det är inte ovanligt att man behöver koppla externa filer på ett eller annat sätt. I slutändan beskrivs WWW ibland som en mängd sammanlänkade dokument. Det kan handla om allt från bilder och videor på sidor till länkar till andra sidor, externa CSS- och JavaScript-filer, våra egna ljudfiler, typsnitt m.m. Det finns två saker att tänka på som jag vill att ni ska känna till.

## Sökvägar

Sökvägar skrivs ofta relativt till filen som man befinner sig i. Webbläsaren utgår från HTML-dokumentets URL när den tolkar relativa sökvägar. Om vi tar följande struktur som exempel:

```text
└── project_folder/
    ├── index.html
    ├── pages/
    │   ├── about.html
    │   ├── contact.html
    │   └── guides.html
    └── img/
        ├── icons/
        │   ├── favico.ico
        │   └── logo.svg
        └── backgrounds/
            └── header-bg.jpeg
```

Vill man skapa en länk från `index.html` till `about.html` är det bara att använda 

```html
<a href="pages/about.html">About</a>
```

Man anger alltså en relativ sökväg till en fil.

Om man vill göra tvärtom, dvs. länka till `index.html` från `about.html`, behöver man först gå ut ett steg, vilket görs med `..`: 

```html
<a href="../index.html">Home</a>
```

Nästlade kataloger och filer läggs till på samma sätt som i det första exemplet. Om man vill använda logotypen på `contact.html` kan man skriva så här: 

```html
<img src="../img/icons/logo.svg" alt="logotyp">
```

Man kan även länka till **andra webbplatser**. Det finns alltså ingenting som stoppar dig från att skriva 

```html
<a href="https://www.google.com/">Klicka på mig!</a>
```

Detsamma gäller bilder, länkar, CSS- och JavaScript-filer och mycket annat. Generellt sett gäller att om du kan skriva in en filsökväg kan du även skriva en webbadress till resursen. Tänk dock på att externa resurser kan ha begränsningar. Exempelvis kan säkerhetsregler påverka om en resurs får hämtas eller användas från en annan webbplats. Det är alltså inte alltid tillräckligt att bara känna till webbadressen. Det är dock inget som jag tänker gå igenom här.

---

## Optimera bilder

**_Att ladda filer tar tid_**. Det spelar ingen roll om filerna tillhör samma projekt eller om du länkar till externa filer. Det är särskilt viktigt för **användarupplevelsen** (UX). Onödigt stora bilder kan till exempel ta tid att ladda så att användarna inte ser dem på en stund, vilket inte är bra. Det finns flera saker man kan göra för att optimera detta.

Det första och enklaste sättet att minska problem med bildladdningen är att anpassa bildens dimensioner efter de faktiska visningsdimensionerna. Har du ett `<img>` som endast kommer att visas i `50x50` pixlar behöver du inte nödvändigtvis ha en bild på `720x720` pixlar för detta. Minska bildens dimensioner så att de ligger närmare den faktiska visningsstorleken (kanske någonstans mellan `100x100` och `50x50`).

Det är också viktigt att inte använda för små bilder för stora visningsdimensioner. Dvs man ska inte försöka visa en `50x50`-bildfil i en `1000x1000`-yta, eftersom kvaliteten blir otroligt försämrad. Man ska alltså hitta någon form av balans och använda tillräckligt stora filer där det behövs, men undvika det när det är onödigt.

En annan sak man kan göra är att konvertera bilden till ett annat format. `.png` brukar ta ganska mycket plats och därmed laddas långsammare. `.jpg` brukar vara lite mer platseffektivt, men det finns även modernare bildformat som kan ge ännu bättre komprimering. `.webp` är ett bra och brett stödd format på webben som har stöd för genomskinliga delar (precis som `.png`) och kan även vara animerat (som `.gif`), samtidigt som det ofta tar relativt lite plats och därmed laddas snabbt. Ett annat modernt format är `.avif` som i många fall kan ge ännu bättre komprimering. Vilket format som är bäst beror dock på bilden och användningsområdet, men nu känner du till några bildformat som du kan leka lite med.

!!!!info
Det som nämns om laddningstid och filstorlek är aktuellt även för egna typsnitt och allt annat innehåll som behöver laddas. Man ska försöka minska storleken på filerna som laddas för att minska väntetiden för användaren.
!!!!

