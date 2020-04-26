import copy
from pf2calcMonster import creatureData
from pf2calcAttacks import Strike, SaveAttack, Save, Effect, Stitch, CombinedAttack, attackSwitcher, Fort, Reflex, Will, Perception
from distribution import Distribution, DistributionsByType



class Target:
    def __init__(self,AC,Fort,Ref,Will,Per):
        self.ac = AC
        self.fort = Fort
        self.ref = Ref
        self.will = Will
        self.per = Per
        self.clumsy = 0
        self.drained = 0
        self.enfeebled = 0
        self.frightened = 0
        self.sickened = 0
        self.stupified = 0
        
        self.customTarget = False
        self.customAC = 10
        self.customFort = 0
        self.customRef = 0
        self.customWill = 0
        self.customPer = 0
        
    def getAC(self, level):
        if self.customTarget:
            return self.customAC
        if level in self.ac.keys():
            return self.ac[level]
    def getSaves(self, level):
        if self.customTarget:
            return self.customRef
        return self.ref[level]
    def getFort(self, level):
        if self.customTarget:
            return self.customFort
        return self.fort[level]
    def getRef(self, level):
        if self.customTarget:
            return self.customRef
        return self.ref[level]
    def getWill(self, level):
        if self.customTarget:
            return self.customWill
        return self.will[level]
    def getPer(self, level):
        if self.customTarget:
            return self.customPer
        return self.per[level]   
    
    def setAC(self, ac):
        self.ac = ac     
    def setSaves(self, saves):
        self.fort = saves
        self.ref = saves
        self.will = saves
        self.per = saves
    def setFort(self, saves):
        self.fort = saves
    def setRef(self, saves):
        self.ref = saves
    def setWill(self, saves):
        self.will = saves
    def setPer(self, saves):
        self.per = saves
    def setCustom(self, ac, fort, ref, will, per):
        self.customTarget = True
        self.customAC = ac
        self.customFort = fort
        self.customRef = ref
        self.customWill = will
        self.customPer = per
    def revertCustom(self):
        self.customTarget = False
        
    def contains(self, level):
        return level in self.ac and level in self.fort and level in self.ref and level in self.will
        
averageAcByLevel = {-1: 15,
 0: 16,
 1: 17,
 2: 18,
 3: 19,
 4: 21,
 5: 22,
 6: 24,
 7: 25,
 8: 27,
 9: 28,
 10: 30,
 11: 31,
 12: 33,
 13: 34,
 14: 36,
 15: 37,
 16: 39,
 17: 40,
 18: 42,
 19: 44,
 20: 46}

averageFortByLevel = {-1: 5,
 0: 6,
 1: 6,
 2: 8,
 3: 9,
 4: 11,
 5: 13,
 6: 16,
 7: 17,
 8: 18,
 9: 19,
 10: 21,
 11: 23,
 12: 23,
 13: 26,
 14: 28,
 15: 27,
 16: 30,
 17: 30,
 18: 33,
 19: 35,
 20: 37}

averageRefByLevel = {-1: 7,
 0: 7,
 1: 8,
 2: 9,
 3: 9,
 4: 11,
 5: 12,
 6: 13,
 7: 15,
 8: 16,
 9: 17,
 10: 17,
 11: 20,
 12: 21,
 13: 21,
 14: 24,
 15: 26,
 16: 28,
 17: 29,
 18: 30,
 19: 32,
 20: 32}

averageWillByLevel = {-1: 3,
 0: 4,
 1: 5,
 2: 6,
 3: 7,
 4: 10,
 5: 10,
 6: 13,
 7: 14,
 8: 15,
 9: 16,
 10: 18,
 11: 20,
 12: 21,
 13: 23,
 14: 24,
 15: 26,
 16: 28,
 17: 32,
 18: 32,
 19: 34,
 20: 35}



 
averageTarget = Target(averageAcByLevel,averageFortByLevel,averageRefByLevel,averageWillByLevel,None)


def critFailureChance(attackMinusAc):
    chance = 0
    if attackMinusAc < -10:
        chance = (-10 - attackMinusAc) * 5
        chance = min(chance, 95)
    elif attackMinusAc < -1:
        chance = 5
    return chance

def failureChance(attackMinusAc):
    chance = 0
    if attackMinusAc < -29:
        chance = 5
    elif attackMinusAc < -19:
        chance = (29 + attackMinusAc) * 5
    elif attackMinusAc < -10:
        chance = 45
    elif attackMinusAc < -1:
        chance = (-2 - attackMinusAc) * 5
    elif attackMinusAc < 9:
        chance = 5
    else:
        chance = 0
    return chance

def successChance(attackMinusAc, keen=False):
    chance = 5
    if attackMinusAc < -29:
        chance = 0
    elif attackMinusAc < -20:
        chance = 5
    elif attackMinusAc < -10:
        chance = (20 + attackMinusAc) * 5
    elif attackMinusAc < -1:
        chance = 50
    elif attackMinusAc < 9:
        chance = (8 - attackMinusAc) * 5
    else:
        chance = 5
        
    if keen and attackMinusAc>-20 and attackMinusAc<-9:
        chance -= 5
        
    return chance
        
def critSuccessChance(attackMinusAc, keen=False):
    chance = 5
    if attackMinusAc < -20:
        chance = 0
    elif attackMinusAc < -9:
        chance = 5
    elif attackMinusAc < 8:
        chance = (11 + attackMinusAc) * 5
    else:
        chance = 95
    
    if keen and attackMinusAc>-20 and attackMinusAc<-9:
        chance += 5
    
    return chance
    
def calculateED(accuracy, defense, damageBonus, damageDice, dm=0, cd=0, fd=0, sd=0, keen=False, cs=False):
    # fd = failure damage, cd = crit added damage, dm is damage that applies on all hits, like weakness/resistance
    exD = 0
    if fd != 0 or sd != 0:
        exD += failureChance(accuracy-defense) * (fd + sd + dm)
    exD += successChance(accuracy-defense, keen) * ((damageBonus + damageDice) + sd + dm)
    exD += critSuccessChance(accuracy-defense, keen) * ((damageBonus + damageDice)*2 + sd + dm)
    if cd != 0:
        exD += critSuccessChance(accuracy-defense, keen) * cd
    return exD / 100



            
