import copy
from pf2calc import Selector, CombinedAttack, createTraces, createLevelTraces, createDamageDistribution, createDebuffDistribution, creatureData
from distribution import Distribution
import plotly.graph_objects as go
from ipywidgets import widgets

targetLabel = widgets.Label(
        value="Target:",
        layout=widgets.Layout(height='auto', min_width='45px'),
        tooltip="Target:"
)

levelDiffLabel = widgets.Label(
        value="LevelDiff:",
        layout=widgets.Layout(height='auto', min_width='65px'),
        tooltip="Level Difference:"
)

levelDiff = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    layout=widgets.Layout(min_width='20px')
    #continuous_update=False
)

ACLabel = widgets.Label(
        value="AC:",
        layout=widgets.Layout(height='auto', min_width='15px')
)
targetACSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low'],
    value='Moderate',
    layout=widgets.Layout(min_width='20px')
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
    description='Target Save:',
    layout=widgets.Layout(width='auto')
)

fortLabel = widgets.Label(
        value="Fort:",
        layout=widgets.Layout(height='auto', min_width='15px')
)
targetFortSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    layout=widgets.Layout(min_width='20px')
)
refLabel = widgets.Label(
        value="Ref:",
        layout=widgets.Layout(height='auto', min_width='15px')
)
targetRefSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    layout=widgets.Layout(min_width='20px')
)
willLabel = widgets.Label(
        value="Will:",
        layout=widgets.Layout(height='auto', min_width='15px')
)
targetWillSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    layout=widgets.Layout(min_width='20px')
)
perLabel = widgets.Label(
        value="Per:",
        layout=widgets.Layout(height='auto', min_width='15px')
)
targetPerSelector = widgets.Dropdown(
    options=['Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    layout=widgets.Layout(min_width='20px')
)

def targetACChangedResponse(change):
    Selector.changeTargetAC(targetACSelector.value)
    updateEDBLGraph()  

def targetSavesChangedResponse(change):
    Selector.changeTargetSaves(targetSavesSelector.value)
    updateEDBLGraph() 
    
def targetFortChangedResponse(change):
    Selector.changeTargetFort(targetFortSelector.value)
    updateEDBLGraph() 

def targetRefChangedResponse(change):
    Selector.changeTargetRef(targetRefSelector.value)
    updateEDBLGraph() 

def targetWillChangedResponse(change):
    Selector.changeTargetWill(targetWillSelector.value)
    updateEDBLGraph() 
    
def targetPerChangedResponse(change):
    Selector.changeTargetPer(targetPerSelector.value)
    updateEDBLGraph() 
    
customTarget = widgets.Checkbox(
        value=False,
        description="Use Custom Target:",
        indent=False,
        layout=widgets.Layout(width='Auto')
        )
customAC = widgets.BoundedIntText(
        value=20.0,
        min=0.0,
        max=100,
        layout=widgets.Layout(min_width='20px')
        )
customFort = widgets.BoundedIntText(
        value=10.0,
        min=-10.0,
        max=100,
        layout=widgets.Layout(min_width='20px')
        )
customRef = widgets.BoundedIntText(
        value=10.0,
        min=-10.0,
        max=100,
        layout=widgets.Layout(min_width='20px')
        )
customWill = widgets.BoundedIntText(
        value=10.0,
        min=-10.0,
        max=100,
        layout=widgets.Layout(min_width='20px')
        )
customPer = widgets.BoundedIntText(
        value=10.0,
        min=-10.0,
        max=100,
        layout=widgets.Layout(min_width='20px')
        )
def customTargetResponse(change):
    if customTarget.value:
        Selector.customTarget(customAC.value,customFort.value,customRef.value,customWill.value,customPer.value)
    else:
        Selector.revertCustom()
    updateEDBLGraph() 

attackBonus = widgets.BoundedIntText(
    value=0.0,
    min=-20.0,
    max=20.0,
    step=1.0,
    description='Attack bonus:',
    layout=widgets.Layout(min_width='130px')
    #continuous_update=False
)
damageBonus = widgets.BoundedIntText(
    value=0.0,
    min=-100.0,
    max=100.0,
    step=1.0,
    description='Weakness:',
    layout=widgets.Layout(min_width='150px')
    #continuous_update=False
)
weakness = widgets.BoundedIntText(
    value=0.0,
    min=-100.0,
    max=100.0,
    step=1.0,
    description='Weakness:',
    layout=widgets.Layout(min_width='130px')
    #continuous_update=False
)

persistentDamageWeightBox = widgets.BoundedFloatText(
    value=2,
    min=0,
    max=10.0,
    description='Persistent Damage Weight',
    disabled=False,
    layout=widgets.Layout(min_width='130px')
)

persistentDamageReroll = widgets.Checkbox(
        value=True,
        description="Reroll Persistent Damage Every time:",
        layout=widgets.Layout(min_width='20px'),
        indent=False
)

flatfootedBox = widgets.BoundedIntText(
    value=0,
    min=0,
    max=100.0,
    description='Flat-Footed %',
    disabled=False,
    layout=widgets.Layout(min_width='140px')
)

applyDebuffs = widgets.Checkbox(
        value=True,
        description="Apply Debuffs"
)

concealment = widgets.Dropdown(
    options=['None',
             'Concealed',
             'Invisible'],
    value='None',
    description='Concealment:',
#    layout=widgets.Layout(width='17%')
)
clumsy = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Clumsy:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)
drained = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Drained:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)
enfeebled = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Enfeebled:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)
frightened = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Frightened:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)
sickened = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Sickened:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)
stupified = widgets.Dropdown(
    options=['0',
             '1',
             '2',
             '3',
             '4'],
    value='0',
    description='Stupified:',
    layout=widgets.Layout(min_width='20px')
#    layout=widgets.Layout(width='17%')
)

