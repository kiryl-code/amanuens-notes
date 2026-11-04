# Font-face

`@font-face` är en så kallad **at-rule** i CSS som låter oss koppla in teckensnitt. Oftast används den för att koppla in specifika teckensnitt som kanske inte finns på användarens maskin. Den har en särskild syntax som måste följas för att allt ska fungera. Vanligtvis brukar man deklarera `@font-face` längst upp i CSS-dokumentet.

```css
@font-face {
    font-family: "Playwrite";
    src:
        local("Playwrite Italia Tradizionale"),
        url("../fonts/playwrite-italia-tradizionale.ttf") format("ttf"),
        url("https://fonts.gstatic.com/s/playwriteittrad/v11/SlG5mR6Yo5oYZX5BFVcEySBSPE50BjHDpZxuvgxzFq96u-6_g0NNXv3D2Q.woff") format("woff");
}
```

Under `font-family` anger man vad teckensnittet ska heta när man sedan använder `font-family` för ett element. Om jag vill att `<p class="fancyText">` ska använda det här teckensnittet ska jag skriva så här:

```css
.fancyText {
    font-family: "Playwrite";
}
```

Under `src` anger man var teckensnittet finns och det kan vara bra att ange flera källor. 

- `local` refererar till de teckensnitt som finns installerade på klientens maskin, vilket kan vara användbart ifall någon redan har teckensnittet installerat. 
- `url` används för att ange en filsökväg eller en webbadress till teckensnittet och kommer att användas ifall teckensnittet inte hittas med `local`.

Observera också att man kan ha flera `url` som fallbacks och att man inte måste ha alla filer lokalt, utan det går lika bra att använda resurser som finns på nätet.

Man kan även ange formatet med `format()` så att webbläsaren får information om vilken typ av teckensnittsfil som ska laddas in. Exempelvis används `format("truetype")` för TTF-filer.

---

## Externa resurser

> [@font-face CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) `MDN`  
> [Google Fonts](https://fonts.google.com/) `Google`