# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:18:59 2019

@author: bhalb
"""
import copy
from pf2calcMonsterStats import creatureData

d4 = [1/4] * 4
d6 = [1/6] * 6
d8 = [1/8] * 8
d10 = [1/10] * 10
d12 = [1/12] * 12

summonAnimalAttackB = [7,
7,
9,
9,
10,
10,
12,
12,
16,
16,
18,
18,
22,
22,
25,
25,
28,
28,
31,
31]
summonAnimalDamageB = [4.5,
4.5,
5.5,
5.5,
11,
11,
10.5,
10.5,
16,
16,
18,
18,
24,
24,
27,
27,
31.5,
31.5,
35.5,
35.5]
summonDragonAttackB = [14,
14,
19,
19,
21,
21,
25,
25,
28,
28,
31,
31]
summonDragonDamageB = [17.5,
17.5,
23.5,
23.5,
26.5,
26.5,
33,
33,
34.5,
34.5,
46,
46]
sumAniAttack = {i: summonAnimalAttackB[i-1] for i in range(1,21)}
sumAniDamage = {i: summonAnimalDamageB[i-1] for i in range(1,21)}
sumDraAttack = {i: summonDragonAttackB[i-9] for i in range(9,21)}
sumDraDamage = {i: summonDragonDamageB[i-9] for i in range(9,21)}

animalFormAttackB = [9,
9,
14,
14,
16,
16,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18]
animalFormDamageB = [10,
10,
14,
14,
18,
18,
25,
25,
25,
25,
25,
25,
25,
25,
25,
25,
25,
25]
insectFormAttackB = [13,
13,
16,
16,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18,
18]
insectFormDamageB = [13,
13,
17,
17,
24,
24,
24,
24,
24,
24,
24,
24,
24,
24,
24,
24]
dinoFormAttackB = [16,
16,
18,
18,
18,
18,
25,
25,
25,
25,
25,
25,
25,
25]
dinoFormDamageB = [18,
18,
24,
24,
24,
24,
33,
33,
33,
33,
33,
33,
33,
33]
aerialFormAttackB = [16,
16,
18,
18,
21,
21,
21,
21,
21,
21,
21,
21,
21,
21]
aerialFormDamageB = [15.5,
15.5,
18.5,
18.5,
25,
25,
25,
25,
25,
25,
25,
25,
25,
25]
elemFormAttackB = [18,
18,
23,
23,
25,
25,
25,
25,
25,
25,
25,
25]
elemFormDamageB = [20,
20,
24,
24,
33,
33,
33,
33,
33,
33,
33,
33]
plantFormAttackB = [17,
17,
21,
21,
21,
21,
21,
21,
21,
21,
21,
21]
plantFormDamageB = [22,
22,
27,
27,
27,
27,
27,
27,
27,
27,
27,
27]
dragonFormAttackB=[22,
22,
22,
22,
28,
28,
28,
28,
28,
28]
dragonFormDamageB = [26,
26,
26,
26,
32,
32,
32,
32,
32,
32]
monFormAttackB = [28,
28,
31,
31,
31,
31]
monFormDamageB = [33,
33,
39.5,
39.5,
39.5,
39.5]
natFormAttackB = [34,
34]
natFormDamageB=[43,
43]

animalFormAttack = {i: animalFormAttackB[i-3] for i in range(3,21)}
animalFormDamage = {i: animalFormDamageB[i-3] for i in range(3,21)}
insectFormAttack = {i: insectFormAttackB[i-5] for i in range(5,21)}
insectFormDamage = {i: insectFormDamageB[i-5] for i in range(5,21)}
dinoFormAttack = {i: dinoFormAttackB[i-7] for i in range(7,21)}
dinoFormDamage = {i: dinoFormDamageB[i-7] for i in range(7,21)}
aerialFormAttack = {i: aerialFormAttackB[i-7] for i in range(7,21)}
aerialFormDamage = {i: aerialFormDamageB[i-7] for i in range(7,21)}
elemFormAttack = {i: elemFormAttackB[i-9] for i in range(9,21)}
elemFormDamage = {i: elemFormDamageB[i-9] for i in range(9,21)}
plantFormAttack = {i: plantFormAttackB[i-9] for i in range(9,21)}
plantFormDamage = {i: plantFormDamageB[i-9] for i in range(9,21)}
dragonFormAttack = {i: dragonFormAttackB[i-11] for i in range(11,21)}
dragonFormDamage = {i: dragonFormDamageB[i-11] for i in range(11,21)}
monFormAttack = {i: monFormAttackB[i-15] for i in range(15,21)}
monFormDamage = {i: monFormDamageB[i-15] for i in range(15,21)}
natFormAttack = {i: natFormAttackB[i-19] for i in range(19,21)}
natFormDamage = {i: natFormDamageB[i-19] for i in range(19,21)}

mProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    mProf[i] += 2
    if i >=5: 
        mProf[i] += 2
    if i >= 13: 
        mProf[i] += 2
        
cProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    cProf[i] += 2
    if i >=11: 
        cProf[i] += 2

wProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    wProf[i] += 2
    if i >=7: 
        wProf[i] += 2

fProf = copy.copy(mProf)
for i in fProf:
    fProf[i] += 2
    
sProf = {i: i+2 for i in range(1,21)}
for i in sProf:
    if i >= 7:
        sProf[i] += 2
    if i >= 15:
        sProf[i] += 2
    if i >= 19:
        sProf[i] +=2
        
wsProf = {i: i+2 for i in range(1,21)}
for i in wsProf:
    if i >= 11:
        wsProf[i] += 2
    if i >= 19:
        wsProf[i] += 2

skillProf = {i: i+2 for i in range(1,21)}
for i in skillProf:
    if i >= 3:
        skillProf[i] += 2
    if i >= 7:
        skillProf[i] += 2
    if i >= 15:
        skillProf[i] += 2
    
mStr = {i: 4 for i in range(1,21)}
for i in mStr:
    if i >= 10:
        mStr[i] += 1
    if i >= 17:
        mStr[i] += 1
    if i >=20:
        mStr[i] +=1
        
#cStr = {i: 3 for i in range(1,21)}
#for i in cStr:
#    if i >= 5:
#        cStr[i] += 1
#    if i >= 15:
#        cStr[i] += 1
#
#wStr = {i: 3 for i in range(1,21)}
#for i in wStr:
#    if i >= 5:
#        wStr[i] += 1
#    if i >= 15:
#        wStr[i] += 1
#    if i >= 17:
#        wStr[i] += 1
        
wiBonus = {i: 0 for i in range(1,21)}
for i in wiBonus:
    if i >= 2:
        wiBonus[i] += 1
    if i >= 10:
        wiBonus[i] += 1
    if i >= 16:
        wiBonus[i] += 1
        
#mutagen item bonus
miBonus = {i: 1 for i in range(1,21)}
for i in miBonus:
    if i >= 3:
        miBonus[i] += 1
    if i >= 11:
        miBonus[i] += 1
    if i >= 17: 
        miBonus[i] +=1
        
siBonus = {i: 0 for i in range(1,21)}
for i in siBonus:
    if i >= 3:
        siBonus[i] += 1
    if i >= 9:
        siBonus[i] += 1
    if i >= 17:
        siBonus[i] += 1
        
wDice = {i: 1 for i in range(1,21)}
for i in wDice:
    if i >= 4:
        wDice[i] += 1
    if i >= 12:
        wDice[i] += 1
    if i >= 19:
        wDice[i] += 1
        
sDice = {i: int((i+1)/2) for i in range(1,21)}

martialAttackBonus = {i: mProf[i]  + wiBonus[i] for i in range(1,21)}

casterAttackBonus = {i: cProf[i] + wiBonus[i] for i in range(1,21)}

warpriestAttackBonus = {i: wProf[i]  + wiBonus[i] for i in range(1,21)}
wildshapeAttackBonus = {i: cProf[i] + wiBonus[i] + 2 for i in range(1,21)}

bombAttackBonus = {i: wProf[i]  + miBonus[i]-1 for i in range(1,21)}
pbombAttackBonus = {i: wProf[i]  + miBonus[i]-2 for i in range(1,21)}
mutagenstrikeAttackBonus = {i: wProf[i]  + miBonus[i] for i in range(1,21)}

fighterAttackBonus = {i: fProf[i]  + wiBonus[i] for i in range(1,21)}

cantripAttackBonus = {i: sProf[i]  for i in range(1,21)}
spellDC = {i: 10 + cantripAttackBonus[i] for i in range(1,21)}
warpriestDC = {i: 10 + wsProf[i] for i in range(1,21)}

trainedSkillBonus = {i: i+2 for i in range(1,21)}
maxSkillBonus = {i: skillProf[i] + siBonus[i] for i in range(1,21)}
rogueMaxSkill = copy.copy(maxSkillBonus)
rogueMaxSkill[2] += 2

basewolf = {i: i+5 for i in range(1,21)}
maturewolf = {i: i+6 for i in range(1,21)}
nimblewolf = {i: i+8 for i in range(1,21)}
specializedwolf = {i: i+12 for i in range(1,21)}

druidwolfattack = {i: basewolf[i] for i in range(1,21)}
for i in druidwolfattack:
    if i >= 4:
        druidwolfattack[i] = maturewolf[i]
    if i >= 8:
        druidwolfattack[i] = nimblewolf[i]
    if i >= 14:
        druidwolfattack[i] = specializedwolf[i]
        
rangerwolfattack = {i: basewolf[i] for i in range(1,21)}
for i in rangerwolfattack:
    if i >= 6:
        rangerwolfattack[i] = maturewolf[i]
    if i >= 10:
        rangerwolfattack[i] = nimblewolf[i]
    if i >= 16:
        rangerwolfattack[i] = specializedwolf[i]

basebear = {i: i+5 for i in range(1,21)}
maturebear = {i: i+6 for i in range(1,21)}
savagebear = {i: i+8 for i in range(1,21)}
specializedbear = {i: i+11 for i in range(1,21)}

druidbearattack = {i: basebear[i] for i in range(1,21)}
for i in druidbearattack:
    if i >= 4:
        druidbearattack[i] = maturebear[i]
    if i >= 8:
        druidbearattack[i] = savagebear[i]
    if i >= 14:
        druidbearattack[i] = specializedbear[i]
        
rangerbearattack = {i: basebear[i] for i in range(1,21)}
for i in rangerbearattack:
    if i >= 6:
        rangerbearattack[i] = maturebear[i]
    if i >= 10:
        rangerbearattack[i] = savagebear[i]
    if i >= 16:
        rangerbearattack[i] = specializedbear[i]

mwSpec = {i: 0 for i in range(1,21)}
for i in mwSpec:
    if i >= 7:
        mwSpec[i] = int((mProf[i]-i)/2)
    if i >= 15:
        mwSpec[i] = int((mProf[i]-i))
        
fwSpec = {i: 0 for i in range(1,21)}
for i in fwSpec:
    if i >= 7:
        fwSpec[i] = int((fProf[i]-i)/2)
    if i >= 15:
        fwSpec[i] = int((fProf[i]-i))
        
cwSpec = {i: 0 for i in range(1,21)}
for i in cwSpec:
    if i >= 13:
        cwSpec[i] = int((cProf[i]-i)/2)
        
        
bombSplashDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        bombSplashDamage[i] = 2
    if i >= 11:
        bombSplashDamage[i] = 3
    if i >= 17:
        bombSplashDamage[i] = 4
        
bomberSplashDamage = copy.copy(bombSplashDamage)
for i in range(4,21):
    bomberSplashDamage[i] = mStr[i]
    if i >= 10:
        bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i]
    if i >= 17:
        bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i] - 1

pbombSplashDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pbombSplashDamage[i] = 1
    if i >= 11:
        pbombSplashDamage[i] = 2
    if i >= 17:
        pbombSplashDamage[i] = 3

pbomberSplashDamage = copy.copy(bomberSplashDamage)
for i in range(10,21):
    pbomberSplashDamage[i] = bomberSplashDamage[i] - 1

        
acidFlaskDamage = {i: 1 for i in range(1,21)}

acidFlaskPersDamage = {i: [d6] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        acidFlaskPersDamage[i] += [d6]
    if i >= 11:
        acidFlaskPersDamage[i] += [d6]
    if i >= 17:
        acidFlaskPersDamage[i] += [d6]

alchemistsFireDamage = {i: [d8] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFireDamage[i] += [d8]
    if i >= 11:
        alchemistsFireDamage[i] += [d8]
    if i >= 17:
        alchemistsFireDamage[i] += [d8]

alchemistsFirePersDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFirePersDamage[i] = 2
    if i >= 11:
        alchemistsFirePersDamage[i] = 3
    if i >= 17:
        alchemistsFirePersDamage[i] = 4

blfvDamage = {i: [d6] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        blfvDamage[i] += [d6]
    if i >= 11:
        blfvDamage[i] += [d6]
    if i >= 17:
        blfvDamage[i] += [d6]
        
thunderStoneDamage = {i: [d4] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        thunderStoneDamage[i] += [d4]
    if i >= 11:
        thunderStoneDamage[i] += [d6]
    if i >= 17:
        thunderStoneDamage[i] += [d6]
       
# perpetual infusions
pacidFlaskDamage = {i: 0 for i in range(1,21)}
for i in range(7,21):
    pacidFlaskDamage[i] = 1

pacidFlaskPersDamage = {i: [] for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pacidFlaskPersDamage[i] += [d6]
    if i >= 11:
        pacidFlaskPersDamage[i] += [d6]
    if i >= 17:
        pacidFlaskPersDamage[i] += [d6]

palchemistsFireDamage = {i: [] for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        palchemistsFireDamage[i] += [d8]
    if i >= 11:
        palchemistsFireDamage[i] += [d8]
    if i >= 17:
        palchemistsFireDamage[i] += [d8]

palchemistsFirePersDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        palchemistsFirePersDamage[i] = 1
    if i >= 11:
        palchemistsFirePersDamage[i] = 2
    if i >= 17:
        palchemistsFirePersDamage[i] = 3

pblfvDamage = {i: [] for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pblfvDamage[i] += [d6]
    if i >= 11:
        pblfvDamage[i] += [d6]
    if i >= 17:
        pblfvDamage[i] += [d6]
        
pthunderStoneDamage = {i: [] for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pthunderStoneDamage[i] += [d4]
    if i >= 11:
        pthunderStoneDamage[i] += [d4]
    if i >= 17:
        pthunderStoneDamage[i] += [d4]
        
bestialClawDamageDice = {i: wDice[i]*[d4] for i in range(1,21)}
for i in bestialClawDamageDice:
    if i >= 3:
        bestialClawDamageDice[i] = wDice[i]*[d6]
    if i >= 11:
        bestialClawDamageDice[i] = wDice[i]*[d8]
    if i >= 17:
        bestialClawDamageDice[i] = wDice[i]*[d8]
        
bestialJawDamageDice = {i: wDice[i]*[d6] for i in range(1,21)}
for i in bestialJawDamageDice:
    if i >= 3:
        bestialJawDamageDice[i] = wDice[i]*[d8]
    if i >= 11:
        bestialJawDamageDice[i] = wDice[i]*[d10]
    if i >= 17:
        bestialJawDamageDice[i] = wDice[i]*[d10]
        
feralClawDamageDice = {i: wDice[i]*[d6] for i in range(1,21)}
for i in feralClawDamageDice:
    if i >= 3:
        feralClawDamageDice[i] = wDice[i]*[d8]
    if i >= 11:
        feralClawDamageDice[i] = wDice[i]*[d10]
    if i >= 17:
        feralClawDamageDice[i] = wDice[i]*[d10]
        
feralJawDamageDice = {i: wDice[i]*[d8] for i in range(1,21)}
for i in feralJawDamageDice:
    if i >= 3:
        feralJawDamageDice[i] = wDice[i]*[d10]
    if i >= 11:
        feralJawDamageDice[i] = wDice[i]*[d12]
    if i >= 17:
        feralJawDamageDice[i] = wDice[i]*[d12]
        
        
animalJawDamageDice = {i: wDice[i]*[d10] for i in range(1,21)}
for i in animalJawDamageDice:
    if i >= 7:
        animalJawDamageDice[i] = wDice[i]*[d12]
        
animalClawDamageDice = {i: wDice[i]*[d6] for i in range(1,21)}
for i in animalClawDamageDice:
    if i >= 7:
        animalClawDamageDice[i] = wDice[i]*[d8]
        
animalragedamage = {i: 2 for i in range(1,21)}
for i in animalragedamage:
    if i >= 7:
        animalragedamage[i] = 5
    if i >= 15:
        animalragedamage[i] = 12

dragonragedamage = {i: 4 for i in range(1,21)}
for i in dragonragedamage:
    if i >= 7:
        dragonragedamage[i] = 8
    if i >= 15:
        dragonragedamage[i] = 16

furyragedamage = {i: 2 for i in range(1,21)}
for i in furyragedamage:
    if i >= 7:
        furyragedamage[i] = 6
    if i >= 15:
        furyragedamage[i] = 12
        
giantragedamage = {i: 6 for i in range(1,21)}
for i in giantragedamage:
    if i >= 7:
        giantragedamage[i] = 10
    if i >= 15:
        giantragedamage[i] = 18

spiritragedamage = {i: 3 for i in range(1,21)}
for i in spiritragedamage:
    if i >= 7:
        spiritragedamage[i] = 7
    if i >= 15:
        spiritragedamage[i] = 13
        
smiteevildamage = {i: 0 for i in range(1,21)}
for i in smiteevildamage:
    if i >= 6:
        smiteevildamage[i] = 4
    if i >= 13:
        smiteevildamage[i] = 6
        
sneakattackdamage = {i: [d6] for i in range(1,21)}
for i in sneakattackdamage:
    if i >= 5:
        sneakattackdamage[i] += [d6]
    if i >= 11:
        sneakattackdamage[i] += [d6]
    if i >= 17:
        sneakattackdamage[i] += [d6]
        
rangerprecedgedamage1 = {i: [d8] for i in range(1,21)}
for i in rangerprecedgedamage1:
    if i >= 11:
        rangerprecedgedamage1[i] += [d8]
    if i >= 19:
        rangerprecedgedamage1[i] += [d8]
        
rangerprecedgedamage2 = {i: [] for i in range(1,21)}
for i in rangerprecedgedamage2:
    if i >= 17:
        rangerprecedgedamage2[i] += [d8] 
    if i >= 19:
        rangerprecedgedamage2[i] += [d8]  
        
rangerprecedgedamage3 = {i: [] for i in range(1,21)}
for i in rangerprecedgedamage3:
    if i >= 19:
        rangerprecedgedamage3[i] += [d8] 
        
rangerbearsupportdamage = {i: [d8] for i in range(1,21)}
for i in rangerbearsupportdamage:
    if i >= 10:
        rangerbearsupportdamage[i] += [d8]
        
druidwolfdamage = {i: 6.5 for i in range(1,21)}
for i in druidwolfdamage:
    if i >= 4:
        druidwolfdamage[i] = 12
    if i >= 8:
        druidwolfdamage[i] = 15 
    if i >= 14:
        druidwolfdamage[i] = 21.5 
        
rangerwolfdamage = {i: 6.5 for i in range(1,21)}
for i in rangerwolfdamage:
    if i >= 6:
        rangerwolfdamage[i] = 12
    if i >= 10:
        rangerwolfdamage[i] = 15 
    if i >= 16:
        rangerwolfdamage[i] = 21.5 
        
druidbeardamage = {i: 7.5 for i in range(1,21)}
for i in druidbeardamage:
    if i >= 4:
        druidbeardamage[i] = 13
    if i >= 8:
        druidbeardamage[i] = 18 
    if i >= 14:
        druidbeardamage[i] = 26.5 
        
rangerbeardamage = {i: 7.5 for i in range(1,21)}
for i in rangerbeardamage:
    if i >= 6:
        rangerbeardamage[i] = 13
    if i >= 10:
        rangerbeardamage[i] = 18
    if i >= 16:
        rangerbeardamage[i] = 26.5 
      
# ability score bonuses by level
as10 = {i: 0 for i in range(1,21)}
as12 = {i: 1 for i in range(1,21)}
as14 = {i: 2 for i in range(1,21)}
as16 = {i: 3 for i in range(1,21)}
as18 = {i: 4 for i in range(1,21)}
as10p = {i: 0 for i in range(1,21)}
as12p = {i: 1 for i in range(1,21)}
as14p = {i: 2 for i in range(1,21)}
as16p = {i: 3 for i in range(1,21)}
as14pp = {i: 2 for i in range(1,21)}
as16pp = {i: 3 for i in range(1,21)}
as18pp = {i: 4 for i in range(1,21)}
as14ppa = {i: 2 for i in range(1,21)}
as16ppa = {i: 3 for i in range(1,21)}
as18ppa = {i: 4 for i in range(1,21)}
for i in range(1,21):
    if i >= 5:
        as10p[i] += 1
        as12p[i] += 1
        as14p[i] += 1
        as16p[i] += 1
        as14pp[i] += 1
        as16pp[i] += 1
        as14ppa[i] += 1
        as16ppa[i] += 1
    if i >= 10:
        as10p[i] += 1
        as12p[i] += 1
        as14p[i] += 1
        as14pp[i] += 1
        as18pp[i] += 1
        as14ppa[i] += 1
        as18ppa[i] += 1
    if i >= 15:
        as10p[i] += 1
        as12p[i] += 1
        as16pp[i] += 1
        as16ppa[i] += 1 
    if i >= 20:
        as10p[i] += 1
        as14pp[i] += 1
        as18pp[i] += 1
        as14ppa[i] += 1
        as18ppa[i] += 1
    if i >= 17:
        as14ppa[i] += 1
        as16ppa[i] += 1
        as18ppa[i] += 1
abilityScoreConverter = {'10 No Boost': as10,
                       '12 No Boost': as12,
                       '14 No Boost': as14,
                       '16 No Boost': as16,
                       '18 No Boost': as18,
                       '10 to  18': as10p,
                       '12 to 18': as12p,
                       '14 to 18': as14p,
                       '16 to 18': as16p,
                       '14 to 20 No Apex': as14pp,
                       '16 to 20 No Apex': as16pp,
                       '18 to 22 No Apex': as18pp,
                       '14 to 20 Apex': as14ppa,
                       '16 to 20 Apex': as16ppa,
                       '18 to 22 Apex': as18ppa}
        

damageDiceConverter = {"1d4": [d4,0],
                       "1d6": [d6,0],
                       "1d8": [d8,0],
                       "1d10": [d10,0],
                       "1d12": [d12,0],
                       "1d4+1": [d4,1],
                       "1d6+1": [d6,1],
                       "1d8+1": [d8,1],
                       "1d10+1": [d10,1],
                       "1d12+1": [d12,1],
                       "1d4+2": [d4,2],
                       "1d6+2": [d6,2],
                       "1d8+2": [d8,2],
                       "1d10+2": [d10,2],
                       "1d12+2": [d12,2]}

noneDamage = {i: 0 for i in range(1,21)}
deadlyd6DamageDice = {i: [d6]*max(1,(wDice[i]-1)) for i in range(1,21)}
deadlyd8DamageDice = {i: [d8]*max(1,(wDice[i]-1)) for i in range(1,21)}
deadlyd10DamageDice = {i: [d10]*max(1,(wDice[i]-1)) for i in range(1,21)}
deadlyd12DamageDice = {i: [d12]*max(1,(wDice[i]-1)) for i in range(1,21)}

criticalDiceConverter = {"No Crit Damage": [False, None],
                 "deadly d6": [False, deadlyd6DamageDice],
                 "deadly d8": [False, deadlyd8DamageDice],
                 "deadly d10": [False, deadlyd10DamageDice],
                 "deadly d12": [False, deadlyd12DamageDice],
                 "fatal d8": [True, d8],
                 "fatal d10": [True, d10],
                 "fatal d12": [True, d12]
        }

#d12pad = {i: 6.5 for i in range(1,21)}
#for i in d12pad:
#    if i>=10:
#        d12pad[i]+=6.5
#    if i>=18:
#        d12pad[i]+=6.5
#
#d10pad = {i: 5.5 for i in range(1,21)}
#for i in d10pad:
#    if i>=10:
#        d10pad[i]+=5.5
#    if i>=18:
#        d10pad[i]+=5.5
#        
#d12bfd = {i: 0 for i in range(1,21)}
#for i in d12bfd:
#    if i>=10:
#        d12bfd[i]+=6.5
#    if i>=18:
#        d12bfd[i]+=6.5
#        
#d10bfd = {i: 0 for i in range(1,21)}
#for i in d10bfd:
#    if i>=10:
#        d10bfd[i]+=5.5
#    if i>=18:
#        d10bfd[i]+=5.5
        
alchemistDamage = {i: cwSpec[i] for i in range(1,21)}
alchemistBestialDamage = {i: cwSpec[i] for i in range(1,21)}
for i in alchemistBestialDamage:
    if i >=17:
        alchemistBestialDamage[i]+=2
alchemistRangedDamage = {i: cwSpec[i] for i in range(1,21)}

strCasterDamage = {i: cwSpec[i] for i in range(1,21)}
rangedCasterDamage = {i: cwSpec[i] for i in range(1,21)}

cantripASDamageDice = {i: int((sDice[i]-1)/2)*[d8] for i in range(1,21)}
cantripASDamageDice[1] = [d8]
cantripASDamageDice[2] = [d8]
cantripASDamageDice[3] = [d8]
cantripASDamageDice[4] = [d8]
cantripDDamageDice = {i:  max(0,int((sDice[i]-1)/2))*[d6] for i in range(1,21)}
cantripTPDamageDice = {i: sDice[i]*[d6] for i in range(1,21)}
cantripRFDamageDice = {i: sDice[i]*[d4] for i in range(1,21)}
cantripASPDamage = {i: int((sDice[i]+1)/2)*1 for i in range(1,21)}
cantripPFPDamageDice = {i: sDice[i]*[d4] for i in range(1,21)}

magicMissleDamage = {i: int((sDice[i]+1)/2) * 1 for i in range(1,21)}
magicMissleDamageDice = {i: int((sDice[i]+1)/2) * [d4] for i in range(1,21)}
spellDamaged4 = {i: sDice[i]*[d4] for i in range(1,21)}
spellDamaged6 = {i: sDice[i]*[d6] for i in range(1,21)}
spellDamaged8 = {i: sDice[i]*[d8] for i in range(1,21)}
spellDamaged10 = {i: sDice[i]*[d10] for i in range(1,21)}
spellDamaged12 = {i: sDice[i]*[d12] for i in range(1,21)}
spellDamage2d4 = {i: sDice[i]*[d4,d4] for i in range(1,21)}
spellDamage2d6 = {i: sDice[i]*[d6,d6] for i in range(1,21)}
spellDamage2d8 = {i: sDice[i]*[d8,d8] for i in range(1,21)}
spellDamage2d10 = {i: sDice[i]*[d10,d10] for i in range(1,21)}
spellDamage2d12 = {i: sDice[i]*[d12,d12] for i in range(1,21)}
spellDamage1 = {i: sDice[i]*1 for i in range(1,21)}
spellDamage2 = {i: sDice[i]*2 for i in range(1,21)}
spellDamage10 = {i: sDice[i]*10 for i in range(1,21)}
spellDamage11 = {i: sDice[i]*11 for i in range(1,21)}
spellDamage12 = {i: sDice[i]*12 for i in range(1,21)}
spellDamage13 = {i: sDice[i]*13 for i in range(1,21)}

martialDamage = {i:  mwSpec[i] for i in range(1,21)}
martialRangedDamage = {i: mwSpec[i] for i in range(1,21)}

barbariananimaldamage = {i: martialDamage[i] + animalragedamage[i] for i in range(1,21)}
barbarianagileanimaldamage = {i: martialDamage[i] + int(animalragedamage[i]/2) for i in range(1,21)}
barbariandragondamage = {i: martialDamage[i] + dragonragedamage[i] for i in range(1,21)}
barbarianfurydamage = {i: martialDamage[i] + furyragedamage[i] for i in range(1,21)}
barbariangiantdamage = {i: martialDamage[i] + giantragedamage[i] for i in range(1,21)}
barbarianspiritdamage = {i: martialDamage[i] + spiritragedamage[i] for i in range(1,21)}

championsmiteevildamage = {i: martialDamage[i] + smiteevildamage[i] for i in range(1,21)}

warpriestDamage = {i: cwSpec[i] for i in range(1,21)}
#warpriestDamage[1] -= 1

warpriestSmiteDamageDice = {i:  sDice[i]*[d8] for i in range(1,21)}



fighterDamage = {i: fwSpec[i] for i in range(1,21)}
fighterrangedDamage = {i: fwSpec[i] for i in range(1,21)}
#fighterd10paDamage = {i: fwSpec[i]+d10pad[i] for i in range(1,21)}
#fighterd12paDamage = {i: fwSpec[i]+d12pad[i] for i in range(1,21)}
#fighterd10bfDamage = {i: fwSpec[i]+d10bfd[i] for i in range(1,21)}
#fighterd12bfDamage = {i: fwSpec[i]+d12bfd[i] for i in range(1,21)}

#
#d12pad = {i: 6.5 for i in range(1,21)}
#for i in d12pad:
#    if i>=10:
#        d12pad[i]+=6.5
#    if i>=18:
#        d12pad[i]+=6.5


class Result:
    def __init__(self, atk, damageDice, staticDamage):
        self.damageDice = damageDice
        self.staticDamage = staticDamage
        
        self.critDamDice = []
        self.critDam = 0
        
        self.persDamDice = []
        self.persDam = 0
        self.critPersDamDice = []
        self.critPersDam = 0
        
        self.splashDam = 0
        self.splashDamDice = []
        
        self.futureAttacksFF = False
        self.nextAttackFF = False
        self.trueStrike = False
        self.nextStrikeBonus = 0
        
        self.addfirsthitdamage = 0
        self.addsecondhitdamage = 0 
        self.addthirdhitdamage = 0 
        self.addeveryhitdamage = 0
        self.addfirsthitdamageDice = []
        self.addsecondhitdamageDice = [] 
        self.addthirdhitdamageDice = []
        self.addeveryhitdamageDice = []
        self.adddamage = 0
        
        self.debuffAttack = 0
        self.debuffDamage = 0
        self.debuffTarget = 0
        
        self.treatWorse = False
        self.ignoreNext = False
        
        self.atk = atk
        self.ishit = False
        self.iscrit = False
        self.doubleDamage = False
        self.halveDamage = False
        self.doublePersOnDouble = True
        
        self.okay = False
        self.good = False
        self.veryGood = False
        
    def setFutureAttacksFF(self):
        self.futureAttacksFF = True
    def setNextAttackFF(self):
        self.nextAttackFF = True
    def setTrueStrike(self):
        self.trueStrike = True
    def setNextStrikeBonus(self, bonus):
        self.nextStrikeBonus = bonus
        
    def setCrit(self):
        self.veryGood = True
        self.ishit = True
        self.iscrit = True
        self.setDoubleDamage()
        
    def setHit(self):
        self.ishit = True
        self.good = True
        
    def setSuccess(self):
        self.good = True
        
    def setCritSuccess(self):
        self.veryGood = True
        
    def setFail(self):
        self.okay = True
        
    def setCritFail(self):
        pass
    
    def setCritSuccessSave(self):
        pass
    
    def setSuccessSave(self):
        self.setHalveDamage()
        self.okay = True
        
    def setFailSave(self):
        self.good = True

    def setCritFailSave(self):
        self.veryGood = True
        self.setDoubleDamage()
        
    def setDoubleDamage(self):
        self.doubleDamage = True
    def setHalveDamage(self):
        self.halveDamage = True
    
    def isHit(self):
        return self.ishit
    def isCrit(self):
        return self.iscrit
        
class AtkSelection:
#         4 types: 'Strike', 'SaveAttack', 'Save', 'Effect'
        def __init__(self, attack, damage):
            
            self.attack = attack
            self.attackBonus = 0
            self.damage = damage
            self.additionalDamage = 0
            self.damageBonus = 0
            
            self.wDice = copy.copy(wDice) # number of dice
            self.damageDie = [1] # 3.5
            self.weaponDamageDice = None
            self.damageDieBonus = None
            self.runeDamageDice = {i: [] for i in range(1,21)}
            self.extraWeaponDice = {i: 0 for i in range(1,21)}
            
            self.persDamage = copy.copy(noneDamage)
            self.persDamageDice = {i: [] for i in range(1,21)}
            
            self.splashDamage = None
            
            self.flatfootedDamage = copy.copy(noneDamage)
            self.flatfootedDamageDice = {i: [] for i in range(1,21)}
            
            self.failureDamage = copy.copy(noneDamage)
            self.failureDamageDice = {i: [] for i in range(1,21)}
            self.certainStrike = False
            self.brutalFinish = False
            
            self.critDamage = copy.copy(noneDamage)
            self.critDamageDice = {i: [] for i in range(1,21)}
            self.critPersDamage = copy.copy(noneDamage)
            self.critPersDamageDice = {i: [] for i in range(1,21)}
            
            self.fatal = False
            self.fatalDie = None
            
            self.isWeapon = False
            self.fixedStrike = False
            self.isSpell = False
            self.spellLevelModifier = 0
            self.minSpellLevel = 1
            self.constantSpellLevel = False
            
            self.critSpecLevel = 21
            self.keenLevel = 21
            self.backswingLevel = 21
        
            self.stickybombLevel = 21
            
            self.ffonCritLevel = 21
            self.ffonSuccessLevel = 21
            self.ffonFailLevel = 21
            
            self.attackBonusOnFail = 0
            
            self.critFailDebuffAttack = 0
            self.failDebuffAttack = 0
            self.successDebuffAttack = 0
            
            self.critFailDebuffDamage = 0
            self.failDebuffDamage = 0
            self.successDebuffDamage = 0
            
            self.critFailDebuffTarget = 0
            self.failDebuffTarget = 0
            self.successDebuffTarget = 0
            
            
            self.minL = 1
            self.maxL = 20
            
        def critSuccessResult(self, level, db):
            return 0
        
        def successResult(self, level, db):
            return 0
        
        def failureResult(self, level, db):
            return 0
        
        def critFailureResult(self, level, db):
            return 0
        
        def addAttackBonuses(self, bonuses):
            for level in self.attack:
                if level in bonuses:
                    self.attack[level] += bonuses[level]
                    
        def addDamageBonuses(self, bonuses):
            for level in self.damage:
                if level in bonuses:
                    self.damage[level] += bonuses[level]
            
        def setWeaponDamageDice(self, weaponDamageDiceName):
            if self.isWeapon and not self.weaponDamageDice:
                self.damageDie = damageDiceConverter[weaponDamageDiceName][0]
                self.damageDieBonus = damageDiceConverter[weaponDamageDiceName][1]
                self.weaponDamageDice = {i: (self.wDice[i]+self.extraWeaponDice[i])*[self.damageDie] for i in range(1,21)}
                
            
        def setCriticalDamageDice(self, weaponCriticalName):
            if self.isWeapon:
                cd = criticalDiceConverter[weaponCriticalName]
                if cd[0]: #if fatal
                    self.fatal = True
                    self.fatalDie = cd[1]
#                    for i in range(1,21):
#                        self.critDamage[i] += cd[1] + wDice[i]*2*(cd[1] - self.damageDie)
                else:
                    if cd[1]:
                        self.critDamageDice = cd[1]
            
        def setCriticalSpecialization(self, csName):
            if self.isWeapon:
                if csName == "other":
                    return
                elif csName == "knife":
                    for i in range(self.critSpecLevel,21):
                        self.critPersDamage[i] += wiBonus[i]
                        self.critPersDamageDice[i] += [d6]
                elif csName == "hammer":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "sword":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "pick":
                    for i in range(self.critSpecLevel,21):
                        self.critDamage[i] += self.wDice[i] * 2
                        
        def setWeaponFeatures(self, featureArray):
            if not self.isWeapon:
                return
            for feature in featureArray:
                if feature[0] == "1d6 Rune":
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d6]
                elif feature[0] == "1d4 Rune":
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d4]
                elif feature[0] == "backswing":
                    self.setBackswing(feature[1])
                elif feature[0] == "keen":
                    self.setKeen(feature[1])
                else:
                    print("feature is ", feature[0])
            return
        
        def setSpellLevel(self, slName):
            if self.isSpell:
                if slName == 'Max':
                    self.spellLevelModifier = 0
                elif slName == '-1':
                    self.spellLevelModifier = -1
                elif slName == '-2':
                    self.spellLevelModifier = -2
                elif slName == '-3':
                    self.spellLevelModifier = -3
                elif slName == '-4':
                    self.spellLevelModifier = -4
                elif slName == '-5':
                    self.spellLevelModifier = -5
                elif slName == '1':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 1
                elif slName == '2':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 2
                elif slName == '3':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 3
                elif slName == '4':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 4
                elif slName == '5':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 5
                elif slName == '6':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 6
                elif slName == '7':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 7
                elif slName == '8':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 8
                elif slName == '9':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 9
                elif slName == '10':
                    self.constantSpellLevel = True
                    self.spellLevelModifier = 10
                
            
        def getAttack(self, level):
            if level>=self.minL and level<=self.maxL:
                if self.isSpell and (sDice[level] + self.spellLevelModifier < self.minSpellLevel
                                     or (self.constantSpellLevel and level < self.spellLevelModifier*2-1)):
                    return None
                if self.isSpell and self.fixedStrike:
                    level = level + self.spellLevelModifier*2
                return self.attack[level] + self.attackBonus
            return None
        
        def getDamageBonus(self, level):
            if level>=self.minL and level<=self.maxL:
                if self.isSpell:
                    level = self.spellLevel(level)
                d = self.damage[level] + self.additionalDamage
                if self.damageDieBonus:
                    d += self.damageDieBonus*self.wDice[level]
                return d
            return 0
        
        def getDamageDice(self, level, crit=False):
            if level>=self.minL and level<=self.maxL:
                if self.isSpell:
                    level = self.spellLevel(level)
                d = []
                if self.weaponDamageDice:
                    for die in self.weaponDamageDice[level]:
                        if self.fatal and crit==True:
                            d += [self.fatalDie]
                        else:
                            d += [die]
                if self.runeDamageDice:
                    for die in self.runeDamageDice[level]:
                        d += [die]
                return d 
            return []
                
        def getCriticalBonusDamage(self, level):
            if self.critDamage:
                if self.isSpell:
                    level = self.spellLevel(level)
                return self.critDamage[level]
            return 0
        
        def getCriticalBonusDamageDice(self, level):
            d = []
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.critDamageDice:
                for die in self.critDamageDice[level]:
                    d += [die]
                
            if self.fatal:
                d += [self.fatalDie]
            return d
        
        def getPersistentDamage(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.persDamage:
                return self.persDamage[level]
            return 0
        
        def getPersistentDamageDice(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.persDamageDice:
                return self.persDamageDice[level]
            return []
        
        def getSplashDamage(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.splashDamage:
                return self.splashDamage[level]
            return 0
        
        def getCriticalPersistentDamage(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.critPersDamage:
                return self.critPersDamage[level]
            return 0
        
        def getCriticalPersistentDamageDice(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.critPersDamageDice:
                return self.critPersDamageDice[level]
            return []
        
        def getFFDamage(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.flatfootedDamage:
                return self.flatfootedDamage[level]
            return 0
        
        def getFFDamageDice(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.flatfootedDamageDice:
                return self.flatfootedDamageDice[level]
            return []
        
        def getFailureDamage(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            if self.failureDamage:
                return self.failureDamage[level]
            return 0
        
        def getFailureDamageDice(self, level):
            if self.isSpell:
                    level = self.spellLevel(level)
            failureDice = []
            if self.failureDamageDice:
                failureDice += self.failureDamageDice[level]
            if self.brutalFinish:
                failureDice += self.extraWeaponDice[level]*[self.damageDie]
            return failureDice

        
        def getKeen(self, level):
            if level >= self.keenLevel:
                return True
            return False
        def getBackswing(self, level):
            if level >= self.backswingLevel:
                return True
            return False
        
        def ffonCrit(self, level):
            if level >= self.ffonCritLevel:
                return True
            return False
        def ffonSuccess(self, level):
            if level >= self.ffonSuccessLevel:
                return True
            return False
        def ffonFail(self, level):
            if level >= self.ffonFailLevel:
                return True
            return False
        
        def modifyAB(self, ab):
            self.attackBonus = ab
        def modifyDB(self, db):
            self.damageBonus = db
        def modifyAD(self, ad):
            self.additionalDamage = ad
            
        def setKeen(self, level):
            self.keenLevel = min(level, self.keenLevel)
        def setBackswing(self, level):
            self.backswingLevel = min(level, self.backswingLevel)
            
        def setFFonCrit(self, level):
            self.ffonCritLevel = min(level,self.ffonCritLevel)
        def setFFonSuccess(self, level):
            self.ffonSuccessLevel = min(level,self.ffonSuccessLevel)
        def setFFonFail(self, level):
            self.ffonFailLevel = min(level,self.ffonFailLevel)
            
        def setLevels(self, minl, maxl):
            self.minL = max(minl, self.minL)
            self.maxL = min(maxl, self.maxL)
        
        def spellLevel(self, level):
            if self.isSpell:
                if self.constantSpellLevel:
                    level = self.spellLevelModifier*2
                else:
                    level = level + self.spellLevelModifier*2
            return level

class Strike(AtkSelection):
    def __init__(self, attack, damage, isWeapon=True, csLevel=21):
        super().__init__(attack, damage)
        self.critSpecLevel = csLevel
        self.isWeapon = isWeapon
        
    def critSuccessResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += self.damageBonus
        staticDamage += context.getExtraDamage()
        
        damageDice = self.getDamageDice(level, crit=True)
        
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)       

        
        r = Result(self, damageDice, staticDamage)
        r.setCrit()
        
        r.critDam = self.getCriticalBonusDamage(level)
        r.critDamDice = self.getCriticalBonusDamageDice(level)
        
        r.persDam = self.getPersistentDamage(level)
        r.persDamDice = self.getPersistentDamageDice(level)
        r.critPersDam = self.getCriticalPersistentDamage(level)
        r.critPersDamDice = self.getCriticalPersistentDamageDice(level)
    
        r.splashDam = self.getSplashDamage(level)
        if level >= self.stickybombLevel:
#            print("adding ",r.persDam,r.splashDam)
            r.persDam += r.splashDam
        
        if self.ffonCrit(level):
            r.setFutureAttacksFF()
            
        return r
        
    def successResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += self.damageBonus
        staticDamage += context.getExtraDamage()
        
        damageDice = self.getDamageDice(level)
        
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)       

        
        r = Result(self, damageDice, staticDamage)
        r.setHit()
        
        r.persDam = self.getPersistentDamage(level)
        r.persDamDice = self.getPersistentDamageDice(level)
    
        r.splashDam = self.getSplashDamage(level)
        if level >= self.stickybombLevel:
#            print("adding ",r.persDam,r.splashDam)
            r.persDam += r.splashDam
            
        if self.ffonSuccess(level):
            r.setFutureAttacksFF()
            
        return r
        
    def failureResult(self, level, context):
        staticDamage = self.getFailureDamage(level)
        if self.certainStrike:
            staticDamage += self.getDamageBonus(level)
            if context.flatfooted:
                staticDamage += self.getFFDamage(level)
            staticDamage += self.damageBonus
                
        damageDice = self.getFailureDamageDice(level)
        
        if damageDice != [] or staticDamage != 0:
            staticDamage += context.getDamageBonus()    
            # only apply weakness/resistance for brutal finish
        

        r = Result(self, damageDice, staticDamage)
        r.setFail()
        
        if(self.getBackswing(level)):
            r.setNextStrikeBonus(self.attackBonusOnFail+1)
        else:
            r.setNextStrikeBonus(self.attackBonusOnFail)
 
        r.splashDam = self.getSplashDamage(level)
        
        if self.ffonFail(level):
            r.setFutureAttacksFF()
            
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritFail()
        return r

class MeleeStrike(Strike):
    def __init__(self, attack, damage, csLevel=21):
        super().__init__(attack, damage, csLevel=csLevel)
        self.prim = True
        self.sec = True
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addDamageBonuses(scoreValues)
        return True
        
class RangedStrike(Strike):
    def __init__(self, attack, damage, csLevel=21):
        super().__init__(attack, damage, csLevel=csLevel)
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
        
class PropulsiveStrike(Strike):
    def __init__(self, attack, damage, csLevel=21):
        super().__init__(attack, damage, csLevel=csLevel)
        self.prim = True
        self.sec = True
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        damage = {i: int(scoreValues[i]/2) for i in scoreValues}
        self.addDamageBonuses(damage)
        return True

#class FinesseThrownStrike(Strike):
#    def __init__(self, attack, damage):
#        super().__init__(attack, damage)
        
class BombStrike(Strike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage, isWeapon=False)
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
        
class CantripStrike(Strike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage, isWeapon=False)
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        self.addDamageBonuses(scoreValues) 
        #acid splash should be different
        return True
    def setSecondaryAS(self, score):
        return False
        
        
class SpecialStrike(Strike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage, isWeapon=False)
        
class FixedStrike(Strike):
    # don't use ability score
    def __init__(self, attack, damage):
        super().__init__(attack, damage, isWeapon=False) 
        self.fixedStrike = True
        self.prim = False
        self.sec = False
        
    def setPrimaryAS(self, score):
        return False
    def setSecondaryAS(self, score):
        return False
    
class TransformStrike(Strike):
    # have a min to hit bonus
    def __init__(self, attack, damage):
        super().__init__(attack, damage, isWeapon=False)
        self.minAttack = None
        self.isSpell = True
        self.weaponDamageDice = {i: [] for i in range(1,21)}
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
    
    def getAttack(self, level):
        oldA = super().getAttack(level)
        newA = 0
        if not oldA is None:
            if self.isSpell:
                    level = level + self.spellLevelModifier*2
            if self.minAttack and level in self.minAttack:
                newA = self.minAttack[level]+self.attackBonus
                return max(oldA,newA)
        return None
    
class SpellStrike(RangedStrike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.isSpell = True
        self.isWeapon = False
        
    def critSuccessResult(self, level, context):
        r = super().critSuccessResult(level, context)
        r.doublePersOnDouble = False
        return r
    
class HPSpellStrike(RangedStrike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.isSpell = True
        self.isWeapon = False
        
    def critSuccessResult(self, level, context):
        r = super().critSuccessResult(level, context)
        r.doubleDamage = False
        return r
    
class SpellStrikeFilter(RangedStrike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.isWeapon = False
        
    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCrit()
        r.treatWorse = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setHit()
        return r
        
    def failureResult(self, level, context):
        r = Result(self, [], 0)
        r.setFail()
        r.ignoreNext = True
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritFail()
        r.ignoreNext = True
        return r
        
        
class SaveAttack(AtkSelection):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
    

    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritSuccess()
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setSuccess()
        return r
        
    def failureResult(self, level, context):
        r = Result(self, [], 0)
        r.setFail()
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritFail()
        return r

class Feint(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        
    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritSuccess()
        
        r.futureAttacksFF = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setSuccess()
        
        r.nextAttackFF = True
        return r
        
class ScoundrelFeint(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
    
    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritSuccess()
        
        r.futureAttacksFF = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setSuccess()
        
        r.futureAttacksFF = True
        return r
    
class Demoralize(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        
    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritSuccess()
        
        r.debuffTarget = 2
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setSuccess()
        
        r.debuffTarget = 1
        return r

class ScareToDeath(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        
    def critSuccessResult(self, level, context):
        r = Result(self, [], 0)
        r.setCritSuccess()
        
        r.debuffTarget = 3
        return r
    
    def successResult(self, level, context):
        r = Result(self, [], 0)
        r.setSuccess()
        
        r.debuffTarget = 2
        return r
    
    def failureResult(self, level, context):
        r = Result(self, [], 0)
        r.setFail()
        
        r.debuffTarget = 1
        return r
        
class Save(AtkSelection):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
        self.prim = True
        self.sec = False
        self.isSpell = True
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
        
    def getDC(self, level):
        return self.getAttack(level)
    
    def critSuccessResult(self, level, context):

        r = Result(self, [], 0)
        r.setCritSuccessSave()
        return r
        
    def successResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        # errorrsdfdafsdfsda
        damageDice = self.getDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.setSuccessSave()
        r.debuffAttack = self.successDebuffAttack
        r.debuffDamage = self.successDebuffDamage
        r.debuffTarget = self.successDebuffTarget
        
        return r
        
    def failureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.setFailSave()
        r.debuffAttack = self.failDebuffAttack
        r.debuffDamage = self.failDebuffDamage
        r.debuffTarget = self.failDebuffTarget
        
        r.persDam = self.getPersistentDamage(level)
        r.persDamDice = self.getPersistentDamageDice(level)
        
        return r
        
    def critFailureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.setCritFailSave()
        r.debuffAttack = self.critFailDebuffAttack
        r.debuffDamage = self.critFailDebuffDamage
        r.debuffTarget = self.critFailDebuffTarget
        
        r.persDam = self.getPersistentDamage(level)
        r.persDamDice = self.getPersistentDamageDice(level)
        
        return r
    
class CantripSave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
        self.prim = True
        self.sec = False
        self.isSpell = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        self.addDamageBonuses(scoreValues) 
        return True
    def setSecondaryAS(self, score):
        return False
    
class PhantomPainSave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
    
    def critSuccessResult(self, level, context):

        r = Result(self, [], 0)
        r.setCritSuccessSave()
        return r
        
    def successResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        # errorrsdfdafsdfsda
        damageDice = self.getDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.setSuccessSave()
        r.halveDamage = False
        return r
        
    def failureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)
        
        r = Result(self, damageDice, staticDamage)
        r.persDamDice = self.getPersistentDamageDice(level)
        r.setFailSave()
        r.debuffAttack = self.failDebuffAttack
        r.debuffTarget = self.failDebuffTarget
        
        return r
        
    def critFailureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.persDamDice = self.getPersistentDamageDice(level)
        r.setCritFailSave()
        r.doubleDamage = False
        r.debuffAttack = self.critFailDebuffAttack
        r.debuffTarget = self.critFailDebuffTarget
       
        return r
    
class PKSave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
    
    def critSuccessResult(self, level, context):

        r = Result(self, [], 0)
        r.setCritSuccessSave()
        return r
        
    def successResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        # errorrsdfdafsdfsda
        damageDice = self.getFailureDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.setSuccessSave()
        r.halveDamage = False
        r.debuffAttack = self.successDebuffAttack
        r.debuffTarget = self.successDebuffTarget
        return r
        
    def failureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)
        
        r = Result(self, damageDice, staticDamage)
        r.setFailSave()
        r.debuffAttack = self.failDebuffAttack
        r.debuffTarget = self.failDebuffTarget
        return r
        
    def critFailureResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getExtraDamage()
        staticDamage += self.damageBonus
        
        damageDice = self.getCriticalBonusDamageDice(level)

        r = Result(self, damageDice, staticDamage)
        r.persDamDice = self.getPersistentDamageDice(level)
        r.setCritFailSave()
        r.doubleDamage = False
        r.debuffAttack = self.critFailDebuffAttack
        r.debuffTarget = self.critFailDebuffTarget
        return r
    
class AttackSave(AtkSelection):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
        self.prim = True
        self.sec = False
        self.isSpell = True
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
    
    def getDC(self, level):
        return self.getAttack(level)+10
    
    
class Effect(AtkSelection):
    def __init__(self, damage):
        super().__init__(casterAttackBonus, damage)
        self.flatfootNextStrike = False
        self.flatfoot = False
        self.trueStrike = False
        
        self.addfirsthitdamage = None
        self.addsecondhitdamage = None 
        self.addthirdhitdamage = None
        self.addeveryhitdamage = None
        
        self.addfirsthitdamageDice = None
        self.addsecondhitdamageDice = None 
        self.addthirdhitdamageDice = None
        self.addeveryhitdamageDice = None
        
        self.addDamage = None
        
        self.prim = False
        self.sec = False
        
    def setPrimaryAS(self, score):
        return False
    def setSecondaryAS(self, score):
        return False
        
    def effectResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        staticDamage += context.getDamageBonus()
        staticDamage += self.damageBonus
        
        damageDice = self.getDamageDice(level)

        r = Result(self,damageDice,staticDamage)
        
        if self.flatfoot:
            r.futureAttacksFF = True
        elif self.flatfootNextStrike:
            r.nextAttackFF = True
        
        r.trueStrike = self.trueStrike
        
        if self.addfirsthitdamage:
            r.addfirsthitdamage = self.addfirsthitdamage[level]
        if self.addsecondhitdamage:
            r.addsecondhitdamage = self.addsecondhitdamage[level]
        if self.addthirdhitdamage:
            r.addthirdhitdamage = self.addthirdhitdamage[level]
        if self.addeveryhitdamage:
            r.addeveryhitdamage = self.addeveryhitdamage[level]
            
        if self.addfirsthitdamageDice:
            r.addfirsthitdamageDice = self.addfirsthitdamageDice[level]
        if self.addsecondhitdamageDice:
            r.addsecondhitdamageDice = self.addsecondhitdamageDice[level]
        if self.addthirdhitdamageDice:
            r.addthirdhitdamageDice = self.addthirdhitdamageDice[level]
        if self.addeveryhitdamageDice:
            r.addeveryhitdamageDice = self.addeveryhitdamageDice[level]
                    
        if self.addDamage:
            if self.isSpell:
                level = self.spellLevel(level)
            #print("adding ",self.addDamage[level])
            r.adddamage = self.addDamage[level]
            
        return r
    
        
class CombinedAttack:
    PDWeight = 0
    def __init__(self, attackList, function=min):
        self.function=function
        self.attackList=attackList
        # what if attackList has a combined attack?
        #also update create Traces
        
    def choose(self, d, pd, newd, newpd, h, c, nh, nc):
        totaldamage = d + pd*CombinedAttack.PDWeight
        newtotal = newd + newpd**CombinedAttack.PDWeight
        if self.function(totaldamage,newtotal) == totaldamage:
            return d, pd, h, c
        elif self.function(totaldamage,newtotal) == newtotal:
            return newd, newpd, nh, nc
        elif self.function(totaldamage,newtotal) == totaldamage + newtotal:
            return d+newd, pd+newpd, h+nh, c+nc
        elif self.function(totaldamage,newtotal) == totaldamage - newtotal:
            return d-newd, pd-newpd, h-nh, c-nc
        else:
            print(d, pd, newd, newpd)
        
    def contains(self, level):
        for sr in self.attackList:
            if type(sr) is CombinedAttack:
                srhas = sr.contains(level)
            else:
                srhas = True
                for st in sr:
                    if not st.getAttack(level):
                        srhas = False
            if srhas: return True
        return False
    
    def validFor(self, level):
        #returns attack lists that work on specified level
        validAttackList = []
        for sr in self.attackList:
            if type(sr) is CombinedAttack:
                if sr.contains(level):
                    validAttackList.append(sr)
            else:
                srhas = True
                for st in sr:
                    if not st.getAttack(level):
                        srhas = False
                if srhas: validAttackList.append(sr)
        return validAttackList
        
    
alchemistStrike = MeleeStrike(warpriestAttackBonus, alchemistDamage)
alchemistRangedStrike = RangedStrike(warpriestAttackBonus, alchemistRangedDamage)

alchemistacids = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistacids.isWeapon = False
alchemistacids.weaponDamage = acidFlaskDamage
alchemistacids.persDamageDice = acidFlaskPersDamage
#alchemistacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistacids.splashDamage = bombSplashDamage

alchemistbacids = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbacids.isWeapon = False
alchemistbacids.weaponDamage = acidFlaskDamage
alchemistbacids.persDamageDice = acidFlaskPersDamage
#alchemistbacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbacids.splashDamage = bomberSplashDamage

alchemistbsacids = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbsacids.isWeapon = False
alchemistbsacids.weaponDamage = acidFlaskDamage
alchemistbsacids.persDamageDice = acidFlaskPersDamage
#alchemistbsacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbsacids.splashDamage = bomberSplashDamage
alchemistbsacids.stickybombLevel = 8

alchemistpacids = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistpacids.isWeapon = False
alchemistpacids.weaponDamage = pacidFlaskDamage
alchemistpacids.persDamageDice = pacidFlaskPersDamage
#alchemistpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistpacids.splashDamage = pbombSplashDamage

alchemistbpacids = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpacids.isWeapon = False
alchemistbpacids.weaponDamage = pacidFlaskDamage
alchemistbpacids.persDamageDice = pacidFlaskPersDamage
#alchemistbpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpacids.splashDamage = pbomberSplashDamage

alchemistbpsacids = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpsacids.isWeapon = False
alchemistbpsacids.weaponDamage = pacidFlaskDamage
alchemistbpsacids.persDamageDice = pacidFlaskPersDamage
#alchemistbpsacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpsacids.splashDamage = pbomberSplashDamage
alchemistbpsacids.stickybombLevel = 8

alchemistfires = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistfires.isWeapon = False
alchemistfires.weaponDamageDice = alchemistsFireDamage
alchemistfires.persDamage = alchemistsFirePersDamage
#alchemistfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistfires.splashDamage = bombSplashDamage

alchemistbfires = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbfires.isWeapon = False
alchemistbfires.weaponDamageDice = alchemistsFireDamage
alchemistbfires.persDamage = alchemistsFirePersDamage
#alchemistbfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbfires.splashDamage = bomberSplashDamage

alchemistbsfires = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbsfires.isWeapon = False
alchemistbsfires.weaponDamageDice = alchemistsFireDamage
alchemistbsfires.persDamage = alchemistsFirePersDamage
#alchemistbsfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbsfires.splashDamage = bomberSplashDamage
alchemistbsfires.stickybombLevel = 8

alchemistpfires = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfires.isWeapon = False
alchemistpfires.weaponDamageDice = palchemistsFireDamage
alchemistpfires.persDamage = palchemistsFirePersDamage
#alchemistpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistpfires.splashDamage = pbombSplashDamage

alchemistbpfires = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfires.isWeapon = False
alchemistbpfires.weaponDamageDice = palchemistsFireDamage
alchemistbpfires.persDamage = palchemistsFirePersDamage
#alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpfires.splashDamage = pbomberSplashDamage

alchemistbpsfires = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpsfires.isWeapon = False
alchemistbpsfires.weaponDamageDice = palchemistsFireDamage
alchemistbpsfires.persDamage = palchemistsFirePersDamage
#alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpsfires.splashDamage = pbomberSplashDamage
alchemistbpsfires.stickybombLevel = 8

alchemistfrosts = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistfrosts.isWeapon = False
alchemistfrosts.weaponDamageDice = blfvDamage
alchemistfrosts.splashDamage = bombSplashDamage

alchemistbfrosts = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbfrosts.isWeapon = False
alchemistbfrosts.weaponDamageDice = blfvDamage
alchemistbfrosts.splashDamage = bomberSplashDamage

alchemistbsfrosts = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbsfrosts.isWeapon = False
alchemistbsfrosts.weaponDamageDice = blfvDamage
alchemistbsfrosts.splashDamage = bomberSplashDamage
alchemistbsfrosts.stickybombLevel = 8

alchemistpfrosts = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfrosts.isWeapon = False
alchemistpfrosts.weaponDamageDice = pblfvDamage
alchemistpfrosts.splashDamage = pbombSplashDamage

alchemistbpfrosts = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfrosts.isWeapon = False
alchemistbpfrosts.weaponDamageDiceDice = pblfvDamage
alchemistbpfrosts.splashDamage = pbomberSplashDamage

alchemistbpsfrosts = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpsfrosts.isWeapon = False
alchemistbpsfrosts.weaponDamageDiceDice = pblfvDamage
alchemistbpsfrosts.splashDamage = pbomberSplashDamage
alchemistbpsfrosts.stickybombLevel = 8

alchemistlightnings = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistlightnings.isWeapon = False
alchemistlightnings.setFFonCrit(1)
alchemistlightnings.setFFonSuccess(1)
alchemistlightnings.weaponDamageDice = blfvDamage
alchemistlightnings.splashDamage = bombSplashDamage

alchemistblightnings = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistblightnings.isWeapon = False
alchemistblightnings.setFFonCrit(1)
alchemistblightnings.setFFonSuccess(1)
alchemistblightnings.weaponDamageDice = blfvDamage
alchemistblightnings.splashDamage = bomberSplashDamage

alchemistbslightnings = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbslightnings.isWeapon = False
alchemistbslightnings.setFFonCrit(1)
alchemistbslightnings.setFFonSuccess(1)
alchemistbslightnings.weaponDamageDice = blfvDamage
alchemistbslightnings.splashDamage = bomberSplashDamage
alchemistbslightnings.stickybombLevel = 8

alchemistplightnings = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistplightnings.isWeapon = False
alchemistplightnings.setFFonCrit(1)
alchemistplightnings.setFFonSuccess(1)
alchemistplightnings.weaponDamageDice = pblfvDamage
alchemistplightnings.splashDamage = pbombSplashDamage

alchemistbplightnings = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbplightnings.isWeapon = False
alchemistbplightnings.setFFonCrit(1)
alchemistbplightnings.setFFonSuccess(1)
alchemistbplightnings.weaponDamageDice = pblfvDamage
alchemistbplightnings.splashDamage = pbomberSplashDamage

alchemistbpslightnings = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpslightnings.isWeapon = False
alchemistbpslightnings.setFFonCrit(1)
alchemistbpslightnings.setFFonSuccess(1)
alchemistbpslightnings.weaponDamageDice = pblfvDamage
alchemistbpslightnings.splashDamage = pbomberSplashDamage
alchemistbpslightnings.stickybombLevel = 8

alchemistbestialClawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistbestialClawStrike.weaponDamageDice = bestialClawDamageDice

alchemistbestialJawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistbestialJawStrike.weaponDamageDice = bestialJawDamageDice

alchemistferalClawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistferalClawStrike.weaponDamageDice = feralClawDamageDice

alchemistferalJawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistferalJawStrike.weaponDamageDice = feralJawDamageDice

alchemistAttackSwitcher = {'Alchemist Melee Strike': [alchemistStrike],
                    'Alchemist Ranged Strike': [alchemistRangedStrike],
                    'Alchemist Bestial Claw': [alchemistbestialClawStrike],
                    'Alchemist Bestial Jaw': [alchemistbestialJawStrike],
                    'Alchemist Feral Claw': [alchemistferalClawStrike],
                    'Alchemist Feral Jaw': [alchemistferalJawStrike],
                    'Alchemist Acid Flask': [alchemistacids],
                    'Alchemist Bomber Acid': [alchemistbacids],
                    'Alchemist Sticky Acid': [alchemistbsacids],
                    'Alchemist Perpetual Acid': [alchemistpacids],
                    'Alchemist Bomber Perpetual Acid': [alchemistbpacids],
                    'Alchemist Sticky Perpetual Acid': [alchemistbpsacids],
                    'Alchemist Fire': [alchemistfires],
                    'Alchemist Bomber Fire': [alchemistbfires],
                    'Alchemist Sticky Fire': [alchemistbsfires],
                    'Alchemist Perpetual Fire': [alchemistpfires],
                    'Alchemist Bomber Perpetual Fire': [alchemistbpfires],
                    'Alchemist Sticky Perpetual Fire': [alchemistbpsfires],
                    'Alchemist Bottled Lightning': [alchemistlightnings],
                    'Alchemist Bomber Lightning': [alchemistblightnings],
                    'Alchemist Sticky Lightning': [alchemistbslightnings],
                    'Alchemist Perpetual Lightning': [alchemistplightnings],
                    'Alchemist Bomber Perpetual Lightning': [alchemistbplightnings],
                    'Alchemist Sticky Perpetual Lightning': [alchemistbpslightnings],
                    'Alchemist Frost Vial': [alchemistfrosts],
                    'Alchemist Bomber Frost': [alchemistbfrosts],
                    'Alchemist Sticky Frost': [alchemistbsfrosts],
                    'Alchemist Perpetual Frost': [alchemistpfrosts],
                    'Alchemist Bomber Perpetual Frost': [alchemistbpfrosts],
                    'Alchemist Sticky Perpetual Frost': [alchemistbpsfrosts]}

# Barbarian
# rage, instinct, devastator


barbariananimaljaws = MeleeStrike(martialAttackBonus, barbariananimaldamage, csLevel=5)
barbariananimaljaws.weaponDamageDice = animalJawDamageDice
barbariananimalclaws = MeleeStrike(martialAttackBonus, barbarianagileanimaldamage, csLevel=5)
barbariananimalclaws.weaponDamageDice = animalClawDamageDice

barbariandragonstrike = MeleeStrike(martialAttackBonus, barbariandragondamage, csLevel=5)

barbarianfurystrike = MeleeStrike(martialAttackBonus, barbarianfurydamage, csLevel=5)

barbariangiantstrike = MeleeStrike(martialAttackBonus, barbariangiantdamage, csLevel=5)

barbarianspiritstrike = MeleeStrike(martialAttackBonus, barbarianspiritdamage, csLevel=5)

barbarianAttackSwitcher = {'Barbarian Animal Claw': [barbariananimalclaws],
                    'Barbarian Animal Jaw': [barbariananimaljaws],
                    'Barbarian Dragon Strike': [barbariandragonstrike],
                    'Barbarian Fury Strike': [barbarianfurystrike],
                    'Barbarian Giant Strike': [barbariangiantstrike],
                    'Barbarian Spirit Strike': [barbarianspiritstrike]}


casterstrike = MeleeStrike(casterAttackBonus, strCasterDamage, csLevel=11)
casterrangedstrike = RangedStrike(casterAttackBonus, rangedCasterDamage, csLevel=11)
casterpropulsive = PropulsiveStrike(casterAttackBonus, rangedCasterDamage, csLevel=11)

martialstrike = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
martialrangedstrike = RangedStrike(martialAttackBonus, martialRangedDamage, csLevel=5)
martialpropulsive = PropulsiveStrike(martialAttackBonus, martialRangedDamage, csLevel=5)

championsmiteevil = MeleeStrike(martialAttackBonus, championsmiteevildamage, csLevel=3)

warprieststrike = MeleeStrike(warpriestAttackBonus, warpriestDamage, csLevel=7)
#warpriestsmite = MeleeStrike(warpriestAttackBonus, warpriestSmiteDamage, csLevel=7)
warpriestsmite = MeleeStrike(warpriestAttackBonus, warpriestDamage, csLevel=7)
warpriestsmite.runeDamageDice = warpriestSmiteDamageDice

roguestrike = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
roguestrike.flatfootedDamageDice = sneakattackdamage

rangerprecedge = Effect(noneDamage)
rangerprecedge.addfirsthitdamageDice = rangerprecedgedamage1
rangerprecedge.addsecondhitdamageDice = rangerprecedgedamage2
rangerprecedge.addthirdhitdamageDice = rangerprecedgedamage3

rangerbearsupport = Effect(noneDamage)
rangerbearsupport.addeveryhitdamageDice = rangerbearsupportdamage

bespellweapon = Effect(noneDamage)
bespellweapon.addeveryhitdamageDice = {i: [d6] for i in range(1,21)}

druidanimalform = TransformStrike(wildshapeAttackBonus, animalFormDamage)
druidanimalform.minAttack = animalFormAttack
druidanimalformR = TransformStrike(wildshapeAttackBonus, animalFormDamage)
druidanimalformR.minAttack = animalFormAttack
druidanimalformR.isWeapon = True

druidinsectform = TransformStrike(wildshapeAttackBonus, insectFormDamage)
druidinsectform.minAttack = insectFormAttack
druidinsectformR = TransformStrike(wildshapeAttackBonus, insectFormDamage)
druidinsectformR.minAttack = insectFormAttack
druidinsectformR.isWeapon = True

druiddinoform = TransformStrike(wildshapeAttackBonus, dinoFormDamage)
druiddinoform.minAttack = dinoFormAttack
druiddinoformR = TransformStrike(wildshapeAttackBonus, dinoFormDamage)
druiddinoformR.minAttack = dinoFormAttack
druiddinoformR.isWeapon = True

druidaerialform = TransformStrike(wildshapeAttackBonus, aerialFormDamage)
druidaerialform.minAttack = aerialFormAttack
druidaerialformR = TransformStrike(wildshapeAttackBonus, aerialFormDamage)
druidaerialformR.minAttack = aerialFormAttack
druidaerialformR.isWeapon = True

druidelemform = TransformStrike(wildshapeAttackBonus, elemFormDamage)
druidelemform.minAttack = elemFormAttack
druidelemformR = TransformStrike(wildshapeAttackBonus, elemFormDamage)
druidelemformR.minAttack = elemFormAttack
druidelemformR.isWeapon = True

druidplantform = TransformStrike(wildshapeAttackBonus, plantFormDamage)
druidplantform.minAttack = plantFormAttack
druidplantformR = TransformStrike(wildshapeAttackBonus, plantFormDamage)
druidplantformR.minAttack = plantFormAttack
druidplantformR.isWeapon = True

druiddragonform = TransformStrike(wildshapeAttackBonus, dragonFormDamage)
druiddragonform.minAttack = dragonFormAttack
druiddragonformR = TransformStrike(wildshapeAttackBonus, dragonFormDamage)
druiddragonformR.minAttack = dragonFormAttack
druiddragonformR.isWeapon = True

druidmonform = TransformStrike(wildshapeAttackBonus, monFormDamage)
druidmonform.minAttack = monFormAttack
druidmonformR = TransformStrike(wildshapeAttackBonus, monFormDamage)
druidmonformR.minAttack = monFormAttack
druidmonformR.isWeapon = True

druidnatform = TransformStrike(wildshapeAttackBonus, natFormDamage)
druidnatform.minAttack = natFormAttack
druidnatformR = TransformStrike(wildshapeAttackBonus, natFormDamage)
druidnatformR.minAttack = natFormAttack
druidnatformR.isWeapon = True

otherAttackSwitcher = {'Caster Strike': [casterstrike],
                       'Caster Ranged Strike': [casterrangedstrike],
                       'Caster Propulsive': [casterpropulsive],
                       'Martial Strike': [martialstrike],
                       'Martial Ranged Strike': [martialrangedstrike],
                       'Martial Propulsive': [martialpropulsive],
                       'Champion Smite Evil': [championsmiteevil],
                       'Warpriest Strike': [warprieststrike],
                       'Warpriest Smite': [warpriestsmite],
                       'Rogue Strike': [roguestrike],
                       'Ranger Precision Edge': [rangerprecedge],
                       'Ranger Bear Support': [rangerbearsupport],
                       'Bespell Weapon': [bespellweapon],
                       'Wildshape Animal': [druidanimalform],
                'Wildshape Insect': [druidinsectform],
                'Wildshape Dino': [druiddinoform],
                'Wildshape Aerial': [druidaerialform],
                'Wildshape Elemental': [druidelemform],
                'Wildshape Plant': [druidplantform],
                'Wildshape Dragon': [druiddragonform],
                'Wildshape Monster': [druidmonform],
                'Wildshape Incarnate': [druidnatform],
                'Wildshape AnimalR': [druidanimalformR],
                'Wildshape InsectR': [druidinsectformR],
                'Wildshape DinoR': [druiddinoformR],
                'Wildshape AerialR': [druidaerialformR],
                'Wildshape ElementalR': [druidelemformR],
                'Wildshape PlantR': [druidplantformR],
                'Wildshape DragonR': [druiddragonformR],
                'Wildshape MonsterR': [druidmonformR],
                'Wildshape IncarnateR': [druidnatformR]
                       }

cantripAS = CantripStrike(cantripAttackBonus, noneDamage)
cantripAS.weaponDamageDice = cantripASDamageDice
cantripAS.critPersDamage = cantripASPDamage

cantripEA = CantripSave(spellDC, noneDamage)
cantripEA.weaponDamageDice = cantripRFDamageDice

cantripD = CantripSave(spellDC, noneDamage)
cantripD.weaponDamageDice = cantripDDamageDice

cantripDL = CantripStrike(cantripAttackBonus, noneDamage)
cantripDL.weaponDamageDice = cantripRFDamageDice

cantripPF = CantripStrike(cantripAttackBonus, noneDamage)
cantripPF.weaponDamageDice = cantripRFDamageDice
cantripPF.critPersDamageDice = cantripPFPDamageDice

cantripTP = CantripStrike(cantripAttackBonus, noneDamage)
cantripTP.weaponDamageDice = cantripTPDamageDice

cantripRF = CantripStrike(cantripAttackBonus, noneDamage)
cantripRF.weaponDamageDice = cantripRFDamageDice

cantripAttackSwitcher = {'Acid Splash': [cantripAS],
                  'Electric Arc': [cantripEA],
                  'Daze': [cantripD],
                  'Divine Lance': [cantripDL],
                  'Produce Flame': [cantripPF],
                  'Ray of Frost': [cantripRF],
                  'Telekinetic Projectile': [cantripTP]
                  }
# fighter, double slice, exacting strike, power attack, snagging strike
# combat grab
        
fighterstrike = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)

fighterexactingstrike = MeleeStrike(fighterAttackBonus, fighterDamage, csLevel=5)
fighterexactingstrike.attackBonusOnFail = 5

fightersnaggingstrike = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
fightersnaggingstrike.setFFonCrit(1)
fightersnaggingstrike.setFFonSuccess(1)

fightercertainstrike = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
fightercertainstrike.certainStrike = True

fighterpowerattack = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
for i in range(1,21):
    fighterpowerattack.extraWeaponDice[i] += 1
    if i >= 10:
        fighterpowerattack.extraWeaponDice[i] += 1
    if i >= 18:
        fighterpowerattack.extraWeaponDice[i] += 1
#fighterd10powerattack = MeleeStrike(fighterAttackBonus,fighterd10paDamage, csLevel=5)
#fighterd12powerattack = MeleeStrike(fighterAttackBonus,fighterd12paDamage, csLevel=5)

fighterbrutishshove = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterbrutishshove.setFFonCrit(1)
fighterbrutishshove.setFFonSuccess(1)
fighterbrutishshove.setFFonFail(1)

fighterknockdown = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterknockdown.setFFonCrit(1)
fighterknockdown.setFFonSuccess(1)

fighterdbrutalfinish = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterdbrutalfinish.brutalFinish = True
for i in range(1,21):
    if i >= 12:
        fighterdbrutalfinish.extraWeaponDice[i] += 1
    if i >= 18:
        fighterdbrutalfinish.extraWeaponDice[i] += 1
#fighterd12brutalfinish = MeleeStrike(fighterAttackBonus,fighterDamage, csLevel=5)
#fighterd12brutalfinish.failureDamage = d12bfd

fighterrangedstrike = RangedStrike(fighterAttackBonus, fighterrangedDamage, csLevel=5)

fighterpropulsive = PropulsiveStrike(fighterAttackBonus, fighterrangedDamage, csLevel=5)

fighterpropulsivecs = PropulsiveStrike(fighterAttackBonus, fighterrangedDamage, csLevel=5)
fighterpropulsivecs.certainStrike = True

fighterpropulsivees = PropulsiveStrike(fighterAttackBonus, fighterrangedDamage, csLevel=5)
fighterpropulsivees.attackBonusOnFail = 5

fighterAttackSwitcher = {'Fighter Melee Strike': 
                  [fighterstrike], 
                  'Fighter Exacting Strike':
                  [fighterexactingstrike],
                  'Fighter Snagging Strike': 
                  [fightersnaggingstrike], 
                  'Fighter Certain Strike': 
                  [fightercertainstrike],
                  'Fighter Power Attack': 
                  [fighterpowerattack],  
                  'Fighter Brutish Shove': 
                  [fighterbrutishshove], 
                  'Fighter Knockdown': 
                  [fighterknockdown], 
                  'Fighter Brutal Finish': 
                  [fighterdbrutalfinish], 
                  'Fighter Ranged Strike':
                  [fighterrangedstrike],
                  'Fighter Propulsive':
                  [fighterpropulsive],
                  'Fighter Propulsive es':
                  [fighterpropulsivees],
                  'Fighter Propulsive cs':
                  [fighterpropulsivecs]
                  }
    
    
druidwolf = FixedStrike(druidwolfattack, druidwolfdamage)
rangerwolf = FixedStrike(rangerwolfattack, rangerwolfdamage)
druidbear = FixedStrike(druidbearattack, druidbeardamage)
rangerbear = FixedStrike(rangerbearattack, rangerbeardamage)
  
animalcompanionAttackSwitcher = {'Druid Bear': [druidbear],
                          'Druid Wolf': [druidwolf],
                          'Ranger Bear': [rangerbear],
                          'Ranger Wolf': [rangerwolf]}

summonanimal = FixedStrike(sumAniAttack, sumAniDamage)
summonanimal.isSpell = True
summondragon = FixedStrike(sumDraAttack, sumDraDamage)
summondragon.isSpell = True
summondragon.minSpellLevel = 5
summondragon.setLevels(9,20)

summonAttackSwitcher = {'Summon Animal': [summonanimal],
                        'Summon Dragon': [summondragon]}
 
attackExtreme = creatureData['Attack']['Extreme']
attackHigh = creatureData['Attack']['High']
attackModerate = creatureData['Attack']['Moderate']
attackLow = creatureData['Attack']['Low']
damageExtreme = creatureData['Damage']['Extreme']
damageHigh = creatureData['Damage']['High']
damageModerate = creatureData['Damage']['Moderate']
damageLow = creatureData['Damage']['Low']

monsterEH = FixedStrike(attackExtreme,damageHigh)
monsterEM = FixedStrike(attackExtreme,damageModerate)

monsterHE = FixedStrike(attackHigh,damageExtreme)
monsterHH = FixedStrike(attackHigh,damageHigh)
monsterHM = FixedStrike(attackHigh,damageModerate)
monsterHL = FixedStrike(attackHigh,damageLow)

monsterME = FixedStrike(attackModerate,damageExtreme)
monsterMH = FixedStrike(attackModerate,damageHigh)
monsterMM = FixedStrike(attackModerate,damageModerate)
monsterML = FixedStrike(attackModerate,damageLow)

monsterLH = FixedStrike(attackLow,damageHigh)
monsterLM = FixedStrike(attackLow,damageModerate)
monsterLL = FixedStrike(attackLow,damageLow)
    
monsterAttackSwitcher = {'Monster Extreme Attack High Damage': [monsterEH],
                  'Monster Extreme Attack Moderate Damage': [monsterEM],
                  'Monster High Attack Extreme Damage': [monsterHE],
                  'Monster High Attack High Damage': [monsterHH],
                  'Monster High Attack Moderate Damage': [monsterHM],
                  'Monster High Attack Low Damage': [monsterHL],
                  'Monster Moderate Attack Extreme Damage': [monsterME],
                  'Monster Moderate Attack High Damage': [monsterMH],
                  'Monster Moderate Attack Moderate Damage': [monsterMM],
                  'Monster Moderate Attack Low Damage': [monsterML],
                  'Monster Low Attack High Damage': [monsterLH],
                  'Monster Low Attack Moderate Damage': [monsterLM],
                  'Monster Low Attack Low Damage': [monsterLL]   
                  }

#effects
flatfoot = Effect(noneDamage)
flatfoot.flatfoot = True

flatfootnext = Effect(noneDamage)
flatfootnext.flatfootNextStrike = True

effectAttackSwitcher = {'Flat Foot Target': [flatfoot],
                        'Flat Foot Next Strike': [flatfootnext]}


magicmissle = Effect(magicMissleDamage)
magicmissle.weaponDamageDice = magicMissleDamageDice
magicmissle.isSpell = True

truestrike = Effect(noneDamage)
truestrike.trueStrike = True

basic45 = Save(spellDC, noneDamage)
basic45.weaponDamageDice = spellDamaged8

basic55 = Save(spellDC, noneDamage)
basic55.weaponDamageDice = spellDamaged10

basic7 = Save(spellDC, noneDamage)
basic7.weaponDamageDice = spellDamage2d6

basic8 = Save(spellDC, spellDamage1)
basic8.weaponDamageDice = spellDamage2d6

basic9 = Save(spellDC, spellDamage2)
basic9.weaponDamageDice = spellDamage2d6

hydralicpush = HPSpellStrike(cantripAttackBonus, noneDamage)
hydralicpush.weaponDamageDice = {i: [d6] + spellDamage2d6[i] for i in range(1,21)}
hydralicpush.critDamageDice = {i: [d6,d6,d6] for i in range(1,21)}

shockinggrasp  =SpellStrike(cantripAttackBonus, noneDamage)
shockinggrasp.weaponDamageDice = {i: [d12]+spellDamaged12[i] for i in range(1,21)}

shockinggraspm  =SpellStrike(cantripAttackBonus, noneDamage)
shockinggraspm.weaponDamageDice = {i: [d12]+spellDamaged12[i] for i in range(1,21)}
shockinggraspm.persDamageDice = {i: [d4] for i in range(1,21)}
shockinggraspm.persDamage = {i: max(0,int((i-1)/2)) for i in range(1,21)}

acidarror = SpellStrike(cantripAttackBonus, noneDamage)
acidarror.minSpellLevel = 2
acidarror.weaponDamageDice = {i: [d8] + int(sDice[i]/2)*[d8,d8] for i in range(3,21)}
acidarror.persDamageDice = {i: int(sDice[i]/2)*[d6] for i in range(3,21)}

lightningbolt = Save(spellDC, noneDamage)
lightningbolt.minSpellLevel = 3
lightningbolt.weaponDamageDice = {i: [d12] + spellDamaged12[i] for i in range(5,21)}

chainlightning = Save(spellDC, noneDamage)
chainlightning.minSpellLevel = 6
chainlightning.weaponDamageDice = {i: [d12,d12] + spellDamaged12[i] for i in range(11,21)}

phantompain = PhantomPainSave(spellDC, noneDamage)
phantompain.weaponDamageDice = spellDamage2d4
phantompain.persDamageDice = spellDamaged4
phantompain.failDebuffTarget = 1
phantompain.critFailDebuffTarget = 2

grimtendrils = Save(spellDC, noneDamage)
grimtendrils.weaponDamageDice = spellDamage2d4
grimtendrils.persDamage = spellDamage1

wallfire = Effect(noneDamage)
wallfire.isSpell = True
wallfire.minSpellLevel = 4
wallfire.weaponDamageDice = spellDamaged6


phantasmalkiller = PKSave(spellDC, noneDamage)
phantasmalkiller.minSpellLevel = 4
phantasmalkiller.failureDamageDice = {i: [d6,d6,d6,d6] for i in range(1,21)}
phantasmalkiller.weaponDamageDice = spellDamage2d6
phantasmalkiller.critDamageDice = {i: sDice[i]*3*[d6] for i in range(1,21)}
phantasmalkiller.successDebuffTarget = 1
phantasmalkiller.failDebuffTarget = 2
phantasmalkiller.critFailDebuffTarget = 4

phantasmalcalamity = Save(spellDC, noneDamage)
phantasmalcalamity.minSpellLevel = 6
phantasmalcalamity.weaponDamageDice = {i: spellDamage2d6[i-2] + [d6] for i in range(11,21)}

spiritblast = Save(spellDC, noneDamage)
spiritblast.minSpellLevel = 6
spiritblast.weaponDamageDice = {i: spellDamage2d6[i] + 4*[d6] for i in range(11,21)}

weird = Save(spellDC, noneDamage)
weird.minSpellLevel = 9
weird.weaponDamageDice = {i: 16*[d6] for i in range(17,21)}
weird.successDebuffTarget = 1
weird.failDebuffTarget = 2
weird.critFailDebuffTarget = 2

visionsdanger = Save(spellDC, noneDamage)
visionsdanger.minSpellLevel = 7
visionsdanger.weaponDamageDice = {i: [d8] + spellDamaged8[i] for i in range(13,21)}

warpriestHarm = Save(warpriestDC, noneDamage)
warpriestHarm.weaponDamageDice = spellDamaged8
warpriestHarm.isSpell = True
warpriestHarm10 = Save(warpriestDC, noneDamage)
warpriestHarm10.weaponDamageDice = spellDamaged10
warpriestHarm10.isSpell = True

dangeroussorcerery = Effect(noneDamage)
dangeroussorcerery.isSpell = True
dangeroussorcerery.addDamage = spellDamage1

debuffAttack123 = Save(spellDC, noneDamage)
debuffAttack123.isSpell = False
debuffAttack123.successDebuffAttack = 1
debuffAttack123.failDebuffAttack = 2
debuffAttack123.critFailDebuffAttack = 3

debuffAttack124 = Save(spellDC, noneDamage)
debuffAttack124.isSpell = False
debuffAttack124.successDebuffAttack = 1
debuffAttack124.failDebuffAttack = 2
debuffAttack124.critFailDebuffAttack = 4

debuffAttack122 = Save(spellDC, noneDamage)
debuffAttack122.isSpell = False
debuffAttack122.successDebuffAttack = 1
debuffAttack122.failDebuffAttack = 2
debuffAttack122.critFailDebuffAttack = 2

debuffAttack012 = Save(spellDC, noneDamage)
debuffAttack012.isSpell = False
debuffAttack012.successDebuffAttack = 0
debuffAttack012.failDebuffAttack = 1
debuffAttack012.critFailDebuffAttack = 2

debuffTarget123 = Save(spellDC, noneDamage)
debuffTarget123.isSpell = False
debuffTarget123.successDebuffTarget = 1
debuffTarget123.failDebuffTarget = 2
debuffTarget123.critFailDebuffTarget = 3

debuffTarget012 = Save(spellDC, noneDamage)
debuffTarget012.isSpell = False
debuffTarget012.successDebuffTarget = 0
debuffTarget012.failDebuffTarget = 1
debuffTarget012.critFailDebuffTarget = 2

disintigrateAttack = SpellStrikeFilter(cantripAttackBonus,noneDamage)
disintigrateSave = Save(spellDC, noneDamage)
disintigrateSave.minSpellLevel = 6
disintigrateSave.weaponDamageDice = spellDamage2d12

debuffAttackDamage123 = Save(spellDC, noneDamage)
debuffAttackDamage123.isSpell = False
debuffAttackDamage123.successDebuffAttack = 1
debuffAttackDamage123.failDebuffAttack = 2
debuffAttackDamage123.critFailDebuffAttack = 3
debuffAttackDamage123.successDebuffDamage = 1
debuffAttackDamage123.failDebuffDamage = 2
debuffAttackDamage123.critFailDebuffDamage = 3



spellAttackSwitcher = {'Basic Save 1d8': [basic45],
                       'Basic Save 1d10': [basic55],
                       'Basic Save 2d6': [basic7],
                'Basic Save 2d6+1': [basic8],
                'Basic Save 2d6+2': [basic9],
                'Magic Missle': [magicmissle],
                'True Strike': [truestrike],
                'Warpriest Harm':[warpriestHarm],
                'Warpriest d10 Harm':[warpriestHarm10],
                'Dangerous Sorcery': [dangeroussorcerery],
                'Phantom Pain': [phantompain],
                'Grim Tendrils': [grimtendrils],
                'Shocking Grasp': [shockinggrasp],
                'Shocking Grasp Metal': [shockinggraspm],
                'Hydralic Push': [hydralicpush],
                'Acid Arrow': [acidarror],
                'Lightning Bolt': [lightningbolt],
                'Phantasmal Killer': [phantasmalkiller],
                'Pantasmal Calamity': [phantasmalcalamity],
                'Spirit Blast': [spiritblast],
                'Weird': [weird],
                'Visions of Danger': [visionsdanger],
                'Wall of Fire': [wallfire],
                'Fear: Debuff Attacker(123)': [debuffAttack123],
                'Fear: Debuff Target(123)': [debuffTarget123],
                'Debuff Attacker(012)': [debuffAttack012],
                'Debuff Target(012)': [debuffTarget012],
                'Disintigrate Attack': [disintigrateAttack],
                'Disintigrate Save': [disintigrateSave],
                'Enfeeblement Save': [debuffAttackDamage123]}

maxfeint = Feint(maxSkillBonus)
trainedfeint = Feint(trainedSkillBonus)
scoundrelfeint = ScoundrelFeint(rogueMaxSkill)
maxdemoralize = Demoralize(maxSkillBonus)
traineddemoralize = Demoralize(trainedSkillBonus)
scaretodeath = ScareToDeath(maxSkillBonus)

skillAttackSwitcher = {
        'Scoundrel Feint': [scoundrelfeint],
        'Trained Feint': [trainedfeint],
        'Max Feint': [maxfeint],
        'Trained Demoralize': [traineddemoralize],
        'Max Demoralize': [maxdemoralize],
        'Scare to Death': [scaretodeath]
        }


attackSwitcher = {**alchemistAttackSwitcher,
                  **barbarianAttackSwitcher,
                  **otherAttackSwitcher,
                  **cantripAttackSwitcher,
                  **fighterAttackSwitcher,
                  **animalcompanionAttackSwitcher,
                  **summonAttackSwitcher,
                  **monsterAttackSwitcher,
                  **effectAttackSwitcher,
                  **spellAttackSwitcher,
                  **skillAttackSwitcher}