# Callbacks, anonyma funktioner och lambda

Här vill jag introducera några viktiga koncept som ofta används i programmering generellt och som används väldigt ofta i frontend-utveckling. Även om sidan ligger under JavaScript och alla exempel här är skrivna i JavaScript, kan man använda samma princip i alla programmeringsspråk som har stöd för dessa mekanismer.

---

## Callbacks

När vi jobbar med funktioner brukar vi kunna skicka med några argument som funktionen kan jobba med, till exempel:

```js
function calculateSum(a, b) {
    return a + b;
}

console.log(calculateSum(5, 7));

// output:
// 12
```

Men man kan också skicka med funktioner som argument! En sådan mekanism, när vi skickar en referens till en funktion som en parameter och därefter anropar den, kallas *callback*.

```js
function calculate(operation, operand1, operand2) {
    return operation(operand1, operand2);
}

function addition(a, b) {
    return a + b;
}

function subtraction(a, b) {
    return a - b;
}

function multiplication(a, b) {
    return a * b;
}

function division(a, b) {
    return a / b;
}


console.log(calculate(addition, 5, 7));
console.log(calculate(subtraction, 12, 3));
console.log(calculate(multiplication, 7, 8));
console.log(calculate(division, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

I koden ovan definieras funktionen `calculate()`. Den tar emot tre argument: en referens till en funktion som implementerar operationen som ska utföras, en första operand och en andra operand. Därefter anropas `operation()`, alltså med parenteser, eftersom det är bara ett namn som refererar till en funktion och det är just så här funktioner anropas. `calculate()` används sedan inuti `console.log()` och skickar med namn på olika funktioner som utför själva beräkningarna.

I början kan det vara lite svårt att förstå hur det egentligen funkar, så ta dig den tid du behöver. Kör exemplet flera gånger, försök att ändra koden och se vad som händer.

!!!!warning   
Det är vanligt att man missar skillnaden mellan funktionsanrop och att skicka en funktion som en parameter.

När man skriver ett namn följt av parenteser betyder det att koden ska exekveras direkt. Om vi kikar på samma exempel, men anropar funktionen `addition()` istället för att skicka med referensen:

```js
console.log(calculate(addition(), 5, 7));
//                            ^ här!!!
```

I så fall kommer vi att få ett felmeddelande, eftersom parenteser efter funktionsnamnet (som markeras med `^ här!!!`) gör att funktionen exekveras istället.

Så det är viktigt att inte anropa funktionen när man bara vill skicka en referens.   
!!!!

---

## Anonyma funktioner

När vi definierar en funktion skriver vi oftast något i stil med:

```js
function addition(a, b) {
    return a + b;
}
```

Vi har alltså nyckelordet `function` och fortsätter med *funktionens namn*. En sådan funktion, som har ett namn, kallas för *en namngiven funktion*. Kan en funktion skapas utan ett namn? I vissa fall - ja! Nämligen när vi jobbar med callbacks. Titta på det här exemplet:

```js
function calculate(operation, operand1, operand2) {
    return operation(operand1, operand2);
}

