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
                
    #breakdown range into a list and return it
    def breakdownRange(self,range):
        resList=[]
        temp=range.split('-')
        lower,higher=int(temp[0]),int(temp[1])
        i=lower
        while(i<=higher):
            resList.append(i)
            i+=1
        return resList
        
    
    # processing for port
    def process(self,map,port,ip_address): 
        if('-' in port):
            portList=self.breakdownRange(port)
            if(len(map)==0):
                for i in range(portList[0],portList[-1]+1):
                    map[int(i)]=ip_address
                return True
            elif(len(map)>0):
                for i in range(portList[0],portList[-1]+1):
                    if(str(i) in map):
                        if(map[str(i)]!=ip_address):
                            return False
                return True
        else:
            if(port not in map and len(map)>0):
                return False
            elif(port in map):
                return map[port]==ip_address
            elif(len(map)==0):
                map[port]=ip_address
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
    
        
fw=Firewall("test.csv")
print(fw.accept_packet('inbound','udp','50-80','192.168.2.1'))

        