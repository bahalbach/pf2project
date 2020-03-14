import copy
from pf2calc import Selector, CombinedAttack, createTraces, createLevelTraces, createDamageDistribution, creatureData
import plotly.graph_objects as go
from ipywidgets import widgets

levelDiff = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Level difference:',
    #continuous_update=False
)
attackBonus = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Attack bonus:',
    #continuous_update=False
)
damageBonus = widgets.BoundedIntText(
    value=0.0,
    min=-20.0,
    max=50.0,
    step=1.0,
    description='Damage bonus:',
    #continuous_update=False
)
weakness = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Weakness:',
    #continuous_update=False
)

targetACSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low'],
    value='Moderate',
    description='Target AC:'
)

targetSavesSelector = widgets.Dropdown(
#    options=['average bestiary high',
#             'average bestiary mid',
#             'average bestiary low',
#             'average bestiary fort',
#             'average bestiary ref',
#             'average bestiary will',
    options=['Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    description='Target Save:'
)

def targetACChangedResponse(change):
    Selector.changeTargetAC(targetACSelector.value)
    updateEDBLGraph()  

def targetSavesChangedResponse(change):
    Selector.changeTargetSaves(targetSavesSelector.value)
    updateEDBLGraph() 

flatfootedBox = widgets.BoundedIntText(
    value=0,
    min=0,
    max=100.0,
    description='flat footed percent',
    disabled=False
)

persistentDamageWeightBox = widgets.BoundedFloatText(
    value=2,
    min=0,
    max=10.0,
    description='Persistent Damage Weight',
    disabled=False
)

applyDebuffs = widgets.Checkbox(
        value=True,
        description="Apply Debuffs"
)

percentageView = widgets.Dropdown(
        options = ['Expected Damage',
                   'Percent of First Selection',
                   'Percent of High HP',
                   'Percent of Moderate HP',
                   'Percent of Low HP',
                   'Expected Persistent Damage',
                   'Number of Hits',
                   'Number of Crits',
                   'Number of Hits+Crits'],
        value='Expected Damage'
)

byLevelView = widgets.Checkbox(
        value=False,
        description="By Level View"
)

levelSelector = widgets.IntSlider(
        value=1,
        min=1,
        max=20,
        step=1,
        continuous_update=False
)

levelViewSelector = widgets.Dropdown(
        options = ['Expected Damage by AC',
                   'Damage Distribution',
                   'Cumulative Distribution'],
        value='Expected Damage by AC'
)


abilityScoreOptions = ['10 No Boost',
                       '12 No Boost',
                       '14 No Boost',
                       '16 No Boost',
                       '18 No Boost',
                       '10 to  18',
                       '12 to 18',
                       '14 to 18',
                       '16 to 18',
                       '14 to 20 No Apex',
                       '16 to 20 No Apex',
                       '18 to 22 No Apex',
                       '14 to 20 Apex',
                       '16 to 20 Apex',
                       '18 to 22 Apex'
                       ]
abilityScoreOptionName = {'10 No Boost':"10",
                       '12 No Boost':"12",
                       '14 No Boost':"14",
                       '16 No Boost':"16",
                       '18 No Boost':"18",
                       '10 to 18':"10+",
                       '12 to 18':"12+",
                       '14 to 18':"14+",
                       '16 to 18':"16+",
                       '14 to 20 No Apex':"14++",
                       '16 to 20 No Apex':"16++",
                       '18 to 22 No Apex':"18++",
                       '14 to 20 Apex':"14a",
                       '16 to 20 Apex':"16a",
                       '18 to 22 Apex':"18a"
                       }
primaryAbilityScore = widgets.Dropdown(
        description = 'Attack Ability Score',
        options=abilityScoreOptions,
        value='18 to 22 Apex'
)
secondaryAbilityScore = widgets.Dropdown(
        description = 'Damage Ability Score',
        options=abilityScoreOptions,
        value='18 to 22 Apex'
)

mapOptions=['x0 = 0',
            'x1 = -5',
            'x1 = -4',
            'x1 = -3',
            'x1 = -2',
            'x1 = -1',
            'x2 = -10',
            'x2 = -8',
            'x2 = -6',
            'x2 = -4',
            'x2 = -2'
            ]
mapSelection = widgets.Dropdown(
        description = 'MAP',
        options=mapOptions,
        value='x0 = 0')

attackModifier = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Attack Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

additionalDamage = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Additional Damage:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

damageModifier = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Damage Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

levelLimiter = widgets.IntRangeSlider(
    value=[1, 20],
    min=1,
    max=20,
    step=1,
    description = 'Level Range',
    layout=widgets.Layout(width='auto')
)

spellLevelSelector = widgets.Dropdown(
        description='Spell Level:',
        options=['Max',
                 '-1',
                 '-2',
                 '-3',
                 '-4',
                 '-5',
                 '1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 '10'],
        value='Max')

weaponLabel = widgets.Label(
        value="Weapon:"
)

weaponDamageDie = widgets.Dropdown(
        options=["1d4",
                       "1d6",
                       "1d8",
                       "1d10",
                       "1d12",
                       "1d4+1",
                       "1d6+1",
                       "1d8+1",
                       "1d10+1",
                       "1d12+1",
                       "1d4+2",
                       "1d6+2",
                       "1d8+2",
                       "1d10+2",
                       "1d12+2"],
        value="1d8",
        layout=widgets.Layout(width='auto')
)

weaponCritical = widgets.Dropdown(
        options=["No Crit Damage",
                 "deadly d6",
                 "deadly d8",
                 "deadly d10",
                 "deadly d12",
                 "fatal d8",
                 "fatal d10",
                 "fatal d12"],
        value="No Crit Damage",
        layout=widgets.Layout(width='auto')
)

criticalSpecialization = widgets.Dropdown(
        options=["other",
                 "knife",
                 "hammer",
                 "pick",
                 "sword"],
        value="other",
        layout=widgets.Layout(width='auto')
)

featureOptions = ["1d6 Rune",
                 "1d4 Rune",
                 "backswing",
                 "keen",
                 "sticky bomb"]

featureSelection1 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel1 = widgets.IntText(
    value=8.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection2 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel2 = widgets.IntText(
    value=15.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection3 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel3 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection4 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel4 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection5 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel5 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection6 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel6 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection7 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel7 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
featureSelection8 = widgets.Dropdown(
        options=featureOptions,
        value="1d6 Rune",
        layout=widgets.Layout(width='auto')
)
featureLevel8 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

elementalRunesLabel = widgets.Label(
        value="Elemental Damage Rune Levels"
)

elementalRune1 = widgets.IntText(
    value=8.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune2 = widgets.IntText(
    value=15.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune3 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune4 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

classSelector = widgets.Dropdown(
        options=["Alchemist",
                 "Barbarian",
                 "Bard", 
                 "Champion",
                 "Cleric",
                 "Druid",
                 "Fighter",
                 "Monk",
                 "Ranger",
                 "Rogue",
                 "Sorcerer",
                 "Wizard",
                 "Animal Companion",
                 "Cantrips",
                 "Spells",
                 "Skills",
                 "Caster Strikes",
                 "Martial Strikes",
                 "Monster",
                 "Effects"],
        value="Fighter",
        layout=widgets.Layout(width='auto')
)
alchemistOptions = ['Alchemist Melee Strike',
                    'Alchemist Ranged Strike',
                    'Alchemist Bestial Claw',
                    'Alchemist Bestial Jaw',
                    'Alchemist Feral Claw',
                    'Alchemist Feral Jaw',
                    'Alchemist Acid Flask',
                    'Alchemist Bomber Acid',
                    'Alchemist Sticky Acid',
                    'Alchemist Perpetual Acid',
                    'Alchemist Bomber Perpetual Acid',
                    'Alchemist Sticky Perpetual Acid',
                    'Alchemist Fire',
                    'Alchemist Bomber Fire',
                    'Alchemist Sticky Fire',
                    'Alchemist Perpetual Fire',
                    'Alchemist Bomber Perpetual Fire',
                    'Alchemist Sticky Perpetual Fire',
                    'Alchemist Bottled Lightning',
                    'Alchemist Bomber Lightning',
                    'Alchemist Sticky Lightning',
                    'Alchemist Perpetual Lightning',
                    'Alchemist Bomber Perpetual Lightning',
                    'Alchemist Sticky Perpetual Lightning',
                    'Alchemist Frost Vial',
                    'Alchemist Bomber Frost',
                    'Alchemist Sticky Frost',
                    'Alchemist Perpetual Frost',
                    'Alchemist Bomber Perpetual Frost',
                    'Alchemist Sticky Perpetual Frost']
barbarianOptions = ['Martial Strike',
                    'Barbarian Animal Claw',
                    'Barbarian Animal Jaw',
                    'Barbarian Dragon Strike',
                    'Barbarian Fury Strike',
                    'Barbarian Giant Strike',
                    'Barbarian Spirit Strike'
                    ]
bardOptions = ['Caster Strike']
championOptions = ['Martial Strike',
                   'Champion Smite Evil']
cantripOptions = ['Acid Splash',
                  'Electric Arc',
                  'Daze',
                  'Divine Lance',
                  'Produce Flame',
                  'Ray of Frost',
                  'Telekinetic Projectile']
casterstrikeOptions = ['Caster Strike',
                       'Caster Ranged Strike',
                       'Caster Propulsive']
clericOptions = ['Caster Strike',
                 'Warpriest Strike',
                 'Warpriest Smite',
                 'Bespell Weapon',
                 'Warpriest Harm',
                 'Warpriest d10 Harm']
druidOptions = ['Caster Strike',
                'Wildshape Animal',
                'Wildshape Insect',
                'Wildshape Dino',
                'Wildshape Aerial',
                'Wildshape Elemental',
                'Wildshape Plant',
                'Wildshape Dragon',
                'Wildshape Monster',
                'Wildshape Incarnate',
                'Wildshape AnimalR',
                'Wildshape InsectR',
                'Wildshape DinoR',
                'Wildshape AerialR',
                'Wildshape ElementalR',
                'Wildshape PlantR',
                'Wildshape DragonR',
                'Wildshape MonsterR',
                'Wildshape IncarnateR'
                ]
fighterOptions = ['Fighter Melee Strike',
                  'Fighter Exacting Strike',
             'Fighter Snagging Strike',
             'Fighter Certain Strike',
             'Fighter Power Attack',
             'Fighter Brutish Shove',
             'Fighter Knockdown',
             'Fighter Brutal Finish',
             'Fighter Propulsive',
             'Fighter Propulsive es',
             'Fighter Propulsive cs'
             ]
martialstrikeOptions = ['Martial Strike',
                        'Martial Ranged Strike',
                        'Martial Propulsive']
monkOptions = ['Martial Strike']
rangerOptions = ['Ranger Precision Edge',
                 'Ranger Bear Support',
                 'Martial Strike',
                        'Martial Ranged Strike',
                        'Martial Propulsive']
rogueOptions = ['Rogue Strike',
                'Flat Foot Next Strike',
                'Scoundrel Feint']
sorcererOptions = ['Caster Strike',
                   'Bespell Weapon']
wizardOptions = ['Caster Strike',
                 'Bespell Weapon']
animalcompanionOptions = ['Druid Bear',
                          'Druid Wolf',
                          'Ranger Bear',
                          'Ranger Wolf']
monsterOptions = ['Monster Extreme Attack High Damage',
                  'Monster Extreme Attack Moderate Damage',
                  'Monster High Attack Extreme Damage',
                  'Monster High Attack High Damage',
                  'Monster High Attack Moderate Damage',
                  'Monster High Attack Low Damage',
                  'Monster Moderate Attack Extreme Damage',
                  'Monster Moderate Attack High Damage',
                  'Monster Moderate Attack Moderate Damage',
                  'Monster Moderate Attack Low Damage',
                  'Monster Low Attack High Damage',
                  'Monster Low Attack Moderate Damage',
                  'Monster Low Attack Low Damage'   
                  ]
effectOptions = ['Flat Foot Target',
                 'Flat Foot Next Strike']
spellOptions = ['Dangerous Sorcery',
                'Basic Save 1d8',
                'Basic Save 1d10',
                'Basic Save 2d6',
                'Basic Save 2d6+1',
                'Basic Save 2d6+2',
                'Magic Missle',
                'True Strike',
                'Phantom Pain',
                'Grim Tendrils',
                'Shocking Grasp',
                'Shocking Grasp Metal',
                'Hydralic Push',
                'Acid Arrow',
                'Lightning Bolt',
                'Wall of Fire',
                'Phantasmal Killer',
                'Pantasmal Calamity',
                'Spirit Blast',
                'Visions of Danger',
                'Weird',
                'Fear: Debuff Attacker(123)',
                'Fear: Debuff Target(123)',
                'Debuff Attacker(012)',
                'Debuff Target(012)',
                'Disintigrate Attack',
                'Disintigrate Save',
                'Enfeeblement Save',
                'Summon Animal',
                'Summon Dragon']
skillOptions = ['Trained Feint',
                'Max Feint',
                'Trained Demoralize',
                'Max Demoralize',
                'Scare to Death']

selectionSwitcher = {"Alchemist": alchemistOptions, 
                     "Barbarian": barbarianOptions,
                     "Bard": bardOptions,
                     "Cantrips": cantripOptions,
                     "Caster Strikes": casterstrikeOptions,
                     "Champion": championOptions,
                     "Cleric": clericOptions,
                     "Druid": druidOptions,
                     "Fighter": fighterOptions,
                     "Monk": monkOptions,
                     "Martial Strikes": martialstrikeOptions,
                     "Ranger": rangerOptions,
                     "Rogue": rogueOptions,
                     "Sorcerer": sorcererOptions,
                     "Wizard": wizardOptions,
                     "Animal Companion": animalcompanionOptions,
                     "Monster": monsterOptions,
                     "Effects": effectOptions,
                     "Spells": spellOptions,
                     "Skills": skillOptions}


selector = widgets.SelectMultiple(
    options=fighterOptions,
    value=[fighterOptions[0]],
    description='Selection:',
    layout=widgets.Layout(width='auto', height='100%'),
    disabled=False,
)

def classSelectorResponse(b):
    selector.options = selectionSwitcher[classSelector.value]
    #selector.value = [selector.options[0]]

selections = widgets.SelectMultiple(
    options=[],
    # rows=10,
    description='Current selections:',
    layout=widgets.Layout(width='80%', height='100%'),
    disabled=False
)

selectorAddButton = widgets.Button(description="Add Selections")
def on_addSelection_clicked(b):
    #add to selections
    for s in selector.value:
        name = s
        if Selector.shouldAddPrimary(s):
            name+= " " + abilityScoreOptionName[primaryAbilityScore.value]
        if Selector.shouldAddSecondary(s):
            name+=abilityScoreOptionName[secondaryAbilityScore.value]
        if Selector.shouldAddSpellLevel(s):
            name += spellLevelSelector.value
        if Selector.shouldAddWeaponDamage(s):
            name += " " + weaponDamageDie.value
        if not weaponCritical.value == "No Crit Damage" and Selector.isWeapon(s):
            name += " " + weaponCritical.value
        if not criticalSpecialization.value == "other" and Selector.isWeapon(s):
            name += " " + criticalSpecialization.value
        if attackModifier.value != 0:
            if attackModifier.value > 0:
                name += " +"
            else:
                name += " "
            name += str(attackModifier.value) + "a"
        if additionalDamage.value != 0:
            if additionalDamage.value > 0:
                name += " +"
            else:
                name += " "
            name += str(additionalDamage.value) + "ad"
        if damageModifier.value != 0:
            if damageModifier.value > 0:
                name += " +"
            else:
                name += " "
            name += str(damageModifier.value) + "d"
        minLevel = levelLimiter.value[0]
        maxLevel = levelLimiter.value[1]
        weaponFeatures = [
                [featureSelection1.value,featureLevel1.value],
                [featureSelection2.value,featureLevel2.value],
                [featureSelection3.value,featureLevel3.value],
                [featureSelection4.value,featureLevel4.value],
                [featureSelection5.value,featureLevel5.value],
                [featureSelection6.value,featureLevel6.value],
                [featureSelection7.value,featureLevel7.value],
                [featureSelection8.value,featureLevel8.value]
                ]
        if not (name in selections.options):
            selections.options += (name,)
            Selector.addSelection(name,
                                  s,
                                  primaryAbilityScore.value,
                                  secondaryAbilityScore.value,
                                  mapSelection.value,
                                  attackModifier.value,
                                  damageModifier.value,
                                  additionalDamage.value,
                                  spellLevelSelector.value,
                                  weaponDamageDie.value,
                                  weaponCritical.value,
                                  criticalSpecialization.value,
                                  weaponFeatures,
                                  minLevel,maxLevel)
#    attackModifier.value = 0
#    additionalDamage.value = 0
#    damageModifier.value = 0
            
    updateEDBLGraph()
selectorAddButton.on_click(on_addSelection_clicked)



removeSelectionButton = widgets.Button(description="Remove Selections")
def on_removeSelection_clicked(b):
    #remove from selections
    if (selections.value):
        l = list(selections.options)
        for s in selections.value:    
            Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        updateEDBLGraph()
removeSelectionButton.on_click(on_removeSelection_clicked)

movetotopButton = widgets.Button(description="Move to top")
def on_movetotop_clicked(b):
    if(selections.value and selections.value[0]):
        v = selections.value[0]
        Selector.moveToTop(v)
        l = list(selections.options)
        l.remove(v)
        selections.options = [v] + l
        updateEDBLGraph()
movetotopButton.on_click(on_movetotop_clicked)

combineSelectionButton = widgets.Button(description="Combine Selections")
def on_combineSelection_clicked(b):
    # check if it's a combined attack, can't combine them
    if not Selector.canCombine(selections.value):
        return
    
    if len(selections.value) == 1:
        name = selections.value[0]
        name += " + " + selections.value[0]
        if not (name in selections.options):
            value = selections.value[0]
            Selector.doubleSelection(name, value)
            selections.options += (name,)
            
            # remove parts from Selections
            l = list(selections.options)  
            Selector.removeSelection(value)
            l.remove(value)
            selections.options = l
     
            updateEDBLGraph()
            
    if len(selections.value) >1:
        name = selections.value[0]
        for i in range(len(selections.value)-1):
            name += " + " + selections.value[i+1]
            
        if not (name in selections.options):
            # add combination to Selections  
            value = selections.value
            Selector.combineSelections(name, value)
            selections.options += (name,)
            
            # remove parts from Selections
            l = list(selections.options)
            for s in value:   
                Selector.removeSelection(s)
                l.remove(s)
            selections.options = l
     
            updateEDBLGraph()
combineSelectionButton.on_click(on_combineSelection_clicked)

minButton = widgets.Button(description="Min/rename Selections")
def on_minButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) == 1:
        oldName = selections.value[0]
        if newName == oldName:
            return
        
        Selector.rename(newName, oldName)
        
        selections.options += (newName,)
        l = list(selections.options)  
        l.remove(oldName)
        selections.options = l
        updateEDBLGraph()
    
    if len(selections.value) ==2:
        oldNames = selections.value
        Selector.minSelections(newName, oldNames)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        selections.options += (newName,)
        
        updateEDBLGraph()
minButton.on_click(on_minButton_clicked)

maxButton = widgets.Button(description="Max/rename Selections")
def on_maxButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) == 1:
        oldName = selections.value[0]
        if newName == oldName:
            return
        
        Selector.rename(newName, oldName)
        
        selections.options += (newName,)
        l = list(selections.options)  
        l.remove(oldName)
        selections.options = l
        updateEDBLGraph()
    
    if len(selections.value) ==2:
        oldNames = selections.value
        Selector.maxSelections(newName, oldNames)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        selections.options += (newName,)
        
        updateEDBLGraph()
maxButton.on_click(on_maxButton_clicked)

sumButton = widgets.Button(description="Sum Selections")
def on_sumButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) ==2:
        oldNames = selections.value
        Selector.sumSelections(newName, oldNames)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        selections.options += (newName,)

        updateEDBLGraph()
sumButton.on_click(on_sumButton_clicked)

difButton = widgets.Button(description="Dif Selections")
def on_difButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) ==2:
        oldNames = selections.value
        Selector.difSelections(newName, oldNames)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        selections.options += (newName,)
        
        updateEDBLGraph()
difButton.on_click(on_difButton_clicked)

newNameBox = widgets.Text(value="",layout=widgets.Layout(width='auto'))

g = go.FigureWidget() 
g.update_layout(title_text="Expected damage by level",
                  title_font_size=20,
               legend_orientation="h",
               legend_y=-0.2,
               height=500
               )
#g.layout.xaxis.range = [0,20]
#g.layout.yaxis.range = [0,60]

def updateEDBLGraph():
    CombinedAttack.PDWeight = persistentDamageWeightBox.value
    if byLevelView.value and (levelViewSelector.value == 'Damage Distribution' or levelViewSelector.value == 'Cumulative Distribution'):
        xLists, yLists, nameList = createDamageDistribution(levelDiff.value,
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value)
        titleText="Damage distribution for level " + str(levelSelector.value) + " vs Level " + str(levelSelector.value+levelDiff.value) + " Target with " + str(targetACSelector.value) + " AC and " + str(targetSavesSelector.value) + " Saves"
        xaxisText="Damage"
        yaxisText="Chance"
        #y axis needs title
        # do all stuff here
        if levelViewSelector.value == 'Cumulative Distribution':
            for yList in yLists:
                totalChance = 1
#                print(yList)
                for i, chance in enumerate(yList):
                    yList[i], totalChance = totalChance, totalChance - yList[i]
        
        with g.batch_update():
            g.data = []
            if levelViewSelector.value == 'Cumulative Distribution':
                for i in range(len(xLists)):
                    g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
            else:
                for i in range(len(xLists)):
                    g.add_trace(go.Bar(x=xLists[i],y=yLists[i],name=nameList[i]))
                                         
        
            # update legend size
            g.update_layout(height=500+10*len(nameList))
        
            g.update_layout(title_text=titleText,
                            xaxis_title_text=xaxisText,
                            yaxis_title_text=yaxisText)
        
        return 
    # don't want to execute the other view code
    
    if byLevelView.value:
        if levelViewSelector.value == 'Expected Damage by AC':
            xLists, xLists2, yLists, pyLists, hitsLists, critsLists, nameList = createLevelTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value)
            titleText="Expected damage for level " + str(levelSelector.value) + " vs Level " + str(levelSelector.value+levelDiff.value) + " Target with " + str(targetACSelector.value) + " AC and " + str(targetSavesSelector.value) + " Saves"
            xaxisText="vs AC"  
#            xaxis2Text="vs Save"
    else:
        xLists, yLists, pyLists, hitsLists, critsLists, nameList = createTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value)
        titleText="Expected damage by level"+ " vs Level+" + str(levelDiff.value) + " Target with " + str(targetACSelector.value) + " AC and " + str(targetSavesSelector.value) + " Saves"
        xaxisText="Level"
