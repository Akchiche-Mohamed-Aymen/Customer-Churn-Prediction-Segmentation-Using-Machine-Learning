'''you have prepped_data.csv file , import it and choose best k for kmeans using elbow method , you have 
   target column 'churn' which you should drop before fitting kmeans model , the elbow curve should be saved as 
   elbow_curve.png  k = range(2 , 11)'''
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
df = pd.read_csv('prepped_data.csv')
df_features = df.drop(columns=['churn'])
scaler = StandardScaler()
inertia_values = []
k_values = range(2 , 11)
best_k = -1
best_score = -1
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_features)
    inertia_values.append(kmeans.inertia_)
    silhouette_avg = silhouette_score(df_features, kmeans.labels_)
    if silhouette_avg > best_score:
        best_k = k
        best_score = silhouette_avg
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.grid()
plt.show()
plt.savefig('elbow_curve.png')
'''store best_k in json file best_k.json as {"K": best_k}'''
import json
with open('best_k.json', 'w') as f:
    json.dump({"K": best_k}, f) 

# Run this script as: py choosing_best_k.py