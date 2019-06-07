# GeoGraphBot

Aquest es un projecte de l'assignatura de Llenguatges de Programació del grau d'enginyeria informàtica de la FIB-UPC que consisteix en un bot de Telegram que genera i dóna informació sobre grafs geogràfics.

## Prerequisits i instalació

És necessari disposar de Python 3, un token.txt vàlid per a la comunicació amb Telegram, a part d'una connexió a Internet, la resta de paquets necessaris es poden obtenir al executar:

```
pip3 -r requirements.txt
```
En concret amb la comanda anterior s'instalaran els següents mòduls de Python:
```
python_telegram_bot
staticmap
haversine
networkx
fuzzywuzzy
telegram
```
Finalment per executar el bot es suficient amb executar:
```
python3 bot.py
```

## Arquitectura

L'arquitectura d'aquest projecte es ben simple, hi ha l'encarregat de desenvolupar les funcions de bot, tres codis que fan les tasques necessàries no trivials per separat i un petit codi que fa de gestor de comandes:

### Bot.py

L'encarregat de la interacci'o amb Telegram, llegeix les comandes i emmagatzema les dades individuals de l'usuari (graf actual i ubicació si l'usuari la comparteix)

### ActualitzaDades.py

Aquest codi s'executa amb la comanda start, per no haver de descarregar l'arxiu d'internet en cada interacció, genera un arxiu ultimaActualitzacio.txt, on mira si la última actualització és del dia actual, en cas de no ser-ho, descarrega les dades novament i en realitza el pretractament.

### GenGraph.py

S'encarrega de llegir les dades i generar el graf que es demana, a l'apartat d'eficiència s'explica l'estratègia per generar el graf

### DrawMap.py

Codi encarregat de la generació dels mapes de les comandes plotpop, plotgraph i route.

### GestorComandes.py

Codi encarregat de gestionar les comandes no trivials.

## Eficiència

### Preprocesament de les dades

Per tal de disminuïr la càrrega a l'hora de interactuar amb les dades, es fa un preprocessat que emmagatzema les dades útils memòria en el fitxer worldCitiesWithPopulation.csv, el que es fa es bastant senzill, donat que treballarem amb uns límits per a la distància i la població, s'eliminen les ciutats de les dades que o bé no tenen dades sobre la població o bé tenen població més petita del límit que es dona. 

Aquest preprocessat és molt simple, pero disminueix el tamany de les dades de forma considerable.

### Generació del graf

El que es fa per generar el graf sense haver de pagar el cost cuadràtic és ordenar les ciutats per longitud creixent, per a cada node es calcula una longitud límit cap a l'est, i es va comprovant amb els nodes següents si són adjacents, quan es troba un node que està a fora del límit inicia la recerca d'adjacències per al següent node.