#     print("selected: ", xLists, yLists)
#     print(Selector.selectedAttack[1])
#     for i in range(1,21):
#         if i in fighterAttackBonus and i+levelDiff.value in averageAcByLevel:
# #             print(selectedAttack[i])
#             xList.append(i)
#             yList.append(calculateED(Selector.selectedAttack[i]+attackBonus.value,averageAcByLevel[i+levelDiff.value],Selector.selectedDamage[i]+damageBonus.value,dm=weakness.value))
    
# add persistent damage to damage
    wantedView = percentageView.value
    
    if wantedView == 'Expected Persistent Damage':
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] =  pyLists[i][ii]
    elif wantedView == 'Number of Hits':
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] =  hitsLists[i][ii]
    elif wantedView == 'Number of Crits':
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] =  critsLists[i][ii]
    elif wantedView == 'Number of Hits+Crits':
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] =  hitsLists[i][ii] + critsLists[i][ii]
    else:
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] += persistentDamageWeightBox.value * pyLists[i][ii]
            
    
    if wantedView == 'Percent of First Selection' and len(yLists)>0:
        firsty = copy.copy(yLists[0])
        firstx = xLists[0]
        for i in range(len(firstx)):
            xi = firstx[i]
            for ii in range(0,len(yLists)):
                xl = xLists[ii]
                yl = yLists[ii]
                if xi in xl:
                    xii = xl.index(xi)
                    
                    yl[xii] = 100 * yl[xii] / firsty[i]
        
        # remove x,y pairs not in firstx
        for i in range(1,len(xLists)):
            for ii in range(1,21):
                if not ii in firstx:
                    if ii in xLists[i]:
                        xi = xLists[i].index(ii)
                        yLists[i].pop(xi)
                        xLists[i].pop(xi)
                        
    elif wantedView == 'Percent of High HP' or wantedView == 'Percent of Moderate HP' or wantedView == 'Percent of Low HP':
        if wantedView == 'Percent of High HP':
            hpList = creatureData['HP']['High']
        if wantedView == 'Percent of Moderate HP':
            hpList = creatureData['HP']['Moderate']
        if wantedView == 'Percent of Low HP':
            hpList = creatureData['HP']['Low']
        if byLevelView.value:
            comparisonHP = hpList[levelSelector.value+levelDiff.value]
            for i in range(len(xLists)):
                for ii in range(len(xLists[i])):
                    y = 100 * yLists[i][ii] / comparisonHP
                    yLists[i][ii] = y
        else:
            for i in range(len(xLists)):
                for ii in range(len(xLists[i])):
                    x = xLists[i][ii]
                    comparisonHP = hpList[x+levelDiff.value]
                    y = 100 * yLists[i][ii] / comparisonHP
                    yLists[i][ii] = y
    
