# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:23:49 2019

@author: bhalb
"""

import csv

extremeAC = dict()
highAC = dict()
moderateAC = dict()
lowAC = dict()
ac = {'Extreme':extremeAC,
      'High': highAC,
      'Moderate': moderateAC,
      'Low': lowAC}
with open("AC.csv") as acData:
    reader = csv.DictReader(acData, delimiter=',')
    line = 0
    for row in reader:
        extremeAC[int(row['Level'])] = int(row['Extreme'])
        highAC[int(row['Level'])] = int(row['High'])
        moderateAC[int(row['Level'])] = int(row['Moderate'])
        lowAC[int(row['Level'])] = int(row['Low'])
        
extremeSaves = dict()
highSaves = dict()
moderateSaves = dict()
lowSaves = dict()
terribleSaves = dict()
saves = {'Extreme':extremeSaves,
         'High': highSaves,
         'Moderate': moderateSaves,
         'Low': lowSaves,
         'Terrible': terribleSaves}
with open("saves.csv") as saveData:
    reader = csv.DictReader(saveData, delimiter=',')
    line = 0
    for row in reader:
        extremeSaves[int(row['Level'])] = int(row['Extreme'])
        highSaves[int(row['Level'])] = int(row['High'])
        moderateSaves[int(row['Level'])] = int(row['Moderate'])
        lowSaves[int(row['Level'])] = int(row['Low'])
        terribleSaves[int(row['Level'])] = int(row['Terrible'])
        
extremePer = dict()
highPer = dict()
moderatePer = dict()
lowPer = dict()
terriblePer = dict()
per = {'Extreme':extremePer,
         'High': highPer,
         'Moderate': moderatePer,
         'Low': lowPer,
         'Terrible': terriblePer}
with open("per.csv") as perData:
    reader = csv.DictReader(perData, delimiter=',')
    line = 0
    for row in reader:
        extremePer[int(row['Level'])] = int(row['Extreme'])
        highPer[int(row['Level'])] = int(row['High'])
        moderatePer[int(row['Level'])] = int(row['Moderate'])
        lowPer[int(row['Level'])] = int(row['Low'])
        terriblePer[int(row['Level'])] = int(row['Terrible'])
        
highHP = dict()
moderateHP = dict()
lowHP = dict()
hp = {'High': highHP,
      'Moderate': moderateHP,
      'Low': lowHP}
with open("hp.csv") as hpData:
    reader = csv.DictReader(hpData, delimiter=',')
    line = 0
    for row in reader:    
        hhpl = (row['High']).split('~')
        ave = (int(hhpl[0])+int(hhpl[1])) / 2
        highHP[int(row['Level'])] = ave
        mhpl = (row['Moderate']).split('~')
        ave = (int(mhpl[0])+int(mhpl[1])) / 2
        moderateHP[int(row['Level'])] = ave
        lhpl = (row['Low']).split('~')
        ave = (int(lhpl[0])+int(lhpl[1])) / 2
        lowHP[int(row['Level'])] = ave
        
extremeAttack = dict()
highAttack = dict()
moderateAttack = dict()
lowAttack = dict()
attack = {'Extreme':extremeAttack,
          'High': highAttack,
          'Moderate': moderateAttack,
          'Low': lowAttack}
with open("attack.csv") as attackData:
    reader = csv.DictReader(attackData, delimiter=',')
    line = 0
    for row in reader:
        extremeAttack[int(row['Level'])] = int(row['Extreme'])
        highAttack[int(row['Level'])] = int(row['High'])
        moderateAttack[int(row['Level'])] = int(row['Moderate'])
        lowAttack[int(row['Level'])] = int(row['Low'])
        
extremeDamage = dict()
highDamage = dict()
moderateDamage = dict()
lowDamage = dict()
damage = {'Extreme':extremeDamage,
          'High': highDamage,
          'Moderate': moderateDamage,
          'Low': lowDamage}
with open("damage.csv") as damageData:
    reader = csv.DictReader(damageData, delimiter=',')
    line = 0
    for row in reader:
        extremeDamage[int(row['Level'])] = int(row['Extreme'])
        highDamage[int(row['Level'])] = int(row['High'])
        moderateDamage[int(row['Level'])] = int(row['Moderate'])
        lowDamage[int(row['Level'])] = int(row['Low'])

creatureData = {'AC': ac,
                'Saves': saves,
                'Perception': per,
                'HP': hp,
                'Attack': attack,
                'Damage': damage}

class Target:
    def __init__(self,AC,saves,hp):
        self.ac = AC
        self.saves = saves
        self.hp = hp
        
    def getAC(self, level):
        if level in self.ac.keys():
            return self.ac[level]
        
