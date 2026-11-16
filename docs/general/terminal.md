# Grundläggande arbete med terminal

Som utvecklare använder man terminalen ganska ofta, och därför är det viktigt att lära sig att använda den. Dessutom används terminalen och terminalkommandon för att arbeta med versionshantering och initialisering av vissa projekt. I den här guiden går jag igenom de absoluta grunderna som du kommer att behöva. Guiden kommer framför allt att täcka hur man arbetar med datorns filsystem.

!!!! warning
Beroende på vilket operativsystem du använder kan vissa delar av terminalen, utskrifter och kommandon se lite olika ut. I guiden nedan använder jag Unix-terminal (Linux/macOS) som ett exempel, men installerar du *git* med *git Bash* på Windows kommer skillnaderna vara minimala:

I Unix-baserade system är rotkatalogen `/`. I Windows är det enhetsbokstäver istället, t.ex. `C:\`. Använder du Git Bash kommer `C:\Users\<ditt_användarnamn>` motsvara `/c/Users/<ditt_användarnamn>`.
!!!!

----

## Navigera i filsystemet

### pwd

På samma sätt som du använder utforskaren för att se innehållet i olika mappar, öppna, skapa, radera mappar och filer, kan du göra detta från terminalen. När du öppnar terminalen brukar du stå i terminalens rotkatalog, vilket oftast är din användarmapp. I terminalen kan det se ut i stil med följande, där `~` betyder `/users/kiya2400`:

```bash
kiya2400@MacBook-Air ~ % 
```

För att ta reda på var exakt du befinner dig, kör följande kommando:

```bash
pwd
```

`pwd` betyder *print working directory* och skriver ut en fullständig sökväg till den katalog där du befinner dig just nu. Resultatet som jag fick är:

```bash
kiya2400@MacBook-Air ~ % pwd
/Users/kiya2400
```

### ls / dir

///tab | macOS & Linux

Vidare kan du exempelvis se vilka kataloger och filer som finns i den mappen där du står just nu, vilket görs med `ls` (list) kommandot. I Command Prompt på *Windows* använder man `dir` istället. `ls` funkar dock i PowerShell.

```bash
kiya2400@MacBook-Air ~ % ls
Applications	Library			Projects
Desktop			MIUN			Public
Documents		Movies			PyCharmMiscProject
Downloads		Music			Zotero
kattis			Pictures
```
///
///tab | Windows
Vidare kan du exempelvis se vilka kataloger och filer som finns i den mappen där du står just nu, vilket görs med `dir` kommandot. `ls` (list) funkar dock i PowerShell.
///

Som standard visas inte dolda kataloger. Vill du verkligen se ALLT kan du köra `ls -a`, vilket kommer att inkludera alla dolda kataloger och filer.

### cd

Nästa kommando låter dig navigera till andra kataloger. Kommandot heter `cd` (change directory) och man skriver även vilken katalog man vill navigera till. Vill man navigera ett steg bakåt kan man skriva `cd ..` (glöm inte mellanslaget!):

```bash
kiya2400@MacBook-Air ~ % cd MIUN
kiya2400@MacBook-Air MIUN % pwd
/Users/kiya2400/MIUN

kiya2400@MacBook-Air MIUN % cd ..
kiya2400@MacBook-Air ~ % pwd
/Users/kiya2400
```

!!!! success
**TIPS!** När du skriver `cd` kan du trycka på ++tab++ på tangentbordet för att få förslag på vilka kataloger du kan navigera till. Du kan även börja skriva namn på katalogen som du vill navigera till och sedan använda ++tab++ för autokomplettering.
!!!!

### mkdir

Ett sista kommando som används för att manipulera kataloger är `mkdir`, som står för *make directory* och som kan användas för att skapa en ny mapp:

```bash
kiya2400@MacBook-Air ~ % mkdir test
kiya2400@MacBook-Air ~ % ls
Applications	Library			Projects
Desktop			MIUN			Public
Documents		Movies			PyCharmMiscProject
Downloads		Music			test
kattis			Pictures		Zotero
```

----

## Skapa, redigera och radera filer

Oftast kan man skapa, redigera och radera filer direkt i sin IDE, men ibland kan man behöva göra det snabbt i terminalen.

### touch/echo

///tab | macOS & Linux

`touch` följt av filnamnet används för att skapa en fil:

```bash
kiya2400@MacBook-Air terminal_guide % ls
# ingen output betyder att det inte finns några kataloger/filer här            
kiya2400@MacBook-Air terminal_guide % touch example.txt
kiya2400@MacBook-Air terminal_guide % ls
example.txt
```
///
///tab | Windows
Använd `echo > <filename>` på Windows (funkar på både CMD och PowerShell). Till exempel `echo > example.txt`.
///

### rm

För att radera en fil kan du använda `rm` (remove) följt av filnamnet.

```bash
kiya2400@MacBook-Air terminal_guide % ls
example.txt
kiya2400@MacBook-Air terminal_guide % rm example.txt
kiya2400@MacBook-Air terminal_guide % ls
kiya2400@MacBook-Air terminal_guide % 
```

Med `rm` kan man även radera kataloger. Dock behöver man lägga till några flaggor för att kunna göra det. När man försöker exekvera `rm` på en katalog får man följande felmeddelande:

```bash
kiya2400@MacBook-Air terminal_guide % cd ..
kiya2400@MacBook-Air ~ % rm terminal_guide
rm: terminal_guide: is a directory
```

Anledningen är att när man raderar en katalog riskerar man även att radera alla underliggande filer/mappar. Lägger man till `-r` (står för rekursivt) kommer alla underliggande filer och kataloger att raderas tillsammans med den katalogen man anger:

```bash
kiya2400@MacBook-Air ~ % rm terminal_guide
rm: terminal_guide: is a directory

kiya2400@MacBook-Air ~ % rm -r terminal_guide
# en tom rad betyder att katalogen har raderats
kiya2400@MacBook-Air ~ % 
```

!!!! warning
**OBS!!!** Filer och kataloger som raderas med `rm` hamnar **inte** i papperskorgen, vilket betyder att de inte kan återställas! Var därför försiktig med det här kommandot.
!!!!

### nano/notepad

Det är sällan man redigerar filer i terminalen, men ifall man absolut behöver kan man såklart göra det. För Windows finns det tyvärr ingen inbyggd terminalbaserad textredigerare, så man får använda Notepad istället genom att skriva `notepad <filename>`, till exempel `notepad example.txt`.

För dig som använder Git Bash eller Unix-baserade OS finns den terminalbaserade texteditorn *nano* tillgänglig:

```bash
kiya2400@MacBook-Air terminal_guide % nano example.txt
```

Du kommer att se något i stil med:

```bash
UW PICO 5.09                       File: example.txt                          

[en massa tomma rader]

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
```

Där kan du redigera texten. Jag lägger till en enkel *Hello World!*:

```bash
UW PICO 5.09                   File: example.txt                    Modified  


Hello World!


^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell 
```

Du ser nu längst upp att filen är modifierad och vi kan spara ändringar genom att trycka på ++ctrl+o++ (writeout) följt av ++enter++ (bekräfta att skriva i `example.txt`). Alternativt kan du trycka på ++ctrl+x++ (exit) följt av ++y++ (bekräfta att spara ändringar) och ++enter++ (bekräfta att skriva i `example.txt`).

På samma sätt kan `nano` eller `notepad` användas för att se innehållet i olika filer.
