import csv
import numpy
from datetime import datetime
with open('data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	row1 = reader.next()
	ts0  = datetime.fromtimestamp(float(row1[0]))
	a = []
	for row in reader:
		ts1  = datetime.fromtimestamp(float(row[0]))
		tdelta = ts1 - ts0
		a.append(float(row[3]))
		if tdelta.seconds >= 5:
			p = numpy.percentile(a, 50)
			avg = sum(a)/float(len(a))			
			print ts0.strftime('%H:%M:%S'),avg,"%0.4f"%p
			a = []
			ts0 = ts1
			tdelta = 0
