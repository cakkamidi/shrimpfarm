# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y-Gkz2xgTsKcf5KuhjzSdvyhqEh03xrE
"""

import pandas as pd

data = pd.read_csv('data_agg.csv')

print(data.describe())
print(data.info())
data.head(20)

data = data.drop(['started_at', 'finished_at', 'harvested_at', 'pond_id'], axis=1)
data['avg_weight'] = data['avg_weight']*1000
data.head(20)

X = data.drop(['id', 'total_weight', 'survival_rate', 'avg_weight', 'total_price', 'total', 'size', 'status'], axis=1)
X_SR = X.drop('total_seed', axis=1)
X_aw = X.drop(['growth_rate', 'duration'], axis=1)

# Make predictions
predictions_sr = model_sr.predict(X_SR)
predictions_aw = model_aw.predict(X_aw)
predictions_biomass = model_biomass.predict(X)
predictions_revenue = model_revenue.predict(X)

predictions_sr.to_csv('sr_results.csv', index=False)
predictions_aw.to_csv('aw_results.csv', index=False)
predictions_biomass.to_csv('biomass_results.csv', index=False)
predictions_revenue.to_csv('revenue_results.csv', index=False)