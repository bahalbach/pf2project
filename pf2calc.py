import copy
from pf2calcMonsterStats import creatureData
from pf2calcAttacks import Strike, SaveAttack, Save, Effect, CombinedAttack, attackSwitcher
from distribution import Distribution



class Target:
    def __init__(self,AC,Fort,Ref,Will):
        self.ac = AC
        self.fort = Fort
        self.ref = Ref
        self.will = Will
        
    def getAC(self, level):
        if level in self.ac.keys():
            return self.ac[level]
        
    def getSaves(self, level):
        return self.fort[level]
    
    def setAC(self, ac):
        self.ac = ac
        
    def setSaves(self, saves):
        self.fort = saves
        self.ref = saves
        self.will = saves
        
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


 
averageTarget = Target(averageAcByLevel,None,None,None)


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
        attack = attackSwitcher[value][0]
        newAttack = copy.deepcopy(attack)
        
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
        
    def removeSelection(key):
        Selector.selections.pop(key)
        Selector.keyList.remove(key)
        
    def rename(newKey, oldKey):
        attack = Selector.selections.get(oldKey)
        Selector.removeSelection(oldKey)
        Selector.selections[newKey] = attack
        Selector.keyList.append(newKey)
        
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

class Context:
    def __init__(self, oldContext, chance, result):
        if oldContext:
            self.flatfooted = oldContext.origffstatus
            self.trueStrike = oldContext.trueStrike
            self.origffstatus = oldContext.origffstatus
            self.treatWorse = False
            self.ignoreNext = False
            self.attackBonus = oldContext.attackBonus
            self.debuffTarget = oldContext.debuffTarget
            self.debuffAttack = oldContext.debuffAttack
            self.debuffDamage = oldContext.debuffDamage
            self.damageBonus = oldContext.damageBonus
            self.chance = oldContext.chance * chance
            self.hits = oldContext.hits
            self.crits = oldContext.crits
            
            self.damageDistribution = copy.deepcopy(oldContext.damageDistribution)
            self.persDistribution = copy.deepcopy(oldContext.persDistribution)
            
            self.thisStrikeBonus = 0
            self.thisDamageBonus = 0
        
            self.onFirstHitDamageDice = oldContext.onFirstHitDamageDice
            self.onSecondHitDamageDice = oldContext.onSecondHitDamageDice
            self.onThirdHitDamageDice = oldContext.onThirdHitDamageDice
            self.onEveryHitDamageDice = oldContext.onEveryHitDamageDice
            
            if result:
                if result.good:
                    self.hits += 1
                if result.veryGood:
                    self.crits += 1
                    
                if result.futureAttacksFF:
                    self.origffstatus = True
                    self.flatfooted = True
                elif result.nextAttackFF:
                    self.flatfooted = True
                elif not type(result.atk) is Strike:
                    self.flatfooted = oldContext.flatfooted
                    
                if result.trueStrike:
                    self.trueStrike = True 
               
                if result.treatWorse:
                    self.treatWorse = True
                    
                if result.ignoreNext:
                    
                    self.ignoreNext = True
                    
                self.thisStrikeBonus = max(oldContext.thisStrikeBonus, result.nextStrikeBonus)
                
                    
                if result.addfirsthitdamageDice != 0:
                    self.onFirstHitDamageDice += result.addfirsthitdamageDice
                if result.addsecondhitdamageDice != 0:
                    self.onSecondHitDamageDice += result.addsecondhitdamageDice
                if result.addthirdhitdamageDice != 0:
                    self.onThirdHitDamageDice += result.addthirdhitdamageDice
                if result.addeveryhitdamageDice != 0:
                    self.onEveryHitDamageDice += result.addeveryhitdamageDice
                    
                self.thisDamageBonus = result.adddamage
                
                if result.debuffAttack > self.debuffAttack:
                    self.debuffAttack = result.debuffAttack
                    
                if result.debuffDamage > self.debuffDamage:
                    self.debuffDamage = result.debuffDamage
                
                if result.debuffTarget > self.debuffTarget:
                    self.debuffTarget = result.debuffTarget
                
                if isinstance(result.atk, Strike) and result.isHit():
                    #self.totalDamage += self.onFirstHitDamage + self.onEveryHitDamage
                    result.damageDice += self.onFirstHitDamageDice + self.onEveryHitDamageDice
                    
                    self.onFirstHitDamageDice = self.onSecondHitDamageDice
                    self.onSecondHitDamageDice = self.onThirdHitDamageDice
                    self.onThirdHitDamageDice = []
                
            
                #apply attacks damage to distribution
                # doubled, halved, or normal
                damageDist = Distribution(result.damageDice,result.staticDamage)
                persDist = Distribution(result.persDamDice,result.persDam)
                
                
                #double for crit
                if result.doubleDamage:
                    damageDist.double()
                    if result.doublePersOnDouble:
                        persDist.double()
                        
                if result.isCrit():
                    damageDist.add(result.critDamDice,result.critDam)
                    persDist.add(result.critPersDamDice,result.critPersDam)
                    
                # halve damage
                if result.halveDamage:
                    damageDist.halve()
                    # ignoring damage...
                
                # add splash damage
                damageDist.add(result.splashDamDice, result.splashDam)
                
                self.damageDistribution.combine(damageDist)
                self.persDistribution.combine(persDist)
                
                # modified by how much we care about pers damage
                #pdWeight = int(CombinedAttack.PDWeight)
                #persDist.multiply(pdWeight)
               
                return
            
            return 
        self.flatfooted = False
        self.origffstatus = False
        self.trueStrike = False
        self.treatWorse = False
        self.ignoreNext = False
        self.attackBonus = 0
        self.debuffAttack = 0
        self.debuffDamage = 0
        self.debuffTarget = 0
        self.damageBonus = 0
        self.chance = chance
        self.totalDamage = 0
        self.totalPDamage = 0
        self.hits = 0
        self.crits = 0
 
        self.damageDistribution = Distribution()
        self.persDistribution = Distribution()
        
        
        self.thisStrikeBonus = 0
        self.thisDamageBonus = 0
        
        self.onFirstHitDamageDice = []
        self.onSecondHitDamageDice = []
        self.onThirdHitDamageDice = []
        self.onEveryHitDamageDice = []
        return
    
    def setFlatfooted(self):
        self.origffstatus = True
        self.flatfooted = True
        
    def setTrueStrike(self):
        self.trueStrike = True
        
    def setAttackBonus(self, ab):
        self.attackBonus = ab
        
    def setDamageBonus(self, db):
        self.damageBonus = db
        
    def getStrikeBonus(self):
        bonus = self.attackBonus + self.thisStrikeBonus
        self.thisStrikeBonus = 0
        return bonus - self.debuffAttack
    
    def getSaveAttackBonus(self):
        return self.attackBonus - self.debuffAttack
    
    def getDCBonus(self):
        return self.attackBonus - self.debuffAttack
    
    def getSaveBonus(self):
        return 0 - self.debuffTarget
    
    def getACBonus(self):
        return 0 - self.debuffTarget
    
    def getEffectBonus(self):
        return 0
    
    def getExtraDamage(self):
        return self.damageBonus + self.thisDamageBonus - self.debuffDamage
    
    def getDamageBonus(self):
        return self.damageBonus - self.debuffDamage
    
    def hasTrueStrike(self):
        tss = self.trueStrike
        self.trueStrike = False
        return tss
    
    def averageDamage(self):
