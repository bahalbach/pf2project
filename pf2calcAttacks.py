# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:18:59 2019

@author: bhalb
"""
import copy
from pf2calcMonster import creatureData
from distribution import Distribution

d4 = [1/4] * 4
d6 = [1/6] * 6
d8 = [1/8] * 8
d10 = [1/10] * 10
d12 = [1/12] * 12

Fort = 'Fort'
Reflex = 'Reflex'
Will = 'Will'
Perception = 'Perception'

Fire = 'Fire'
Bleed = 'Bleed'
Acid = 'Acid'
Poison = 'Poison'
Mental = 'Mental'
Cold = 'Cold'
Physical = 'Physical'
Electricity = 'Electric'

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
bestWildAttack = copy.copy( animalFormAttack )
for i in range(9,21):
    if i >= 9:
        bestWildAttack[i] = max(bestWildAttack[i],elemFormAttack[i])
    if i >= 15:
        bestWildAttack[i] = max(bestWildAttack[i],monFormAttack[i])
    if i >= 19:
        bestWildAttack[i] = max(bestWildAttack[i],natFormAttack[i])

bestWildDamage = copy.copy( animalFormDamage )
for i in range(9,21):
    if i >= 9:
        bestWildDamage[i] = max(bestWildDamage[i],elemFormDamage[i])
    if i >= 15:
        bestWildDamage[i] = max(bestWildDamage[i],monFormDamage[i])
    if i >= 19:
        bestWildDamage[i] = max(bestWildDamage[i],natFormDamage[i])


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
 
alchProf = {i: i+2 for i in range(1,21)}
for i in alchProf:
    if i >= 9:
        alchProf[i] += 2
    if i >= 17:
        alchProf[i] += 2
        
barbProf = {i: i+2 for i in range(1,21)}
for i in barbProf:
    if i >= 11:
        barbProf[i] += 2
    if i >= 19:
        barbProf[i] += 2
        
acProf = {i: i+2 for i in range(1,21)}
for i in acProf:
    if i >= 9:
        acProf[i] += 2
    if i >= 17:
        acProf[i] += 2
        
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
sbombAttackBonus = copy.copy(bombAttackBonus)
for i in range(8,21):
    sbombAttackBonus[i] = wProf[i] + miBonus[i-2]-1
pbombAttackBonus = {i: wProf[i]  + miBonus[i]-2 for i in range(1,21)}
mutagenstrikeAttackBonus = {i: wProf[i]  + miBonus[i] for i in range(1,21)}
mutagenspellstrikeAttackBonus = {i: sProf[i]  + miBonus[i] for i in range(1,21)}
alchDC = {i: acProf[i] + 10 for i in range(1,21)}

fighterAttackBonus = {i: fProf[i]  + wiBonus[i] for i in range(1,21)}

cantripAttackBonus = {i: sProf[i]  for i in range(1,21)}
cantripAttackBonusItem = {i: wiBonus[i] + sProf[i]  for i in range(1,21)}
spellDC = {i: 10 + cantripAttackBonus[i] for i in range(1,21)}
warpriestDC = {i: 10 + wsProf[i] for i in range(1,21)}

alchemistDC = {i: 10 + alchProf[i] for i in range(1,21)}

barbarianDC = {i: 10 + barbProf[i] for i in range(1,21)}
spiritswrathattackBonus = {i: mProf[i] + 2 for i in range(1,21)}

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
sbombSplashDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        sbombSplashDamage[i] = 2
    if i >= 13:
        sbombSplashDamage[i] = 3
    if i >= 19:
        sbombSplashDamage[i] = 4
        
# bomberSplashDamage = copy.copy(bombSplashDamage)
# for i in range(4,21):
#     bomberSplashDamage[i] = mStr[i]
#     if i >= 10:
#         bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i]
#     if i >= 17:
#         bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i] - 1
        
# sbomberSplashDamage = copy.copy(bombSplashDamage)
# for i in range(4,21):
#     sbomberSplashDamage[i] = mStr[i]
#     if i >= 10:
#         sbomberSplashDamage[i] = mStr[i] + bombSplashDamage[i-2]
#     if i >= 17:
#         sbomberSplashDamage[i] = mStr[i] + bombSplashDamage[i-2] - 1

pbombSplashDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pbombSplashDamage[i] = 1
    if i >= 11:
        pbombSplashDamage[i] = 2
    if i >= 17:
        pbombSplashDamage[i] = 3

# pbomberSplashDamage = copy.copy(bomberSplashDamage)
# for i in range(10,21):
#     pbomberSplashDamage[i] = bomberSplashDamage[i] - 1

        
acidFlaskDamage = {i: 1 for i in range(1,21)}
sacidFlaskDamage = {i: 1 for i in range(1,21)}

acidFlaskPersDamage = {i: [d6] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        acidFlaskPersDamage[i] += [d6]
    if i >= 11:
        acidFlaskPersDamage[i] += [d6]
    if i >= 17:
        acidFlaskPersDamage[i] += [d6]
sacidFlaskPersDamage = copy.copy(acidFlaskPersDamage)
for i in range(8,21):
    sacidFlaskPersDamage[i] = acidFlaskPersDamage[i-2]


alchemistsFireDamage = {i: [d8] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFireDamage[i] += [d8]
    if i >= 11:
        alchemistsFireDamage[i] += [d8]
    if i >= 17:
        alchemistsFireDamage[i] += [d8]
salchemistsFireDamage = copy.copy(alchemistsFireDamage)
for i in range(8,21):
    salchemistsFireDamage[i] = alchemistsFireDamage[i-2]
    
alchemistsFirePersDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFirePersDamage[i] = 2
    if i >= 11:
        alchemistsFirePersDamage[i] = 3
    if i >= 17:
        alchemistsFirePersDamage[i] = 4
salchemistsFirePersDamage = copy.copy(alchemistsFirePersDamage)
for i in range(8,21):
    salchemistsFirePersDamage[i] = alchemistsFirePersDamage[i-2]
    
blfvDamage = {i: [d6] for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        blfvDamage[i] += [d6]
    if i >= 11:
        blfvDamage[i] += [d6]
    if i >= 17:
        blfvDamage[i] += [d6]
sblfvDamage = copy.copy(blfvDamage)
for i in range(8,21):
    sblfvDamage[i] = blfvDamage[i-2]
        
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

noneDamage = {i: 0 for i in range(-1,24)}
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
spellDamage8 = {i: sDice[i]*8 for i in range(1,21)}
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
    def __init__(self, atk, damageDist, persDist):
        self.damageDist = damageDist
        self.persDist = persDist
        
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
        
        self.addConcealment = False
        self.removeConcealment = False
        self.addHidden = False
        self.removeHidden = False
        self.applyPersistentDamage = False
        
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
        self.enfeebled = 0
        
        self.clumsy = 0
        self.drained = 0
        self.frightened = 0
        self.sickened = 0
        self.stupified = 0
        
        self.treatWorse = False
        self.ignoreNext = False
        self.setAttack = None
        
        self.addConcealment = False
        self.removeConcealment = False
        self.addHidden = False
        self.removeHidden = False
        
        self.setFortification = False
        self.fortification = 0
        
        self.atk = atk
        self.ishit = False
        self.iscrit = False
        self.doubleDamage = False
        self.halveDamage = False
        self.doublePersOnDouble = True
        
        self.okay = False
        self.good = False
        self.veryGood = False
        
        self.targetAC = None
        self.targetFort = None
        self.targetRef = None
        self.targetWill = None
        self.targetPer = None
        
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
            self.name = "Attack"
            self.details = ""
            self.attack = attack
            self.attackBonus = 0
            self.damage = damage
            self.additionalDamage = 0
            self.damageBonus = 0
            
            self.wDice = copy.copy(wDice) # number of dice
            self.damageDie = [1] # 3.5
            self.weaponDamageDice = None
            self.damageDieBonus = None
            self.runeDamageDice = {i: [] for i in range(-1,25)}
            self.extraWeaponDice = {i: 0 for i in range(-1,25)}
            
            self.persDamage = {i: 0 for i in range(-1,25)}
            self.persDamageDice = {i: [] for i in range(-1,25)}
            self.persDamageType = None
#            self.NDpersDamage = copy.copy(noneDamage)
#            self.NDpersDamageDice = {i: [] for i in range(1,21)}
            
            self.splashDamage = None
            
            self.flatfootedDamage = {i: 0 for i in range(-1,25)}
            self.flatfootedDamageDice = {i: [] for i in range(-1,25)}
            
#            self.failureDamage = copy.copy(noneDamage)
            self.failureDamageDice = {i: [] for i in range(-1,25)}
            self.certainStrike = False
            self.brutalFinish = False
            
            self.critDamage = {i: 0 for i in range(-1,25)}
            self.critDamageDice = {i: [] for i in range(-1,25)}
            self.critPersDamage = {i: 0 for i in range(-1,25)}
            self.critPersDamageDice = {i: [] for i in range(-1,25)}
            
            self.fatal = False
            self.fatalDie = None
            
            self.isWeapon = False
            self.fixedStrike = False
            self.isSpell = False
            self.spellLevelModifier = 0
            self.minSpellLevel = 1
            self.constantSpellLevel = False
            self.useMCSpellLevel = False
            
            self.doubleDamage = True
            self.doublePersDamage = True
            self.halveDamage = True
            self.damageOnSuccesSave = True
            
            self.ignoreConcealment = False
            
            self.critSpecLevel = 21
            self.keenLevel = 21
            self.backswingLevel = 21
        
            self.stickybombLevel = 21
            
            self.ffonCritLevel = 21
            self.ffonSuccessLevel = 21
            self.ffonFailLevel = 21
            
            self.attackBonusOnFail = 0
            
            self.okayDebuffAttack = 0
            self.goodDebuffAttack = 0
            self.veryGoodDebuffAttack = 0 
            self.okayEnfeebled = 0
            self.goodEnfeebled = 0
            self.veryGoodEnfeebled = 0
            
            self.okayClumsy = 0
            self.goodClumsy = 0
            self.veryGoodClumsy = 0
            self.okayDrained = 0
            self.goodDrained = 0
            self.veryGoodDrained = 0
            self.okayFrightened = 0
            self.goodFrightened = 0
            self.veryGoodFrightened = 0
            self.okaySickened = 0
            self.goodSickened = 0
            self.veryGoodSickened = 0
            self.okayStupified = 0
            self.goodStupified = 0
            self.veryGoodStupified = 0
            
            self.ignoreNextonMiss = False
            
            self.addConcealment = False
            self.removeConcealment = False
            self.addHidden = False
            self.removeHidden = False
            
            self.minL = -1
            self.maxL = 24
            self.levelAdjustment = {i: 0 for i in range(-1,24)}
        def getAttackObject(self,level):
            return self
            
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
                        self.persDamageType  = Bleed
                elif csName == "hammer":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "sword":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "pick":
                    for i in range(self.critSpecLevel,21):
                        self.critDamage[i] += self.wDice[i] * 2
                        
        def setWeaponFeatures(self, featureArray):
            self.details= "features: "
            for feature in featureArray:
                if feature[0] == "1d12 Rune":
                    if not self.isWeapon:
                        continue
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d12]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "1d10 Rune":
                    if not self.isWeapon:
                        continue
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d10]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "1d8 Rune":
                    if not self.isWeapon:
                        continue
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d8]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "1d6 Rune":
                    if not self.isWeapon:
                        continue
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d6]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "1d4 Rune":
                    if not self.isWeapon:
                        continue
                    for i in self.runeDamageDice:
                        if i >= feature[1]:
                            self.runeDamageDice[i]+=[d4]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "Flaming Crit Persistent":
                    if not self.isWeapon:
                        continue
                    for i in range(feature[1],21):
                        self.critPersDamageDice[i] += [d10]
                        self.persDamageType  = Fire
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "Add 1 Die":
                    for i in self.weaponDamageDice:
                        if i >= feature[1]:
                            if len(self.weaponDamageDice[i]) > 0:
                                self.weaponDamageDice[i]+=[self.weaponDamageDice[i][0]]
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "Remove 1 Die":
                    for i in self.weaponDamageDice:
                        if i >= feature[1]:
                            if len(self.weaponDamageDice[i]) > 0:
                                self.weaponDamageDice[i].pop()
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == 'MC Caster Proficiency':
                    self.setMCCaster(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "backswing":
                    self.setBackswing(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "backstabber":
                    self.setBackstabber(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"     
                elif feature[0] == "keen":
                    self.setKeen(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "Brutal Critical":
                    self.setBrutalCritical(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "Burn it!":
                    self.setBurnIt(feature[1])
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+1 level":
                    self.adjustLevels(feature[1],1)
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-1 level":
                    self.adjustLevels(feature[1],-1)
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+1 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] += 1
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+2 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] += 2
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+3 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] += 3
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+4 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] += 4
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+5 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] += 5
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-1 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] -= 1
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-2 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] -= 2
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-3 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] -= 3
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-4 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] -= 4
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-5 attack":
                    for i in self.attack:
                        if i >= feature[1]:
                            self.attack[i] -= 5
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+1 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 1
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+2 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 2
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+3 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 3
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+4 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 4
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+5 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 5
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+6 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 6
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+7 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 7
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+8 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 8
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+9 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 9
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "+10 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] += 10
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-1 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 1
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-2 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 2
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-3 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 3
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-4 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 4
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-5 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 5
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-6 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 6
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-7 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 7
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-8 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 8
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-9 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 9
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
                elif feature[0] == "-10 damage":
                    for i in self.damage:
                        if i >= feature[1]:
                            self.damage[i] -= 10
                    if feature[1] < 21:
                        self.details += "[" + str(feature) + "]\n"
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
                elif slName == 'MC Max':
                    self.useMCSpellLevel = True
                    self.spellLevelModifier = 0
                
            
        def getAttack(self, level):
            if level>=self.minL and level<=self.maxL:
                if self.isSpell and (sDice[level] + self.spellLevelModifier < self.minSpellLevel
                                     or (self.constantSpellLevel and level < self.spellLevelModifier*2-1)
                                     or (self.useMCSpellLevel and level<4)):
                    return None
                if self.isSpell and self.fixedStrike:
                    level = level + self.spellLevelModifier*2
                if level in self.attack:
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
        
#        def getNDPersistentDamage(self, level):
#            if self.isSpell:
#                    level = self.spellLevel(level)
#            if self.NDpersDamage:
#                return self.NDpersDamage[level]
#            return 0
#        
#        def getNDPersistentDamageDice(self, level):
#            if self.isSpell:
#                    level = self.spellLevel(level)
#            if self.NDpersDamageDice:
#                return self.NDpersDamageDice[level]
#            return []
        
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
        
#        def getFailureDamage(self, level):
#            if self.isSpell:
#                    level = self.spellLevel(level)
#            if self.failureDamage:
#                return self.failureDamage[level]
#            return 0
        
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
        def setBackstabber(self, level):
            for i in range(level,21):
                self.flatfootedDamage[i] += 1
                if wiBonus[i] >= 3:
                    self.flatfootedDamage[i] += 1
        def setBrutalCritical(self, level):
            for i in range(level, 21):
                self.critDamageDice[i] += [self.damageDie]
                self.persDamageType = Bleed
                self.critPersDamageDice[i] += 2*[self.damageDie]
        def setBurnIt(self, level):
            if self.isSpell:
                for i in range(level,21):
                    slevel = self.spellLevel(i)
                    bonus = sDice[slevel]
                    bonus = max(1,int(bonus/2))
                    self.damage[i] += bonus
                    if self.persDamage[i] != 0 or self.persDamageDice[i] != []:
                        self.persDamage[i] += 1
                    if self.critPersDamage[i] != 0 or self.critPersDamageDice[i] != []:
                        self.critPersDamage[i] += 1
                
        def setFFonCrit(self, level):
            self.ffonCritLevel = min(level,self.ffonCritLevel)
        def setFFonSuccess(self, level):
            self.ffonSuccessLevel = min(level,self.ffonSuccessLevel)
        def setFFonFail(self, level):
            self.ffonFailLevel = min(level,self.ffonFailLevel)
            
        def adjustLevels(self, startLevel, amount):
            for i in self.levelAdjustment:
                if i >= startLevel:
                    self.levelAdjustment[i] += amount
        def attackLevel(self, level):
            return level + self.levelAdjustment[level]
        
        def setLevels(self, minl, maxl):
            # if self.fixedStrike:
            #     if minl != 1:
            #         self.minL = max(minl, self.minL)
            #     if maxl != 20:
            #         self.maxL = min(maxl, self.maxL)
            #     return
            self.minL = max(minl, self.minL)
            self.maxL = min(maxl, self.maxL)
            
        def setMCCaster(self, level):
            for i in range(level, 21):
                if i >= 19:
                    self.attack[i] -= 2
                elif i >= 18:
                    pass
                elif i >= 15:
                    self.attack[i] -= 2
                elif i >= 12:
                    pass
                elif i >= 7:
                    self.attack[i] -= 2
        
        def spellLevel(self, level):
            if self.isSpell:
                if self.constantSpellLevel:
                    level = self.spellLevelModifier*2
                elif self.useMCSpellLevel:
                    level = AtkSelection.getMCSpellLevel(level)
                else:
                    level = level + self.spellLevelModifier*2
            return level
        
        def getMCSpellLevel(level):
            if level >= 20:
                level = 16
            elif level >= 18:
                level = 14
            elif level >= 16:
                level = 12
            elif level >= 14:
                level = 10
            elif level >= 12:
                level = 8
            elif level >= 8:
                level = 6
            elif level >= 6:
                level = 4
            elif level >= 4:
                level = 2
            return level
                
        def info(self):
            return self.name + ": " + self.details
class Stitch:
    def __init__(self, attackList):
        self.attackList = attackList
        
    def getAttackObject(self,level):
        for attack in self.attackList:
            if not attack.getAttack(level) is None:
                return attack.getAttackObject(level)
        raise Exception("No valid attack")
        return None
    def getAttack(self, level):
        for attack in self.attackList:
            if not attack.getAttack(level) is None:
                return attack.getAttack(level)
        else:
            return None
    def info(self):
        string = "Stitch:\n"
        for attack in self.attackList:
            string += attack.info()
        return string
        
class Strike(AtkSelection):
    def __init__(self, attack, damage, isWeapon=True, csLevel=21):
        super().__init__(attack, damage)
        self.critSpecLevel = csLevel
        self.isWeapon = isWeapon
        
    def critSuccessResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
        bonus += context.getDamageBonus()
        bonus += context.getExtraDamage()
        damageDice = self.getDamageDice(level, crit=True)
        damageDice += context.getHitDamageDice()
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)     
        
        persDam = self.getPersistentDamage(level)
        persDamDice = self.getPersistentDamageDice(level)
        persDamType = self.persDamageType
        
        splashDam = self.getSplashDamage(level)
        if level >= self.stickybombLevel:
            persDam += splashDam
          
        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        persDist = Distribution(persDamDice, persDam, persDamType)
        
        # double for crit 
        if self.doubleDamage:
            damageDist.double()
            if self.doublePersDamage:
                persDist.double()
        
        # splash damage
        damageDist.add([],splashDam)
        
        # crit damage
        critDam = self.getCriticalBonusDamage(level)
        critDamDice = self.getCriticalBonusDamageDice(level)
        damageDist.add(critDamDice,critDam)
        critPersDam = self.getCriticalPersistentDamage(level)
        critPersDamDice = self.getCriticalPersistentDamageDice(level)
        persDist.add(critPersDamDice,critPersDam)
        
#        # no double persistent damage
#        NDpersDam = self.getNDPersistentDamage(level)
#        NDpersDamDice = self.getNDPersistentDamageDice(level)
#        persDist.add(NDpersDamDice,NDpersDam)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        persDist.addWeakness(weakness)
        
        r = Result(self, damageDist, persDist)
        r.setCrit()
        
        # on crit effects
        if self.ffonCrit(level):
            r.setFutureAttacksFF()
            
        r.debuffAttack = self.veryGoodDebuffAttack
        r.clumsy = self.veryGoodClumsy
        r.drained = self.veryGoodDrained
        r.enfeebled = self.veryGoodEnfeebled
        r.frightened = self.veryGoodFrightened
        r.sickened = self.veryGoodSickened
        r.stupified = self.veryGoodStupified
            
        return r
        
    def successResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
        bonus += context.getDamageBonus()
        bonus += context.getExtraDamage()
        damageDice = self.getDamageDice(level)
        damageDice += context.getHitDamageDice()
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)     
        
        persDam = self.getPersistentDamage(level)
        persDamDice = self.getPersistentDamageDice(level)
        persDamType = self.persDamageType
        
        splashDam = self.getSplashDamage(level)
        if level >= self.stickybombLevel:
            persDam += splashDam
          
        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        persDist = Distribution(persDamDice, persDam, persDamType)
        
        # splash damage
        damageDist.add([],splashDam)
        
#        # no double persistent damage
#        NDpersDam = self.getNDPersistentDamage(level)
#        NDpersDamDice = self.getNDPersistentDamageDice(level)
#        persDist.add(NDpersDamDice,NDpersDam)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        persDist.addWeakness(weakness)      
        
        r = Result(self, damageDist, persDist)
        r.setHit()
            
        if self.ffonSuccess(level):
            r.setFutureAttacksFF()
            
        r.debuffAttack = self.goodDebuffAttack
        r.clumsy = self.goodClumsy
        r.drained = self.goodDrained
        r.enfeebled = self.goodEnfeebled
        r.frightened = self.goodFrightened
        r.sickened = self.goodSickened
        r.stupified = self.goodStupified
            
        return r
        
    def failureResult(self, level, context):
        context.getExtraDamage() # just clear this
        
        staticDamage = 0
        if self.certainStrike:
            staticDamage += self.getDamageBonus(level)
            if context.flatfooted:
                staticDamage += self.getFFDamage(level)
                
        damageDice = self.getFailureDamageDice(level)
        
        # apply bonuses and penelties to brutal finish
        bonus = self.damageBonus
        bonus += context.getDamageBonus()
            
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        
        # splash damage
        splashDam = self.getSplashDamage(level)
        damageDist.add([],splashDam)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        
        r = Result(self, damageDist, Distribution())
        r.setFail()
        
        if(self.getBackswing(level)):
            r.setNextStrikeBonus(self.attackBonusOnFail+1)
        else:
            r.setNextStrikeBonus(self.attackBonusOnFail)
        
        if self.ffonFail(level):
            r.setFutureAttacksFF()
            
        r.debuffAttack = self.okayDebuffAttack
        r.clumsy = self.okayClumsy
        r.drained = self.okayDrained
        r.enfeebled = self.okayEnfeebled
        r.frightened = self.okayFrightened
        r.sickened = self.okaySickened
        r.stupified = self.okayStupified
        
        if self.ignoreNextonMiss:
            r.ignoreNext
            
        return r
        
    def critFailureResult(self, level, context):
        context.getExtraDamage() # just clear this
        r = Result(self, Distribution(), Distribution())
        r.setCritFail()
        if self.ignoreNextonMiss:
            r.ignoreNext
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
class TigerSlash(MeleeStrike):
    def __init__(self, attack, damage, csLevel=21):
        super().__init__(attack, damage, csLevel=csLevel)

    def setSecondaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addDamageBonuses(scoreValues)
        for i in range(1,21):
            self.critPersDamage[i] += scoreValues[i]
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
    
    def setBurnIt(self, level):
        for i in range(level,21):
            bonus = len(self.weaponDamageDice[i])
            bonus = max(1,(bonus-2)*2)
            self.damage[i] += bonus
            if self.persDamage[i] != 0 or self.persDamageDice[i] != []:
                self.persDamage[i] += 1
            if self.critPersDamage[i] != 0 or self.critPersDamageDice[i] != []:
                self.critPersDamage[i] += 1
            

            
class BomberStrike(BombStrike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.prim = True
        self.sec = True
        self.damageScores = None
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.damageScore = scoreValues
        return True
        
    def getSplashDamage(self, level):
        splash = super().getSplashDamage(level)
        if level >= 10:
            splash = self.damageScore[level] + splash
        elif level >= 4:
            splash = max(self.damageScore[level],splash)
        return splash
    
class DBombStrike(RangedStrike):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        self.isWeapon = False
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCrit()
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setHit()
        return r
        
    def failureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setFail()
        r.ignoreNext = True
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritFail()
        r.ignoreNext = True
        return r
        
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
    
    def setBurnIt(self, level):
        for i in range(level,21):
            bonus = len(self.weaponDamageDice[i])
            bonus = max(1,int((bonus)/2))
            self.damage[i] += bonus
            if self.persDamage[i] != 0 or self.persDamageDice[i] != []:
                self.persDamage[i] += 1
            if self.critPersDamage[i] != 0 or self.critPersDamageDice[i] != []:
                self.critPersDamage[i] += 1
        
        
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
        self.minL = -1
        self.maxL = 24
        
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
        
    
class SpellStrikeFilter(RangedStrike):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.isWeapon = False
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCrit()
        r.treatWorse = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setHit()
        return r
        
    def failureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setFail()
        r.ignoreNext = True
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritFail()
        r.ignoreNext = True
        return r
        
        
class SaveAttack(AtkSelection):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)
        self.prim = True
        self.sec = False
        self.targetSave = Reflex
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
    

    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccess()
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setSuccess()
        return r
        
    def failureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setFail()
        return r
        
    def critFailureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritFail()
        return r

class Feint(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        self.targetSave = Perception
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccess()
        
        r.futureAttacksFF = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setSuccess()
        
        r.nextAttackFF = True
        return r
        
class ScoundrelFeint(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        self.targetSave = Perception
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccess()
        
        r.futureAttacksFF = True
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setSuccess()
        
        r.futureAttacksFF = True
        return r
    
class Demoralize(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        self.targetSave = Will
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccess()
        
        r.frightened = 2
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setSuccess()
        
        r.frightened = 1
        return r

class ScareToDeath(SaveAttack):
    def __init__(self, attack):
        super().__init__(attack, noneDamage)
        self.targetSave = Will
        
    def critSuccessResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccess()
        
        r.frightened = 3
        return r
    
    def successResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setSuccess()
        
        r.frightened = 2
        return r
    
    def failureResult(self, level, context):
        r = Result(self, Distribution(),Distribution())
        r.setFail()
        
        r.frightened = 1
        return r
        
class Save(AtkSelection):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
        self.prim = True
        self.sec = False
        self.isSpell = True
        self.targetSave = Reflex
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
        
    def getDC(self, level):
        return self.getAttack(level)
    
    def critSuccessResult(self, level, context):
        context.getExtraDamage()
        
        r = Result(self, Distribution(),Distribution())
        r.setCritSuccessSave()
        return r
        
    def successResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bonus += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        if self.damageOnSuccesSave:
            damageDice = self.getDamageDice(level)
        else: damageDice = []
        
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)     
        
        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        
        if self.halveDamage:
            damageDist.halve()
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        
        
        r = Result(self, damageDist, Distribution())
        r.setSuccessSave()

        r.debuffAttack = self.okayDebuffAttack
        r.clumsy = self.okayClumsy
        r.drained = self.okayDrained
        r.enfeebled = self.okayEnfeebled
        r.frightened = self.okayFrightened
        r.sickened = self.okaySickened
        r.stupified = self.okayStupified
        
        return r
        
    def failureResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bnous += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        damageDice = self.getDamageDice(level)
        
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)  
            
        persDam = self.getPersistentDamage(level)
        persDamDice = self.getPersistentDamageDice(level)
        persDamType = self.persDamageType
        
        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        persDist = Distribution(persDamDice, persDam, persDamType)
        
#        # no double persistent damage
#        NDpersDam = self.getNDPersistentDamage(level)
#        NDpersDamDice = self.getNDPersistentDamageDice(level)
#        persDist.add(NDpersDamDice,NDpersDam)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        persDist.addWeakness(weakness)
        
        r = Result(self, damageDist, persDist)
        r.setFailSave()
        
        r.debuffAttack = self.goodDebuffAttack
        r.clumsy = self.goodClumsy
        r.drained = self.goodDrained
        r.enfeebled = self.goodEnfeebled
        r.frightened = self.goodFrightened
        r.sickened = self.goodSickened
        r.stupified = self.goodStupified
        
        r.addConcealment = self.addConcealment
        r.addHidden = self.addHidden
        r.removeConcealment = self.removeConcealment
        r.removeHidden = self.removeHidden
       
        if self.ffonFail(level):
            r.setFutureAttacksFF()
        
        return r
        
    def critFailureResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bonus += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        damageDice = self.getDamageDice(level)
        
        if context.flatfooted:
            staticDamage += self.getFFDamage(level)
            damageDice += self.getFFDamageDice(level)  
            
        persDam = self.getPersistentDamage(level)
        persDamDice = self.getPersistentDamageDice(level)
        persDamType = self.persDamageType
        
        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        persDist = Distribution(persDamDice, persDam, persDamType)
        
        # double for crit fail
        if self.doubleDamage:
            damageDist.double()
            if self.doublePersDamage:
                persDist.double()
        
        # crit damage
        critDam = self.getCriticalBonusDamage(level)
        critDamDice = self.getCriticalBonusDamageDice(level)
        damageDist.add(critDamDice,critDam)
        critPersDam = self.getCriticalPersistentDamage(level)
        critPersDamDice = self.getCriticalPersistentDamageDice(level)
        persDist.add(critPersDamDice,critPersDam)
        
#        # no double persistent damage
#        NDpersDam = self.getNDPersistentDamage(level)
#        NDpersDamDice = self.getNDPersistentDamageDice(level)
#        persDist.add(NDpersDamDice,NDpersDam)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        persDist.addWeakness(weakness)
        
        r = Result(self, damageDist, persDist)
        r.setCritFailSave()
        
        r.debuffAttack = self.veryGoodDebuffAttack
        r.clumsy = self.veryGoodClumsy
        r.drained = self.veryGoodDrained
        r.enfeebled = self.veryGoodEnfeebled
        r.frightened = self.veryGoodFrightened
        r.sickened = self.veryGoodSickened
        r.stupified = self.veryGoodStupified
        
        r.addConcealment = self.addConcealment
        r.addHidden = self.addHidden
        r.removeConcealment = self.removeConcealment
        r.removeHidden = self.removeHidden
        
        if self.ffonFail(level):
            r.setFutureAttacksFF()
            
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
    
class FixedSave(Save):
    # don't use ability score
    def __init__(self, dc, damage):
        super().__init__(dc, damage) 
        self.fixedStrike = True
        self.isSpell = False
        self.prim = False
        self.sec = False
        
    def setPrimaryAS(self, score):
        return False
    def setSecondaryAS(self, score):
        return False
    
class EnergySave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
        self.prim = False
        self.sec = False
        self.isSpell = False
        self.targetSave = Reflex
        
    def setPrimaryAS(self, score):
        return False
    
class PKSave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
    
        
    def successResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bonus += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        
        # only use failure damage
        damageDice = self.getFailureDamageDice(level)

        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        
        r = Result(self, damageDist, Distribution())
        r.setSuccessSave()

        r.debuffAttack = self.okayDebuffAttack
        r.clumsy = self.okayClumsy
        r.drained = self.okayDrained
        r.enfeebled = self.okayEnfeebled
        r.frightened = self.okayFrightened
        r.sickened = self.okaySickened
        r.stupified = self.okayStupified
        
        return r
        

    def critFailureResult(self, level, context):
        #get damage
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bonus += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        
        # only use critical damage
        damageDice = self.getCriticalBonusDamageDice(level)

        #create distribution
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        
        r = Result(self, damageDist, Distribution())
        r.setCritFailSave()
        
        r.debuffAttack = self.veryGoodDebuffAttack
        r.clumsy = self.veryGoodClumsy
        r.drained = self.veryGoodDrained
        r.enfeebled = self.veryGoodEnfeebled
        r.frightened = self.veryGoodFrightened
        r.sickened = self.veryGoodSickened
        r.stupified = self.veryGoodStupified
        
        return r

class TDSave(Save):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)
    def successResult(self, level, context):
        return super().failureResult(level, context)
    
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
    def __init__(self):
        super().__init__(noneDamage, noneDamage)
        self.applyConcealment = False
        self.flatfootNextStrike = False
        self.flatfoot = False
        self.trueStrike = False
        
        self.setFortification = False
        self.fortification = 0
        
        self.targetAC = None
        self.targetFort = None
        self.targetRef = None
        self.targetWill = None
        self.targetPer = None
        
        self.addfirsthitdamage = None
        self.addsecondhitdamage = None 
        self.addthirdhitdamage = None
        self.addeveryhitdamage = None
        
        self.addfirsthitdamageDice = None
        self.addsecondhitdamageDice = None 
        self.addthirdhitdamageDice = None
        self.addeveryhitdamageDice = None
        
        self.addDamage = None
        self.addAttack = None
        
        self.prim = False
        self.sec = False
        
    def setPrimaryAS(self, score):
        return False
    def setSecondaryAS(self, score):
        return False
        
    def effectResult(self, level, context):
        
        r = Result(self,Distribution(),Distribution())
        
        if self.targetAC:
            r.targetAC = self.targetAC[level]
        if self.targetFort:
            r.targetFort = self.targetFort[level]
        if self.targetRef:
            r.targetRef = self.targetRef[level]
        if self.targetWill:
            r.targetWill = self.targetWill[level]
        if self.targetPer:
            r.targetPer = self.targetPer[level]
        
        if self.flatfoot:
            r.futureAttacksFF = True
        elif self.flatfootNextStrike:
            r.nextAttackFF = True
        
        r.trueStrike = self.trueStrike
        r.addConcealment = self.addConcealment
        r.addHidden = self.addHidden
        r.removeConcealment = self.removeConcealment
        r.removeHidden = self.removeHidden
        
        if self.setFortification:
            r.setFortification = True
            r.fortification = self.fortification
        
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
        if self.addAttack:
            r.setNextStrikeBonus(self.addAttack[level])
            
        r.debuffAttack = self.goodDebuffAttack
        r.clumsy = self.goodClumsy
        r.drained = self.goodDrained
        r.enfeebled = self.goodEnfeebled
        r.frightened = self.goodFrightened
        r.sickened = self.goodSickened
        r.stupified = self.goodStupified
            
        return r
class AutoDamage(Effect):
    def __init__(self, damage):
        super().__init__()
        self.applyConcealment = True
        self.damage = damage
        
    def effectResult(self, level, context):
        staticDamage = self.getDamageBonus(level)
        bonus = self.damageBonus
#        bnous += context.getDamageBonus() no enfeebled
        bonus += context.getExtraDamage()
        damageDice = self.getDamageDice(level)
        
        damageDist = Distribution(damageDice,staticDamage)
        damageDist.addBonus(bonus)
        
        # weakness
        weakness = context.getWeakness()
        damageDist.addWeakness(weakness)
        
        r = Result(self,damageDist,Distribution())
        return r
    
class Quicksilver(Effect):
    def __init__(self, attack):
        super().__init__()
        self.attack = attack
        self.prim = True
        self.sec = False
        
    def setPrimaryAS(self, score):
        scoreValues = abilityScoreConverter[score]
        self.addAttackBonuses(scoreValues)
        return True
    def setSecondaryAS(self, score):
        return False
        
    def effectResult(self, level, context):
        r = Result(self,Distribution(),Distribution())
        r.setAttack = self.getAttack(level)
        return r
    
class ApplyPersistentDamage(Effect):
    def __init__(self):
        super().__init__()
        
    def effectResult(self, level, context):
        r = Result(self,Distribution(),Distribution())
        r.applyPersistentDamage = True
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
                    if st.getAttack(level) is None:
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
                    if st.getAttack(level) is None:
                        srhas = False
                if srhas: validAttackList.append(sr)
        return validAttackList
        
    
alchemistStrike = MeleeStrike(warpriestAttackBonus, alchemistDamage)
alchemistRangedStrike = RangedStrike(warpriestAttackBonus, alchemistRangedDamage)

quicksilverMutagenBomb = Quicksilver(mutagenstrikeAttackBonus)
quicksilverMutagenWeapon = Effect()
quicksilverMutagenWeapon.addAttack = {i: miBonus[i] - wiBonus[i] for i in range(1,21)}
quicksilverMutagenSpellAttack = Effect()
quicksilverMutagenSpellAttack.addAttack =  {i: miBonus[i] for i in range(1,21)}

energyMutagenDice = {i: [d4] for i in range(1,21)}
energyMutagenDice[1] = []
energyMutagenDice[2] = []
for i in energyMutagenDice:
    if i >= 11:
        energyMutagenDice[i] = [d6]
    if i >= 17:
        energyMutagenDice[i] = [d6,d6]
energyMutagen = Effect()
energyMutagen.addeveryhitdamageDice = energyMutagenDice

{i: int(sDice[i]/3) for i in range(1,21)}
energyDC = {i: 25 for i in range(11,21)}
for i in range(17,21):
    energyDC[i] = 32
energyDamage = {i: 12*[d6] for i in range(11,21)}
for i in range(17,21):
    energyDamage[i] = 18*[d6]
energyMutagenAttack = EnergySave(energyDC, noneDamage)
energyMutagenAttack.minL = 11
energyMutagenAttack.weaponDamageDice = energyDamage

powerfulEnergyAttack = Save(alchDC, noneDamage)
powerfulEnergyAttack.minL = 11
powerfulEnergyAttack.weaponDamageDice = energyDamage
powerfulEnergyAttack.isSpell = False

elixirLifeStatic = {i: 0 for i in range(1,21)}
for i in elixirLifeStatic:
    if i >= 5:
        elixirLifeStatic[i] = 6
    if i >= 9: 
        elixirLifeStatic[i] = 12
    if i >= 13:
        elixirLifeStatic[i] = 18
    if i >= 15:
        elixirLifeStatic[i] = 21
    if i >= 19:
        elixirLifeStatic[i] = 27
elixirLifeDice = {i: [d6] for i in range(1,21)}
for i in elixirLifeDice:
    if i >= 5:
        elixirLifeDice[i] = 3*[d6]
    if i >= 9: 
        elixirLifeDice[i] = 5*[d6]
    if i >= 13:
        elixirLifeDice[i] = 7*[d6]
    if i >= 15:
        elixirLifeDice[i] = 8*[d6]
    if i >= 19:
        elixirLifeDice[i] = 10*[d6]
elixirLife = AutoDamage(elixirLifeStatic)
elixirLife.weaponDamageDice = elixirLifeDice

alchemistAcidDamage = {i: alchemistRangedDamage[i]+1 for i in range(1,21)}
alchemistacids = BombStrike(bombAttackBonus, alchemistAcidDamage)
alchemistacids.isWeapon = False
alchemistacids.weaponDamage = acidFlaskDamage
alchemistacids.persDamageDice = acidFlaskPersDamage
#alchemistacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistacids.splashDamage = bombSplashDamage
alchemistacids.persDamageType = Acid

alchemistbacids = BomberStrike(bombAttackBonus, alchemistAcidDamage)
alchemistbacids.isWeapon = False
alchemistbacids.weaponDamage = acidFlaskDamage
alchemistbacids.persDamageDice = acidFlaskPersDamage
#alchemistbacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbacids.splashDamage = bombSplashDamage
alchemistbacids.persDamageType = Acid

alchemistbsacids = BomberStrike(sbombAttackBonus, alchemistAcidDamage)
alchemistbsacids.isWeapon = False
alchemistbsacids.weaponDamage = sacidFlaskDamage
alchemistbsacids.persDamageDice = sacidFlaskPersDamage
#alchemistbsacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbsacids.splashDamage = sbombSplashDamage
alchemistbsacids.stickybombLevel = 8
alchemistbsacids.persDamageType = Acid

alchemistbdacids = BomberStrike(sbombAttackBonus, alchemistAcidDamage)
alchemistbdacids.isWeapon = False
alchemistbdacids.weaponDamage = sacidFlaskDamage
alchemistbdacids.persDamageDice = sacidFlaskPersDamage
#alchemistbdacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbdacids.splashDamage = sbombSplashDamage
alchemistbdacids.persDamageType = Acid
alchemistbdacids.ignoreNextonMiss = True

alchemistpacids = BombStrike(pbombAttackBonus, alchemistAcidDamage)
alchemistpacids.isWeapon = False
alchemistpacids.weaponDamage = pacidFlaskDamage
alchemistpacids.persDamageDice = pacidFlaskPersDamage
#alchemistpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistpacids.splashDamage = pbombSplashDamage
alchemistpacids.persDamageType = Acid

alchemistbpacids = BomberStrike(pbombAttackBonus, alchemistAcidDamage)
alchemistbpacids.isWeapon = False
alchemistbpacids.weaponDamage = pacidFlaskDamage
alchemistbpacids.persDamageDice = pacidFlaskPersDamage
#alchemistbpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpacids.splashDamage = pbombSplashDamage
alchemistbpacids.persDamageType = Acid

alchemistbpsacids = BomberStrike(pbombAttackBonus, alchemistAcidDamage)
alchemistbpsacids.isWeapon = False
alchemistbpsacids.weaponDamage = pacidFlaskDamage
alchemistbpsacids.persDamageDice = pacidFlaskPersDamage
#alchemistbpsacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpsacids.splashDamage = pbombSplashDamage
alchemistbpsacids.stickybombLevel = 8
alchemistbpsacids.persDamageType = Acid

alchemistbpdacids = BomberStrike(pbombAttackBonus, alchemistAcidDamage)
alchemistbpdacids.isWeapon = False
alchemistbpdacids.weaponDamage = pacidFlaskDamage
alchemistbpdacids.persDamageDice = pacidFlaskPersDamage
#alchemistbpsacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpdacids.splashDamage = pbombSplashDamage
alchemistbpdacids.persDamageType = Acid
alchemistbpdacids.ignoreNextonMiss = True

alchemistfires = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistfires.isWeapon = False
alchemistfires.weaponDamageDice = alchemistsFireDamage
alchemistfires.persDamage = alchemistsFirePersDamage
#alchemistfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistfires.splashDamage = bombSplashDamage
alchemistfires.persDamageType = Fire

alchemistbfires = BomberStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbfires.isWeapon = False
alchemistbfires.weaponDamageDice = alchemistsFireDamage
alchemistbfires.persDamage = alchemistsFirePersDamage
#alchemistbfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbfires.splashDamage = bombSplashDamage
alchemistbfires.persDamageType = Fire

alchemistbsfires = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbsfires.isWeapon = False
alchemistbsfires.weaponDamageDice = salchemistsFireDamage
alchemistbsfires.persDamage = salchemistsFirePersDamage
#alchemistbsfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbsfires.splashDamage = sbombSplashDamage
alchemistbsfires.stickybombLevel = 8
alchemistbsfires.persDamageType = Fire

alchemistbdfires = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbdfires.isWeapon = False
alchemistbdfires.weaponDamageDice = salchemistsFireDamage
alchemistbdfires.persDamage = salchemistsFirePersDamage
#alchemistbdfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbdfires.splashDamage = sbombSplashDamage
alchemistbdfires.persDamageType = Fire
alchemistbdfires.ignoreNextonMiss = True

alchemistpfires = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfires.isWeapon = False
alchemistpfires.weaponDamageDice = palchemistsFireDamage
alchemistpfires.persDamage = palchemistsFirePersDamage
#alchemistpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistpfires.splashDamage = pbombSplashDamage
alchemistpfires.persDamageType = Fire

alchemistbpfires = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfires.isWeapon = False
alchemistbpfires.weaponDamageDice = palchemistsFireDamage
alchemistbpfires.persDamage = palchemistsFirePersDamage
#alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpfires.splashDamage = pbombSplashDamage
alchemistbpfires.persDamageType = Fire

alchemistbpsfires = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpsfires.isWeapon = False
alchemistbpsfires.weaponDamageDice = palchemistsFireDamage
alchemistbpsfires.persDamage = palchemistsFirePersDamage
#alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpsfires.splashDamage = pbombSplashDamage
alchemistbpsfires.stickybombLevel = 8
alchemistbpsfires.persDamageType = Fire

alchemistbpdfires = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpdfires.isWeapon = False
alchemistbpdfires.weaponDamageDice = palchemistsFireDamage
alchemistbpdfires.persDamage = palchemistsFirePersDamage
#alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpdfires.splashDamage = pbombSplashDamage
alchemistbpdfires.persDamageType = Fire
alchemistbpdfires.ignoreNextonMiss = True

alchemistfrosts = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistfrosts.isWeapon = False
alchemistfrosts.weaponDamageDice = blfvDamage
alchemistfrosts.splashDamage = bombSplashDamage

alchemistbfrosts = BomberStrike(bombAttackBonus, alchemistRangedDamage)
alchemistbfrosts.isWeapon = False
alchemistbfrosts.weaponDamageDice = blfvDamage
alchemistbfrosts.splashDamage = bombSplashDamage

alchemistbsfrosts = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbsfrosts.isWeapon = False
alchemistbsfrosts.weaponDamageDice = sblfvDamage
alchemistbsfrosts.splashDamage = sbombSplashDamage
alchemistbsfrosts.stickybombLevel = 8
alchemistbsfrosts.persDamageType = Cold

alchemistbdfrosts = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbdfrosts.isWeapon = False
alchemistbdfrosts.weaponDamageDice = sblfvDamage
alchemistbdfrosts.splashDamage = sbombSplashDamage
alchemistbdfrosts.persDamageType = Cold
alchemistbdfrosts.ignoreNextonMiss = True

alchemistpfrosts = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfrosts.isWeapon = False
alchemistpfrosts.weaponDamageDice = pblfvDamage
alchemistpfrosts.splashDamage = pbombSplashDamage

alchemistbpfrosts = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfrosts.isWeapon = False
alchemistbpfrosts.weaponDamageDice = pblfvDamage
alchemistbpfrosts.splashDamage = pbombSplashDamage

alchemistbpsfrosts = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpsfrosts.isWeapon = False
alchemistbpsfrosts.weaponDamageDice = pblfvDamage
alchemistbpsfrosts.splashDamage = pbombSplashDamage
alchemistbpsfrosts.stickybombLevel = 8
alchemistbpsfrosts.persDamageType = Cold

alchemistbpdfrosts = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpdfrosts.isWeapon = False
alchemistbpdfrosts.weaponDamageDice = pblfvDamage
alchemistbpdfrosts.splashDamage = pbombSplashDamage
alchemistbpdfrosts.persDamageType = Cold
alchemistbpdfrosts.ignoreNextonMiss = True

alchemistlightnings = BombStrike(bombAttackBonus, alchemistRangedDamage)
alchemistlightnings.isWeapon = False
alchemistlightnings.setFFonCrit(1)
alchemistlightnings.setFFonSuccess(1)
alchemistlightnings.weaponDamageDice = blfvDamage
alchemistlightnings.splashDamage = bombSplashDamage

alchemistblightnings = BomberStrike(bombAttackBonus, alchemistRangedDamage)
alchemistblightnings.isWeapon = False
alchemistblightnings.setFFonCrit(1)
alchemistblightnings.setFFonSuccess(1)
alchemistblightnings.weaponDamageDice = blfvDamage
alchemistblightnings.splashDamage = bombSplashDamage

alchemistbslightnings = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbslightnings.isWeapon = False
alchemistbslightnings.setFFonCrit(1)
alchemistbslightnings.setFFonSuccess(1)
alchemistbslightnings.weaponDamageDice = sblfvDamage
alchemistbslightnings.splashDamage = sbombSplashDamage
alchemistbslightnings.stickybombLevel = 8
alchemistbslightnings.persDamageType = Electricity

alchemistbdlightnings = BomberStrike(sbombAttackBonus, alchemistRangedDamage)
alchemistbdlightnings.isWeapon = False
alchemistbdlightnings.setFFonCrit(1)
alchemistbdlightnings.setFFonSuccess(1)
alchemistbdlightnings.weaponDamageDice = sblfvDamage
alchemistbdlightnings.splashDamage = sbombSplashDamage
alchemistbdlightnings.persDamageType = Electricity
alchemistbdlightnings.ignoreNextonMiss= True

alchemistplightnings = BombStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistplightnings.isWeapon = False
alchemistplightnings.setFFonCrit(1)
alchemistplightnings.setFFonSuccess(1)
alchemistplightnings.weaponDamageDice = pblfvDamage
alchemistplightnings.splashDamage = pbombSplashDamage

alchemistbplightnings = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbplightnings.isWeapon = False
alchemistbplightnings.setFFonCrit(1)
alchemistbplightnings.setFFonSuccess(1)
alchemistbplightnings.weaponDamageDice = pblfvDamage
alchemistbplightnings.splashDamage = pbombSplashDamage

alchemistbpslightnings = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpslightnings.isWeapon = False
alchemistbpslightnings.setFFonCrit(1)
alchemistbpslightnings.setFFonSuccess(1)
alchemistbpslightnings.weaponDamageDice = pblfvDamage
alchemistbpslightnings.splashDamage = pbombSplashDamage
alchemistbpslightnings.stickybombLevel = 8
alchemistbpslightnings.persDamageType = Electricity

alchemistbpdlightnings = BomberStrike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpdlightnings.isWeapon = False
alchemistbpdlightnings.setFFonCrit(1)
alchemistbpdlightnings.setFFonSuccess(1)
alchemistbpdlightnings.weaponDamageDice = pblfvDamage
alchemistbpdlightnings.splashDamage = pbombSplashDamage
alchemistbpdlightnings.persDamageType = Electricity
alchemistbpdlightnings.ignoreNextonMiss

alchemistbestialClawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistbestialClawStrike.weaponDamageDice = bestialClawDamageDice

alchemistbestialJawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistbestialJawStrike.weaponDamageDice = bestialJawDamageDice

alchemistferalClawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistferalClawStrike.weaponDamageDice = feralClawDamageDice

alchemistferalJawStrike = MeleeStrike(mutagenstrikeAttackBonus, alchemistBestialDamage)
alchemistferalJawStrike.weaponDamageDice = feralJawDamageDice

alchemistDebilitatingBomb = DBombStrike(sbombAttackBonus)
alchemistPDebilitatingBomb = DBombStrike(pbombAttackBonus)

debilitatingFlatFootedSave = Save(alchemistDC,noneDamage)
debilitatingFlatFootedSave.isSpell = False
debilitatingFlatFootedSave.ffonFailLevel = 1

debilitatingDazzledSave = Save(alchemistDC,noneDamage)
debilitatingDazzledSave.isSpell = False
debilitatingDazzledSave.addConcealment = True

debilitatingClumsySave = Save(alchemistDC,noneDamage)
debilitatingClumsySave.isSpell = False
debilitatingClumsySave.goodClumsy = 1
debilitatingClumsySave.veryGoodClumsy = 1

debilitatingEnfeebledSave = Save(alchemistDC,noneDamage)
debilitatingEnfeebledSave.isSpell = False
debilitatingEnfeebledSave.goodEnfeebled = 1
debilitatingEnfeebledSave.veryGoodEnfeebled = 1

debilitatingStupifiedSave = Save(alchemistDC,noneDamage)
debilitatingStupifiedSave.isSpell = False
debilitatingStupifiedSave.goodStupified = 1
debilitatingStupifiedSave.veryGoodStupified = 1

debilitatingTrueClumsySave = Save(alchemistDC,noneDamage)
debilitatingTrueClumsySave.isSpell = False
debilitatingTrueClumsySave.goodClumsy = 2
debilitatingTrueClumsySave.veryGoodClumsy = 2

debilitatingTrueEnfeebledSave = Save(alchemistDC,noneDamage)
debilitatingTrueEnfeebledSave.isSpell = False
debilitatingTrueEnfeebledSave.goodEnfeebled = 2
debilitatingTrueEnfeebledSave.veryGoodEnfeebled = 2

debilitatingTrueStupifiedSave = Save(alchemistDC,noneDamage)
debilitatingTrueStupifiedSave.isSpell = False
debilitatingTrueStupifiedSave.goodStupified = 2
debilitatingTrueStupifiedSave.veryGoodStupified = 2

debilitatingTrueFlatFootedSave = TDSave(alchemistDC,noneDamage)
debilitatingTrueFlatFootedSave.isSpell = False
debilitatingTrueFlatFootedSave.ffonFailLevel = 1

debilitatingTrueDazzledSave = TDSave(alchemistDC,noneDamage)
debilitatingTrueDazzledSave.isSpell = False
debilitatingTrueDazzledSave.addConcealment = True

alchemistAttackSwitcher = {'Alchemist Melee Strike': [alchemistStrike],
                    'Alchemist Ranged Strike': [alchemistRangedStrike],
                    'Quicksilver Mutagen': [quicksilverMutagenBomb],
                    'Quicksilver Weapon Bonus': [quicksilverMutagenWeapon],
                    'Quicksilver Spell Bonus': [quicksilverMutagenSpellAttack],
                    'Energy Mutagen': [energyMutagen],
                    'Energy Mutagen Breath': [energyMutagenAttack],
                    'Powerful Energy Breath': [powerfulEnergyAttack],
                    'Elixir of Life': [elixirLife],
                    'Alchemist Bestial Claw': [alchemistbestialClawStrike],
                    'Alchemist Bestial Jaw': [alchemistbestialJawStrike],
                    'Alchemist Feral Claw': [alchemistferalClawStrike],
                    'Alchemist Feral Jaw': [alchemistferalJawStrike],
                    'Alchemist Acid Flask': [alchemistacids],
                    'Alchemist Bomber Acid': [alchemistbacids],
                    'Alchemist Sticky Acid': [alchemistbsacids],
                    'Alchemist Debilitating Acid': [alchemistbdacids],
                    'Alchemist Perpetual Acid': [alchemistpacids],
                    'Alchemist Bomber Perpetual Acid': [alchemistbpacids],
                    'Alchemist Sticky Perpetual Acid': [alchemistbpsacids],
                    'Alchemist Debilitating Perpetual Acid': [alchemistbpdacids],
                    'Alchemist Fire': [alchemistfires],
                    'Alchemist Bomber Fire': [alchemistbfires],
                    'Alchemist Sticky Fire': [alchemistbsfires],
                    'Alchemist Debilitating Fire': [alchemistbdfires],
                    'Alchemist Perpetual Fire': [alchemistpfires],
                    'Alchemist Bomber Perpetual Fire': [alchemistbpfires],
                    'Alchemist Sticky Perpetual Fire': [alchemistbpsfires],
                    'Alchemist Debilitating Perpetual Fire': [alchemistbpdfires],
                    'Alchemist Bottled Lightning': [alchemistlightnings],
                    'Alchemist Bomber Lightning': [alchemistblightnings],
                    'Alchemist Sticky Lightning': [alchemistbslightnings],
                    'Alchemist Debilitating Lightning': [alchemistbdlightnings],
                    'Alchemist Perpetual Lightning': [alchemistplightnings],
                    'Alchemist Bomber Perpetual Lightning': [alchemistbplightnings],
                    'Alchemist Sticky Perpetual Lightning': [alchemistbpslightnings],
                    'Alchemist Debilitating Perpetual Lightning': [alchemistbpdlightnings],
                    'Alchemist Frost Vial': [alchemistfrosts],
                    'Alchemist Bomber Frost': [alchemistbfrosts],
                    'Alchemist Sticky Frost': [alchemistbsfrosts],
                    'Alchemist Debilitating Frost': [alchemistbdfrosts],
                    'Alchemist Perpetual Frost': [alchemistpfrosts],
                    'Alchemist Bomber Perpetual Frost': [alchemistbpfrosts],
                    'Alchemist Sticky Perpetual Frost': [alchemistbpsfrosts],
                    'Alchemist Debilitating Perpetual Frost': [alchemistbpdfrosts],
                    'Debilitating Bomb': [alchemistDebilitatingBomb],
                    'Debilitating Perpetual': [alchemistPDebilitatingBomb],
                    'Debilitating Flat-Footed Save': [debilitatingFlatFootedSave],
                    'Debilitating Dazzled Save': [debilitatingDazzledSave],
                    'Debilitating Clumsy Save': [debilitatingClumsySave],
                    'Debilitating Enfeebled Save': [debilitatingEnfeebledSave],
                    'Debilitating Stupified Save': [debilitatingStupifiedSave],
                    'Debilitating True Flat-Footed Save': [debilitatingTrueFlatFootedSave],
                    'Debilitating True Dazzled Save': [debilitatingTrueDazzledSave],
                    'Debilitating True Clumsy 2 Save': [debilitatingTrueClumsySave],
                    'Debilitating True Enfeebled 2 Save': [debilitatingTrueEnfeebledSave],
                    'Debilitating True Stupified 2 Save': [debilitatingTrueStupifiedSave]}

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

dragonragebreath = Save(barbarianDC, noneDamage)
dragonragebreath.isSpell = False
dragonragebreath.weaponDamageDice = {i: i*[d6] for i in range(1,21)}
dragonragebreath.minL = 6
dragonragebreath2 = Save(barbarianDC, noneDamage)
dragonragebreath2.isSpell = False
dragonragebreath2.weaponDamageDice = {i: int(i/2)*[d6] for i in range(1,21)}
dragonragebreath2.minL = 6

barbAnimalThrash = CantripSave(barbarianDC, barbariananimaldamage)
barbAnimalThrash.targetSave = Fort
barbDragonThrash = CantripSave(barbarianDC, barbariandragondamage)
barbDragonThrash.targetSave = Fort
barbFuryThrash = CantripSave(barbarianDC, barbarianfurydamage)
barbFuryThrash.targetSave = Fort
barbGiantThrash = CantripSave(barbarianDC, barbariangiantdamage)
barbGiantThrash.targetSave = Fort
barbSpiritThrash = CantripSave(barbarianDC, barbarianspiritdamage)
barbSpiritThrash.targetSave = Fort

spiritsWrath = MeleeStrike(spiritswrathattackBonus,noneDamage)
spiritsWrath.veryGoodFrightened = 1
spiritsWrath.isWeapon = False
spiritsWrath.minL = 12
spiritsWrath.weaponDamageDice = {i: 4*[d8] for i in range(1,21)}

viciousEvisceration = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
viciousEvisceration.goodDrained = 1
viciousEvisceration.veryGoodDrained = 2

viciousEviscerationAnimal = MeleeStrike(martialAttackBonus, barbariananimaldamage, csLevel=5)
viciousEviscerationAnimal.goodDrained = 1
viciousEviscerationAnimal.veryGoodDrained = 2
viciousEviscerationAnimal.weaponDamageDice = animalJawDamageDice

viciousEviscerationDragon = MeleeStrike(martialAttackBonus, barbariandragondamage, csLevel=5)
viciousEviscerationDragon.goodDrained = 1
viciousEviscerationDragon.veryGoodDrained = 2

viciousEviscerationFury = MeleeStrike(martialAttackBonus, barbarianfurydamage, csLevel=5)
viciousEviscerationFury.goodDrained = 1
viciousEviscerationFury.veryGoodDrained = 2

viciousEviscerationGiant = MeleeStrike(martialAttackBonus, barbariangiantdamage, csLevel=5)
viciousEviscerationGiant.goodDrained = 1
viciousEviscerationGiant.veryGoodDrained = 2

viciousEviscerationSpirit = MeleeStrike(martialAttackBonus, barbarianspiritdamage, csLevel=5)
viciousEviscerationSpirit.goodDrained = 1
viciousEviscerationSpirit.veryGoodDrained = 2

barbarianAttackSwitcher = {'Barbarian Animal Claw': [barbariananimalclaws],
                    'Barbarian Animal Jaw': [barbariananimaljaws],
                    'Barbarian Dragon Strike': [barbariandragonstrike],
                    'Barbarian Fury Strike': [barbarianfurystrike],
                    'Barbarian Giant Strike': [barbariangiantstrike],
                    'Barbarian Spirit Strike': [barbarianspiritstrike],
                    'Barbarian Dragon Breath': [dragonragebreath],
                    'Barbarian Dragon Breath2': [dragonragebreath2],
                    'Barbarian Animal Thrash': [barbAnimalThrash],
                    'Barbarian Dragon Thrash': [barbDragonThrash],
                    'Barbarian Fury Thrash': [barbFuryThrash],
                    'Barbarian Giant Thrash': [barbGiantThrash],
                    'Barbarian Spirit Thrash': [barbSpiritThrash],
                    "Barbarian Spirit's Wrath": [spiritsWrath],
                    'Vicious Evisceration': [viciousEvisceration],
                    'Vicious Evisceration Animal': [viciousEviscerationAnimal],
                    'Vicious Evisceration Dragon': [viciousEviscerationDragon],
                    'Vicious Evisceration Fury': [viciousEviscerationFury],
                    'Vicious Evisceration Giant': [viciousEviscerationGiant],
                    'Vicious Evisceration Spirit': [viciousEviscerationSpirit]}


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

rangerprecedge = Effect()
rangerprecedge.addfirsthitdamageDice = rangerprecedgedamage1
rangerprecedge.addsecondhitdamageDice = rangerprecedgedamage2
rangerprecedge.addthirdhitdamageDice = rangerprecedgedamage3

rangerbearsupport = Effect()
rangerbearsupport.addeveryhitdamageDice = rangerbearsupportdamage

kistrike = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
kistrike.runeDamageDice = {i: int((3+sDice[i])/4)*[d6] for i in range(1,21)}

tigerclaw = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
tigerclaw.persDamageType  = Bleed
tigerclaw.critPersDamageDice = {i: [d4] for i in range(1,21)}

tigerslash = TigerSlash(martialAttackBonus, martialDamage, csLevel=5)
tigerslash.critPersDamageDice = {i: [d4] for i in range(1,21)}
tigerslash.persDamageType  = Bleed
for i in range(8,21):
    tigerslash.extraWeaponDice[i] = 1
    if i >=14:
        tigerslash.extraWeaponDice[i] = 2

kitigerclaw = MeleeStrike(martialAttackBonus, martialDamage, csLevel=5)
kitigerclaw.runeDamageDice = {i: int((3+sDice[i])/4)*[d6] for i in range(1,21)}
kitigerclaw.persDamageType  = Bleed
kitigerclaw.critPersDamageDice = {i: [d4] for i in range(1,21)}

handapp = MeleeStrike(cantripAttackBonus, strCasterDamage, csLevel=1)
handappitem = MeleeStrike(cantripAttackBonusItem, strCasterDamage, csLevel=1)

bespellweapon = Effect()
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

bestWild = TransformStrike(wildshapeAttackBonus, bestWildDamage)
bestWild.minAttack = bestWildAttack
bestWildR = TransformStrike(wildshapeAttackBonus, bestWildDamage)
bestWildR.minAttack = bestWildAttack
bestWildR.isWeapon = True

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
                       'Ki Strike': [kistrike],
                       'Tiger Claw': [tigerclaw],
               'Tiger Slash': [tigerslash],
               'Ki Tiger Claw': [kitigerclaw],
                       "Hand of the Apprentence": [handapp],
                       "Hand of the Apprentence +item": [handappitem],
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
                'Wildshape IncarnateR': [druidnatformR],
                'Ani-Elem-Mons-Inc': [bestWild],
                'Ani-Elem-Mons-IncR': [bestWildR]
                       }

cantripAS = CantripStrike(cantripAttackBonus, noneDamage)
cantripAS.weaponDamageDice = cantripASDamageDice
cantripAS.critPersDamage = cantripASPDamage
cantripAS.persDamageType = Acid

cantripEA = CantripSave(spellDC, noneDamage)
cantripEA.weaponDamageDice = cantripRFDamageDice

cantripD = CantripSave(spellDC, noneDamage)
cantripD.weaponDamageDice = cantripDDamageDice

cantripDL = CantripStrike(cantripAttackBonus, noneDamage)
cantripDL.weaponDamageDice = cantripRFDamageDice

cantripPF = CantripStrike(cantripAttackBonus, noneDamage)
cantripPF.weaponDamageDice = cantripRFDamageDice
cantripPF.critPersDamageDice = cantripPFPDamageDice
cantripPF.persDamageType = Fire

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

dcExtreme = creatureData['DC']['Extreme']
dcHigh = creatureData['DC']['High']
dcModerate = creatureData['DC']['Moderate']
aoeLimited = creatureData['AoE']['Limited']
aoeUnlimited = creatureData['AoE']['Unlimited']

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

monsterSEL = FixedSave(dcExtreme,aoeLimited)
monsterSEU = FixedSave(dcExtreme,aoeUnlimited)
monsterSHL = FixedSave(dcHigh,aoeLimited)
monsterSHU = FixedSave(dcHigh,aoeUnlimited)
monsterSML = FixedSave(dcModerate,aoeLimited)
monsterSMU = FixedSave(dcModerate,aoeUnlimited)
    
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
                  'Monster Low Attack Low Damage': [monsterLL],
                  'Monster Extreme DC Limited Damage': [monsterSEL],
                  'Monster Extreme DC Unlimited Damage': [monsterSEU],
                  'Monster High DC Limited Damage': [monsterSHL],
                  'Monster High DC Unlimited Damage': [monsterSHU],
                  'Monster Moderate DC Limited Damage': [monsterSML],
                  'Monster Moderate DC Unlimited Damage': [monsterSMU]
                  }

#effects
flatfoot = Effect()
flatfoot.flatfoot = True

flatfootnext = Effect()
flatfootnext.flatfootNextStrike = True

blur = Effect()
blur.addConcealment = True

invisibility = Effect()
invisibility.addHidden = True

removeConcealment = Effect()
removeConcealment.removeConcealment = True

addFortification = Effect()
addFortification.setFortification = True
addFortification.fortification = 20

addFortification2 = Effect()
addFortification2.setFortification = True
addFortification2.fortification = 35

removeFortification = Effect()
removeFortification.setFortification = True
removeFortification.fortification = 0

applyPersistent = ApplyPersistentDamage()

effectAttackSwitcher = {'Flat Foot Target': [flatfoot],
                        'Flat Foot Next Strike': [flatfootnext],
                        'Blur': [blur],
                        'Invisibility':[invisibility],
                        'Remove Concealment': [removeConcealment],
                        'Add Fortification': [addFortification],
                        'Add Fortification(Greater)': [addFortification2],
                        'Remove Fortification': [removeFortification],
                        'Apply Persistent Damage': [applyPersistent]}


magicmissle = AutoDamage(magicMissleDamage)
magicmissle.weaponDamageDice = magicMissleDamageDice
magicmissle.isSpell = True

truestrike = Effect()
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

basicr6 = Save(spellDC, noneDamage)
basicr6.weaponDamageDice = spellDamaged6
basicr6.targetSave = Reflex
basicr8 = Save(spellDC, noneDamage)
basicr8.weaponDamageDice = spellDamaged8
basicr8.targetSave = Reflex
basicr10 = Save(spellDC, noneDamage)
basicr10.weaponDamageDice = spellDamaged10
basicr10.targetSave = Reflex
basicr12 = Save(spellDC, noneDamage)
basicr12.weaponDamageDice = spellDamaged12
basicr12.targetSave = Reflex
basicr26 = Save(spellDC, noneDamage)
basicr26.weaponDamageDice = spellDamage2d6
basicr26.targetSave = Reflex
basicr261 = Save(spellDC, spellDamage1)
basicr261.weaponDamageDice = spellDamage2d6
basicr261.targetSave = Reflex
basicr262 = Save(spellDC, spellDamage2)
basicr262.weaponDamageDice = spellDamage2d6
basicr262.targetSave = Reflex
basicr28 = Save(spellDC, noneDamage)
basicr28.weaponDamageDice = spellDamage2d8
basicr28.targetSave = Reflex
basicr210 = Save(spellDC, noneDamage)
basicr210.weaponDamageDice = spellDamage2d10
basicr210.targetSave = Reflex
basicr212 = Save(spellDC, noneDamage)
basicr212.weaponDamageDice = spellDamage2d12
basicr212.targetSave = Reflex

basicf6 = Save(spellDC, noneDamage)
basicf6.weaponDamageDice = spellDamaged6
basicf6.targetSave = Fort
basicf8 = Save(spellDC, noneDamage)
basicf8.weaponDamageDice = spellDamaged8
basicf8.targetSave = Fort
basicf10 = Save(spellDC, noneDamage)
basicf10.weaponDamageDice = spellDamaged10
basicf10.targetSave = Fort
basicf12 = Save(spellDC, noneDamage)
basicf12.weaponDamageDice = spellDamaged12
basicf12.targetSave = Fort
basicf26 = Save(spellDC, noneDamage)
basicf26.weaponDamageDice = spellDamage2d6
basicf26.targetSave = Fort
basicf261 = Save(spellDC, spellDamage1)
basicf261.weaponDamageDice = spellDamage2d6
basicf261.targetSave = Fort
basicf262 = Save(spellDC, spellDamage2)
basicf262.weaponDamageDice = spellDamage2d6
basicf262.targetSave = Fort
basicf28 = Save(spellDC, noneDamage)
basicf28.weaponDamageDice = spellDamage2d8
basicf28.targetSave = Fort
basicf210 = Save(spellDC, noneDamage)
basicf210.weaponDamageDice = spellDamage2d10
basicf210.targetSave = Fort
basicf212 = Save(spellDC, noneDamage)
basicf212.weaponDamageDice = spellDamage2d12
basicf212.targetSave = Fort

basicw6 = Save(spellDC, noneDamage)
basicw6.weaponDamageDice = spellDamaged6
basicw6.targetSave = Will
basicw8 = Save(spellDC, noneDamage)
basicw8.weaponDamageDice = spellDamaged8
basicw8.targetSave = Will
basicw10 = Save(spellDC, noneDamage)
basicw10.weaponDamageDice = spellDamaged10
basicw10.targetSave = Will
basicw12 = Save(spellDC, noneDamage)
basicw12.weaponDamageDice = spellDamaged12
basicw12.targetSave = Will
basicw26 = Save(spellDC, noneDamage)
basicw26.weaponDamageDice = spellDamage2d6
basicw26.targetSave = Will
basicw261 = Save(spellDC, spellDamage1)
basicw261.weaponDamageDice = spellDamage2d6
basicw261.targetSave = Will
basicw262 = Save(spellDC, spellDamage2)
basicw262.weaponDamageDice = spellDamage2d6
basicw262.targetSave = Will
basicw28 = Save(spellDC, noneDamage)
basicw28.weaponDamageDice = spellDamage2d8
basicw28.targetSave = Will
basicw210 = Save(spellDC, noneDamage)
basicw210.weaponDamageDice = spellDamage2d10
basicw210.targetSave = Will
basicw212 = Save(spellDC, noneDamage)
basicw212.weaponDamageDice = spellDamage2d12
basicw212.targetSave = Will

hydralicpush = SpellStrike(cantripAttackBonus, noneDamage)
hydralicpush.doubleDamage  = False
hydralicpush.weaponDamageDice = {i: [d6] + spellDamage2d6[i] for i in range(1,21)}
hydralicpush.critDamageDice = {i: [d6,d6,d6] for i in range(1,21)}

shockinggrasp  =SpellStrike(cantripAttackBonus, noneDamage)
shockinggrasp.weaponDamageDice = {i: [d12]+spellDamaged12[i] for i in range(1,21)}

shockinggraspm  =SpellStrike(cantripAttackBonus, noneDamage)
shockinggraspm.weaponDamageDice = {i: [d12]+spellDamaged12[i] for i in range(1,21)}
shockinggraspm.persDamageDice = {i: [d4] for i in range(1,21)}
shockinggraspm.persDamage = {i: max(0,int((i-1)/2)) for i in range(1,21)}
shockinggraspm.doublePersDamage = False
shockinggraspm.persDamageType = Electricity

acidarror = SpellStrike(cantripAttackBonus, noneDamage)
acidarror.minSpellLevel = 2
acidarror.weaponDamageDice = {i: [d8] + int(sDice[i]/2)*[d8,d8] for i in range(3,21)}
acidarror.persDamageDice = {i: int(sDice[i]/2)*[d6] for i in range(3,21)}
acidarror.doublePersDamage = False
acidarror.persDamageType  = Acid

lightningbolt = Save(spellDC, noneDamage)
lightningbolt.minSpellLevel = 3
lightningbolt.weaponDamageDice = {i: [d12] + spellDamaged12[i] for i in range(5,21)}

chainlightning = Save(spellDC, noneDamage)
chainlightning.minSpellLevel = 6
chainlightning.weaponDamageDice = {i: [d12,d12] + spellDamaged12[i] for i in range(11,21)}

phantompain = Save(spellDC, noneDamage)
phantompain.doubleDamage = False
phantompain.doublePersDamage = False
phantompain.halveDamage = False
phantompain.weaponDamageDice = spellDamage2d4
phantompain.persDamageDice = spellDamaged4
phantompain.goodSickened = 1
phantompain.veryGoodSickened = 2
phantompain.targetSave = Will
phantompain.persDamageType = Mental

grimtendrils = Save(spellDC, noneDamage)
grimtendrils.weaponDamageDice = spellDamage2d4
grimtendrils.persDamage = spellDamage1
grimtendrils.targetSave = Fort
grimtendrils.persDamageType = Bleed

wallfire = AutoDamage(noneDamage)
wallfire.isSpell = True
wallfire.minSpellLevel = 4
wallfire.weaponDamageDice = spellDamaged6


phantasmalkiller = PKSave(spellDC, noneDamage)
phantasmalkiller.minSpellLevel = 4
phantasmalkiller.failureDamageDice = {i: [d6,d6,d6,d6] for i in range(1,21)}
phantasmalkiller.weaponDamageDice = spellDamage2d6
phantasmalkiller.critDamageDice = {i: sDice[i]*3*[d6] for i in range(1,21)}
phantasmalkiller.okayFrightened = 1
phantasmalkiller.goodFrightened = 2
phantasmalkiller.veryGoodFrightened = 4
phantasmalkiller.targetSave = Will

phantasmalcalamity = Save(spellDC, noneDamage)
phantasmalcalamity.minSpellLevel = 6
phantasmalcalamity.weaponDamageDice = {i: spellDamage2d6[i-2] + [d6] for i in range(11,21)}
phantasmalcalamity.targetSave = Will

spiritblast = Save(spellDC, noneDamage)
spiritblast.minSpellLevel = 6
spiritblast.weaponDamageDice = {i: spellDamage2d6[i] + 4*[d6] for i in range(11,21)}
spiritblast.targetSave = Fort

weird = Save(spellDC, noneDamage)
weird.minSpellLevel = 9
weird.weaponDamageDice = {i: 16*[d6] for i in range(17,21)}
weird.okayFrightened = 1
weird.goodFrightened = 2
weird.veryGoodFrightened = 2
weird.targetSave = Will

visionsdanger = Save(spellDC, noneDamage)
visionsdanger.minSpellLevel = 7
visionsdanger.weaponDamageDice = {i: [d8] + spellDamaged8[i] for i in range(13,21)}
visionsdanger.targetSave = Will

heal = AutoDamage(noneDamage)
heal.weaponDamageDice = spellDamaged8
heal2 = AutoDamage(spellDamage8)
heal2.weaponDamageDice = spellDamaged8
heal10 = AutoDamage(noneDamage)
heal10.weaponDamageDice = spellDamaged10
heal210 = AutoDamage(spellDamage8)
heal210.weaponDamageDice = spellDamaged10

harm = Save(spellDC, noneDamage)
harm.weaponDamageDice = spellDamaged8
harm.targetSave = Fort
harm10 = Save(spellDC, noneDamage)
harm10.weaponDamageDice = spellDamaged10
harm10.targetSave = Fort
warpriestHarm = Save(warpriestDC, noneDamage)
warpriestHarm.weaponDamageDice = spellDamaged8
warpriestHarm.targetSave = Fort
warpriestHarm10 = Save(warpriestDC, noneDamage)
warpriestHarm10.weaponDamageDice = spellDamaged10
warpriestHarm10.targetSave = Fort

dangeroussorcerery = Effect()
dangeroussorcerery.isSpell = True
dangeroussorcerery.addDamage = spellDamage1

debuffAttack123 = Save(spellDC, noneDamage)
debuffAttack123.isSpell = False
debuffAttack123.okayDebuffAttack = 1
debuffAttack123.goodDebuffAttack = 2
debuffAttack123.veryGoodFailDebuffAttack = 3
debuffAttack123.targetSave = Will

debuffAttack012 = Save(spellDC, noneDamage)
debuffAttack012.isSpell = False
debuffAttack012.okayDebuffAttack = 0
debuffAttack012.goodDebuffAttack = 1
debuffAttack012.veryGoodFailDebuffAttack = 2
debuffAttack012.targetSave = Will

frightenedSave123 = Save(spellDC, noneDamage)
frightenedSave123.isSpell = False
frightenedSave123.okayFrightened = 1
frightenedSave123.goodFrightened = 2
frightenedSave123.veryGoodFrightened = 3
frightenedSave123.targetSave = Will

frightenedSave012 = Save(spellDC, noneDamage)
frightenedSave012.isSpell = False
frightenedSave012.okayFrightened = 0
frightenedSave012.goodFrightened = 1
frightenedSave012.veryGoodFrightened = 2
frightenedSave012.targetSave = Will

disintigrateAttack = SpellStrikeFilter(cantripAttackBonus,noneDamage)
disintigrateSave = Save(spellDC, noneDamage)
disintigrateSave.minSpellLevel = 6
disintigrateSave.weaponDamageDice = spellDamage2d12
disintigrateSave.targetSave = Fort

enfeebleSave123 = Save(spellDC, noneDamage)
enfeebleSave123.isSpell = False
enfeebleSave123.okayEnfeebled = 1
enfeebleSave123.goodEnfeebled = 2
enfeebleSave123.veryGoodEnfeebled = 3
enfeebleSave123.targetSave = Fort

fingerofdeath = Save(spellDC, spellDamage10)
fingerofdeath.minSpellLevel = 7
fingerofdeath.targetSave = Fort

meteorSwarm = Save(spellDC, noneDamage)
meteorSwarm.weaponDamageDice = {i: (sDice[i]-9)*[d10,d6,d6] + 6*[d10] + 14*[d6] for i in range(17,21)}
meteorSwarm.minSpellLevel = 9

polarRay = SpellStrike(cantripAttackBonus, noneDamage)
polarRay.minSpellLevel = 8
polarRay.goodDrained = 2
polarRay.veryGoodDrained = 2
polarRay.doubleDamage = False
polarRay.weaponDamageDice = {i: (sDice[i]-8)*[d8,d8] + 10*[d8] for i in range(15,21)}

horridWilting = Save(spellDC, noneDamage)
horridWilting.minSpellLevel = 8
horridWilting.weaponDamageDice = {i: spellDamaged10[i] + [d10,d10] for i in range(15,21)}
horridWilting.targetSave = Fort

eclipseBurst = Save(spellDC, noneDamage)
eclipseBurst.minSpellLevel = 7
eclipseBurst.weaponDamageDice = {i: spellDamaged10[i]+[d10]+spellDamaged4[i]+[d4] for i in range(13,21)}

sunburst = Save(spellDC, noneDamage)
sunburst.minSpellLevel = 7
sunburst.weaponDamageDice = {i: spellDamaged10[i]+[d10]+spellDamaged10[i]+[d10] for i in range(13,21)}
sunburst.doubleDamage = False

flamingSphere = Save(spellDC, noneDamage)
flamingSphere.minSpellLevel = 2
flamingSphere.weaponDamageDice = {i: spellDamaged6[i] + [d6] for i in range(3,21)}
flamingSphere.damageOnSuccesSave = False

spiritualWeapon = CantripStrike(cantripAttackBonus, noneDamage)
spiritualWeapon.isSpell = True
spiritualWeapon.minSpellLevel = 2
spiritualWeapon.weaponDamageDice = {i: int(sDice[i]/2)*[d8] for i in range(3,21)}

searingLight = SpellStrike(cantripAttackBonus, noneDamage)
searingLight.minSpellLevel = 3
searingLight.weaponDamageDice = {i: (sDice[i]-3)*[d6,d6] + 5*[d6] for i in range(5,21)}
searingLight2 = SpellStrike(cantripAttackBonus, noneDamage)
searingLight2.minSpellLevel = 3
searingLight2.weaponDamageDice = {i: (sDice[i]-3)*[d6,d6,d6,d6] + 10*[d6] for i in range(5,21)}

holyCascade = Save(spellDC, noneDamage)
holyCascade.weaponDamageDice = {i: (sDice[i]-4)*[d6] + 3*[d6] for i in range(7,21)}
holyCascade.minSpellLevel = 4
holyCascade2 = Save(spellDC, noneDamage)
holyCascade2.weaponDamageDice = {i: (sDice[i]-4)*3*[d6] + 9*[d6] for i in range(7,21)}
holyCascade2.minSpellLevel = 4

divineWrath = Save(spellDC, noneDamage)
divineWrath.minSpellLevel = 4
divineWrath.weaponDamageDice = spellDamaged10
divineWrath.targetSave = Fort
divineWrath.goodSickened = 1
divineWrath.veryGoodSickened = 2

heroismBonus = {i: int(sDice[i]/3) for i in range(1,21)}
heroism = Effect()
heroism.isSpell = True
heroism.addAttack = heroismBonus

spellAttackSwitcher = {'Basic Reflex 1d6': [basicr6],
                       'Basic Reflex 1d8': [basicr8],
                       'Basic Reflex 1d10': [basicr10],
                       'Basic Reflex 1d12': [basicr12],
                       'Basic Reflex 2d6': [basicr26],
                'Basic Reflex 2d6+1': [basicr261],
                'Basic Reflex 2d6+2': [basicr262],
                'Basic Reflex 2d8': [basicr28],
                'Basic Reflex 2d10': [basicr210],
                'Basic Reflex 2d12': [basicr212],
                'Basic Fort 1d6': [basicf6],
                       'Basic Fort 1d8': [basicf8],
                       'Basic Fort 1d10': [basicf10],
                       'Basic Fort 1d12': [basicf12],
                       'Basic Fort 2d6': [basicf26],
                'Basic Fort 2d6+1': [basicf261],
                'Basic Fort 2d6+2': [basicf262],
                'Basic Fort 2d8': [basicf28],
                'Basic Fort 2d10': [basicf210],
                'Basic Fort 2d12': [basicf212],
                'Basic Will 1d6': [basicw6],
                       'Basic Will 1d8': [basicw8],
                       'Basic Will 1d10': [basicw10],
                       'Basic Will 1d12': [basicw12],
                       'Basic Will 2d6': [basicw26],
                'Basic Will 2d6+1': [basicw261],
                'Basic Will 2d6+2': [basicw262],
                'Basic Will 2d8': [basicw28],
                'Basic Will 2d10': [basicw210],
                'Basic Will 2d12': [basicw212],
                
                'Magic Missle': [magicmissle],
                'True Strike': [truestrike],
                'Heal': [heal],
                'd10 Heal': [heal10],
                '2action Heal': [heal2],
                '2action d10 Heal': [heal210],
                'Harm':[harm],
                'd10 Harm':[harm10],
                'Warpriest Harm':[warpriestHarm],
                'Warpriest d10 Harm':[warpriestHarm10],
                'Dangerous Sorcery': [dangeroussorcerery],
                'Phantom Pain': [phantompain],
                'Grim Tendrils': [grimtendrils],
                'Shocking Grasp': [shockinggrasp],
                'Shocking Grasp Metal': [shockinggraspm],
                'Hydralic Push': [hydralicpush],
                'Acid Arrow': [acidarror],
                'Flaming Sphere': [flamingSphere],
                'Spiritual Weapon': [spiritualWeapon],
                'Searing Light': [searingLight],
                'Searing Light vs Fiend': [searingLight2],
                'Lightning Bolt': [lightningbolt],
                'Holy Cascade': [holyCascade],
                'Holy Cascade vs Fiend': [holyCascade2],
                'Divine Wrath': [divineWrath],
                'Phantasmal Killer': [phantasmalkiller],
                'Pantasmal Calamity': [phantasmalcalamity],
                'Spirit Blast': [spiritblast],
                'Weird': [weird],
                'Visions of Danger': [visionsdanger],
                'Wall of Fire': [wallfire],
                'Fear: Debuff Attacker(123)': [debuffAttack123],
                'Fear: Debuff Target(123)': [frightenedSave123],
                'Debuff Attacker(012)': [debuffAttack012],
                'Debuff Target(012)': [frightenedSave012],
                'Disintigrate Attack': [disintigrateAttack],
                'Disintigrate Save': [disintigrateSave],
                'Enfeeblement Attack': [disintigrateAttack],
                'Enfeeblement Save': [enfeebleSave123],
                'Finger of Death': [fingerofdeath],
                'Meteor Swarm': [meteorSwarm],
                'Polar Ray':[polarRay],
                'Horrid Wilting': [horridWilting],
                'Eclipse Burst': [eclipseBurst],
                'Sunburst': [sunburst],
                'Heroism': [heroism]
                }

elementalToss = SpellStrike(cantripAttackBonus, spellDamage1)
elementalToss.weaponDamageDice = spellDamaged8

fireRay = SpellStrike(cantripAttackBonus, noneDamage)
fireRay.weaponDamageDice = spellDamage2d6
fireRay.critPersDamageDice = spellDamaged4
fireRay.persDamageType = Fire

tempestSurge = Save(spellDC, noneDamage)
tempestSurge.weaponDamageDice = spellDamaged6
tempestSurge.goodClumsy  = 2
tempestSurge.veryGoodClumsy = 2
tempestSurge.persDamage  = spellDamage1
tempestSurge.persDamageType = Electricity
focusSpellAttackSwitcher = {'Elemental Toss': [elementalToss],
                            'Fire Ray': [fireRay],
                            'Force Bolt': [magicmissle],
                            'Tempest Surge': [tempestSurge]
        }

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
shardness = {i: 5 for i in range(1,21)}
for i in shardness:
    if i >= 4:
        shardness[i] = 8
    if i >= 7:
        shardness[i] = 10
    if i >= 10:
        shardness[i] = 13
    if i >= 13:
        shardness[i] = 15
    if i >= 16:
        shardness[i] = 17
    if i >= 19:
        shardness[i] = 20
shp = {i: 20 for i in range(1,21)}
for i in shp:
    if i >= 4:
        shp[i] = 64
    if i >= 7:
        shp[i] = 80
    if i >= 10:
        shp[i] = 104
    if i >= 13:
        shp[i] = 120
    if i >= 16:
        shp[i] = 136
    if i >= 19:
        shp[i] = 160
studyhardness = AutoDamage(shardness)
studyhp = AutoDamage(shp)

itemSwitcher = {
    'Study Shield Hardness': [studyhardness],
    'Sturdy Shield HP': [studyhp]}

targetEAC = Effect()
targetEAC.targetAC = creatureData['AC']['Extreme']
targetHAC = Effect()
targetHAC.targetAC = creatureData['AC']['High']
targetMAC = Effect()
targetMAC.targetAC = creatureData['AC']['Moderate']
targetLAC = Effect()
targetLAC.targetAC = creatureData['AC']['Low']

targetFighterAC = Effect()
targetFighterAC.targetAC = creatureData['AC']['Moderate']

targetWizardAC = Effect()
targetWizardAC.targetAC = creatureData['AC']['Moderate']

targetRogueAC = Effect()
targetRogueAC.targetAC = creatureData['AC']['Moderate']

targetDexMonkAC = Effect()
targetDexMonkAC.targetAC = creatureData['AC']['Moderate']

targetChampionAC = Effect()
targetChampionAC.targetAC = creatureData['AC']['Moderate']

targetEF = Effect()
targetEF.targetFort = creatureData['Saves']['Extreme']
targetHF = Effect()
targetHF.targetFort = creatureData['Saves']['High']
targetMF = Effect()
targetMF.targetFort = creatureData['Saves']['Moderate']
targetLF = Effect()
targetLF.targetFort = creatureData['Saves']['Low']
targetTF = Effect()
targetTF.targetFort = creatureData['Saves']['Terrible']

targetER = Effect()
targetER.targetRef = creatureData['Saves']['Extreme']
targetHR = Effect()
targetHR.targetRef = creatureData['Saves']['High']
targetMR = Effect()
targetMR.targetRef = creatureData['Saves']['Moderate']
targetLR = Effect()
targetLR.targetRef = creatureData['Saves']['Low']
targetTR = Effect()
targetTR.targetRef = creatureData['Saves']['Terrible']

targetEW = Effect()
targetEW.targetWill = creatureData['Saves']['Extreme']
targetHW = Effect()
targetHW.targetWill = creatureData['Saves']['High']
targetMW = Effect()
targetMW.targetWill = creatureData['Saves']['Moderate']
targetLW = Effect()
targetLW.targetWill = creatureData['Saves']['Low']
targetTW = Effect()
targetTW.targetWill = creatureData['Saves']['Terrible']

targetEP = Effect()
targetEP.targetPer = creatureData['Saves']['Extreme']
targetHP = Effect()
targetHP.targetPer = creatureData['Saves']['High']
targetMP = Effect()
targetMP.targetPer = creatureData['Saves']['Moderate']
targetLP = Effect()
targetLP.targetPer = creatureData['Saves']['Low']
targetTP = Effect()
targetTP.targetPer = creatureData['Saves']['Terrible']



targetSwitcher = {
    'Target Extreme AC': [targetEAC],
                 'Target High AC': [targetHAC],
                 'Target Moderate AC': [targetMAC],
                 'Target Low AC': [targetLAC],
                 'Target Fighter AC': [targetFighterAC],
                 'Target Wizard AC': [targetWizardAC],
                 'Target DexMonk AC': [targetDexMonkAC],
                 'Target Rogue AC': [targetRogueAC],
                 'Target Champion AC': [targetChampionAC],
                 'Target Extreme Fort': [targetEF],
                 'Target High Fort': [targetHF],
                 'Target Moderate Fort': [targetMF],
                 'Target Low Fort': [targetLF],
                 'Target Terrible Fort': [targetTF],
                 'Target Extreme Ref': [targetER],
                 'Target High Ref': [targetHR],
                 'Target Moderate Ref': [targetMR],
                 'Target Low Ref': [targetLR],
                 'Target Terrible Ref': [targetTR],
                 'Target Extreme Will': [targetEW],
                 'Target High Will': [targetHW],
                 'Target Moderate Will': [targetMW],
                 'Target Low Will': [targetLW],
                 'Target Terrible Will': [targetTW],
                 'Target Extreme Per': [targetEP],
                 'Target High Per': [targetHP],
                 'Target Moderate Per': [targetMP],
                 'Target Low Per': [targetLP],
                 'Target Terrible Per': [targetTP]}

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
                  **focusSpellAttackSwitcher,
                  **skillAttackSwitcher,
                  **itemSwitcher,
                  **targetSwitcher}