def targetClumsyChangedResponse(change):
    Selector.changeTargetClumsy(clumsy.value)
    updateEDBLGraph() 
def targetDrainedChangedResponse(change):
    Selector.changeTargetDrained(drained.value)
    updateEDBLGraph() 
def targetEnfeebledChangedResponse(change):
    Selector.changeTargetEnfeebled(enfeebled.value)
    updateEDBLGraph() 
def targetFrightenedChangedResponse(change):
    Selector.changeTargetFrightened(frightened.value)
    updateEDBLGraph() 
def targetSickenedChangedResponse(change):
    Selector.changeTargetSickened(sickened.value)
    updateEDBLGraph() 
def targetStupifiedChangedResponse(change):
    Selector.changeTargetStupified(stupified.value)
    updateEDBLGraph() 

percentageView = widgets.Dropdown(
        options = ['Expected Damage',
                   'Percent of First Selection',
                   'Percent of High HP',
                   'Percent of Moderate HP',
                   'Percent of Low HP',
                   'Expected Persistent Damage',
                   'Number of Hits',
                   'Number of Crits',
                   'Number of Hits+Crits',
                   'Max Debuff'],
        value='Expected Damage'
)

isBlended = widgets.Checkbox(
    value = False,
    description="Blend vs Level +-2",
    indent=False)

