# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:15:56 2019

@author: Nicolas
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

degree_dirt = ctrl.Antecedent(np.arange(1, 101, 1), 'degree_dirt')
type_dirt= ctrl.Antecedent(np.arange(1, 101, 1), 'type_dirt')
wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')

degree_name = ["Low", "Medium", "High"]
type_name = ["NonFat", "Medium", "Fat"]

degree_dirt.automf(names=degree_name)
type_dirt.automf(names=type_name)

degree_dirt.view()
type_dirt.view()

wash_time['very_short'] = fuzz.trimf(wash_time.universe, [0, 8, 12])
wash_time['short'] = fuzz.trimf(wash_time.universe, [8, 12, 20])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [12, 20, 40])
wash_time['long'] = fuzz.trimf(wash_time.universe, [20, 40, 60])
wash_time['very_long'] = fuzz.trimf(wash_time.universe, [40, 60, 60])

wash_time.view()


rule1 = ctrl.Rule(degree_dirt['High'] | type_dirt['Fat'], wash_time['very_long'])
rule2 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['Fat'], wash_time['long'])
rule3 = ctrl.Rule(degree_dirt['Low'] | type_dirt['Fat'], wash_time['long'])
rule4 = ctrl.Rule(degree_dirt['High'] | type_dirt['Medium'], wash_time['long'])
rule5 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['Medium'], wash_time['medium'])
rule6 = ctrl.Rule(degree_dirt['Low'] | type_dirt['Medium'], wash_time['medium'])
rule7 = ctrl.Rule(degree_dirt['High'] | type_dirt['NonFat'], wash_time['medium'])
rule8 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['NonFat'], wash_time['short'])
rule9 = ctrl.Rule(degree_dirt['Low'] | type_dirt['NonFat'], wash_time['very_short'])


washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
washing = ctrl.ControlSystemSimulation(washing_ctrl)

washing.input['degree_dirt'] = 40
washing.input['type_dirt'] = 70

washing.compute()

print(washing.output['wash_time'])
wash_time.view(sim=washing)