#        print("ave dam is ",self.damageDistribution.average())
#        print("dam dist is ")
        return self.damageDistribution.average()
    
    def averagePDamage(self):
        return self.persDistribution.average()
    
    def numberHits(self):
        return self.hits
    
    def numberCrits(self):
        return self.crits
    
    def getDamageDist(self):
        return self.damageDistribution.generate()
    
def generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    oContext = Context(None, 1, None)
    oContext.setAttackBonus(attackBonus)
    oContext.setDamageBonus(damageBonus)
    normalContext = Context(oContext, 1-flatfootedStatus/100,None)
    ffContext = Context(oContext, flatfootedStatus/100, None)
    ffContext.setFlatfooted()
    contextList = [normalContext, ffContext]
    
    for atk in routine: #for each strike in that routine
        newContextList = []
        for context in contextList:
            # calculate the effects for this attack
            if context.chance == 0:
                continue 
                
            keenStatus = False
            trueStrike = False
            if(isinstance(atk, Strike)):
                totalBonus = atk.getAttack(level)
                totalBonus += context.getStrikeBonus()
                keenStatus = atk.getKeen(level)
                trueStrike = context.hasTrueStrike()
                
                totalDC = target.getAC(level+levelDiff) + context.getACBonus()
            
                if context.flatfooted:
                    totalDC -= 2
            elif(isinstance(atk,SaveAttack)):
                totalBonus = atk.getAttack(level)
                totalBonus += context.getSaveAttackBonus()
                keenStatus = atk.getKeen(level)
                
                trueStrike = context.hasTrueStrike()
            
                totalDC = 10 + target.getSaves(level+levelDiff) + context.getSaveBonus()
            elif(isinstance(atk, Save)):
                totalBonus = target.getSaves(level+levelDiff)
                totalBonus += context.getSaveBonus() 
                
                totalDC = atk.getDC(level)
                totalDC += context.getDCBonus()
