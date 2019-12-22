# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import heapdict as hd
import networkx as nx
class graph:
    def __init__(self):
        self.g = {}
        self.visited ={}    
    
    def insert(self, v1, v2, weight = 0):
        g = self.g
        if v1 not in g:
            g[v1] = {}
        if v2 not in g:
            g[v2] = {}
        g[v1][v2] = weight
    
    def symmetricInsert(self,v1, v2, weight = 0):
        self.insert(v1, v2, weight)
        self.g[v2][v1] = weight
    
    def toString(self):
        g = self.g
        for v1 in g:
            for v2 in g[v1]:
                print(v1, "-->",v2, g[v1][v2]) 
                
    def DFS(self):
        visited = self.visited
        g = self.g
        for v in g:
            visited[v] = False
        tour = []
        for v in g:
            if not visited[v]:
                self.dfs(v, tour)
                tour.append("conexa")
        return tour
    
    def dfs(self, vertex, tour):
        visited = self.visited
        g = self.g
        visited[vertex] = True
        tour += [vertex]
        for v in g[vertex]:
            if not visited[v]:
                self.dfs(v, tour)
        return tour
    
    def Prim(self,v):
        g=self.g
        visited=self.visited
        father={}
        cost=hd.heapdict()
        for u in g:
            father[u]=""
            visited[u]=False
            cost[u]=np.inf
        cost[v]=0
        i=0
        l=len(g)
        while i<l:
            i+=1
            v1,weight=cost.popitem()
            visited[v1]=True
            for v2 in g[v1]:
                if not visited[v2] and g[v1][v2]<cost[v2]:
                    father[v2]=v1
                    cost[v2]=g[v1][v2]
        return father
    
    def getGrafo(self):
        G = self.g
        G2={}
        for v1 in G:
            G2[v1]=[]
            for v2 in G[v1]:
                G2[v1]+=[v2]
        return G2
    
    def getGrafo2(self,G):
        if G == None:
            G = self.G
        G2={}
        for v1 in G:
            G2[v1]=[]
            for v2 in G[v1]:
                G2[v1]+=[v2]
        return G2
    
    def hamiltonian(self):
        tour = []
        visited = self.visited
        for u in self.g:
            visited[u]=False
        for u in self.g:
            flag = self.hamiltonianR(u, tour, len(self.g))
            if flag == True:
                break
        return tour
    
    def hamiltonianR(self, v, tour, sizeOfG):
        self.visited[v] = True 
        tour.append(v)
        if len(tour) == sizeOfG:
            return True
        else:
            flag = False
            for son in self.g[v]:
                if not self.visited[son]:
                    flag = self.hamiltonianR(son, tour, sizeOfG)
                    if flag == True:
                        return True
            tour.pop()
            self.visited[v] = False
            return False
    
    def getSymmetricG(self):
        g = graph()
        for v1 in self.g:
            for v2 in self.g[v1]:
                g.symmetricInsert(v1, v2)
        return g.g
        
    def color(self, numberOfColors):
        colors = {}
        g = self.getSymmetricG()
        ini = None
        for v in g:
            ini = v
            colors[v] = 0
            self.visited[v] = False
        self.colorR(ini, 0, colors, len(self.g), numberOfColors, g)
        return colors
    
    def checkAvailableColors(self, v, n, colors, g):
        av = [1]*(n+1)
        for son in g[v]:
            av[colors[son]] = 0
        resp = []
        for i in range(1,n+1):
            if av[i]==1:
                resp.append(i)
        return resp
        
    def colorR(self, v, colored, colors, sizeOfG, n, g):
        av = self.checkAvailableColors(v, n, colors, g)
        flag = False
        for num in av:
            colors[v] = num
            self.visited[v] = True
            if colored == sizeOfG:
                return True
            for son in g[v]:
                if not self.visited[son]:
                    flag = self.colorR(son, colored+1, colors, sizeOfG, n, g)
                if flag == True:
                    break
            if flag == True:
                    break
        if flag == False:
            colors[v] = 0
            self.visited[v] = False
        return flag
        
G = graph()
G.symmetricInsert("a", "b")
G.symmetricInsert("b", "c")
G.symmetricInsert("b", "d")
G.symmetricInsert("a", "e")
print(G.DFS())

G=graph()
G.insert("a","b",4)
G.symmetricInsert("a","h",8)
G.insert("b","h",11)
G.symmetricInsert("b","c",8)
G.symmetricInsert("h","i",7)
G.symmetricInsert("h","g",1)
G.symmetricInsert("i","c",2)
G.symmetricInsert("i","g",6)
G.insert("c","d",7)
G.symmetricInsert("c","f",4)
G.symmetricInsert("g","f",2)
G.symmetricInsert("f","d",14)
G.symmetricInsert("f","e",10)
G.insert("d","e",9)
"""
a = G.Prim('a')
grafo=nx.DiGraph(G.getGrafo2(a))
nx.draw(grafo,with_labels=True)
"""

a = G.hamiltonian()
print("hamiltoniano",a)
b = G.color(3)
print("color", b)
grafo=nx.DiGraph(G.getGrafo())
nx.draw(grafo,with_labels=True)
