# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:33:39 2019

@author: abhis
"""

import csv
res=[]

with open('loci.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
        if(i[0]!='position'):
            count=0
            with open('reads.csv') as csv_file2:
                csv_reader2 = csv.reader(csv_file2, delimiter=',')
                for j in csv_reader2:
                    if(j[0]!='start'):
                        if(int(j[0])>=int(i[0]) and (int(j[0])+int(j[1]))<=int(i[0])):
                            count+=1
                res.append(count)
                print(count)


with open('loci.csv', mode='w') as csv_file:
    lcsv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(lcsv_writer)):
        lcsv_writer.writerow([lcsv_writer[i],res[i]])
            

        