#    maxY = 0
#    for l in yLists:
#        for y in l:
#            maxY = max(maxY,y)
            
#    minX = 100
#    maxX = 0
#    for l in xLists:
#        for x in l:
#            minX = min(minX,x)
#            maxX = max(maxX,x)
            
            
    with g.batch_update():
        g.data = []
        for i in range(len(xLists)):
            g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
        
        # update legend size
        g.update_layout(height=500+10*len(nameList))
        if byLevelView.value:
            g.update_layout(title_text=titleText,
                            xaxis_title_text=xaxisText,
#                            xaxis2_title_text =  xaxis2Text, 
#                            xaxis2_overlaying= 'x', 
                            yaxis_title_text=wantedView)
        else:
            g.update_layout(title_text=titleText,
                            xaxis_title_text=xaxisText,
                            yaxis_title_text=wantedView)
            
        # should update the axis so the data fits
#        if percentageView.value == 'Percent of First Selection':
#            g.layout.yaxis.range = [0,200]
#        else:
#            if maxY > 15:
#                if maxY > 30:
#                    if maxY > 60:
#                        if maxY > 120:
#                            if maxY > 240:
#                                g.layout.yaxis.range = [0,480]
#                            else:
#                                g.layout.yaxis.range = [0,240]
#                        else:
#                            g.layout.yaxis.range = [0,120]
#                    else:
#                        g.layout.yaxis.range = [0,60]
#                else:
#                    g.layout.yaxis.range = [0,30]
#            else:
#                g.layout.yaxis.range = [0,15]
#        if byLevelView.value:
#            g.layout.xaxis.range = [minX-2,maxX+2]
#        else:
#            g.layout.xaxis.range = [1,20]
            