class Selector:
    selectedTarget = averageTarget # use averageTarget later
    selectedTarget.setSaves(creatureData['Saves']['Moderate'])
    selectedTarget.setPer(creatureData['Perception']['Moderate'])
    selectedTarget.setAC(creatureData['AC']['Moderate'])
    selections = dict()
    keyList = list()
    
    def changeTargetAC(name):
        if name == 'average bestiary':
            Selector.selectedTarget.setAC(averageAcByLevel)
        else:
            Selector.selectedTarget.setAC(creatureData['AC'][name])
     
    def changeTargetSaves(name):
        Selector.selectedTarget.setSaves(creatureData['Saves'][name])
    def changeTargetFort(name):
        if name == 'average bestiary':
            Selector.selectedTarget.setFort(averageFortByLevel)
        else:
            Selector.selectedTarget.setFort(creatureData['Saves'][name])
        
    def changeTargetRef(name):
        if name == 'average bestiary':
            Selector.selectedTarget.setRef(averageRefByLevel)
        else:
            Selector.selectedTarget.setRef(creatureData['Saves'][name])
    def changeTargetWill(name):
        if name == 'average bestiary':
            Selector.selectedTarget.setWill(averageWillByLevel)
        else:
            Selector.selectedTarget.setWill(creatureData['Saves'][name])
    def changeTargetPer(name):
        Selector.selectedTarget.setPer(creatureData['Perception'][name])
    def changeTargetClumsy(name):
        Selector.selectedTarget.clumsy = int(name)
    def changeTargetDrained(name):
        Selector.selectedTarget.drained = int(name)
    def changeTargetEnfeebled(name):
        Selector.selectedTarget.enfeebled = int(name)
    def changeTargetFrightened(name):
        Selector.selectedTarget.frightened = int(name)
    def changeTargetSickened(name):
        Selector.selectedTarget.sickened = int(name)
    def changeTargetStupified(name):
        Selector.selectedTarget.stupified = int(name)
    def customTarget(ac,fort,ref,will,per):
        Selector.selectedTarget.setCustom(ac,fort,ref,will,per)
    def revertCustom():
        Selector.selectedTarget.revertCustom()
    def shouldAddPrimary(key):
        attack = attackSwitcher[key][0]
        return attack.prim
    
    def shouldAddSecondary(key):
        attack = attackSwitcher[key][0]
        return attack.sec
    
    def shouldAddWeaponDamage(key):
        attack = attackSwitcher[key][0]
        return attack.isWeapon and not attack.weaponDamageDice
    
    def shouldAddSpellLevel(key):
        attack = attackSwitcher[key][0]
        return attack.isSpell
    
    def isWeapon(key):
        attack = attackSwitcher[key][0]
        return attack.isWeapon
    
    def addSelection(key, value, primaryAS, secondaryAS, mapValue, attackBonus, 
                     damageBonus, additionalDamage, spellLevelMod, weaponDamage, 
                     weaponCritDamage, weaponCritSpec, weaponFeatures, 
                     minLevel, maxLevel):
        while(key in Selector.keyList):
            key += "."
            
        attack = attackSwitcher[value][0]
        newAttack = copy.deepcopy(attack)
        newAttack.name = key
        
        newAttack.setPrimaryAS(primaryAS)
        newAttack.setSecondaryAS(secondaryAS)
        #newAttack.setMAP(mapValue)

        newAttack.setWeaponDamageDice(weaponDamage)
        newAttack.setCriticalDamageDice(weaponCritDamage)
        newAttack.setCriticalSpecialization(weaponCritSpec)
        
        newAttack.setWeaponFeatures(weaponFeatures)
        
        newAttack.modifyAB(attackBonus)
        newAttack.modifyAD(additionalDamage)
        newAttack.modifyDB(damageBonus)
        
        newAttack.setSpellLevel(spellLevelMod)
        newAttack.setLevels(minLevel, maxLevel)
        
        

        Selector.selections[key] = [newAttack]
        Selector.keyList.append(key)
        return key
		
    def combineSelections(key, keyList):
        # check if it's a combined attack, can't combine them
        atkList = []  
        for k in keyList:
            attack = Selector.selections.get(k)
            atkList += attack
        Selector.selections[key] = atkList
        Selector.keyList.append(key)
        
    def moveToTop(key):
        Selector.keyList.remove(key)
        Selector.keyList = [key] + Selector.keyList
    
    def doubleSelection(key, value):
        attack = Selector.selections.get(value)
        atkList = attack
        atkList += attack
        Selector.selections[key] = atkList
        Selector.keyList.append(key)
        
    def duplicate(key):
        attack = copy.deepcopy(Selector.selections.get(key))
        newKey = key + "."
        while(newKey in Selector.keyList):
            newKey += "."
        Selector.selections[newKey] = attack
        Selector.keyList.append(newKey)
        return newKey
        
    def removeSelection(key):
        Selector.selections.pop(key)
        Selector.keyList.remove(key)
        
    def rename(newKey, oldKey):
        attack = Selector.selections.get(oldKey)
        Selector.removeSelection(oldKey)
        Selector.selections[newKey] = attack
        Selector.keyList.append(newKey)
        
    def stitch(keyList):
        key  = keyList[0]
        attackList = []
        for k in keyList:
            attack = Selector.selections.get(k)
            attackList += attack
        Selector.selections[key] = [Stitch(attackList)]
        for k in keyList[1:]:
            Selector.selections.pop(k)
            Selector.keyList.remove(k)
        
    def minSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=min)
        Selector.selections[newKey] = newAttack
        if not newKey in Selector.keyList:
            Selector.keyList.append(newKey)      
    
    def maxSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=max)
        Selector.selections[newKey] = newAttack
        if not newKey in Selector.keyList:
            Selector.keyList.append(newKey) 
        
    def sumSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=lambda a, b: a + b)
        Selector.selections[newKey] = newAttack
        if not newKey in Selector.keyList:
            Selector.keyList.append(newKey) 
        
    def difSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=lambda a, b: a - b)
        Selector.selections[newKey] = newAttack
        if not newKey in Selector.keyList:
            Selector.keyList.append(newKey) 
    
    def canCombine(keyList):
        if len(keyList)==0:
            return False
        for key in keyList:
            attack = Selector.selections.get(key)
            if type(attack) is CombinedAttack:
                return False
        return True
    
    def getSelectionInfo(key):
        info = ""
        attackList = Selector.selections.get(key)
        for attack in attackList:
            info += attack.info() + "\n"
        return info

