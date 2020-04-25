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
    OnlyAverage = False
    NoCalculation = False
    ConvolutionDict = {}
    ConvolutionDiceDict = {}
    count = 0
    def __init__(self,dice=[],static=0,damageType=None):
        self.dist = [1]
        self.minimum = 0
        if Distribution.NoCalculation:
            self.average = 0
        else:
            self.average = None
#        self.name = ""
        self.add(dice,static)
        self.type = damageType
        
        
    def getAverage(self):
        if not self.average is None:
            return self.average
        self.average = 0
        if Distribution.NoCalculation:
            raise Exception("No average")
        for i, chance in enumerate(self.dist):
            self.average += chance * (i + self.minimum)
        
        return self.average
    
    def halve(self):
        if Distribution.NoCalculation:
            self.average /= 2
            return self
        
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
        self.average = None
#        self.name+=".5"
        return self
        
    def double(self):
        return self.multiply(2)
        
    
    def multiply(self, multiplier):
        if Distribution.NoCalculation:
            self.average *= multiplier
            return self
        
        if multiplier == 0:
            self.dist = [1]
            self.minimum = 0
            self.average= 0
            return self
        if multiplier < 1:
            newDist = []
            newMinimum = int(self.minimum*multiplier)
            oldValue = newMinimum
            for i, chance in enumerate(self.dist):
                newValue = int((self.minimum+i)*multiplier)
                if newValue == oldValue and len(newDist) >= 1:
                    newDist[-1] += chance
                else:
                    newDist += [chance]
                oldValue = newValue
            self.dist = newDist
            self.minimum = newMinimum
            self.average = 0
            return self
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
        self.average = None
        return self
            
    def add(self, dice, static):
        if Distribution.NoCalculation:
            self.average += static
            for die in dice:
                self.average += (len(die)+1)/2
            return self
        
        dist = self.dist
        dist = Distribution.ConvolveDice(dist,dice)
#        
#        for die in dice:
#            dist = numpy.convolve(dist,die)
##            dist = Distribution.Convolve(dist,die)
#            self.name+="d"+str(len(die))
        self.dist = dist
        self.minimum += len(dice)
        return self.addBonus(static, alwaysAdd=True)
        # self.minimum += static
        # self.average = None
        
        # if self.minimum < 0:
        #     raise Exception("< 0 damage not implimented")
        # return self
    
    def addBonus(self, static, alwaysAdd=False):
        if Distribution.NoCalculation:
            self.average += static
            if self.average > 0:
                self.average = max(self.average,1)
            return self
        
        if self.minimum == 0 and not alwaysAdd:
            return self
        if self.minimum == 0 and static <= 0:
            return self
        
        # don't go below 1, only if already above 1
        if self.minimum + static < 1:
            negativeShift = static + self.minimum - 1
            self.dist = Distribution.ShiftDown(self.dist,-negativeShift)
            self.minimum = 1
        else:
            self.minimum += static
        self.average = None
        
    def addWeakness(self, static):
        if Distribution.NoCalculation:
            self.average += static
            self.average = max(self.average,0)
            return self
        
        if self.minimum == 0:
            return self
        
        # don't go below 1, only if already above 1
        if self.minimum + static < 0:
            negativeShift = static + self.minimum 
            self.dist = Distribution.ShiftDown(self.dist,-negativeShift)
            self.minimum = 0
        else:
            self.minimum += static
        self.average = None
            
    def combine(self,d2):
        if Distribution.NoCalculation:
            self.average += d2.average
            return self
        
        self.dist = Distribution.Convolve(self.dist, d2.dist)
        self.minimum = self.minimum + d2.minimum
        self.average = None
        return self
    
    def addDistributions(self, dists):
        for d in dists.distributions.values():
            self.combine(d)
            
    
    def minimum(self):
        if Distribution.NoCalculation:
            raise Exception("no min")
        return self.minimum
    def maximum(self):
        if Distribution.NoCalculation:
            raise Exception("no max")
        return self.minimum + len(self.dist) - 1
    
    def chanceLessThanOrEqualTo(self, number):
        if Distribution.NoCalculation:
            raise Exception("no chance")
        if number < self.minimum:
            return 0
        elif number > self.maximum():
            return 1
        else:
            return sum(self.dist[0:(number-self.minimum+1)])
        
    def combineMax(self, d2):
        if Distribution.NoCalculation:
            raise Exception("no combine")
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
        self.average = None
        
    def selectMax(self, d2):
        if Distribution.NoCalculation:
            if d2.average > self.average:
                self.average = d2.average
            return self
        
        if d2.getAverage() > self.getAverage():
            self.minimum = d2.minimum
            self.dist = d2.dist
        self.average = None
        
    def generate(self):
        if Distribution.NoCalculation:
            raise Exception("no generate")
        for d, chance in enumerate(self.dist):
            yield d + self.minimum, chance
            
    def Combine(d1, d2):
        if Distribution.NoCalculation:
            raise Exception("no combine")
        newDist = Distribution([],0)
        newDist.dist = Distribution.Convolve(d1.dist,d2.dist)
        newDist.minimum = d1.minimum + d2.minimum
        return newDist
    
    def Convolve(a1, a2):
        # unhashable type: 'list'
        if Distribution.NoCalculation:
            raise Exception("no convolve")
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
        if Distribution.NoCalculation:
            raise Exception("no convolve")
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
        if Distribution.NoCalculation:
            raise Exception("no shift")
        newDist = [0]
        for i in range(len(dist)):
            if i <= num:
                newDist[0] += dist[i]
            else:
                newDist.append(dist[i])
        return newDist
    
