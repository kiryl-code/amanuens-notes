# Objekt i JavaScript

!!!!warning
Den här sidan handlar inte om objektorienterad programmering i JavaScript och berör därför inte de koncept som har med OOP att göra. Jag går bara igenom objekt som datatyp och introducerar begreppet **metod**. OOP i sig förtjänar kanske en separat sida, om inte en hel separat modul.
!!!!

Objekt i JavaScript är en _mutable_ datatyp som består av nyckel-värde-par. Om du har arbetat med Python kan du jämföra JavaScript-objekt med `dict`. De är inte samma sak, men bygger på en liknande princip. Även `Map` i vissa andra programmeringsspråk kan liknas vid JavaScript-objekt. Titta på det här exemplet:

```js
const myObject = {
    year: 2026,
    day: "Monday",
    status: true
}
```

Du kan komma åt objektets olika egenskaper antingen med `.` eller med hakparenteser och egenskapens namn:

```js
console.log(myObject.year);
console.log(myObject["day"]);
// output:
// 2026
// Monday
```

Om du försöker komma åt en egenskap som inte finns i objektet returnerar JavaScript `undefined`:

```js
console.log(myObject.month);
// output:
// undefined
```

Det går även att lägga till nya egenskaper i ett objekt:

```js
myObject["century"] = 21; 
// eller:
myObject.century = 21;
```

För att ta bort en egenskap använder du nyckelordet `delete`:

```js
delete myObject.year;
console.log(myObject.year);
// output:
// undefined
```

!!!!info
När du skriver `something.something` syftar det oftast (men inte alltid) på att det som står till vänster om punkten är objektets namn och det som står till höger är antingen en egenskap eller en **metod** i objektet. Skillnaden mellan **_en funktion_** och **_en metod_** är att en metod är en funktion som är kopplad till ett objekt.
!!!!