class Context:
    def __init__(self, oldContext, chance, result):
        if oldContext:
            self.initialize(oldContext, chance)
            # self.chance = oldContext.chance * chance
            if result:
                self.processResult(result)              
                return           
            return 
        self.setup(chance)
        return
    def setup(self, chance):
        # self.oldContext = None
        # self.chance = chance
        # self.damageDist = None
        # self.persDists = None
        # self.isHit = False
        # self.isCrit = False
        
        self.targetLevel = 0
        self.flatfooted = False
        self.origffstatus = False
        self.trueStrike = False
        self.treatWorse = False
        self.ignoreNext = False
        self.setAttack = None
        
        self.attackBonus = 0
        
        self.concealment = 0
        self.fortification = 0
        
        self.clumsy = 0
        self.drained = 0
        self.enfeebled = 0
        self.frightened = 0
        self.sickened = 0
        self.stupified = 0
        
        self.debuffAttack = 0
        
        self.damageBonus = 0
        
        self.targetAC = None
        self.targetFort = None
        self.targetRef = None
        self.targetWill = None
        self.targetPer = None

        if Distribution.OnlyAverage:
            self.damageChances = DamageChanceAverageRecord()
        else:
            self.damageChances = DamageChanceRecord()
        # self.persChances = DamageChanceRecord()
        self.applyChance(chance)
        
        self.thisStrikeBonus = 0
        self.thisDamageBonus = 0
        
        self.onFirstHitDamageDice = []
        self.onSecondHitDamageDice = []
        self.onThirdHitDamageDice = []
        self.onEveryHitDamageDice = []
        
        self.didHit = False
        self.usedDamage = False
        return
    def initialize(self, oldContext,chance):
        # self.oldContext = oldContext
        # self.chance = chance
        
        # self.damageDist = None
        # self.persDists = None
        # self.isHit = False
        # self.isCrit = False
        
        self.targetLevel = oldContext.targetLevel
        self.flatfooted = oldContext.flatfooted
        self.trueStrike = oldContext.trueStrike
        self.origffstatus = oldContext.origffstatus
        self.treatWorse = False
        self.ignoreNext = False
        self.setAttack = oldContext.setAttack
        
        self.attackBonus = oldContext.attackBonus
            
        self.concealment = oldContext.concealment
        self.fortification = oldContext.fortification
        
        self.debuffAttack = oldContext.debuffAttack
        self.clumsy = oldContext.clumsy
        self.drained = oldContext.drained
        self.enfeebled = oldContext.enfeebled
        self.frightened = oldContext.frightened
        self.sickened = oldContext.sickened
        self.stupified = oldContext.stupified
            
        self.damageBonus = oldContext.damageBonus
        
        self.targetAC = oldContext.targetAC
        self.targetFort = oldContext.targetFort
        self.targetRef = oldContext.targetRef
        self.targetWill = oldContext.targetWill
        self.targetPer = oldContext.targetPer
        
        self.damageChances = copy.deepcopy(oldContext.damageChances)
        # self.persChances = copy.deepcopy(oldContext.persChances)
        self.applyChance(chance)
        
        self.thisStrikeBonus = oldContext.thisStrikeBonus
        self.thisDamageBonus = oldContext.thisDamageBonus
        
        self.onFirstHitDamageDice = copy.deepcopy(oldContext.onFirstHitDamageDice)
        self.onSecondHitDamageDice = copy.deepcopy(oldContext.onSecondHitDamageDice)
        self.onThirdHitDamageDice = copy.deepcopy(oldContext.onThirdHitDamageDice)
        self.onEveryHitDamageDice = copy.deepcopy(oldContext.onEveryHitDamageDice)
        
        if oldContext.didHit:
            self.onFirstHitDamageDice = self.onSecondHitDamageDice
            self.onSecondHitDamageDice = self.onThirdHitDamageDice
            self.onThirdHitDamageDice = []
        self.didHit = False
        
        if oldContext.usedDamage:
            self.thisDamageBonus = 0
        self.usedDamage = False
    def processResult(self, result):
        if result.targetAC:
            self.targetAC = result.targetAC
        if result.targetFort:
            self.targetFort = result.targetFort
        if result.targetRef:
            self.targetRef = result.targetRef
        if result.targetWill:
            self.targetWill = result.targetWill
        if result.targetPer:
            self.targetPer = result.targetPer
            
        if result.futureAttacksFF:
            self.origffstatus = True
            self.flatfooted = True
        elif result.nextAttackFF:
            self.flatfooted = True
        elif type(result.atk) is Strike:
            self.flatfooted = self.origffstatus
                    
        if result.trueStrike:
            self.trueStrike = True 
               
        if result.addConcealment:
            if self.concealment <= 20:
                self.concealment = 20
        if result.addHidden:
            if self.concealment <= 50:
                self.concealment = 50
        if result.removeConcealment:
            if self.concealment >= 0:
                self.concealment = 0
        if result.removeHidden:
            if self.concealment >= 20:
                self.concealment = 20
                
        if result.setFortification:
            self.fortification = result.fortification
                        
        if result.applyPersistentDamage:
            self.damageChances.applyPersistentDamage()
        if result.treatWorse:
            self.treatWorse = True
                    
        if result.ignoreNext:
            self.ignoreNext = True
                    
        if not result.setAttack is None:
            self.setAttack = result.setAttack
                    
        self.thisStrikeBonus += result.nextStrikeBonus
                
                    
        if result.addfirsthitdamageDice:
            self.onFirstHitDamageDice += result.addfirsthitdamageDice
        if result.addsecondhitdamageDice:
            self.onSecondHitDamageDice += result.addsecondhitdamageDice
        if result.addthirdhitdamageDice:
            self.onThirdHitDamageDice += result.addthirdhitdamageDice
        if result.addeveryhitdamageDice:
            self.onEveryHitDamageDice += result.addeveryhitdamageDice
                    
        if result.adddamage:
            self.thisDamageBonus += result.adddamage
                
        if result.debuffAttack > self.debuffAttack:
            self.debuffAttack = result.debuffAttack
                
        self.clumsy = max(result.clumsy,self.clumsy)
                
        damage = 0
        if result.drained > self.drained:
            damage = (result.drained-self.drained) * self.targetLevel  
        self.drained = max(result.drained,self.drained)
        
        self.enfeebled = max(result.enfeebled,self.enfeebled)
        self.frightened = max(result.frightened,self.frightened)
        self.sickened = max(result.sickened,self.sickened)
        self.stupified = max(result.stupified,self.stupified)
                
