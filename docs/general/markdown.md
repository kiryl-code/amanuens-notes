# Markdown

Markdown är ett formateringsspråk som används för att skriva dokument. Det används ofta i versionskontrollsystem och det kan därför vara bra att kunna språket. Man behöver inte ha någon särskild utvecklingsmiljö för att skriva markdown, utan det kan göras i vilken texteditor som helst. Många utvecklingsmiljöer såsom VSCode eller IDE:er från JetBrains en inbyggd förhandsvisning av markdown-filer. Markdown-filer har filändelsen `.md`, till exempel: `README.md`.

För att göra det lite enklare i den här guiden kan du använda dig av onlineverktyget [Online Markdown](https://onlinemarkdown.com/). När du öppnar Online Markdown kommer du att få upp ett exempel på en sida med en massa text som är skriven med markdown och redan detta kan vara ett bra exempel som du kan kika på eller experimentera med för att förstå hur markdown fungerar. Den vänstra delen visar markdown-kod och den högra delen visar resultatet.

----

## Textformatering

### Rubriker

Enligt konventionen ska alla markdown-filer inledas med en rubrik. I Markdown finns det 6 olika rubriksnivåer där den första nivån motsvarar den största rubriken och den lägsta motsvarar den minsta. Konventionen är att man endast ska ha ***en*** rubrik på nivå 1. Sedan följer vi en enkel regel: en underrubrik ska alltid vara ett steg mindre än tillhörande huvudrubrik. Rubrikerna skapas med `#` följt av mellanslag och rubriktexten.

!!!! warning
OBS! Ett vanligt misstag är att skippa mellanslaget, vilket kommer att resultera i felaktig formatering.
!!!!

Antalet `#` tecken definierar rubriksnivån. Till exempel kan vi skriva rubriker i den här guiden som följande:

```md
# Markdown

## Textformatering
### Rubriker
...
```

### Textstycke

En stor fördel med Markdown är att man även kan formatera brödtext för att göra den mer lättläst. En grundläggande del av texten i Markdown är ett stycke som skapas genom att skriva text mellan tomma rader:

```md
Det här är ett textstycke.
```

!!!! warning
Observera att en enkel radbrytning inte skapar ett nytt stycke. För att skapa ett nytt textstycke behöver du ha en tom rad, till exempel:

```md
Textstycke 1

Textstycke 2
```

Vill du ha en radbrytning utan att starta ett nytt stycke behöver du avsluta raden med två mellanslag.
!!!!

### Fet, kursiv och kod

Sedan kan du såklart formatera text genom att applicera **fet** eller *kursiv* stil eller betona `kod` i löpande text. Den här meningen kan formateras genom att skriva följande markdown:

```md
Sedan kan du såklart formatera text genom att applicera **fet** eller *kursiv* stil eller betona `kod` i löpande text. 
```

För att göra texten till kursiv eller fetstil kan du använda både `*` och `_`.

### Punktlistor

Du kan även använda punktlistor genom att skriva `*`, `-` eller `1.` som markör. En punktlista ska separeras med en tom rad innan och en tom rad efter. För icke-ordnade listor kan underpunkter läggas till med hjälp av indentering:


```md
- Punkt 1
- Punkt 2
    - Punkt 2.1
    - Punkt 2.2
- Punkt 3

1. Punkt 1
2. Punkt 2
3. Punkt 3
```

### Länkar

En sista textformatering som ofta kan vara användbar är länkar. Följande syntax används för att rendera länkar med önskad text:

```md
[Amanuensanteckningar](https://kiryl-code.github.io/amanuens-notes/)
```

----

## Kodformatering

När du skriver markdown-filer försök att alltid betona kodrelaterade delar av löpande text som `kod` (se exempel ovan). Ibland kan man behöva skriva ett kodblock, en lite större del av koden för att illustrera sina tankar eller visa ett exempel. Markdown har stöd för sådana kodblock som även har syntax highlighting, vilket betyder att det blir mycket enklare för läsaren att ta del av koden.

    ```py
    print("Hello world")
    ```

    ```js
    console.log("Hello world");
    ```

----

## Övriga (text)block

Det finns en del andra block man kan använda. De används inte lika ofta som de block som beskrivs ovan, men kan vara bra att känna till.

### Bilder

Man kan klistra in **bilder** med följande syntax, där *url_till_bilden* kan vara en URL till bilden på internet eller en relativ sökväg till en fil.

```md
![Alternativ text som visas om bilden inte kan laddas](<url_till_bilden>)

Ett exempel:
![Pythons logotyp](https://www.python.org/static/img/python-logo.png)
```

### Citat

Citat kan man skriva med hjälp av följande syntax:

```md
> Man kan inte köra `git status` för många gånger
```

### Tabeller

Med Markdown kan man även inkludera tabeller i sin text:

```md
Exempel på en tabell i en relationsdatabas:

| Id | Name          | registrationDate |
|----|---------------|------------------|
| 1  | Alexa Elisedd | 2026-09-13       |
| 2  | Silas Ryker   | 2026-11-11       |
```