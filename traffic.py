# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 06:04:49 2019

@author: Own
"""
print("-------------------------------------------------------------------------\n---------------WELCOME TO TRAFFIC AVOIDANCE SYSTEM----------------------\n------------------------------------------------------------------------\n")


import random

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


print("The directly connceted junctions are listed below along with the distance between them:")
main=[]
lis=[]
if __name__ == '__main__':
    global g,v
    g = Graph()

    g.add_vertex('kalanki')
    g.add_vertex('balkhu')
    g.add_vertex('kalimati')
    g.add_vertex('bafal')
    g.add_vertex('teku')
    g.add_vertex('tinkune')
    g.add_vertex('koteswor')
    

    g.add_edge('kalanki','balkhu',12)
    g.add_edge('kalanki','kalimati',6)
    g.add_edge('kalanki','bafal',7)
    g.add_edge('balkhu','kalimati',4)
    g.add_edge('kalimati','teku',2)
    g.add_edge('kalimati','bafal',8)
    g.add_edge('bafal','teku',9)
    g.add_edge('teku','balkhu',5)
    g.add_edge('teku','koteswor',10)
    g.add_edge('balkhu','tinkune',5)
    g.add_edge('tinkune','koteswor',7)
    g.add_edge('bafal','koteswor',15)
    
    

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()

            lis.append(vid)
            lis.append(wid)
            lis.append(v.get_weight(w))
            print(vid,"=>", wid, v.get_weight(w))
            
    print("\n")
      

n=3
final=[lis[i*n:(i+1)*n] for i in range((len(lis)+n-1)//n)]
"""print(final)"""

def rak():
    global a,b,cost
    a=input("Enter source where you want to start:")
    b=input("Enter the destination location:")
    
    
    
    for k in range(len(final)):
        if (a == final[k][0]) and (b == final[k][1]):
            print(a,"=>",b,final[k][2])
            
        
        for l in range(len(final)-1):
            if (final[k][0] == a) and (final[l+1][1]==b) and (final[k][1]==final[l+1][0]):
                cost=final[k][2]+final[l+1][2]
                print(a,"=>",final[k][1],"=>",b,"\nDistance:",cost,"\n")
            
            for x in range(len(final)-2):
                if (final[k][0] == a) and (final[x+2][1]==b) and (final[k][1]==final[l+1][0]) and (final[l+1][1]==final[x+2][0]):
                    cost=final[k][2]+final[l+1][2]+final[x+2][2]
                    print(a,"=>",final[k][1],"=>",final[l+1][1],"=>",b,"\nDistance:",cost,"\n")
rak()

def traffic():    
    
    q=random.randint(0,13)
    
    if q==0:
        print("\n NO TRAFFIC!")
    if q==1:
        print("Traffic in betn:",final[0][0],"=>",final[0][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[0][0],"=>",final[0][1],"* !!!")
        
    if q==2:
        print("Traffic in betn:",final[1][0],"=>",final[1][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[1][0],"=>",final[1][1],"* !!!")
        
    if q==3:
        print("Traffic in betn:",final[2][0],"=>",final[2][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[2][0],"=>",final[2][1],"* !!!")

    if q==4:
        print("Traffic in betn:",final[4][0],"=>",final[4][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[4][0],"=>",final[4][1],"* !!!")
        
    if q==5:
        print("Traffic in betn:",final[5][0],"=>",final[5][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[5][0],"=>",final[5][1],"* !!!")
    
    if q==6:
        print("Traffic in betn:",final[8][0],"=>",final[8][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[8][0],"=>",final[8][1],"* !!!")
        
    if q==7:
        print("Traffic in betn:",final[11][0],"=>",final[11][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[11][0],"=>",final[11][1],"* !!!")
        
    if q==8:
        print("Traffic in betn:",final[12][0],"=>",final[12][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[12][0],"=>",final[12][1],"* !!!")
        
    if q==9:
        print("Traffic in betn:",final[19][0],"=>",final[19][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[19][0],"=>",final[19][1],"* !!!")
        
    if q==10:
        print("Traffic in betn:",final[20][0],"=>",final[20][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[20][0],"=>",final[20][1],"* !!!")
    
    if q==11:
        print("Traffic in betn:",final[21][0],"=>",final[21][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[21][0],"=>",final[21][1],"* !!!")
    
    if q==12:
        print("Traffic in betn:",final[23][0],"=>",final[23][1])
        print("\n!!PLEASE TAKE THE ROUTE WITH THE MIN DISTANCE WHICH DO NOT INCLUDE  \n*",final[23][0],"=>",final[23][1],"* !!!")
                
traffic()
    
    
    
    
    
    