# #    
        damageDist = result.damageDist
        damageDist.addBonus(damage)
        # self.persDists = DistributionsByType()
        persDist = result.persDist
        
        self.damageChances.add(damageDist, result.good, result.veryGood)
        if CombinedAttack.PersistentReRoll or Distribution.OnlyAverage:
            self.damageChances.selectMax(persDist)
        else:
            self.damageChances.combineMax(persDist)
        # self.oldContext = None
    def getChance(self):
        return self.damageChances.getChance()
    def applyChance(self, chance):
        self.damageChances.applyChance(chance)
        
    def setFlatfooted(self):
        self.origffstatus = True
        self.flatfooted = True
        
    def setTrueStrike(self):
        self.trueStrike = True
        
    def setAttackBonus(self, ab):
        self.attackBonus = ab
        
    def setDamageBonus(self, db):
        self.damageBonus = db
        
    def getStrikeBonus(self, isSpell):
        bonus = self.attackBonus + self.thisStrikeBonus
        self.thisStrikeBonus = 0
        if isSpell:
            return bonus - self.debuffAttack
        return bonus - max(self.debuffAttack,self.enfeebled)
    
    def getSaveAttackBonus(self):
        return self.attackBonus - self.debuffAttack
    
    def getDCBonus(self):
        return self.attackBonus - self.debuffAttack
    
#    def getSaveBonus(self):
#        return 0 - self.debuffTarget
    def getFortBonus(self):
        return 0 - max(self.frightened,self.sickened,self.drained)
    def getRefBonus(self):
        return 0 - max(self.frightened,self.sickened,self.clumsy)
    def getWillBonus(self):
        return 0 - max(self.frightened,self.sickened,self.stupified)
    def getPerBonus(self):
        return 0 - max(self.frightened,self.sickened,self.stupified)
    
    def getACBonus(self):
        return 0 - max(self.frightened,self.sickened,self.clumsy)
    
    def getEffectBonus(self):
        return 0
    
    def getDamageBonus(self):
        return 0 - self.enfeebled
    
    def getExtraDamage(self):
        db = self.thisDamageBonus
        self.usedDamage = True 
        return db
    
    def getWeakness(self):
        return self.damageBonus
    
    def getHitDamageDice(self):
        dice = self.onFirstHitDamageDice + self.onEveryHitDamageDice
        self.didHit = True
        return dice
    
    def hasTrueStrike(self):
        tss = self.trueStrike
        self.trueStrike = False
        return tss
    

    def averageDamage(self):
#        print("ave dam is ",self.damageDistribution.average())
#        print("dam dist is ")
        # if self.damageDist:
        #     return self.damageDist.getAverage() * self.getChance()
        # else:
        #     return 
        return self.damageChances.getAverage()
    def averagePDamage(self):
        # if self.persDists:
        #     return self.persDists.getAverage() * self.getChance()
        # else:
        #     return 0
        return self.damageChances.getPersAverage()
    def numberHits(self):
        # if self.oldContext:
        #     return (self.chance*self.isHit) + self.oldContext.numberHits()
        # return (self.chance*self.isHit)
        return self.damageChances.getHits()
    def numberCrits(self):
        # if self.oldContext:
        #     return (self.chance*self.isCrit) + self.oldContext.numberCrits()
        # return (self.chance*self.isCrit)
        return self.damageChances.getCrits()
    def maxDebuff(self):
        return max(self.clumsy,self.drained,self.frightened,self.sickened,self.stupified)
    
    def generate(self):
        dl = len(self.damageChances.chances)
        # pl = len(self.persChances.chances)
        # if dl != pl:
            # raise Exception("distributions not equal")
        for i in range(dl):
            chance = self.damageChances.chances[i]
            dDists = self.damageChances.damages[i]
            pDists = self.damageChances.persDamages[i]
            yield chance, dDists, pDists
            
    def combine(self, sameContext):
        self.damageChances.addDamageChances(sameContext.damageChances)
    def __eq__(self, obj):
        
        if not isinstance(obj, Context):
            return False
        return \
        self.targetLevel == obj.targetLevel and \
        self.flatfooted == obj.flatfooted and \
        self.trueStrike == obj.trueStrike and \
        self.origffstatus == obj.origffstatus and \
        self.treatWorse == obj.treatWorse and \
        self.ignoreNext == obj.ignoreNext and \
        self.setAttack == obj.setAttack and \
        self.attackBonus == obj.attackBonus and \
        self.concealment == obj.concealment and \
        self.debuffAttack == obj.debuffAttack and \
        self.clumsy == obj.clumsy and \
        self.drained == obj.drained and \
        self.enfeebled == obj.enfeebled and \
        self.frightened == obj.frightened and \
        self.sickened == obj.sickened and \
        self.stupified == obj.stupified and \
        self.damageBonus == obj.damageBonus and \
        self.thisStrikeBonus == obj.thisStrikeBonus and \
        self.thisDamageBonus == obj.thisDamageBonus and \
        self.onFirstHitDamageDice == obj.onFirstHitDamageDice and \
        self.onSecondHitDamageDice == obj.onSecondHitDamageDice and \
        self.onThirdHitDamageDice == obj.onThirdHitDamageDice and \
        self.onEveryHitDamageDice == obj.onEveryHitDamageDice

            
    def ConsolidateContexes(contextList):
        newContextList = []
        for context in contextList:
            found = False
            for uniqueContext in newContextList:
                if context == uniqueContext:
                    uniqueContext.combine(context)
                    found = True
                    break
            if not found:
                newContextList.append(context)
        return newContextList
    