#            elif(isinstance(atk, AttackSave)):
#                totalBonus = atk.getAttack(level)
#                totalBonus += context.getStrikeBonus()
#                keenStatus = atk.getKeen(level)
#                trueStrike = context.hasTrueStrike()
#                
#                totalDC = target.getAC(level+levelDiff) + context.getACBonus()
#                if context.flatfooted:
#                    totalDC -= 2
#                    
#                
            elif(isinstance(atk, Effect)):
                r = atk.effectResult(level, context)
                eContext = Context(context, 1, r)
                newContextList.append(eContext)
                continue
            else:
                # this should not happen
                print("attack type was", type(atk))
                continue
            
            # create a new context for each degree of success
            if trueStrike:
                notcrit = 100 - critSuccessChance(totalBonus-totalDC, keen=keenStatus)
                critSuccessPercent = 100 - (notcrit * notcrit / 100)
                nothit = notcrit - successChance(totalBonus-totalDC, keen=keenStatus)
                successPercent = 100 - (nothit * nothit / 100) - critSuccessPercent
                notfail = nothit - failureChance(totalBonus-totalDC)
                failurePercent = 100 - (notfail * notfail / 100) - successPercent - critSuccessPercent
                critFailurePercent = critFailureChance(totalBonus-totalDC) * critFailureChance(totalBonus-totalDC) / 100
                
            else:
                critSuccessPercent = critSuccessChance(totalBonus-totalDC, keen=keenStatus)
                successPercent = successChance(totalBonus-totalDC, keen=keenStatus)
                failurePercent = failureChance(totalBonus-totalDC)
                critFailurePercent = critFailureChance(totalBonus-totalDC)
                
            if context.treatWorse:
                critFailurePercent = critFailurePercent + failurePercent
                failurePercent = successPercent
                successPercent = critSuccessPercent
                critSuccessPercent = 0
                
            if context.ignoreNext:
                ignoreContext = Context(context, 1, None)
                newContextList.append(ignoreContext)
            else:
                critSuccessResult = atk.critSuccessResult(level, context)
                csContext = Context(context, critSuccessPercent/100, critSuccessResult)
                newContextList.append(csContext)
            
                
                successResult = atk.successResult(level, context)
                sContext = Context(context, successPercent/100, successResult)
                newContextList.append(sContext)
                
            
                failureResult = atk.failureResult(level, context)
                fContext = Context(context, failurePercent/100, failureResult)
                newContextList.append(fContext)
            
            
                critFailureResult = atk.critFailureResult(level, context)
                cfContext = Context(context, critFailurePercent/100, critFailureResult)
                newContextList.append(cfContext)      
            
        # replace contextList with the list of newly created contexts
        contextList = newContextList
        
    return contextList
    
    
