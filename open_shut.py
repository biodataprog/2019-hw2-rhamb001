door = 0
closedword = 0
doorword = 0
openword = 0

import os,gzip

# write a script to create new file called closed.txt

file="/bigdata/gen220/shared/simple/title.basics.tsv.gz"

if not os.path.exists(file):
    os.system("curl -O https://datasets.imdbws.com/title.basics.tsv.gz")
    
with gzip.open(file,"r") as fh:
    header = next(fh)
    for line in fh:
        row = line.decode('utf-8').strip().split("\t")
        title = row[2]
        title2 = title.lower()
        words1 = title2.split()
        for n in words1:
            if n == 'door':
                doorword = doorword + 1
                #print(words1)
                #print(doorword)
        if 'door' in title2:
            door = door + 1
            #print(row)
            #print(door)
        elif 'Open ' in title:
            openword = openword + 1
            #print(row)
            #print(openword)
        elif 'Closed ' in title:
            closedword = closedword + 1
            #print(row)
            #print(closedword)
            
#print(door)
#print(doorword)
#print(openword)
#print(closedword)

#write to outfile
outfile = open("closed.txt","w")
outfile.write("The number of movies containing door in the title is: %s"%(door))
outfile.write("\n")
outfile.write("The number of movies containing the word door in the title is: %s"%doorword)
outfile.write("\n")
outfile.write("The number of movies containing the words 'Open' or 'Closed' in the title is: %s"%(openword+closedword))