class DamageChanceRecord:
    def __init__(self):
        self.chances = [1]
        self.damages = [Distribution()]
        self.persDamages = [DistributionsByType()]
            
        self.hits = [0]
        self.crits = [0]
    def getChance(self):
        return sum(self.chances)
    def applyChance(self, chance):
        for i in range(len(self.chances)):
            self.chances[i] *= chance 
            
    def add(self, dist, isHit, isCrit):
        for i in range(len(self.damages)):
            self.damages[i].combine(dist)   
            if isHit:
                self.hits[i] += 1
            if isCrit:
                self.crits[i] +=1
    def selectMax(self, dist):
        for i in range(len(self.persDamages)):
            self.persDamages[i].selectMax(dist)
    def combineMax(self, dist):
        for i in range(len(self.persDamages)):
            self.persDamages[i].combineMax(dist)
    def addDamageChances(self, damageChanceRecord):
        self.chances += damageChanceRecord.chances
        self.damages += damageChanceRecord.damages
        self.persDamages += damageChanceRecord.persDamages
        self.hits += damageChanceRecord.hits
        self.crits += damageChanceRecord.crits
        
    def applyPersistentDamage(self):
        newChances = self.chances
        newDamages = self.damages
        newPersDamages = self.persDamages
        for i in range(len(self.chances)):
            chance = (14) / 20
            
            self.damages[i].addDistributions(self.persDamages[i])
            
            newChance = self.chances[i] * (1 - chance)
            self.chances[i] = self.chances[i] * chance
            
            newDamage = copy.deepcopy(self.damages[i])
            newPersDamage = DistributionsByType()
            
            newChances.append(newChance)
            newDamages.append(newDamage)
            newPersDamages.append(newPersDamage)
        self.chances = newChances
        self.damages = newDamages
        self.persDamages = newPersDamages
            
        
        
    def getAverage(self):
        total = 0
        for i in range(len(self.chances)):
            ave = self.damages[i].getAverage()
            chance = self.chances[i]
            total += ave * chance
        return total
    
    def getPersAverage(self):
        total = 0
        for i in range(len(self.chances)):

            ave = self.persDamages[i].getAverage()
            chance = self.chances[i]
            total += ave * chance
        return total
    
    def getHits(self):
        total = 0
        for i in range(len(self.chances)):
            hits = self.hits[i]
            chance = self.chances[i]
            total += hits * chance
        return total
    def getCrits(self):
        total = 0
        for i in range(len(self.chances)):
            crits = self.crits[i]
            chance = self.chances[i]
            total += crits * chance
        return total
#    
#    def getDamageDist(self):
#        return self.damageDistributions.generate()

class DamageChanceAverageRecord:
    def __init__(self):
        self.chance = 1
        # self.persChances = [1]

        self.damage = 0
        self.persDamages = {}
        # dict of damage types with lists of chances and damages

        self.hits = 0
        self.crits = 0
        
    def getChance(self):
        return self.chance
    
    def applyChance(self, chance):
        self.chance *= chance
        for dt in self.persDamages.keys():
            for i in range(len(self.persDamages[dt][0])):
                self.persDamages[dt][0][i] *= chance
        
    def add(self, dist, isHit, isCrit):
        self.damage += dist.getAverage()
        if isHit:
            self.hits += 1
        if isCrit:
            self.crits += 1
        # for i in range(len(self.damages)):
        #     self.damages[i] += dist.getAverage()
  
        #     if isHit:
        #         self.hits[i] += 1
        #     if isCrit:
        #         self.crits[i] +=1
    def selectMax(self, dist):
        ave = dist.getAverage()
        if(ave==0):
            return
        if dist.type in self.persDamages:
            chances = self.persDamages[dist.type][0]
            damages = self.persDamages[dist.type][1]
            newChances = []
            newDamages = []
            sumChance = 0
            for i in range(len(chances)):
                if damages[i] <= ave:
                    sumChance += chances[i]
                else:
                    newChances.append(chances[i])
                    newDamages.append(damages[i])
            newChances.append(sumChance)
            newDamages.append(ave)
            self.persDamages[dist.type] = (newChances,newDamages)
            # make a new list of chances and damage averages
            # first element is the sum of all chances for damages <= new average
            # then add elements of chances for damages greater than average
        else:
            self.persDamages[dist.type] = ([self.chance],[ave])
        # for i in range(len(self.persDamages)):
        #     if dist.type in self.persDamages[i]:
        #         self.persDamages[i][dist.type] = max(ave, self.persDamages[i][dist.type])
        #     else:
        #         self.persDamages[i][dist.type] = ave


    def addDamageChances(self, damageChanceRecord):
        weightedDamage = self.chance*self.damage + damageChanceRecord.chance*damageChanceRecord.damage
        weightedHits = self.chance*self.hits + damageChanceRecord.chance*damageChanceRecord.hits
        weightedCrits = self.chance*self.crits + damageChanceRecord.chance*damageChanceRecord.crits
        
        for dt in damageChanceRecord.persDamages:
            if dt in self.persDamages:
                chances = damageChanceRecord.persDamages[dt][0]
                damages = damageChanceRecord.persDamages[dt][1]
                selfChances = self.persDamages[dt][0]
                selfDamages = self.persDamages[dt][1]
                for i in range(len(chances)):
                    if damages[i] in selfDamages:
                        selfChances[selfDamages.index(damages[i])] += chances[i]
                    else:
                        selfChances.append(chances[i])
                        selfDamages.append(damages[i])
                self.persDamages[dt] = (selfChances,selfDamages)
            else:
                chances = damageChanceRecord.persDamages[dt][0]
                damages = damageChanceRecord.persDamages[dt][1]
                newChances = []
                newDamages = []
                zeroChance = self.chance
                for i in range(len(chances)):
                    if damages[i] == 0:
                        zeroChance += chances[i]
                    else:
                        newChances.append(chances[i])
                        newDamages.append(damages[i])
                newChances.append(zeroChance)
                newDamages.append(0)
                self.persDamages[dt] = (newChances,newDamages)
                
        self.chance += damageChanceRecord.chance 
        self.damage = weightedDamage / self.chance
        self.hits = weightedHits / self.chance
        self.crits = weightedCrits / self.chance
                
        #     chances = self.persDamages[dist.type][0]
        #     damages = self.persDamages[dist.type][1]
        
        # for i in range(len(damageChanceRecord.persChances)):
        #     newPersDict = damageChanceRecord.persDamages[i]
        #     found = False
        #     for ii in range(len(self.persChances)):
        #         persDict = self.persDamages[ii]
        #         if persDict == newPersDict:
        #             self.persChances[ii] += damageChanceRecord.persChances[i]
        #             found = True
        #             break
        #     if not found:
        #         self.persChances.append(damageChanceRecord.persChances[i])
        #         self.persDamages.append(damageChanceRecord.persDamages[i])

    def applyPersistentDamage(self):
        chance = 14 / 20
        for dt in self.persDamages:
            selfChances = self.persDamages[dt][0]
            selfDamages = self.persDamages[dt][1]
            newChances = []
            newDamages = []
            zeroChance = 0
            for i in range(len(selfChances)):
                if selfDamages[i] == 0:
                    zeroChance += selfChances[i]
                else:
                    zeroChance += selfChances[i] * (1 - chance)
                    newChances.append(selfChances[i] * chance)
                    newDamages.append(selfDamages[i])
                    self.damage += selfChances[i] * selfDamages[i] / self.chance
            newChances.append(zeroChance)
            newDamages.append(0)
            self.persDamages[dt] = (newChances,newDamages)
        # for i in range(len(self.persChances)):
        #     chance = self.persChances
    
    def getAverage(self):
        return self.chance * self.damage
        # for i in range(len(self.chances)):
        #     if Distribution.OnlyAverage:
        #         ave = self.damages[i]
        #     else:
        #         ave = self.damages[i].getAverage()
        #     chance = self.chances[i]
        #     total += ave * chance
        # return total
    
    def getPersAverage(self):
        total = 0
        # print(self.persDamages)
        
        for chanceDamage in self.persDamages.values():
            chances = chanceDamage[0]
            damages = chanceDamage[1]
            for i in range(len(chances)):
                total += chances[i] * damages[i]
        
        # for i in range(len(self.persChances)):
        #     if Distribution.OnlyAverage:
        #         ave = sum(self.persDamages[i].values())
        #     chance = self.persChances[i]
        #     total += ave * chance
        return total
    
    def getHits(self):
        return self.hits
    def getCrits(self):
        return self.crits
    
def generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    oContext = Context(None, 1, None)
    oContext.targetLevel = level + levelDiff
    oContext.setAttackBonus(attackBonus)
    oContext.setDamageBonus(damageBonus)
    oContext.clumsy = target.clumsy
    oContext.drained = target.drained
    oContext.enfeebled = target.enfeebled
    oContext.frightened = target.frightened
    oContext.sickened = target.sickened
    oContext.stupified = target.stupified
    if (100-flatfootedStatus) != 0:
        normalContext = Context(oContext, 1-flatfootedStatus/100,None)
        if flatfootedStatus != 0:
            ffContext = Context(oContext, flatfootedStatus/100, None)
            ffContext.setFlatfooted()
            contextList = [normalContext, ffContext]
        else:
            contextList = [normalContext]
    else:
        ffContext = Context(oContext, 1, None)
        ffContext.setFlatfooted()
        contextList = [ffContext]

    
    for atk in routine: #for each strike in that routine
        atk = atk.getAttackObject(level)
        attackLevel = atk.attackLevel(level)
        newContextList = []
        for context in contextList:
            # calculate the effects for this attack
            if context.getChance() == 0:
                continue 
                
            keenStatus = False
            trueStrike = False
            concealment = context.concealment
            if concealment<=20 and atk.ignoreConcealment:
                concealment = 0
            if(isinstance(atk, Strike)):
                if context.setAttack is None:
                    totalBonus = atk.getAttack(attackLevel)
                else:
                    totalBonus = context.setAttack
                    context.setAttack = None
                totalBonus += context.getStrikeBonus(atk.isSpell)
                keenStatus = atk.getKeen(attackLevel)
                trueStrike = context.hasTrueStrike()
                
                totalDC = target.getAC(level+levelDiff) + context.getACBonus()
                if context.targetAC:
                        totalDC = context.targetAC
                if context.flatfooted:
                    totalDC -= 2
            elif(isinstance(atk,SaveAttack)):
                totalBonus = atk.getAttack(attackLevel)
                totalBonus += context.getSaveAttackBonus()
                keenStatus = atk.getKeen(attackLevel)
                
                trueStrike = context.hasTrueStrike()
            
                # totalDC = 10 + target.getSaves(level+levelDiff,atk.targetSave) 
                if atk.targetSave == Fort:
                    totalDC = 10 + target.getFort(level+levelDiff)
                    if context.targetFort:
                        totalDC = 10 + context.targetFort
                    totalDC += context.getFortBonus()
                if atk.targetSave == Reflex:
                    totalDC = 10 + target.getRef(level+levelDiff)
                    if context.targetRef:
                        totalDC = 10 + context.targetRef
                    totalDC += context.getRefBonus()
                if atk.targetSave == Will:
                    totalDC = 10 + target.getWill(level+levelDiff)
                    if context.targetWill:
                        totalDC = 10 + context.targetWill
                    totalDC += context.getWillBonus()
                if atk.targetSave == Perception:
                    totalDC = 10 + target.getPer(level+levelDiff)
                    if context.targetPer:
                        totalDC = 10 + context.targetPer
                    totalDC += context.getPerBonus()
            elif(isinstance(atk, Save)):
                # totalBonus = target.getSaves(level+levelDiff)
                if atk.targetSave == Fort:
                    totalBonus = target.getFort(level+levelDiff)
                    if context.targetFort:
                        totalBonus = context.targetFort
                    totalBonus += context.getFortBonus()
                if atk.targetSave == Reflex:
                    totalBonus = target.getRef(level+levelDiff)
                    if context.targetRef:
                        totalBonus = context.targetRef
                    totalBonus += context.getRefBonus()
                if atk.targetSave == Will:
                    totalBonus = target.getWill(level+levelDiff)
                    if context.targetWill:
                        totalBonus = context.targetWill
                    totalBonus += context.getWillBonus()
                if atk.targetSave == Perception:
                    totalBonus = target.getPer(level+levelDiff)
                    if context.targetPer:
                        totalBonus = context.targetPer
                    totalBonus += context.getPerBonus()
                
                totalDC = atk.getDC(attackLevel)
                totalDC += context.getDCBonus()
