# -*- coding: utf-8 -*-
# Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('california_housing_train.csv', sep=',')

min_population = df.population.min()
print(df.population.min())
df[df['population'] == min_population].households.max()
print(df.households.max())
exit()