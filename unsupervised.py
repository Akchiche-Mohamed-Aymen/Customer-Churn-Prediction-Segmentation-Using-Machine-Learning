from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import json
from sklearn.pipeline import Pipeline
data = pd.read_csv('prepped_data.csv')
#==============================================================================
X = data.drop('churn', axis=1)
y = data['churn']
with open('best_k.json', 'r') as f:
    best_k = json.load(f)['K']
kmeans_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('kmeans', KMeans(n_clusters=best_k, random_state=42))
])
kmeans_pipeline.fit(X)
data['Segment'] = kmeans_pipeline.named_steps['kmeans'].labels_
data.to_csv('data_for classification.csv' , index=False)
import pickle
with open('kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans_pipeline, f)


#py unsupervised.py