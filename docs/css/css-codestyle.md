# Kodstil

## Grundläggande kodstil

Den grundläggande strukturen för CSS-syntax har du redan sett i mina tidigare exempel:

```css
/* block 1 */
selector {
    property: value;
}

/* block 2 */
selector {
    property: value;
}
```

Observera att `{` skrivs på samma rad som `selector`, att samtliga egenskaper indenteras med ett steg och att en stängande `}` skrivs på en ny rad. En tom rad lämnas mellan två block. Du ser även att man kan skriva kommentarer med syntaxen `/* ... */`. Man brukar även skriva stilar från de mest generiska högst upp (till exempel `*` eller elementselektorer) till de mest konkreta längst ner (klasser och `id`).

---

## Ordning på egenskaper

När det kommer till hur man skriver olika stilar finns det som sagt ingen gemensam konvention. För ett exempel på hur du kan strukturera stilar kan du läsa [den här artikeln](https://fordinteractive.com/2009/02/order-of-the-day-css-properties/). Du kanske inte vill använda exakt samma ordning, men ta med dig huvudtanken och försök att vara konsekvent med den stil du väljer.

---

## Namnkonventioner

Det finns även ett flertal namnkonventioner för hur man ska namnge klasser på bästa sätt. Beroende på vad man utvecklar kan man använda sig av olika namngivningskonventioner.

### BEM

BEM står för block-element-modifier, till exempel:

```css
.nav {
    ...
}

.nav__link {
    ...
}

.nav__link--active {
    ...
}
```

### Atomic CSS

Atomic CSS används ofta när man utvecklar CSS-ramverk eller större bibliotek, till exempel *Tailwind*. I det här systemet skriver man mer atomära regler. Flera regler kan tillämpas på ett element för att nå ett önskat resultat. Till exempel:

```css
.text-red {
    color: red;
}

.w-full {
    width: 100%;
}
```

---

I början kan du använda enklare, beskrivande namn för CSS-klasser och det kommer att fungera lika bra. Men vill du ha ännu mer strukturerad kod kan du försöka hålla dig till någon av konventionerna.

---

## Externa resurser

> [Organizing your CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Organizing) `MDN`