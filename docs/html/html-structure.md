# Struktur för ett HTML5 dokument

Alla HTML dokument följer samma struktur och initialt innehåller följande:

```html
<!DOCTYPE html>     (1)
<html lang="sv">    (2)
    <head>          (3)
    </head>

    <body>          (4)
    </body>
</html>
```

**(1)** Alla HTML5 dokument inleds med denna rad som indikerar att HTML5 ska användas på den här sidan. Viktigt att ha med!

**(2)** Därefter kommer själva `<html>` root-elementet för en HTML fil. Här sätter man även språket för hemsidan genom att ange respektive värde för `lang` attributet.

**(3)** Inuti `<head>` skriver man metadata, till exempel sidans titel (som visas i webbläsare som ett namn på en flik), teckenkodning, information för sökmotorer osv. Detta innehåll visas inte på själva webbsidan, men det är viktigt att komma ihåg att all HTML kod är alltid synlig för alla som kör den. Den ska alltså **_inte_** innehålla någon kännslig information.

**(4)** Inuti `<body>` skriver man den "visuella" innehållet, dvs deklarera de element som faktiskt visas på sidan, till exempel rubriker, textstycken, listor, bilder, formulär m.m.
