# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:52:41 2020

@author: bhalb
"""

import numpy

d4 = [1/4] * 4
d6 = [1/6] * 6
d8 = [1/8] * 8
d10 = [1/10] * 10
d12 = [1/12] * 12

class Distribution:
    ConvolutionDict = {}
    
    def __init__(self,dice=[],static=0):
        self.dist = [1]
        self.minimum = 0
        self.add(dice,static)
            
        
    def average(self):
        average = 0
        for i, chance in enumerate(self.dist):
            average += chance * (i + self.minimum)
        
        return average
    
    def halve(self):
        d = self.dist
        d2 = []
        minimumRoll = self.minimum
        
        if minimumRoll % 2 ==0:
            minimumRoll = int(minimumRoll / 2)
            for i in range(int(len(d)/2)):
                a = d[2*i]
                a += d[2*i+1]
                d2 += [a]
            if len(d) % 2 != 0:
                d2 += [d[-1]]
        else:
            minimumRoll = int(minimumRoll / 2)
            d2 += [d[0]]
            if len(d) >= 2:
                for i in range(int(len(d)/2)-1):
                    a = d[2*i+1]
                    a += d[2*i+2]
                    d2 += [a]
                if len(d) % 2 == 0:
                    d2 += [d[-1]]
                else:
                    d2 += [d[-1]+d[-2]]
        
        self.dist = d2
        self.minimum = minimumRoll
        return self
        
    def double(self):
        return self.multiply(2)
        
    
    def multiply(self, multiplier):
        if type(multiplier) != int:
            raise Exception("must use an int")
        if multiplier < 1:
            self.dist = [1]
            self.minimum = 0
        if multiplier == 1:
            return self
        
        newDist = []
        for chance in self.dist:
            newDist += [chance] + [0]*(multiplier-1)
        self.dist = newDist
        self.minimum = self.minimum*multiplier
        return self
            
    def add(self, dice, static):
        dist = self.dist
        #dist = Distribution.Convolve(dist,dice)
        for die in dice:
            dist = numpy.convolve(dist,die)
        self.dist = dist
        self.minimum += len(dice)+static
        if self.minimum < 0:
            raise Exception("< 0 damage not implimented")
        return self
    
    def combine(self,d2):
        self.dist = numpy.convolve(self.dist, d2.dist)
        self.minimum = self.minimum + d2.minimum
        return self
        
    def generate(self):
        for d, chance in enumerate(self.dist):
            yield d + self.minimum, chance
            
    def Combine(d1, d2):
        newDist = Distribution([],0)
        newDist.dist = numpy.convolve(d1.dist,d2.dist)
        newDist.minimum = d1.minimum + d2.minimum
        return newDist
    
    def Convolve(a1, a2):
        # unhashable type: 'list'
        if (a1,a2) in Distribution.ConvolutionDict:
            return Distribution.ConvolutionDict[(a1,a2)]
        else:
            c = numpy.convolve(a1, a2)
            Distribution.ConvolutionDict[(a1,a2)] = c
            return c
        
#dice= [] 
#static = 1
#
#dist = Distribution(dice, static)


# create this once the distrubution is finished
#damageChanceDict = {}
#for d, chance in enumerate(result):
#    damage = minimumRoll + d
#    damageChanceDict[damage] = chance
    

