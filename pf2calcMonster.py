# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:23:49 2019

@author: bhalb
"""

extremeAC = {
    -1:18,
    0:19,
    1:19,
    2:21,
    3:22,
    4:24,
    5:25,
    6:27,
    7:28,
    8:30,
    9:31,
    10:33,
    11:34,
    12:36,
    13:37,
    14:39,
    15:40,
    16:42,
    17:43,
    18:45,
    19:46,
    20:48,
    21:49,
    22:51,
    23:52,
    24:54
}
highAC = {k: v-3 for k,v in extremeAC.items()}
moderateAC = {k: v-4 for k,v in extremeAC.items()}
lowAC = {k: v-6 for k,v in extremeAC.items()}
ac = {'Extreme':extremeAC,
      'High': highAC,
      'Moderate': moderateAC,
      'Low': lowAC}

extremeSaves = {
    -1:9,
    0:10,
    1:11,
    2:12,
    3:14,
    4:15,
    5:17,
    6:18,
    7:20,
    8:21,
    9:23,
    10:24,
    11:26,
    12:27,
    13:29,
    14:30,
    15:32,
    16:33,
    17:35,
    18:36,
    19:38,
    20:39,
    21:41,
    22:43,
    23:44,
    24:46
}
highSaves = {
    -1:8,
    0:9,
    1:10,
    2:11,
    3:12,
    4:14,
    5:15,
    6:17,
    7:18,
    8:19,
    9:21,
    10:22,
    11:24,
    12:25,
    13:26,
    14:28,
    15:29,
    16:30,
    17:32,
    18:33,
    19:35,
    20:36,
    21:38,
    22:39,
    23:40,
    24:42
}
moderateSaves = {
    -1:5,
    0:6,
    1:7,
    2:8,
    3:9,
    4:11,
    5:12,
    6:14,
    7:15,
    8:16,
    9:18,
    10:19,
    11:21,
    12:22,
    13:23,
    14:25,
    15:26,
    16:28,
    17:29,
    18:30,
    19:32,
    20:33,
    21:35,
    22:36,
    23:37,
    24:38
}
lowSaves = {
    -1:2,
    0:3,
    1:4,
    2:5,
    3:6,
    4:8,
    5:9,
    6:11,
    7:12,
    8:13,
    9:15,
    10:16,
    11:18,
    12:19,
    13:20,
    14:22,
    15:23,
    16:25,
    17:26,
    18:27,
    19:29,
    20:30,
    21:32,
    22:33,
    23:34,
    24:36
}
terribleSaves = {
    -1:0,
    0:1,
    1:2,
    2:3,
    3:4,
    4:6,
    5:7,
    6:8,
    7:10,
    8:11,
    9:12,
    10:14,
    11:15,
    12:16,
    13:18,
    14:19,
    15:20,
    16:22,
    17:23,
    18:24,
    19:26,
    20:27,
    21:28,
    22:30,
    23:31,
    24:32
}
saves = {'Extreme':extremeSaves,
         'High': highSaves,
         'Moderate': moderateSaves,
         'Low': lowSaves,
         'Terrible': terribleSaves}
        
extremePer = extremeSaves
highPer = highSaves
moderatePer = moderateSaves
lowPer = lowSaves
terriblePer = terribleSaves
per = {'Extreme':extremePer,
         'High': highPer,
         'Moderate': moderatePer,
         'Low': lowPer,
         'Terrible': terriblePer}
        
highHP = {
    -1:9,
    0:18,
    1:25,
    2:38,
    3:56,
    4:75,
    5:94,
    6:119,
    7:144,
    8:169,
    9:194,
    10:219,
    11:244,
    12:269,
    13:294,
    14:319,
    15:344,
    16:369,
    17:394,
    18:419,
    19:444,
    20:469,
    21:499,
    22:538,
    23:575,
    24:625
}
moderateHP = {
    -1:7,
    0:15,
    1:20,
    2:30,
    3:45,
    4:60,
    5:75,
    6:95,
    7:115,
    8:135,
    9:155,
    10:175,
    11:195,
    12:215,
    13:235,
    14:255,
    15:275,
    16:295,
    17:315,
    18:335,
    19:355,
    20:375,
    21:400,
    22:430,
    23:460,
    24:500
}
lowHP = {
    -1:5,
    0:12,
    1:15,
    2:23,
    3:34,
    4:45,
    5:56,
    6:71,
    7:86,
    8:101,
    9:116,
    10:131,
    11:146,
    12:161,
    13:176,
    14:191,
    15:206,
    16:221,
    17:236,
    18:251,
    19:266,
    20:281,
    21:300,
    22:323,
    23:345,
    24:375
}
hp = {'High': highHP,
      'Moderate': moderateHP,
      'Low': lowHP}
        
extremeAttack = {
    -1:10,
    0:10,
    1:11,
    2:13,
    3:14,
    4:16,
    5:17,
    6:19,
    7:20,
    8:22,
    9:23,
    10:25,
    11:27,
    12:28,
    13:29,
    14:31,
    15:32,
    16:34,
    17:35,
    18:37,
    19:38,
    20:40,
    21:41,
    22:43,
    23:44,
    24:46
}
highAttack = {k: v-2 for k,v in extremeAttack.items()}
moderateAttack = {k: v-4 for k,v in extremeAttack.items()}
lowAttack = {k: v-6 for k,v in extremeAttack.items()}
attack = {'Extreme':extremeAttack,
          'High': highAttack,
          'Moderate': moderateAttack,
          'Low': lowAttack}

extremeDamage = {
    -1:4,
    0:6,
    1:8,
    2:11,
    3:15,
    4:18,
    5:20,
    6:23,
    7:25,
    8:28,
    9:30,
    10:33,
    11:35,
    12:38,
    13:40,
    14:43,
    15:45,
    16:48,
    17:50,
    18:53,
    19:55,
    20:58,
    21:60,
    22:63,
    23:65,
    24:68
}
highDamage = {
    -1:3,
    0:5,
    1:6,
    2:9,
    3:12,
    4:14,
    5:16,
    6:18,
    7:20,
    8:22,
    9:24,
    10:26,
    11:28,
    12:30,
    13:32,
    14:34,
    15:36,
    16:37,
    17:38,
    18:40,
    19:42,
    20:44,
    21:46,
    22:48,
    23:50,
    24:52
}
moderateDamage = {
    -1:3,
    0:4,
    1:5,
    2:8,
    3:10,
    4:12,
    5:13,
    6:15,
    7:17,
    8:18,
    9:20,
    10:22,
    11:23,
    12:25,
    13:27,
    14:28,
    15:30,
    16:31,
    17:32,
    18:33,
    19:35,
    20:37,
    21:38,
    22:40,
    23:42,
    24:44
}
lowDamage = {
    -1:2,
    0:3,
    1:4,
    2:6,
    3:8,
    4:9,
    5:11,
    6:12,
    7:13,
    8:15,
    9:16,
    10:17,
    11:19,
    12:20,
    13:21,
    14:23,
    15:24,
    16:25,
    17:26,
    18:27,
    19:28,
    20:29,
    21:31,
    22:32,
    23:33,
    24:35
}
damage = {'Extreme':extremeDamage,
          'High': highDamage,
          'Moderate': moderateDamage,
          'Low': lowDamage}

extremeDC = {
    -1:19,
    0:19,
    1:20,
    2:22,
    3:23,
    4:25,
    5:26,
    6:27,
    7:29,
    8:30,
    9:32,
    10:33,
    11:34,
    12:36,
    13:37,
    14:39,
    15:40,
    16:41,
    17:43,
    18:44,
    19:46,
    20:47,
    21:48,
    22:50,
    23:51,
    24:52
}
highDC = {
    -1:16,
    0:16,
    1:17,
    2:18,
    3:20,
    4:21,
    5:22,
    6:24,
    7:25,
    8:26,
    9:28,
    10:29,
    11:30,
    12:32,
    13:33,
    14:34,
    15:36,
    16:37,
    17:38,
    18:40,
    19:41,
    20:42,
    21:44,
    22:45,
    23:46,
    24:48
}

moderateDC = {k: v-3 for k,v in highDC.items()}
dcs = {'Extreme':extremeDC,
          'High': highDC,
          'Moderate': moderateDC}

LimitedDamage = {
    -1:4,
    0:6,
    1:7,
    2:11,
    3:14,
    4:18,
    5:21,
    6:25,
    7:28,
    8:32,
    9:35,
    10:39,
    11:42,
    12:46,
    13:49,
    14:53,
    15:56,
    16:60,
    17:63,
    18:67,
    19:70,
    20:74,
    21:77,
    22:81,
    23:84,
    24:88
}
UnlimitedDamage = {
    -1:2,
    0:4,
    1:5,
    2:7,
    3:9,
    4:11,
    5:12,
    6:14,
    7:15,
    8:17,
    9:18,
    10:20,
    11:21,
    12:23,
    13:24,
    14:26,
    15:27,
    16:28,
    17:29,
    18:30,
    19:32,
    20:33,
    21:35,
    22:36,
    23:38,
    24:39
}
aoe = {'Limited': LimitedDamage,
          'Unlimited': UnlimitedDamage}

creatureData = {'AC': ac,
                'Saves': saves,
                'Perception': per,
                'HP': hp,
                'Attack': attack,
                'Damage': damage,
                'DC': dcs,
                'AoE': aoe}