def edblResponse(change):
    updateEDBLGraph()        

levelDiff.observe(edblResponse, names="value")
attackBonus.observe(edblResponse, names="value")
damageBonus.observe(edblResponse, names="value")
weakness.observe(edblResponse, names="value")
applyDebuffs.observe(edblResponse, names="value")
flatfootedBox.observe(edblResponse, names="value")
percentageView.observe(edblResponse, names="value")
byLevelView.observe(edblResponse, names="value")
levelSelector.observe(edblResponse, names="value")
levelViewSelector.observe(edblResponse, names="value")
persistentDamageWeightBox.observe(edblResponse, names="value")

targetACSelector.observe(targetACChangedResponse, names="value")
targetSavesSelector.observe(targetSavesChangedResponse, names="value")
classSelector.observe(classSelectorResponse, names="value")


adjustments = widgets.HBox([levelDiff,attackBonus,damageBonus])#weakness, applyDebuffs
targetRow = widgets.HBox([targetACSelector, targetSavesSelector,flatfootedBox,persistentDamageWeightBox])

levelViewRow = widgets.HBox([percentageView,byLevelView,levelSelector,levelViewSelector])

    # no ,mapSelection
selectorModifiers = widgets.VBox([primaryAbilityScore,secondaryAbilityScore,attackModifier,damageModifier,additionalDamage,levelLimiter,spellLevelSelector,selectorAddButton])
weaponModifiers = widgets.VBox([weaponLabel,weaponDamageDie,weaponCritical,criticalSpecialization])
featureModifiers = widgets.VBox([featureSelection1,featureSelection2,featureSelection3,featureSelection4,featureSelection5,featureSelection6,featureSelection7,featureSelection8])
featureLevels = widgets.VBox([featureLevel1,featureLevel2,featureLevel3,featureLevel4,featureLevel5,featureLevel6,featureLevel7,featureLevel8])
#runeModifiers = widgets.VBox([elementalRunesLabel,elementalRune1,elementalRune2,elementalRune3,elementalRune4])
selectorBox = widgets.VBox([classSelector,selector])
selectorRow = widgets.HBox([selectorBox,selectorModifiers,weaponModifiers,featureModifiers,featureLevels])

selectionsButtons = widgets.VBox([removeSelectionButton,movetotopButton,combineSelectionButton,minButton,maxButton,sumButton,difButton,newNameBox],
                                 layout=widgets.Layout(height='105%'))
selectionsBox = widgets.HBox([selections,selectionsButtons],layout=widgets.Layout(height='105%'))

ExpectedDamageByLevelWidget = widgets.VBox([targetRow,
                                            adjustments,
              levelViewRow,
              g,
             selectorRow,
             selectionsBox])