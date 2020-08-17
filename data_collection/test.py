import pickle
import csv
f = open('./img1.csv','r')
rdr = csv.reader(f)
print(rdr)

for line in rdr:
    print(line)
 
f.close()