# Manipulera HTML-element

Med hjälp av JavaScript kan man manipulera olika HTML-element på olika sätt. Från JavaScript har man tillgång till alla element, alla stilar, attribut och innehåll som finns på sidan (och till och med lite mer!).

## Elementets innehåll

Man kan komma åt det som finns inuti ett specifikt element. Till exempel:

///tab | JavaScript

```js
const content = document.querySelector("body").innerHTML;
console.log(content);

// output:
// <h1>Rubrik</h1>
// <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.</p>
// <p style="display: none;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusantium error excepturi harum, quis repellendus.</p>
```
///
/// tab | HTML
```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    <h1>Rubrik</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.</p>
    <p style="display: none;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusantium error excepturi harum, quis repellendus.</p>
</body>
</html>
```
///

Kommer att skriva ut allt som finns på webbsidan mellan `<body>` och `</body>`, precis som i källkoden (om ingenting har ändrats med någon annan JavaScript-kod, av tillägg som finns installerade i webbläsaren osv.).

Där ser du första fältet som alla HTML-element har (bättre sagt, de flesta): `innerHTML`. Vi kan också tilldela ett nytt värde för att byta ut det befintliga:

///tab | JavaScript
```js
document.querySelector("body").innerHTML = "<h1>Hello World!</h1>"
```
/// 
/// tab | resultat i HTML
```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
///

Om man kör den här koden kommer en sida att bara visa "Hello World!". Allt innehåll kommer alltså att bytas ut mot det man anger som värdet.

---

Att manipulera `.innerHTML` är av olika skäl inte den bästa lösningen om man vill exempelvis ändra texten som visas i en rubrik eller en paragraf. Detta beror på att `.innerHTML` tolkas som kod och man kan injektera JavaScript-kod, vilket är en säkerhetsrisk. Därför ska man föredra `.innerText` i sådana situationer:

///tab | JavaScript
```js
const content = document.querySelector("body").innerText;
console.log(content);

// output:
// Rubrik
// Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.
// den tredje texten kommer inte synas här, eftersom den inte renderats på skärmen
```
///
/// tab | HTML
```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    <h1>Rubrik</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.</p>
    <p style="display: none;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusantium error excepturi harum, quis repellendus.</p>
</body>
</html>
```
///

Ett annat exempel:

///tab | JavaScript
```js
document.querySelector("body").innerText = "<h1>Hello World!</h1>";
```
/// 
/// tab | resultat i HTML
```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    &lt;h1&gt;Hello World!&lt;/h1&gt;
    <!-- 
        Det betyder att resultatet på skärmen kommer att vara "<h1>Hello World!</h1>",
        inklusive HTML-syntaxen
    -->
</body>
</html>
```
///

Några begränsningar med `innerText` är att den returnerar texten som är renderad på skärmen. Den tar alltså hänsyn till stilar. Om man till exempel använder `text-transform` för att göra alla bokstäver till versaler, kommer `innerText` att returnera texten med versaler.

---

Om man istället vill jobba med den texten som står i själva elementen i koden, dvs ignorera CSS och annan formatering, kan man använda `textContent` istället. Det blir även lite mer effektivt utifrån ett prestandaperspektiv.

///tab | JavaScript
```js
const content = document.querySelector("body").textContent;
console.log(content);

// output:
// Rubrik
// Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.
// Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusantium error excepturi harum, quis repellendus.
```
///
/// tab | HTML

```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    <h1>Rubrik</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, tempore.</p>
    <p style="display: none;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusantium error excepturi harum, quis repellendus.</p>
</body>
</html>
```
///

Om man vill ändra innehållet med `.textContent` kommer det att se ut så här:

///tab | JavaScript
```js
document.querySelector("body").textContent = `
    <h1>Hello World!</h1>
    <h2>Hello World!</h2>
    <h3>Hello World!</h3>
`;
```
/// 
/// tab | HTML
```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
    <meta name="viewport" 
       content="width=device-width, user-scalable=no, 
                initial-scale=1.0, maximum-scale=1.0, 
                minimum-scale=1.0"
    >
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exempel</title>
</head>
<body>
    &lt;h1&gt;Hello World!&lt;/h1&gt;&lt;h2&gt;Hello World!&lt;/h2&gt;&lt;h3&gt;Hello World!&lt;/h3&gt;
    <!--
        Resultatet på skärmen kommer att vara:
            <h1>Hello World!</h1><h2>Hello World!</h2><h3>Hello World!</h3>
    -->