def graphTrace(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    y = 0
    py = 0
    hits = 0
    crits = 0
    
    if type(routine) is CombinedAttack:
        # what if it contains more combined attacks?
        for atk in routine.validFor(level):
            newy, newpy, nh, nc = graphTrace(atk, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
            if y == 0:
                y = newy
                py = newpy
                hits = nh
                crits = nc
            else:
                y, py, hits, crits = routine.choose(y, py, newy, newpy, hits, crits, nh, nc)
        return y, py, hits, crits
        
    contextList = generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
        
    for context in contextList:
#        print("level is ", level)
#        print("chance is ", context.chance)
        y += context.averageDamage() * context.chance
        py += context.averagePDamage() * context.chance
        hits += context.numberHits() * context.chance
        crits += context.numberCrits() * context.chance
        
    return y, py, hits, crits

                    
def graphChanceDamage(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    # returns an xList of damages and a yList of chances
    damageList = []
    chanceList = []
    
    if type(routine) is CombinedAttack:
        # what if it contains more combined attacks?
        print("not implimented")
        raise Exception("Can't handle Combinded Attacks")
    
    contextList = generateContextList(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
        
    damageChanceDict = {}
    for context in contextList:
        # get chance and damage
        for damage, chance in context.getDamageDist():
            damage = int(damage)
            if damage in damageChanceDict:
                damageChanceDict[damage] += chance * context.chance
            else:
                damageChanceDict[damage] = chance * context.chance
    
    maxDamage = max(damageChanceDict.keys())
    for damage in range(maxDamage+1):
        chance = 0
        if damage in damageChanceDict:
            chance = damageChanceDict[damage]
        damageList.append(damage)
        chanceList.append(chance)
    
    return damageList, chanceList
	
def createTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness):
#     print("c t")
    xLists = []
    yLists = []
    pyLists = []
    hitsLists = []
    critsLists = []
    target = Selector.selectedTarget
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        pyList = []
        hitsList = []
        critsList = []
        for i in range(1,21):
            toAdd = True
            if(type(s) is CombinedAttack):
                if s.contains(i) and target.contains(i+levelDiff):
                    xList.append(i)
            else:
                for st in s:  
                    if not(st.getAttack(i) is not None and target.contains(i+levelDiff)):
                        toAdd = False
                if toAdd:
                    xList.append(i) 
        for i in range(1,21): 
            if i in xList:
                # reset damage and things like flat footed status             
                y, py, hits, crits = graphTrace(s, target, i, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
     
                yList.append(y)
                pyList.append(py)
                hitsList.append(hits)
                critsList.append(crits)
        xLists.append(xList)
        yLists.append(yList)
        pyLists.append(pyList)
        hitsLists.append(hitsList)
        critsLists.append(critsList)
        
    
    return xLists, yLists, pyLists, hitsLists, critsLists, Selector.keyList

def createLevelTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level):
    xLists = []
    xLists2 = []
    yLists = []
    pyLists = []
    hitsLists = []
    critsLists = []
    target = Selector.selectedTarget
    
    if not target.contains(level+levelDiff):
        return xLists, yLists, pyLists, hitsLists, critsLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        xList2 = []
        yList = []
        pyList = []
        hitsList = []
        critsList = []
        
        # is this strike routine valid for this level?
        toAdd = True
        if(type(s) is CombinedAttack):
            if not s.contains(level):
                    toAdd = False
        else:
            for st in s:  
                if not(st.getAttack(level) ):
                    toAdd = False
        
        if toAdd:
            for i in range(-8,9):
                ac = target.getAC(level+levelDiff)-i
                save = target.getSaves(level+levelDiff)-i
                xList.append(ac)
                xList2.append(save)
                y, py, hits, crits = graphTrace(s, target, level, levelDiff, attackBonus+i, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
                pyList.append(py)
                hitsList.append(hits)
                critsList.append(crits)
        xLists.append(xList)
        xLists2.append(xList2)
        yLists.append(yList)
        pyLists.append(pyList)
        hitsLists.append(hitsList)
        critsLists.append(critsList)
    
    return xLists, xLists2, yLists, pyLists, hitsLists, critsLists, Selector.keyList
        
def createDamageDistribution(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level):
    xLists = []
    yLists = []
    target = Selector.selectedTarget
    
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
                if not(st.getAttack(level) ):
                    toAdd = False
        
        if toAdd:
            # get the damage, x, and chance, y, for this attack
            xList, yList = graphChanceDamage(s, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
            
            
        xLists.append(xList)
        yLists.append(yList)
    
    return xLists, yLists, Selector.keyList