import csv
with open('./worldcities.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	with open('worldCitiesWithPopulation.csv', 'w') as newFile:
	    writer = csv.writer(newFile)
	    for row in readCSV:
	    	if row[4] != "":
	    		writer.writerow([row[0], row[1], row[4], row[5], row[6]])
	newFile.close()
csvfile.close()
