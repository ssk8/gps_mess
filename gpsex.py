import csv
import simplekml

inputfile = csv.reader(open('GPS.CSV','r'))
kml=simplekml.Kml()

for row in inputfile:
  kml.newpoint(timestamp=row[0], coords=[(row[2],row[1])])

kml.save('gps.kml')