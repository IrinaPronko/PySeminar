# -*- coding: utf-8 -*-
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

df = pd.read_csv('california_housing_train.csv', sep=',')

df[
    (df['population'] > 0) &
    (df['population'] < 500)
].medianHouseValue.mean()
print(df.medianHouseValue.mean())
exit()