class DistributionsByType:
    
    # don't keep distributions, only the average, should have made that a seperate class...
    def __init__(self):
        self.distributions = dict()
        self.averages = dict()
        
    def add(self, distribution):
        damageType = distribution.type
        if Distribution.OnlyAverage:
            if damageType in self.averages:
                self.averages[damageType]+= distribution.getAverage()
            else:
                self.averages[damageType] = distribution.getAverage()
        else:
            if damageType in self.distributions:
                self.distributions[damageType].combine(distribution)
            else:
                self.distributions[damageType] = distribution
            
    def combineMax(self, distribution):
        damageType = distribution.type
        if Distribution.OnlyAverage:
            raise Exception("Can't combine max without distributions")
            if damageType in self.distributions:
                self.averages[damageType].combineMax(distribution)
            else:
                self.averages[damageType] = distribution.getAverage()
        else:
            if damageType in self.distributions:
                self.distributions[damageType].combineMax(distribution)
            else:
                self.distributions[damageType] = distribution
    
    def combineMaxDists(self, distsByType):
        if Distribution.OnlyAverage:
            raise Exception("Can't combine max without distributions")
            # for damageType, average in distsByType.averages.items():
        else:
            for damageType, dist in distsByType.distributions.items():
                if damageType in self.distributions:
                    self.distributions[damageType].combineMax(dist)
                else:
                    self.distributions[damageType] = dist
    
    def selectMax(self, distribution):
        damageType = distribution.type
        if Distribution.OnlyAverage:
            if damageType in self.averages:
                self.averages[damageType] = max(distribution.getAverage(),self.averages[damageType])
            else:
                self.averages[damageType] = distribution.getAverage()
        else:
            if damageType in self.distributions:
                self.distributions[damageType].selectMax(distribution)
            else:
                self.distributions[damageType] = distribution
            
    def selectMaxDists(self, distsByType):
        if Distribution.OnlyAverage:
            for damageType, average in distsByType.averages.items():
                if damageType in self.averages:
                    self.averages[damageType] =  max(average,self.averages[damageType])
                else:
                    self.averages[damageType] = average
        else:
            for damageType, dist in distsByType.distributions.items():
                if damageType in self.distributions:
                    self.distributions[damageType].selectMax(dist)
                else:
                    self.distributions[damageType] = dist
    
    def addDistributions(self, dists):
        if Distribution.OnlyAverage:
            for dt in dists.averages:
                if dt in self.distributions:
                    self.averages[dt]+= dists.averages[dt]
                else:
                    self.averages[dt] =dists.averages[dt]
        else:
            for dist in dists.distributions.values():
                self.add(dist)
            
    def multiply(self, multiplier):
        if Distribution.OnlyAverage:
            for dt in self.averages:
                self.averages[dt] *= multiplier
        else:
            for dist in self.distributions.values():
                dist.multiply(multiplier)
            
    def getAverage(self):
        average = 0
        if Distribution.OnlyAverage:
            for dt in self.averages:
                average += self.averages[dt]
        else:
            for dist in self.distributions.values():
                average += dist.getAverage()
        return average
            
    def generate(self):
        if Distribution.OnlyAverage:
            raise Exception("Not implimented")
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
    

