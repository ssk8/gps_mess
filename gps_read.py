import csv
import simplekml

inputfile = csv.reader(open('GPS.CSV','r'))
kml=simplekml.Kml()


for line in inputfile:
  kml.newpoint(coords=[line[2], line[1]])

kml.save('gps.kml')