# JavaScript syntax

Om du har jobbat med något av de C-baserade programmeringsspråken, såsom C, C++, C# eller Java, kommer du att förstå JavaScripts syntax snabbt och enkelt. Man använder olika parenteser `()` och `{}` på precis samma sätt och alla rader ska avslutas med ett `;`. Det finns dock några specifika grejer som främst gäller datatyper och jämförelser som kan vara lite annorlunda. Sådana grejer ska jag fokusera lite mer på medan enklare syntaxkonstruktioner (såsom `if`-satser, loopar och enkla definitioner av funktioner) kommer jag att nämna väldigt kort.

^^^^Angående semikolon
Egentligen finns det en mekanism som kallas ASI (automatic semicolon insertion) som gör att man **kan** hoppa över `;` i JavaScript. Dock är det **dålig praxis**, eftersom man kan få ett oväntat resultat. Du kan läsa mer om hur ASI fungerar här:

> [Exploring JavaScript - Automatic Semicolon Insertion](https://witch.work/en/posts/javascript-semicolon-insertion) `Witch-Work`

^^^^

---

## Att skriva ut saker

Den här syntaxen kommer i flera exempel nedan, så det är väl lika bra att introducera den här raden redan nu:

```javascript
console.log("Hello world!");
```

Det är alltså innehållet inom parenteserna efter `console.log` som ska skrivas ut i JavaScript-konsolen i webbläsaren.

---

## Variabler och datatyper

JavaScript är ett dynamiskt typat språk, vilket innebär att man inte anger datatyper för variabler, utan att de bestäms vid körning baserat på de värden som lagras i variablerna.

Variabler i JavaScript kan deklareras med tre olika nyckelord, beroende på vilket beteende du vill uppnå. Det sätt som liknar hur variablerna fungerar i de flesta andra programmeringsspråk är att använda nyckelordet `let`:

```javascript
let year = 2026;
```

I äldre resurser kan du även hitta deklarationer med `var`:

```javascript
var i = 0;
```

Anledningen till att det **_inte_** rekommenderas att använda `var` är dess scope. `var` gör variabeln synlig inuti den funktionen där variabeln deklarerats och inte bara inuti det blocket där variabeln används. Med andra ord, om vi tar en `for`-loop som exempel:

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
// i finns inte här

// Men om man kör var:
var i = 15;
for (var i = 0; i < 5; i++) {
    console.log(i);
}
// här har i värdet 5.
```

Detta skapar otydligheter med scope och ska därför undvikas. 

Ett väldigt typiskt sätt att deklarera något i JavaScript är att använda `const`. Variabeln blir då konstant och man får inte tilldela något annat värde till samma variabel, men i modern JavaScript-praxis är det oftast just konstanter man använder. Till exempel om man väljer ett element från HTML så är det högst lämpligt att lagra det i en konstant variabel.

```javascript
const message = "Hello World!";
```

De vanligaste primitiva datatyperna i JavaScript är följande:

| Datatyp   | Exempel                           |
|-----------|-----------------------------------|
| Number    | `const year = 2026;`              |
| String    | `const message = "Hello World!";` |
| Boolean   | `const isComplete = true;`        |
| Null      | `const nothing = null;`           |
| Undefined | `let toBeDefined;`                |

^^^^NaN, Null och Undefined
Det är viktigt att förstå skillnaden mellan `null` och `undefined`. Särskilt när man debuggar sin JavaScript-kod.

Till exempel:

```js
const nothing = null;
let toBeDefined;

console.log(nothing);
console.log(toBeDefined);
// result:
// null
// undefined
```

Här finns det inget värde som lagras i `toBeDefined`. Förresten, kika på det här:

```js
let toBeDefined;
const anotherVariable = toBeDefined;

console.log(anotherVariable);
// result: undefined
```

---

`NaN` är ännu en intressant egenskap i JavaScript som betyder *Not a Number*. Detta värde returneras vid ogiltig numerisk beräkning eller konvertering, till exempel:

```javascript
console.log("Hello World!" / 10);
// result: NaN
```

`NaN` har förresten datatypen `Number` och `NaN === NaN` resulterar i `false`. Så spännande är det att jobba med JavaScript!
^^^^

---

## `const` och mutability

Jag vill förtydliga hur `const` egentligen fungerar och introducera begreppet *mutability*. Mutability kan beskrivas som ett värdes förmåga att ändras. Men det finns en skillnad mellan tilldelning och ändring av faktiska värden som lagras. `const` förhindrar just **tilldelningen**:

```javascript
const year = 2026;
year = 2027;
```

Den här koden kommer att ge ett runtime error, eftersom man använder `=` på ett namn som har deklarerats med `const`. Å andra sidan kan vi skriva så här:

```javascript
const lastTwoYears = [2026, 2025];
console.log(lastTwoYears);

lastTwoYears[0] = 2027;
lastTwoYears[1] = 2026;
console.log(lastTwoYears);

// output:
// [2026, 2025]
// [2027, 2026]
```

Det här är dock helt rimligt och kommer fungera hur bra som helst. Utskrifterna blir dock olika. `lastTwoYears` refererar fortfarande till samma array, men innehållet har ändrats.

Det finns alltså datastrukturer vars innehåll kan ändras även om själva variabeln som håller värdena är `const`. Dessa datastrukturer är **mutable**; deras värde kan ändras. Exempel på sådana datastrukturer är listor och objekt. 

Å andra sidan finns det även **immutable** datastrukturer som inte går att ändra, till exempel strängar.

---

## Konkatenering

Man kan konkatenera strängar på olika sätt i JavaScript. Man kan använda operationen `+`:

```javascript
const year = 2026;
const message = "Today is year ";
console.log(message + year);

// output:
// Today is year 2026
```

Alternativt kan man använda ett tillvägagångssätt som liknar `f`-strängar i Python. En sådan sträng i JavaScript skrivs med backtick (ett <code>&#x0060;</code>) istället för vanliga citattecken. Sedan omsluter man en variabel som man vill klistra in i `${}`:

```javascript
const year = 2026;
console.log(`Today is year ${year}`);

// ger samma output
```

---

## Villkor, jämförelser och boolesk algebra

### `if`-sats

Syntaxen för själva `if`-satsen är ganska enkel och följer den här strukturen:

```js
if (statement) {
    // exekvera koden här om statement är true
} else if (statement2) {
    // exekvera koden här om
    // statement är false och
    // statement2 är true
} else {
    // exekvera koden här om 
    // både statement och statement2
    // är false
}
```

### `switch`-sats

JavaScript har stöd för `switch-case`:

```js
switch (variable) {
    case value1:
        // exekvera koden här
        break;
    case value2:
        // exekvera koden här
        break;
    default:
        // om inget matchar,
        // exekvera koden här
}
```

### Jämförelser i JavaScript

Men när det kommer till jämförelser så är JavaScript ganska unikt i syntaxen och felaktig syntax här kan leda till oväntat resultat. Se följande exempel:

```js
// \n betyder radbrytning
const stringValue = "\n";
const numberValue = 0;

console.log(stringValue == numberValue);
// result: true
```

Hur kommer det sig att vi kan jämföra en sträng med radbrytning med ett numeriskt värde (0) och få ett resultat? Anledningen är just `==`. I JavaScript används `==` för att jämföra två värden, men bakom kulisserna kan JavaScript konvertera värdena enligt särskilda regler. I det här fallet kommer JavaScript att konvertera `"\n"` till ett tal, vilket kommer att resultera i `0`, eftersom strängen endast innehåller en radbrytning (samma skulle hända med `"\t"` eller en sträng som endast består av mellanslag). `0 == 0` ger såklart `true`. 

Det vore väldigt opraktiskt om det inte funnits något sätt att jämföra två värden med hänsyn till deras datatyper, såklart. Lösningen finns såklart och det är... att lägga till ett extra lika med tecken! `===`:

```js
// \n betyder radbrytning
const stringValue = "\n";
const numberValue = 0;

console.log(stringValue === numberValue);
// result: false
```

Nu får vi ett lite mer intuitivt förväntat resultat.

Detsamma gäller `!=` och `!==`. Det första konverterar värdena till samma datatyp och den andra kommer att ge ett lite mer intuitivt resultat.

### Boolesk algebra

När man vill kombinera flera villkor kan man använda följande logiska operatorer:

- `&&` betyder **AND** (och)
- `||` betyder **OR** (eller)
- `!` betyder **NOT** (icke)

Man kan såklart kombinera olika operatorer, till exempel:

```javascript
if ((age > 0 && age < 18) || (age > 50 && age < 110)) {
    doSomething();
}
```

---

## Loopar

Huvudsakligen finns det två vanligaste loopkonstruktioner i JavaScript: `for` och `while`. Det är ganska vanligt att använda metoden `.forEach()` för att iterera över en lista, men det är inte en loop i sig, så jag tar inte upp det här. Dessutom kräver det förståelse för vad callbacks är, vilket jag inte har gått igenom än.

### `for`:

```javascript
const lastFiveYears = [2026, 2025, 2024, 2023, 2022];
for(let i = 0; i < lastFiveYears.length; i++) {
    console.log(lastFiveYears[i]);
}
// output:
// 2026
// 2025
// 2024
// 2023
// 2022
```

Man kan även iterera över elementen istället för index:

```js
const lastFiveYears = [2026, 2025, 2024, 2023, 2022];
for(const year of lastFiveYears) {
    console.log(year);
}
// ger samma output
```

### `while`:

```javascript
const lastFiveYears = [2026, 2025, 2024, 2023, 2022];
let i = 0;
while(i < lastFiveYears.length) {
    console.log(lastFiveYears[i]);
    i++;
}
// ger samma output
```

### `break` och `continue`:

Båda nyckelorden finns i JavaScript och kan användas för att:

- `break` - avsluta loopen
- `continue` - gå direkt till nästa iteration

Här är ett exempel:

```javascript
const temperatures = [21.5, null, 22.0, -999, 23.4, 104.2, 22.8];
for (const temp of temperatures) {
    if (temp === null || temp < -50) {
        console.log("Inappropriate value, skipping...");
        continue;
    }
    
    if (temp > 100) {
        console.log(`WARNING: Overheating (${temp}°C)! Shutting down...`);
        break;
    }

    console.log(`Normal temperature: ${temp}°C`);
}

// output:
// Normal temperature: 21.5°C
// Inappropriate value, skipping...
// Normal temperature: 22°C
// Inappropriate value, skipping...
// Normal temperature: 23.4°C
// WARNING: Overheating (104.2°C)! Shutting down...
```

---

## Funktioner

Funktionerna kan deklareras med nyckelordet `function` följt av namnet och en lista av parametrar som funktionen kan ta emot. Funktionen anropas genom att skriva funktionens namn, följt av parenteser med eventuella förväntade argument.

```javascript
function printMessage(message) {
    console.log(message);
}

printMessage("Hello World!");

// output:
// Hello World!
```

Man kan såklart returnera resultatet från funktionen:

```javascript
function add(x, y) {
    return x + y;
}

console.log(add(5, 9));

// output:
// 14
```

---

## Felhantering

I JavaScript kan man såklart hantera fel som kastas ut:

```javascript
try {
    // koden som kan orsaka runtime exception
    throw new Error();
} catch (e) {
    console.log("An error occured: " + e.toString());
} finally {
    // koden som exekveras oavsett om 
    // exception har kastats ut eller inte
}
```

---

## Externa resurser

> [JavaScript Data Types](https://www.geeksforgeeks.org/javascript/javascript-data-types/) `GeeksForGeeks`  
> [Interesting Facts About JavaScript Data Types](https://www.geeksforgeeks.org/javascript/interesting-facts-about-javascript-data-types/) `GeeksForGeeks`  
> [Mutable](https://developer.mozilla.org/en-US/docs/Glossary/Mutable) `MDN`  
