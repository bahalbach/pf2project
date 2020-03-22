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

#diename={4: "d4",
#         6: "d6",
#         8: }

class Distribution:
    ConvolutionDict = {}
    ConvolutionDiceDict = {}
    count = 0
    def __init__(self,dice=[],static=0,damageType=None):
        self.dist = [1]
        self.minimum = 0
#        self.name = ""
        self.add(dice,static)
        self.type = damageType
        
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
#        self.name+=".5"
        return self
        
    def double(self):
        return self.multiply(2)
        
    
    def multiply(self, multiplier):

        if multiplier < 1:
            self.dist = [1]
            self.minimum = 0
        if multiplier == 1:
            return self

        newDist = []
        newMinimum = int(self.minimum*multiplier)
        oldValue = newMinimum
        for i, chance in enumerate(self.dist):
            newDist += [chance]
            newValue = int((self.minimum+i+1)*multiplier)
            newDist += [0]*max(0,newValue-oldValue-1)
            
            oldValue = newValue
          
#        newDist = []
#        for chance in self.dist:
#            newDist += [chance] + [0]*(multiplier-1)
        self.dist = newDist
        self.minimum = newMinimum #self.minimum*multiplier
#        self.name+=str(multiplier)
        return self
            
    def add(self, dice, static):
        
        dist = self.dist
        dist = Distribution.ConvolveDice(dist,dice)
#        
#        for die in dice:
#            dist = numpy.convolve(dist,die)
##            dist = Distribution.Convolve(dist,die)
#            self.name+="d"+str(len(die))
        self.dist = dist
        self.minimum += len(dice)
        self.minimum += static
        
        if self.minimum < 0:
            raise Exception("< 0 damage not implimented")
        return self
    
    def addBonus(self, static):
        if self.minimum == 0:
            return self
        
        # don't go below 1, only if already above 1
        if self.minimum + static < 1:
            negativeShift = static + self.minimum - 1
            self.dist = Distribution.ShiftDown(self.dist,-negativeShift)
            self.minimum = 1
        else:
            self.minimum += static
    def addWeakness(self, static):
        if self.minimum == 0:
            return self
        
        # don't go below 1, only if already above 1
        if self.minimum + static < 0:
            negativeShift = static + self.minimum 
            self.dist = Distribution.ShiftDown(self.dist,-negativeShift)
            self.minimum = 0
        else:
            self.minimum += static
            
    def combine(self,d2):
        self.dist = Distribution.Convolve(self.dist, d2.dist)
        self.minimum = self.minimum + d2.minimum
        return self
    
    def minimum(self):
        return self.minimum
    def maximum(self):
        return self.minimum + len(self.dist) - 1
    
    def chanceLessThanOrEqualTo(self, number):
        if number < self.minimum:
            return 0
        elif number > self.maximum():
            return 1
        else:
            return sum(self.dist[0:(number-self.minimum+1)])
        
    def combineMax(self, d2):
        d1 = self
        minimum = max(d1.minimum,d2.minimum)
        maximum = max(d1.maximum(),d2.maximum())
        i = minimum
        previousChance = 0
        newDist = []
        while(i <= maximum):
            chance = d1.chanceLessThanOrEqualTo(i) * d2.chanceLessThanOrEqualTo(i)
            newDist.append(chance - previousChance)
            previousChance = chance
            i += 1
        self.minimum = minimum
        self.dist = newDist
        
    def selectMax(self, d2):
        if d2.average() > self.average():
            self.minimum = d2.minimum
            self.dist = d2.dist
        
    def generate(self):
        for d, chance in enumerate(self.dist):
            yield d + self.minimum, chance
            
    def Combine(d1, d2):
        newDist = Distribution([],0)
        newDist.dist = Distribution.Convolve(d1.dist,d2.dist)
        newDist.minimum = d1.minimum + d2.minimum
        return newDist
    
    def Convolve(a1, a2):
        # unhashable type: 'list'
        return numpy.convolve(a1, a2)
        key = (*a1,*a2)
        if key in Distribution.ConvolutionDict:
            Distribution.count += 1
#            print("found")
            return Distribution.ConvolutionDict[key]
        else:
            c = numpy.convolve(a1, a2)
            Distribution.ConvolutionDict[key] = c
            return c
        
    def ConvolveDice(dist, dice):
        for die in dice:
            dist = numpy.convolve(dist,die)
        return dist
#        return numpy.convolve(a1, a2)
        if dist != [1]:
            for die in dice:
                dist = numpy.convolve(dist,die)
            return dist
#        key = (*dist,)
        key = tuple()
        for die in dice:
            key += (len(die),)
        if key in Distribution.ConvolutionDiceDict:
            Distribution.count += 1
#            print("found")
            return Distribution.ConvolutionDiceDict[key]
        else:
            for die in dice:
                dist = numpy.convolve(dist,die)
            Distribution.ConvolutionDiceDict[key] = dist
            return dist
        
    def ShiftDown(dist, num):
        newDist = [0]
        for i in range(len(dist)):
            if i <= num:
                newDist[0] += dist[i]
            else:
                newDist.append(dist[i])
        return newDist
    
class DistributionsByType:
    def __init__(self):
        self.distributions = dict()
        
    def add(self, distribution):
        damageType = distribution.type
        if damageType in self.distributions:
            self.distributions[damageType].combine(distribution)
        else:
            self.distributions[damageType] = distribution
            
    def combineMax(self, distribution):
        damageType = distribution.type
        if damageType in self.distributions:
            self.distributions[damageType].combineMax(distribution)
        else:
            self.distributions[damageType] = distribution
            
    def selectMax(self, distribution):
        damageType = distribution.type
        if damageType in self.distributions:
            self.distributions[damageType].selectMax(distribution)
        else:
            self.distributions[damageType] = distribution
            
    def addDistributions(self, dists):
        for dist in dists.distributions.values():
            self.add(dist)
            
    def multiply(self, multiplier):
        for dist in self.distributions.values():
            dist.multiply(multiplier)
            
    def average(self):
        average = 0
        for dist in self.distributions.values():
            average += dist.average()
        return average
            
    def generate(self):
        combinationDist = Distribution()
        for dist in self.distributions.values():
            combinationDist.combine(dist)
        return combinationDist.generate()
#dice= [] 
#static = 1
#
#dist = Distribution(dice, static)


# create this once the distrubution is finished
#damageChanceDict = {}
#for d, chance in enumerate(result):
#    damage = minimumRoll + d
#    damageChanceDict[damage] = chance
    