</body>
</html>
```
///

---

| Tillvägagångssätt | Egenskaper                                                                                   |
|:------------------|:---------------------------------------------------------------------------------------------|
| `.innerHTML`      | Manipulerar själva koden. Inte säkert att använda om man inte kontrollerar innehållet själv. |
| `.innerText`      | Manipulerar texten som finns på skärmen. Tar hänsyn till formatering och stilar.             |
| `.textContent`    | Manipulerar texten inuti elementen. Ignorerar formatering och stilar.                        |

---

## Manipulera attribut

Såklart kan man använda JavaScript även för att lägga till eller ta bort attribut. De flesta attribut är åtkomliga på samma sätt som `innerHTML` och hämtas eller ändras med liknande syntax:

```js
document.querySelector("img").src = "newImagePath.jpg";
```

Om attributet saknar något värde används då ett booleskt uttryck:

```js
// gör <input id="exampleInput" type="..."> 
// obligatorisk
document.querySelector("#exampleInput").required = true;
```

---

Det finns även en del mer generiska metoder (vilket betyder att dessa anropas på ett HTML-element som valdes med `getElementBy...()` eller `querySelector()`), se tabellen nedan:

| Metod (anropas på en instans av Element) | Beskrivning                                                                                                                                      |
|:-----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| `.getAttribute()`                        | Returnerar ett värde av ett specificerat attribut                                                                                                |
| `.getAttributeNames()`                   | Returnerar en lista av alla attribut som har angivits för elementet                                                                              |
| `.setAttribute()`                        | Tar emot två argument: det första är attributets namn och det andra är värdet som ska sättas                                                     |
| `.hasAttribute()`                        | Returnerar `true` om ett element har det angivna attributet och `false` om attributet saknas på elementet                                        |
| `.removeAttribute()`                     | Tar bort ett specificerat attribut från ett element                                                                                              |
| `.toggleAttribute()`                     | Används för boleska attribut (såsom `required`, `disabled` osv.)  för att lägga till det om attributet inte redan finns och ta bort om det finns |

---

För attributet `class` finns det flera olika metoder för att hantera klasser på ett effektivt sätt, särskilt när elementet har flera klasser. Först kan man komma åt alla klasser via `Element.classList` och därefter använda någon av följande metoder:

| Metod (anropas på `Element.classList`) | Beskrivning                                                                                 |
|:---------------------------------------|:--------------------------------------------------------------------------------------------|
| `.add()`                               | Lägga till en (eller flera) klasser i elementets klasslista                                 |
| `.remove()`                            | Ta bort en klass från elementets klasslista                                                 |
| `.replace()`                           | Ersätta en klass i elementets klasslista till med en annan klass                            |
| `.toggle()`                            | Växla klassen i elementets klasslista. Om klassen inte finns med läggs den till och tvärtom |

Ett väldigt kort exempel för att demonstrera syntaxen.

```js
document.querySelector("button").classList.add("active", "btn-blue");
document.querySelector("input").classList.toggle("hidden");
```

---

## Tips

!!!!success
Fokusera inte så mycket på att jag använder just `document.querySelector()` i mina exempel. Du kan köra samtliga metoder på de HTML-element som lagras i andra variabler eller returneras av andra metoder:

```js
document.getElementById("btn-submit").toggleAttribute("disabled");

const form = document.querySelector("form");
form.classList.toggle("hidden");
```

En lite renare lösning är såklart att plocka elementet först, kontrollera att elementet sparades korrekt (`!== null` och `!== undefined`, tex genom `if (element)`) och därefter anropa olika metoder.   
!!!!