byLevelView = widgets.Checkbox(
        value=False,
        description="By Level View",
        indent=False
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

calculateButton = widgets.Button(description="Calculate!")
def on_calculateButton_clicked(b):
    calculateGraph()
calculateButton.on_click(on_calculateButton_clicked)
autoCalculate = widgets.Checkbox(
        value=True,
        description="Autocalculate",
        layout=widgets.Layout(min_width='20px'),
        indent=False
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
        value='18 to 22 Apex',
        layout=widgets.Layout(width='auto')
)
secondaryAbilityScore = widgets.Dropdown(
        description = 'Damage Ability Score',
        options=abilityScoreOptions,
        value='18 to 22 Apex',
        layout=widgets.Layout(width='auto')
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
        value='x0 = 0',
        layout=widgets.Layout(width='auto'))
weaponTraits = widgets.SelectMultiple(
    options=['forceful',
             'backswing'],
    # rows=10,
#    description='Current selections:',
    layout=widgets.Layout(width='100%', height='90%'),
    disabled=False
)

attackModifier = widgets.BoundedIntText(
    value=0.0,
    min=-20.0,
    max=20.0,
    step=1.0,
    description='Attack Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

additionalDamage = widgets.BoundedIntText(
    value=0.0,
    min=-100.0,
    max=100.0,
    step=1.0,
    description='Additional Damage:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

damageModifier = widgets.BoundedIntText(
    value=0.0,
    min=-100.0,
    max=100.0,
    step=1.0,
    description='Damage Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

levelLimiter = widgets.IntRangeSlider(
    value=[-1, 24],
    min=-1,
    max=24,
    step=1,
    description = 'Level Range',
    layout=widgets.Layout(width='auto')
)

spellLevelSelector = widgets.Dropdown(
        description='Spell Level:',
        options=['Max',
                 'MC Max',
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
        value='Max',
        layout=widgets.Layout(width='auto')
)

weaponLabel = widgets.Label(
        value="Weapon:",
        layout=widgets.Layout(height='auto')
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

featureOptions = ["1d12 Rune",
                  "1d10 Rune",
                  "1d8 Rune",
                  "1d6 Rune",
                 "1d4 Rune",
                 "Flaming Crit Persistent",
                 "MC Caster Proficiency",
                 "backswing",
                 "backstabber",
                 "keen",
                 "Brutal Critical",
                 "Burn it!",
                 "Add 1 Die",
                 "Remove 1 Die",
                 "+1 attack",
                 "+2 attack",
                 "+3 attack",
                 "+4 attack",
                 "+5 attack",
                 "-1 attack",
                 "-2 attack",
                 "-3 attack",
                 "-4 attack",
                 "-5 attack",
                 "+1 damage",
                 "+2 damage",
                 "+3 damage",
                 "+4 damage",
                 "+5 damage",
                 "+6 damage",
                 "+7 damage",
                 "+8 damage",
                 "+9 damage",
                 "+10 damage",
                 "-1 damage",
                 "-2 damage",
                 "-3 damage",
                 "-4 damage",
                 "-5 damage",
                 "-6 damage",
                 "-7 damage",
                 "-8 damage",
                 "-9 damage",
                 "-10 damage",
                 "+1 level",
                 "-1 level"
                 ]

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
                 "Basic Saves",
                 "Debuff Spells",
                 "Focus Spells",
                 "Skills",
                 "Caster Strikes",
                 "Martial Strikes",
                 "Monster Strikes",
                 "Summon Strikes",
                 "Effects",
                 "Items",
                 "Targets"],
        value="Fighter",
        layout=widgets.Layout(width='auto')
)
alchemistOptions = ['Alchemist Melee Strike',
                    'Alchemist Ranged Strike',
                    'Quicksilver Mutagen',
                    'Quicksilver Weapon Bonus',
                    'Quicksilver Spell Bonus',
                    'Alchemist Bestial Claw',
                    'Alchemist Bestial Jaw',
                    'Alchemist Feral Claw',
                    'Alchemist Feral Jaw',
                    'Energy Mutagen',
                    'Energy Mutagen Breath',
                    'Powerful Energy Breath',
                    'Elixir of Life',
                    'Alchemist Acid Flask',
                    'Alchemist Bomber Acid',
                    'Alchemist Sticky Acid',
                    'Alchemist Debilitating Acid',
                    'Alchemist Perpetual Acid',
                    'Alchemist Bomber Perpetual Acid',
                    'Alchemist Sticky Perpetual Acid',
                    'Alchemist Debilitating Perpetual Acid',
                    'Alchemist Fire',
                    'Alchemist Bomber Fire',
                    'Alchemist Sticky Fire',
                    'Alchemist Debilitating Fire',
                    'Alchemist Perpetual Fire',
                    'Alchemist Bomber Perpetual Fire',
                    'Alchemist Sticky Perpetual Fire',
                    'Alchemist Debilitating Perpetual Fire',
                    'Alchemist Bottled Lightning',
                    'Alchemist Bomber Lightning',
                    'Alchemist Sticky Lightning',
                    'Alchemist Debilitating Lightning',
                    'Alchemist Perpetual Lightning',
                    'Alchemist Bomber Perpetual Lightning',
                    'Alchemist Sticky Perpetual Lightning',
                    'Alchemist Debilitating Perpetual Lightning',
                    'Alchemist Frost Vial',
                    'Alchemist Bomber Frost',
                    'Alchemist Sticky Frost',
                    'Alchemist Debilitating Frost',
                    'Alchemist Perpetual Frost',
                    'Alchemist Bomber Perpetual Frost',
                    'Alchemist Sticky Perpetual Frost',
                    'Alchemist Debilitating Perpetual Frost',
                    'Debilitating Bomb',
                    'Debilitating Perpetual',
                    'Debilitating Flat-Footed Save',
                    'Debilitating Dazzled Save',
                    'Debilitating Clumsy Save',
                    'Debilitating Enfeebled Save',
                    'Debilitating Stupified Save',
                    'Debilitating True Flat-Footed Save',
                    'Debilitating True Dazzled Save',
                    'Debilitating True Clumsy 2 Save',
                    'Debilitating True Enfeebled 2 Save',
                    'Debilitating True Stupified 2 Save']
barbarianOptions = ['Martial Strike',
                    'Barbarian Animal Claw',
                    'Barbarian Animal Jaw',
                    'Barbarian Dragon Strike',
                    'Barbarian Fury Strike',
                    'Barbarian Giant Strike',
                    'Barbarian Spirit Strike',
                    'Barbarian Dragon Breath',
                    'Barbarian Dragon Breath2',
                    'Barbarian Animal Thrash',
                    'Barbarian Dragon Thrash',
                    'Barbarian Fury Thrash',
                    'Barbarian Giant Thrash',
                    'Barbarian Spirit Thrash',
                    "Barbarian Spirit's Wrath",
                    'Vicious Evisceration',
                    'Vicious Evisceration Animal',
                    'Vicious Evisceration Dragon',
                    'Vicious Evisceration Fury',
                    'Vicious Evisceration Giant',
                    'Vicious Evisceration Spirit'
                    ]
bardOptions = ['Caster Strike']
championOptions = ['Martial Strike',
                   'Champion Smite Evil']
cantripOptions = ['Electric Arc',
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
                 'Heal',
                'd10 Heal',
                '2action Heal',
                '2action d10 Heal',
                'Harm',
                'd10 Harm',
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
                'Ani-Elem-Mons-Inc',
                'Wildshape AnimalR',
                'Wildshape InsectR',
                'Wildshape DinoR',
                'Wildshape AerialR',
                'Wildshape ElementalR',
                'Wildshape PlantR',
                'Wildshape DragonR',
                'Wildshape MonsterR',
                'Wildshape IncarnateR',
                'Ani-Elem-Mons-IncR'
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
monkOptions = ['Martial Strike',
               'Ki Strike',
               'Tiger Claw',
               'Tiger Slash',
               'Ki Tiger Claw']
rangerOptions = ['Ranger Precision Edge',
                 'Ranger Bear Support',
                 'Martial Strike',
                        'Martial Ranged Strike',
                        'Martial Propulsive']
rogueOptions = ['Rogue Strike',
                'Flat Foot Next Strike',
                'Scoundrel Feint']
sorcererOptions = ['Dangerous Sorcery',
                   'Caster Strike',
                   'Bespell Weapon']
wizardOptions = ['Caster Strike',
                 'Bespell Weapon',
                 "Hand of the Apprentence",
                 "Hand of the Apprentence +item"]
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
                  'Monster Low Attack Low Damage',
                  'Monster Extreme DC Limited Damage',
                  'Monster Extreme DC Unlimited Damage',
                  'Monster High DC Limited Damage',
                  'Monster High DC Unlimited Damage',
                  'Monster Moderate DC Limited Damage',
                  'Monster Moderate DC Unlimited Damage'
                  ]
summonOptions = ['Summon Animal',
                'Summon Dragon']
effectOptions = ['Flat Foot Target',
                 'Flat Foot Next Strike',
                 'Blur',
                        'Invisibility',
                        'Remove Concealment',
                        'Add Fortification',
                        'Add Fortification(Greater)',
                        'Remove Fortification',
                        'Apply Persistent Damage']
targetOptions = ['Target Extreme AC',
                 'Target High AC',
                 'Target Moderate AC',
                 'Target Low AC',
                 'Target Fighter AC',
                 'Target Wizard AC',
                 'Target DexMonk AC',
                 'Target Rogue AC',
                 'Target Champion AC',
                 'Target Extreme Fort',
                 'Target High Fort',
                 'Target Moderate Fort',
                 'Target Low Fort',
                 'Target Terrible Fort',
                 'Target Extreme Ref',
                 'Target High Ref',
                 'Target Moderate Ref',
                 'Target Low Ref',
                 'Target Terrible Ref',
                 'Target Extreme Will',
                 'Target High Will',
                 'Target Moderate Will',
                 'Target Low Will',
                 'Target Terrible Will',
                 'Target Extreme Per',
                 'Target High Per',
                 'Target Moderate Per',
                 'Target Low Per',
                 'Target Terrible Per'
    ]
debuffSpellOptions = ['Heroism',
                      'Enfeeblement Attack',
                      'Enfeeblement Save',
                      'Fear: Debuff Attacker(123)',
                'Fear: Debuff Target(123)',
                'Debuff Attacker(012)',
                'Debuff Target(012)'
        ]
basicSpellOptions = ['Basic Reflex 1d6',
                'Basic Reflex 1d8',
                'Basic Reflex 1d10',
                'Basic Reflex 1d12',
                'Basic Reflex 2d6',
                'Basic Reflex 2d6+1',
                'Basic Reflex 2d6+2',
                'Basic Reflex 2d8',
                'Basic Reflex 2d10',
                'Basic Reflex 2d12',
                'Basic Fort 1d6',
                'Basic Fort 1d8',
                'Basic Fort 1d10',
                'Basic Fort 1d12',
                'Basic Fort 2d6',
                'Basic Fort 2d6+1',
                'Basic Fort 2d6+2',
                'Basic Fort 2d8',
                'Basic Fort 2d10',
                'Basic Fort 2d12',
                'Basic Will 1d6',
                'Basic Will 1d8',
                'Basic Will 1d10',
                'Basic Will 1d12',
                'Basic Will 2d6',
                'Basic Will 2d6+1',
                'Basic Will 2d6+2',
                'Basic Will 2d8',
                'Basic Will 2d10',
                'Basic Will 2d12'
        ]
spellOptions = ['Heal',
                'd10 Heal',
                '2action Heal',
                '2action d10 Heal',
                'Harm',
                'd10 Harm',
                'Magic Missle',
                'True Strike',
                'Phantom Pain',
                'Grim Tendrils',
                'Shocking Grasp',
                'Shocking Grasp Metal',
                'Hydralic Push',
                'Acid Arrow',
                'Flaming Sphere',
                'Spiritual Weapon',
                'Searing Light',
                'Searing Light vs Fiend',
                'Lightning Bolt',
                'Holy Cascade',
                'Holy Cascade vs Fiend',
                'Divine Wrath',
                'Wall of Fire',
                'Phantasmal Killer',
                'Pantasmal Calamity',
                'Spirit Blast',
                'Visions of Danger',
                'Weird',
                'Disintigrate Attack',
                'Disintigrate Save',
                'Finger of Death',
                'Meteor Swarm',
                'Polar Ray',
                'Horrid Wilting',
                'Eclipse Burst',
                'Sunburst']
focusSpellOptions = ['Elemental Toss',
                     'Fire Ray',
                     'Force Bolt',
                     'Tempest Surge'
                     
            ]
skillOptions = ['Trained Feint',
                'Max Feint',
                'Trained Demoralize',
                'Max Demoralize',
                'Scare to Death']
itemOptions = ['Study Shield Hardness',
               'Sturdy Shield HP']

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
                     "Monster Strikes": monsterOptions,
                     "Summon Strikes": summonOptions,
                     "Effects": effectOptions,
                     "Targets": targetOptions,
                     "Spells": spellOptions,
                     "Skills": skillOptions,
                     "Basic Saves": basicSpellOptions,
                     "Debuff Spells": debuffSpellOptions,
                     "Focus Spells": focusSpellOptions,
                     "Items": itemOptions}


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
    layout=widgets.Layout(width='80%', height='90%'),
    disabled=False
)

def selectionsChangedResponse(b):
    if selections.value:
        if len(selections.value) >= 1:
            newNameBox.value = selections.value[0]

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

        name = Selector.addSelection(name,
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
        selections.options += (name,)
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
        while (name in selections.options):
            name += "."
            
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
            
        while (name in selections.options):
            name += "."
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

stitchButton = widgets.Button(description="Stitch Selections")
def on_stitchButton_clicked(b):
    if not Selector.canCombine(selections.value):
        return
    
    if len(selections.value) >1:
        
        value = selections.value
        Selector.stitch(value)
            
        # remove parts from Selections
        l = list(selections.options)
        for s in value[1:]:   
#            Selector.removeSelection(s) # already removed in stich()
            l.remove(s)
        selections.options = l
        updateEDBLGraph()
stitchButton.on_click(on_stitchButton_clicked)

duplicateButton = widgets.Button(description="Duplicate Selections")
def on_duplicateButton_clicked(b):
    for key in selections.value:
        newKey = Selector.duplicate(key)
        selections.options += (newKey,)
    updateEDBLGraph()
duplicateButton.on_click(on_duplicateButton_clicked)
    
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
    
    if len(selections.value) >=2:
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
    
    if len(selections.value) >=2:
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
printBox = widgets.Textarea(value="",
                            placeholder="print data",
                            layout=widgets.Layout(width='auto',height='auto')
)
data = []
printButton = widgets.Button(description="Print Data")
def on_printButton_clicked(b):
#    printBox.value = str(Distribution.count)
#    Distribution.count = 0
    printBox.value = str(data)
printButton.on_click(on_printButton_clicked)

printSelectionButton = widgets.Button(description="Print Selection Info")
def on_printSelectionButton_clicked(b):
    selectionData = []
    if(selections.value and selections.value[0]):
        v = selections.value[0]
        selectionData = Selector.getSelectionInfo(v)
        printBox.value = v + ": \n" + str(selectionData)
printSelectionButton.on_click(on_printSelectionButton_clicked)
    
    
    
    
    
g = go.FigureWidget() 
g.update_layout(title_text="Expected damage by level",
                  title_font_size=20,
               legend_orientation="h",
               legend_y=-0.2,
               height=700
               )
#g.layout.xaxis.range = [0,20]
#g.layout.yaxis.range = [0,60]

def updateEDBLGraph():
    if autoCalculate.value:
        calculateGraph()
def calculateGraph():
    global data
    CombinedAttack.PDWeight = persistentDamageWeightBox.value
    CombinedAttack.PersistentReRoll = persistentDamageReroll.value
    if customTarget.value:
        targetText = " Target w/ AC:" + str(customAC.value) + " F:" + str(customFort.value) + " R:" + str(customRef.value)  + " W:" + str(customWill.value) + " P:" + str(customPer.value)
    elif byLevelView.value:
        ac = " AC:"+str(Selector.selectedTarget.getAC(levelSelector.value+levelDiff.value))
        fort = " Fort:"+str(Selector.selectedTarget.getFort(levelSelector.value+levelDiff.value))
        reflex = " Reflex:"+str(Selector.selectedTarget.getRef(levelSelector.value+levelDiff.value))
        will = " Will:"+str(Selector.selectedTarget.getWill(levelSelector.value+levelDiff.value))
        perception = " Perception:"+str(Selector.selectedTarget.getPer(levelSelector.value+levelDiff.value))
        targetText =" Target w/" + ac + fort + reflex + will + perception
    else:
        targetText = " Target w/ AC:" + str(targetACSelector.value) + " F:" + str(targetFortSelector.value) + " R:" + str(targetRefSelector.value)  + " W:" + str(targetWillSelector.value) + " P:" + str(targetPerSelector.value)
    
    if byLevelView.value and (levelViewSelector.value == 'Damage Distribution' or levelViewSelector.value == 'Cumulative Distribution'):
        if percentageView.value == 'Expected Persistent Damage':
            displayPersistent = True
        else:  # 'Max Debuff': 
            displayPersistent = False
        if percentageView.value == 'Max Debuff': 
            xLists, yLists, nameList = createDebuffDistribution(levelDiff.value,
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value,
                                            displayPersistent)
            titleText="For lvl" + str(levelSelector.value) + " vs lvl" + str(levelSelector.value+levelDiff.value) + targetText
            xaxisText="Max Debuff"
        else:
            xLists, yLists, nameList = createDamageDistribution(levelDiff.value,
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value,
                                            displayPersistent)
            titleText="For lvl" + str(levelSelector.value) + " vs lvl" + str(levelSelector.value+levelDiff.value) + targetText
            if displayPersistent:
                xaxisText="Persistent Damage"
            else:
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
            data = [xLists,yLists,nameList]
            if levelViewSelector.value == 'Cumulative Distribution':
                for i in range(len(xLists)):
                    g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
            else:
                for i in range(len(xLists)):
                    g.add_trace(go.Bar(x=xLists[i],y=yLists[i],name=nameList[i]))
                                         
        
            # update legend size
            g.update_layout(height=700+20*len(nameList))
        
            g.update_layout(title_text=titleText,
                            xaxis_title_text=xaxisText,
                            yaxis_title_text=yaxisText)
        
        return 
    # don't want to execute the other view code
    
    if byLevelView.value:
        if levelViewSelector.value == 'Expected Damage by AC':
            xLists, yLists, pyLists, hitsLists, critsLists, debuffLists, nameList = createLevelTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value)
            titleText="For lvl" + str(levelSelector.value) + " vs lvl" + str(levelSelector.value+levelDiff.value) + targetText
            xaxisText="+/- X AC/Fort/Reflex/Will/Perception"
                
#            xaxis2Text="vs Save"
    else:
        xLists, yLists, pyLists, hitsLists, critsLists, debuffLists, nameList = createTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            isBlended.value)
        if isBlended.value:
            targetText = " Blended" + targetText
        titleText="Vs lvl+" + str(levelDiff.value) + targetText
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
    elif wantedView == 'Max Debuff':
        for i in range(len(yLists)):
            for ii in range(len(yLists[i])):
                yLists[i][ii] =  debuffLists[i][ii]
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
                    if firsty[i] != 0:
                        yl[xii] = 100 * yl[xii] / firsty[i]
                    else:
                        yl[xii] = 0
        
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
        data = [xLists,yLists,nameList]
        for i in range(len(xLists)):
            g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
        
        # update legend size
        g.update_layout(height=700+20*len(nameList))
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
isBlended.observe(edblResponse, names="value")
levelSelector.observe(edblResponse, names="value")
levelViewSelector.observe(edblResponse, names="value")
persistentDamageWeightBox.observe(edblResponse, names="value")
persistentDamageReroll.observe(edblResponse, names="value")

targetACSelector.observe(targetACChangedResponse, names="value")
targetSavesSelector.observe(targetSavesChangedResponse, names="value")
targetFortSelector.observe(targetFortChangedResponse, names="value")
targetRefSelector.observe(targetRefChangedResponse, names="value")
targetWillSelector.observe(targetWillChangedResponse, names="value")
targetPerSelector.observe(targetPerChangedResponse, names="value")
customTarget.observe(customTargetResponse,names="value")
clumsy.observe(targetClumsyChangedResponse, names="value")
drained.observe(targetDrainedChangedResponse, names="value")
enfeebled.observe(targetEnfeebledChangedResponse, names="value")
frightened.observe(targetFrightenedChangedResponse, names="value")
sickened.observe(targetSickenedChangedResponse, names="value")
stupified.observe(targetStupifiedChangedResponse, names="value")

classSelector.observe(classSelectorResponse, names="value")
selections.observe(selectionsChangedResponse, names="value")


targetRow = widgets.HBox([targetLabel,levelDiffLabel,levelDiff,ACLabel, targetACSelector, fortLabel, targetFortSelector, refLabel, targetRefSelector,willLabel, targetWillSelector, perLabel, targetPerSelector])
targetRow.layout.width = '100%'
customRow = widgets.HBox([customTarget,ACLabel,customAC,fortLabel,customFort,refLabel,customRef,willLabel,customWill,perLabel,customPer])
debuffs = widgets.HBox([flatfootedBox,clumsy,drained,frightened,sickened,stupified])
adjustments = widgets.HBox([enfeebled,attackBonus,damageBonus,persistentDamageWeightBox,persistentDamageReroll]) #weakness, applyDebuffs
levelViewRow = widgets.HBox([percentageView,isBlended, byLevelView,levelSelector,levelViewSelector])

    # no ,mapSelection
selectorModifiers = widgets.VBox([primaryAbilityScore,secondaryAbilityScore,attackModifier,damageModifier,additionalDamage,levelLimiter,spellLevelSelector,selectorAddButton])
weaponModifiers = widgets.VBox([weaponLabel,weaponDamageDie,weaponCritical,criticalSpecialization]) # mapSelection, weaponTraits  
featureModifiers = widgets.VBox([featureSelection1,featureSelection2,featureSelection3,featureSelection4,featureSelection5,featureSelection6,featureSelection7,featureSelection8])
featureLevels = widgets.VBox([featureLevel1,featureLevel2,featureLevel3,featureLevel4,featureLevel5,featureLevel6,featureLevel7,featureLevel8])
#runeModifiers = widgets.VBox([elementalRunesLabel,elementalRune1,elementalRune2,elementalRune3,elementalRune4])
selectorBox = widgets.VBox([classSelector,selector])
selectorRow = widgets.HBox([selectorBox,selectorModifiers,weaponModifiers,featureModifiers,featureLevels])

selectionsButtons = widgets.VBox([removeSelectionButton,movetotopButton,duplicateButton,combineSelectionButton,stitchButton,minButton,maxButton,sumButton,difButton,newNameBox],
                                 layout=widgets.Layout(height='100%'))
selectionsBox = widgets.HBox([selections,selectionsButtons],layout=widgets.Layout(height='300px'))
printButtonRow = widgets.HBox([printButton,printSelectionButton])

ExpectedDamageByLevelWidget = widgets.VBox([targetRow,
                                            customRow,
                                            debuffs,
                                            adjustments,
              levelViewRow,
              g,
              widgets.HBox([calculateButton,autoCalculate]),
             selectorRow,
             selectionsBox,
             printButtonRow,
             printBox])
            
mtargetRow = widgets.VBox([targetLabel,levelDiffLabel,levelDiff,ACLabel, targetACSelector, fortLabel, targetFortSelector, refLabel, targetRefSelector,willLabel, targetWillSelector, perLabel, targetPerSelector])
mcustomRow = widgets.VBox([customTarget,customAC,customFort,customRef,customWill,customPer])
mdebuffs = widgets.VBox([flatfootedBox,clumsy,drained,frightened,sickened,stupified])
madjustments = widgets.VBox([enfeebled,attackBonus,damageBonus,persistentDamageWeightBox,persistentDamageReroll]) #weakness, applyDebuffs
mlevelViewRow = widgets.VBox([percentageView,byLevelView,levelSelector,levelViewSelector])
mselectorRow = widgets.VBox([selectorBox,selectorModifiers,weaponModifiers,featureModifiers,featureLevels])
mselectionsBox = widgets.VBox([selections,selectionsButtons],layout=widgets.Layout(height='300px'))
mprintButtonRow = widgets.VBox([printButton,printSelectionButton])

MobileViewWidget = widgets.VBox([mtargetRow,
                                            mcustomRow,
                                            mdebuffs,
                                            madjustments,
              mlevelViewRow,
              g,
              calculateButton,
             mselectorRow,
             mselectionsBox,
             mprintButtonRow,
             printBox])