#            elif(isinstance(atk, AttackSave)):
#                totalBonus = atk.getAttack(attackLevel)
#                totalBonus += context.getStrikeBonus()
#                keenStatus = atk.getKeen(attackLevel)
#                trueStrike = context.hasTrueStrike()
#                
#                totalDC = target.getAC(level+levelDiff) + context.getACBonus()
#                if context.flatfooted:
#                    totalDC -= 2
#                    
#                
            elif(isinstance(atk, Effect)):
                r = atk.effectResult(attackLevel, context)
                if trueStrike or not atk.applyConcealment:
                    concealment = 0 
                eContext = Context(context, (100-concealment)/100, r)
                newContextList.append(eContext)
                if concealment != 0:
                    neContext = Context(context, concealment/100, None)
                    newContextList.append(neContext) 
                continue
            else:
                # this should not happen
                print("attack type was", type(atk))
                continue
            
            # create a new context for each degree of success
            if trueStrike:
                if not isinstance(atk, Save):
                    notcrit = 100 - critSuccessChance(totalBonus-totalDC, keen=keenStatus)
                    critSuccessPercent = 100 - (notcrit * notcrit / 100)
                    nothit = notcrit - successChance(totalBonus-totalDC, keen=keenStatus)
                    successPercent = 100 - (nothit * nothit / 100) - critSuccessPercent
                    notfail = nothit - failureChance(totalBonus-totalDC)
                    failurePercent = 100 - (notfail * notfail / 100) - successPercent - critSuccessPercent
                    critFailurePercent = critFailureChance(totalBonus-totalDC) * critFailureChance(totalBonus-totalDC) / 100
                noEffectPercent = 0
            else:
                critSuccessPercent = critSuccessChance(totalBonus-totalDC, keen=keenStatus)
                successPercent = successChance(totalBonus-totalDC, keen=keenStatus)
                failurePercent = failureChance(totalBonus-totalDC)
                critFailurePercent = critFailureChance(totalBonus-totalDC)
                
                critSuccessPercent = critSuccessPercent * (100-concealment)/100
                successPercent = successPercent * (100-concealment)/100
                failurePercent = failurePercent * (100-concealment)/100
                critFailurePercent = critFailurePercent * (100-concealment)/100
                noEffectPercent = concealment
                
            if isinstance(atk, Strike):
                critSuccessPercent = critSuccessPercent * (100-context.fortification)/100
                successPercent += critSuccessPercent * context.fortification/100
                
            if context.treatWorse:
                critFailurePercent = critFailurePercent + failurePercent
                failurePercent = successPercent
                successPercent = critSuccessPercent
                critSuccessPercent = 0
                
            if context.ignoreNext:
                ignoreContext = Context(context, 1, None)
                newContextList.append(ignoreContext)
            else:
                if critSuccessPercent != 0:
                    critSuccessResult = atk.critSuccessResult(attackLevel, context)
                    csContext = Context(copy.copy(context), critSuccessPercent/100, critSuccessResult)
                    newContextList.append(csContext)
            
                if successPercent != 0:
                    successResult = atk.successResult(attackLevel, context)
                    sContext = Context(context, successPercent/100, successResult)
                    newContextList.append(sContext)
                
                if failurePercent != 0:
                    failureResult = atk.failureResult(attackLevel, context)
                    fContext = Context(context, failurePercent/100, failureResult)
                    newContextList.append(fContext)
            
                if critFailurePercent != 0:
                    critFailureResult = atk.critFailureResult(attackLevel, context)
                    cfContext = Context(context, critFailurePercent/100, critFailureResult)
                    newContextList.append(cfContext) 
                
                if noEffectPercent != 0:
                    neContext = Context(context, noEffectPercent/100, None)
                    if atk.backswingLevel <= attackLevel:
                        neContext.thisStrikeBonus += 1
                    newContextList.append(neContext) 
                
            
        # replace contextList with the list of newly created contexts
        contextList = Context.ConsolidateContexes(newContextList)
        # contextList = newContextList
    return contextList
    
    
