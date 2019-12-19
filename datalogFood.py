# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:23:55 2019

@author: Johann
"""

from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms("X, food")
pyDatalog.create_terms("asian, eastern, western")
pyDatalog.create_terms("rice, contain_coconut, mush_fried, hassambal, variant_type, hasilment, fried_rice")
pyDatalog.create_terms("noodle, has_soup, no_soup, sichon_noodle, denden_noodle ")
pyDatalog.create_terms("contain_meat, use_muteq, has_rice, kebab, binguin, has_veggies, falafel")
pyDatalog.create_terms("french_origin, pastay, bread, croissant, baguette")
pyDatalog.create_terms("italian_origin, has_sauce, penne")


food(X) <= asian(X)
food(X) <= eastern(X)
food(X) <= western(X)

asian(X) <= rice(X)
asian(X) <= noodle(X)
rice(X) <= contain_coconut(X) & hassambal(X) & hasilment(X)
rice(X) <= mush_fried(X) & variant_type(X) & fried_rice(X)
noodle(X) <= has_soup(X) & sichon_noodle(X)
noodle(X) <= no_soup(X) & denden_noodle(X)

eastern(X) <= contain_meat(X)
eastern(X) <= has_veggies(X)
contain_meat(X) <= use_muteq(X) & kebab(X)
has_veggies(X) <= has_rice(X) & binguin(X)
has_veggies(X) <= falafel(X)

western(X) <= french_origin(X)
western(X) <= italian_origin(X)
french_origin(X) <= pastay(X) & croissant(X)
french_origin(X) <= bread(X) & baguette(X)

italian_origin(X) <= has_sauce(X) & penne(X)


+use_muteq('my_food')
+kebab('my_food')

print(pyDatalog.ask('contain_meat(X)'))

-kebab('my_food')

print(pyDatalog.ask('contain_meat(X)'))
