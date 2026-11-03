# Display: inline & block

Det är också bra att känna till skillnaden mellan _**blockelement**_ och _**inline-element**_. 

---

## Blockelement

Ett blockelement börjar normalt på en ny rad och tar som standard upp hela tillgängliga bredden. Exempel på sådana element är `<div>`, `<p>` och `<section>`. 

---

## Inline-element

Ett inline-element placeras däremot i det löpande innehållet och börjar inte automatiskt på en ny rad. Exempel är `<span>`, `<a>` och `<strong>`.

---

## Inline-block

Det finns även `inline-block` som kombinerar egenskaper från båda typerna. Ett element med `display: inline-block` placeras i löpande innehållet ungefär som ett inline-element, men man kan också ange dess `width` och `height`, ungefär som för ett blockelement. Ett tydligt exempel på ett användningsområde är hur navigationsmenyer byggdes upp tidigare. Då använde man en lista med länkar och eftersom `<li>` normalt visas som blockelement satte man `display: inline-block` för att placera listelementen bredvid varandra.

---

!!!! warning
Kom ihåg att `inline`, `block` och `inline-block` handlar om elementens CSS-egenskap `display`. Detta är alltså inte elementets egna egenskap, utan man kan ändra hur ett element visas med CSS.
!!!!