console.log(calculate(function (a, b) {return a + b}, 5, 7));
console.log(calculate(function (a, b) {return a - b}, 12, 3));
console.log(calculate(function (a, b) {return a * b}, 7, 8));
console.log(calculate(function (a, b) {return a / b}, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

Det här är precis samma kod som vi hade i tidigare exempel, men i det här fallet definierar vi själva funktionen direkt inuti anropet till `calculate`. Som du ser saknar en sådan funktion något namn och vi anropar inte funktionen (inga `()` förekommer). Den här funktionen kommer dock att skickas som callback på ett helt korrekt sätt och det kommer att ge ett förväntat resultat. Om du behöver något enklare exempel med mindre funktioner och lite snyggare (snyggare och snyggare... :D) syntax, kika här:

/// tab | Namngiven funktion

```js
function getHelloWorld() {
    return "Hello World!";
}
console.log(getHelloWorld());
// output:
// Hello World!
```

///   
/// tab | Anonym funktion

```js
console.log(function() {
    return "Hello World!";
}());

// output:
// Hello World!
```

///

I det här exemplet skapar vi en anonym funktion som bara returnerar strängen "Hello World!". Sedan anropar vi funktionen inuti `console.log()`, notera `()` efter `}`, vilket gör att returvärdet skrivs ut i konsolen.

---

## Lambda (arrow function)

En *lambda* är en typ av anonym funktion som definieras utan nyckelordet `function`. I JavaScript fick lambda ett speciellt namn, *arrow function* på grund av dess `=>` syntax. Vi kan alltså använda precis samma miniräknarkod och skriva om den till lambda:

```js
function calculate(operation, operand1, operand2) {
    return operation(operand1, operand2);
}

console.log(calculate((a, b) => a + b, 5, 7));
console.log(calculate((a, b) => {return a - b}, 12, 3));
console.log(calculate((a, b) => a * b, 7, 8));
console.log(calculate((a, b) => {return a / b}, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

Syntaxen är alltså att börja med argument som lambda tar emot. Om lambda inte behöver några argument lämnar man bara parenteser `()`:

```js
// En funktion som bara
// exekverar en annan funktion...
// Så onödigt, men så illustrativt!
function execute(func) {
    func();
}

// lambda som inte tar emot några argument
execute(() => console.log("Hello World!"));
```

Därefter skriver man `=>` och sedan själva koden som ska exekveras av funktionen. Beroende på om det är ett enkelt uttryck eller flera rader kod eller om det förekommer nyckelord kan man behöva omsluta koden i `{}`. Du har sett att jag har det i vissa exempel med miniräknare, eftersom nyckelordet `return` används. Jag skippar dock `{}` i `execute()`-exemplet, eftersom inga nyckelord förekommer och koden är en enda expression. Jag skippar `{}` i vissa miniräknarexempel också, eftersom lambda kommer att försöka returnera resultatet från enkla uttryck när `{}` utelämnas.

---

## Alternativa sätt att definiera funktioner

Förutom ett "klassiskt" sätt kan vi använda syntaxen `function () {}` och lambda för att skapa namngivna funktioner.

///tab | Klassisk

```js
function calculate(operation, operand1, operand2) {
    return operation(operand1, operand2);
}

function addition(a, b) {
    return a + b;
}

function subtraction(a, b) {
    return a - b;
}

function multiplication(a, b) {
    return a * b;
}

function division(a, b) {
    return a / b;
}

console.log(calculate(addition, 5, 7));
console.log(calculate(subtraction, 12, 3));
console.log(calculate(multiplication, 7, 8));
console.log(calculate(division, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

///   
///tab | `function () {}`

```js
const calculate = function(operation, operand1, operand2) {
    return operation(operand1, operand2);
}

const addition = function(a, b) {
    return a + b;
}

const subtraction = function(a, b) {
    return a - b;
}

const multiplication = function(a, b) {
    return a * b;
}

const division = function (a, b) {
    return a / b;
}

console.log(calculate(addition, 5, 7));
console.log(calculate(subtraction, 12, 3));
console.log(calculate(multiplication, 7, 8));
console.log(calculate(division, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

///  
///tab | Lambda

```js
const calculate = (operation, operand1, operand2) => {
    return operation(operand1, operand2);
}

const addition = (a, b) => {
    return a + b;
}

const subtraction = (a, b) => {
    return a - b;
}

const multiplication = (a, b) =>  a * b;
const division = (a, b) => a / b;


console.log(calculate(addition, 5, 7));
console.log(calculate(subtraction, 12, 3));
console.log(calculate(multiplication, 7, 8));
console.log(calculate(division, 1, 0));

// output:
// 12
// 9
// 56
// Infinity
```

///

---

Jag kan inte hitta den där bilden som jag har sett för några år sedan, men jag tycker att om man förstår det så förstår man hur lambda- och anonyma funktioner fungerar. På bilden stod något i stil med:

!!!!   
Det är roligt hur `(()=>{})();` kan användas för precis vad som helst!   
!!!!  
