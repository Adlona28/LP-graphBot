import urllib.request
import os
import csv
import gzip
import datetime


def comprovaActualitzat():
    if os.path.isfile('ultimaActualitzacio.txt'):

        if not os.path.isfile('worldCitiesWithPopulation.csv'):
            d = datetime.datetime.now().day
            writeF = open('ultimaActualitzacio.txt', 'w')
            writeF.write(str(d))
            writeF.close()
            actualitza()

        else:
            readF = open('ultimaActualitzacio.txt', 'r')
            d = datetime.datetime.now().day
            dv = readF.read()
            readF.close()
            if int(dv) != d:
                writeF = open('ultimaActualitzacio.txt', 'w')
                writeF.write(str(d))
                writeF.close()
                actualitza()

    else:
        d = datetime.datetime.now().day
        writeF = open('ultimaActualitzacio.txt', 'w')
        writeF.write(str(d))
        writeF.close()
        actualitza()


def actualitza():
    urllib.request.urlretrieve("https://github.com/jordi-petit/lp-graphbot-2019/blob/master/dades/worldcitiespop.csv.gz?raw=true", "dades.gz")
    file = gzip.open('dades.gz', mode='rt')
    readCSV = csv.reader(file, delimiter=',')

    with open('worldCitiesWithPopulation.csv', 'w') as newFile:
        writer = csv.writer(newFile)
        bandera = False
        for row in readCSV:
            if bandera and row[4] != "" and float(row[4]) > 49999:
                writer.writerow([row[0], row[1], row[4], row[5], row[6]])
            bandera = True
    newFile.close()
