#!/usr/bin/python
import sys
import re

id_list_file = sys.argv[1]
seq_file = sys.argv[2]
id_list = set()
f = open (id_list_file, 'r')

for line in f:
    line = line.rstrip()
    fields = str.split(line)
    id_list.add(fields[0])
    #sys.stdout.write(fields[0])

f.close()

f = open (seq_file,"r")
lastid = ''
lastseq = ''
x = re.compile('^\>sp|')

for line in f:
        id_search = re.search('^\\>sp\\|(.*)\\|',line)
        if id_search:
            id = id_search.group(1)
            #print (id + "found")
            if (lastid and (lastid in id_list)) :
                sys.stdout.write(lastseq)
            lastid = id
            lastseq = line
        else:
            lastseq = lastseq + line
