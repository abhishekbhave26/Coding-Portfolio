# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:54:18 2019

@author: abhis
"""

import csv

class Firewall():
    
    def __init__(self,path):
        self.path=path
        self.inboundMapTCP={}
        self.outboundMapTCP={}
        self.inboundMapUDP={}
        self.outboundMapUDP={}
        
        splitPath=self.path.split('/')
        file=splitPath[-1]
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                    res=self.accept_packet(row[0],row[1],row[2],row[3])
                    print(res)
    
    def checkPort(self,port):
        if('-' in port):
            return True
        else:
            return False
    
    # for processing ip_address
    def checkIP(self,ip1,ip2):
        pass
    
    # processing for port
    def process(self,map,port,ip_address): 
        if('-' in port):
            temp=port.split('-')
            lower,higher=int(temp[0]),int(temp[1])
            if(len(map)==1):
                if(port not in map):
                    if(self.checkPort(port)):
                        
                else:
                    
            else:
                map[port]=ip_address
        else:
            if(len(map)==1):
                if(port not in map):
                    return False
                else:
                    return self.checkIP(map[port],ip_address)
        return True
        
    def accept_packet(self,direction,protocol,port,ip_address):
        # processing for direction and protocol
        if(direction=='inbound'):
            if(protocol=='tcp'):
                return self.process(self.inboundMapTCP,port,ip_address)
            else:
                return self.process(self.inboundMapUDP,port,ip_address)
        else:
            if(protocol=='tcp'):
                return self.process(self.outboundMapTCP,port,ip_address)
            else:
                return self.process(self.outboundMapUDP,port,ip_address)
    
        
fw=Firewall("D:/All Repositories/Coding Portfolio/file.csv")
#print(fw.accept_packet('inbound','tcp','80','192.168.1.2'))
    

        