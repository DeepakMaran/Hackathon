# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:39:51 2017

@author: Deepak Maran
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import xlrd
import sklearn
import warnings
from sklearn.linear_model import LinearRegression

linear_regression_model = LinearRegression()

os.chdir('C:/Users/Deepak Maran/Projects/Hackathon')

enigma_data = []
d1 = pd.read_csv("green_tripdata_2016-01.csv")
enigma_data.append(d1)

spending = []
housing_spending = []
i=13
for i in range(0,13):
    print(i)
    fname = 'GovernmentSpendingContracts-' + str(2000+i) + '.csv'
    g = pd.read_csv(fname)
    g = g[['dollars_obligated','maj_agency_cat','signed_date','registration_date','number_of_employees','annual_revenue']]
    spending.append(sum(g.dollars_obligated))
    ids = g['maj_agency_cat'].str.contains('8600')
    g = g[ids]

#    enigma_data.append(g)

plt.plot(range(2000,2018),spending[0:18])
plt.scatter(years, whisky, color = 'red')
plt.scatter(years, parsnips, color = 'blue')
plt.show()

i = 0
print(i)
fname = 'GovernmentSpendingContracts-' + str(2000+i) + '.csv'
g = pd.read_csv(fname)
ids = g['maj_agency_cat'].str.contains('8600')
g = g[ids]

plt.clf()
g = g.drop_duplicates(subset=['piid'], keep='first')
c = g['state'].value_counts()
c = c[1:20]
c.to_frame(name='No_of_projects').to_excel('Projects_by_state.xlsx', sheet_name='Housing_only')
p = c.plot(kind='barh')
plt.title('Housing projects')
plt.ylabel('States')
plt.xlabel('No_of_projects')
p.figure


## Model

housing_data = pd.read_csv('pos_05_12_housing.csv')
housing_data.columns
housing_data.signed_date =  pd.to_datetime(housing_data.signed_date)
housing_data.registration_date =  pd.to_datetime(housing_data.registration_date)

housing_data['age_of_company'] = housing_data['signed_date'] - housing_data['registration_date']
avg_age = housing_data.age_of_company.mean()
avg_revenue = housing_data.annual_revenue.mean()
avg_emply = housing_data.number_of_employees.mean()

#linear_regression_model.fit(housing_data.dollars_obligated('output', axis = 1), housing_data.dollars_obligated)

#risk_metric = housing_data.dollars_obligated/()

age_days = pd.to_numeric(housing_data.age_of_company)/(24*3600*1e9)
plt.scatter(age_days, housing_data.dollars_obligated)

housing_data = housing_data[housing_data.annual_revenue < 1e10]
plt.scatter(housing_data.annual_revenue, housing_data.dollars_obligated)
plt.xlabel('Revenue (in dollars)',fontsize=20)
plt.ylabel('Obligated_amount (in dollars)',fontsize=20)
plt.show()