def graphTrace(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    y = 0
    py = 0
    hits = 0
    crits = 0
    debuffs = 0
    
    if type(routine) is CombinedAttack:
        # what if it contains more combined attacks?
        for atk in routine.validFor(level):
            newy, newpy, nh, nc, nd = graphTrace(atk, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
            if y == 0:
                y = newy
                py = newpy
                hits = nh
                crits = nc
                debuffs = nd
            else:
                y, py, hits, crits = routine.choose(y, py, newy, newpy, hits, crits, nh, nc)
        return y, py, hits, crits, debuffs
        
    contextList = generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
        
    for context in contextList:
#        print("level is ", level)
#        print("chance is ", context.chance)
        y += context.averageDamage() 
        py += context.averagePDamage() 
        hits += context.numberHits() 
        crits += context.numberCrits() 
        debuffs += context.maxDebuff() * context.getChance()
        
        
    return y, py, hits, crits, debuffs

                    
def graphChanceDamage(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent):
    # returns an xList of damages and a yList of chances
    damageList = []
    chanceList = []
    
    if type(routine) is CombinedAttack:
        for atk in routine.validFor(level):
            return graphChanceDamage(atk, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent)
            
    
    contextList = generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
        
    damageChanceDict = {}
    for context in contextList:
        for chance, damageDists, persDists in context.generate():
            if displayPersistent:
                damageDists = persDists
            else:
                pdWeight = CombinedAttack.PDWeight
                persDists.multiply(pdWeight)
                damageDists.addDistributions(persDists)
            for damage, dc in damageDists.generate():
                damage = int(damage)
                if damage in damageChanceDict:
                    damageChanceDict[damage] += dc * chance
                else:
                    damageChanceDict[damage] = dc * chance
    
        # get chance and damage
        # combine damage with persistent damage
        # damageDists = context.damageChances
        # persDists = context.persChances
        # if displayPersistent:
        #     damageDists = persDists
        # else:
        #     pdWeight = CombinedAttack.PDWeight
        #     persDists.multiply(pdWeight)
        #     damageDists.addDistributions(persDists)
        
        # for damage, chance in damageDists.generate():
        #     damage = int(damage)
        #     if damage in damageChanceDict:
        #         damageChanceDict[damage] += chance * context.chance
        #     else:
        #         damageChanceDict[damage] = chance * context.chance
    
    maxDamage = max(damageChanceDict.keys())
    for damage in range(maxDamage+1):
        chance = 0
        if damage in damageChanceDict:
            chance = damageChanceDict[damage]
        damageList.append(damage)
        chanceList.append(chance)
    
    return damageList, chanceList

def graphChanceDebuff(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent):
    # returns an xList of damages and a yList of chances
    debuffList = []
    chanceList = []
    
    if type(routine) is CombinedAttack:
        for atk in routine.validFor(level):
            return graphChanceDebuff(atk, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent)
    
    contextList = generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
        
    debuffChanceDict = {}
    for context in contextList:
        # get chance and damage
        # combine damage with persistent damage
        debuff = context.maxDebuff()
        if debuff in debuffChanceDict:
            debuffChanceDict[debuff] +=  context.getChance()
        else:
            debuffChanceDict[debuff] = context.getChance()
    
    maxDebuff= max(debuffChanceDict.keys())
    for debuff in range(maxDebuff+1):
        chance = 0
        if debuff in debuffChanceDict:
            chance = debuffChanceDict[debuff]
        debuffList.append(debuff)
        chanceList.append(chance)
    
    return debuffList, chanceList
	
def createTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, blend=False):
#     print("c t")
    xLists = []
    yLists = []
    pyLists = []
    hitsLists = []
    critsLists = []
    debuffLists = []
    target = Selector.selectedTarget
    Distribution.OnlyAverage = True
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        pyList = []
        hitsList = []
        critsList = []
        debuffList = []
        for i in range(1,21):
            toAdd = target.contains(i+levelDiff)
            if blend:
                toAdd = target.contains(i+levelDiff-2) and target.contains(i+levelDiff+2)
            if(type(s) is CombinedAttack):
                if s.contains(i) and toAdd:
                    xList.append(i)
            else:
                for st in s:  
                    if (st.getAttack(st.attackLevel(i)) is None):
                        toAdd = False
                if toAdd:
                    xList.append(i) 
        for i in range(1,21): 
            if i in xList:
                # reset damage and things like flat footed status  
                if blend:
                    y, py, hits, crits, debuffs = 0, 0, 0, 0, 0
                    for pm, weight in [(-2,.25),(1,.75),(0, 1),(1,.75),(2,.25)]:
                        ny, npy, nhits, ncrits, ndebuffs = graphTrace(s, target, i, levelDiff+pm, attackBonus, damageBonus, weakness, flatfootedStatus)
                        y += ny * weight
                        py += npy * weight
                        hits += nhits * weight
                        crits += ncrits * weight
                        debuffs += ndebuffs * weight
                    y, py, hits, crits, debuffs = y/3, py/3, hits/3, crits/3, debuffs/3
                else:
                    y, py, hits, crits, debuffs = graphTrace(s, target, i, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
     
                yList.append(y)
                pyList.append(py)
                hitsList.append(hits)
                critsList.append(crits)
                debuffList.append(debuffs)
        xLists.append(xList)
        yLists.append(yList)
        pyLists.append(pyList)
        hitsLists.append(hitsList)
        critsLists.append(critsList)
        debuffLists.append(debuffList)
        
    
    return xLists, yLists, pyLists, hitsLists, critsLists, debuffLists, Selector.keyList

def createLevelTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level):
    xLists = []
#    xLists2 = []
    yLists = []
    pyLists = []
    hitsLists = []
    critsLists = []
    debuffLists = []
    target = Selector.selectedTarget
    Distribution.OnlyAverage = True
 
    if not target.contains(level+levelDiff):
        return xLists, yLists, pyLists, hitsLists, critsLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
#        xList2 = []
        yList = []
        pyList = []
        hitsList = []
        critsList = []
        debuffList = []
        
        # is this strike routine valid for this level?
        toAdd = True
        if(type(s) is CombinedAttack):
            if not s.contains(level):
                    toAdd = False
        else:
            for st in s:  
                if not(st.getAttack(st.attackLevel(level)) ):
                    toAdd = False
        
        if toAdd:
            for i in range(-8,9):
#                ac = target.getAC(level+levelDiff)-i
#                save = target.getSaves(level+levelDiff)-i
                xList.append(-i)
#                xList2.append(save)
                y, py, hits, crits, debuffs = graphTrace(s, target, level, levelDiff, attackBonus+i, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
                pyList.append(py)
                hitsList.append(hits)
                critsList.append(crits)
                debuffList.append(debuffs)
        xLists.append(xList)
#        xLists2.append(xList2)
        yLists.append(yList)
        pyLists.append(pyList)
        hitsLists.append(hitsList)
        critsLists.append(critsList)
        debuffLists.append(debuffList)
    
    return xLists, yLists, pyLists, hitsLists, critsLists, debuffLists, Selector.keyList
        
def createDamageDistribution(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level, displayPersistent):
    xLists = []
    yLists = []
    target = Selector.selectedTarget
    Distribution.OnlyAverage = False
    
    if not target.contains(level+levelDiff):
        return xLists, yLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        
        # is this strike routine valid for this level?
        toAdd = True
        if(type(s) is CombinedAttack):
            if not s.contains(level):
                    toAdd = False
        else:
            for st in s:  
                if not(st.getAttack(st.attackLevel(level)) ):
                    toAdd = False
        
        if toAdd:
            # get the damage, x, and chance, y, for this attack
            xList, yList = graphChanceDamage(s, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent)
            
            
        xLists.append(xList)
        yLists.append(yList)
    
    return xLists, yLists, Selector.keyList

def createDebuffDistribution(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level, displayPersistent):
    xLists = []
    yLists = []
    target = Selector.selectedTarget
    Distribution.OnlyAverage = True
    
    if not target.contains(level+levelDiff):
        return xLists, yLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        
        # is this strike routine valid for this level?
        toAdd = True
        if(type(s) is CombinedAttack):
            if not s.contains(level):
                    toAdd = False
        else:
            for st in s:  
                if not(st.getAttack(st.attackLevel(level)) ):
                    toAdd = False
        
        if toAdd:
            # get the maxDebuff, x, and chance, y, for this attack
            xList, yList = graphChanceDebuff(s, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus, displayPersistent)
            
            
        xLists.append(xList)
        yLists.append(yList)
    
    return xLists, yLists, Selector.keyList