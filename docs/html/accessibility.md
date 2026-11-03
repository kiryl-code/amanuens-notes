# Tillgänglighet

Tillgänglighet handlar ofta om mer än att bara välja rätt HTML-element. Det finns flera enkla och avancerade tekniker för att öka webbsidans tillgänglighet.

---

## Färgkontrast

Den enklaste och mest uppenbara saken som man måste tänka på är färgkontrast. Detta innebär att det måste finnas tillräcklig skillnad i ljusstyrka mellan text och bakgrund. Ibland handlar det inte bara om tillgänglighet för personer med nedsatt syn eller färgblindhet. Testa till exempel bakgrundsfärgen `#EEEEEE` och textfärgen `#FFFFFF`. Detta är ett exempel på dålig kontrast där texten blir oläsbar.

---

## Alternativ text

Som du har sett i tidigare exempel har `<img>`-elementet ett `alt`-attribut för att visa alternativtext. Förutom att visa texten när bilden inte kan laddas används alternativtext också av skärmläsare, vilket innebär att det är viktigt att ange en alternativ beskrivning för att öka sidans tillgänglighet. Däremot kan man lämna `alt` tomt om bilden endast används som dekoration. I så fall hoppar skärmläsaren över bilden.

---

## Etiketter

Ännu en mekanism som är inbyggd i HTML är etiketter (`label`). Etiketter kopplar en beskrivande text till ett fält i formuläret, till exempel:

```html
<label for="userEmail">E-postadress</label>
<input type="email" id="userEmail" name="email" required>
```

Etiketter är ett standardiserat sätt att beskriva vad som ska fyllas i och de används också av skärmläsare. Dessutom förstorar etiketter den klickbara ytan så att motsvarande `input` aktiveras när man klickar på etiketten.

---

## Tabindex

En annan sak är tangentbordsnavigering, vilket betyder att alla interaktiva element (såsom knappar och formulärfält) måste gå att använda med enbart tangentbordet. Vanligtvis används tangenterna `Tab`, `Enter`, `Space` och piltangenterna. Man kan göra ett element nåbart med `Tab` genom att lägga till attributet `tabindex="0"`.

---

## ARIA

ARIA (*Accessible Rich Internet Applications*) är en standard som ger extra information till skärmläsare när vanlig HTML inte räcker till. Ett exempel kan vara `aria-expanded="true"` eller `aria-expanded="false"` på en knapp som expanderar en meny. Skärmläsare har ingen information om huruvida menyn är visad eller inte och behöver därför `aria-expanded` för att ta reda på det. **Den viktigaste** regeln med ARIA är att om du kan klara dig med befintliga HTML-element och deras inbyggda semantik, ska du göra det istället för att bygga ett element av `div` och lägga till ARIA-attribut.

---

## Externa resurser

> [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms) `MDN`  
> [Tabindex HTML global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex) `MDN`  
> [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) `MDN`   