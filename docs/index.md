# Amanuensanteckningar

Den här sidan innehåller information om programmeringsspråk, verktyg och andra koncept. Allt material har skrivits av en amanuens som har jobbat i några kurser på programvaruteknik. Även om sidan inte är en officiell kursmaterial kan informationen som finns här hjälpa till med vissa kurser.

!!!!warning
**OBS!** Vissa delar av innehållet är fortfarande under utveckling. Du hittar mer information under "Utveckling pågår" i menyn till vänster.
!!!!

---

## Genomgång av webbsidan

Den här sidan är genererad från markdown-filer med hjälp av [MkDocs](https://www.mkdocs.org/). I den vänstra delen hittar du "moduler". Under varje sådan "modul" hittar du en massa sidor, men var inte rädd, eftersom de oftast är väldigt korta och behandlar endast ett koncept i taget så att du enkelt ska kunna hitta information när du behöver den.

När du går in på en sida kommer du att se underrubrikerna som länkar i den högra delen, vilket kanske också hjälper dig att navigera.

Du kan förresten söka efter specifika nyckelord eller något annat. Det är bara att skriva in i sökfältet längst upp till höger.

Sist, men inte minst, kan du växla mellan ljust och mörkt läge. Jag vet att vissa föredrar att ha all text mot en mörk bakgrund så jag lade till den funktionen. Bakgrunden för kodexempel är dock alltid mörk. Det är inget att diskutera om, man får ju inte koda med ljust färgtema 😈.

---

## Uppenbara saker som är viktiga att nämna

### Expanderande block

På olika sidor kan du se sådana block:

^^^^Klicka på mig!
Hej hej!
^^^^

Klicka på texten där för att visa eller dölja informationen inuti.

### Kodblock

Ibland får mina kodexempel inte plats så scrolla gärna horisontellt inuti kodblocket om någon rad verkar vara för lång. Testa här:

```python
print('\n'.join([''.join(['PROGRAMMERING'[(x - y) % 6] if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3 <= 0 else ' ' for x in range(-30, 30)]) for y in range(15, -15, -1)]))
```

### Quiz

På vissa sidor kan du hitta ett litet quiz där du kan testa dina kunskaper. Testa hur det funkar:

<iframe style="border: medium none currentcolor;" src="../../exercises/demo-exercise.html" width="100%" height="280px"></iframe>
