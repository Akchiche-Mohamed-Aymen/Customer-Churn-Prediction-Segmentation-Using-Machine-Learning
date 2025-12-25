import pandas as pd
import pickle
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)
with open('random_forest_clf.pkl', 'rb') as file:
    rf_model = pickle.load(file)       
def predict_cluster(data):
    cluster = kmeans_model.predict(data)
    return cluster[0]

df = pd.read_csv('data_for classification.csv')
df = df.drop(columns=['Segment' , 'churn'])
def predict_churn(data):
    try:
        data = pd.DataFrame(data)
        data = data[df.columns]
        data['Segment'] = predict_cluster(data.iloc[[0]])
        churn , churn_prob = rf_model.predict(data) , rf_model.predict_proba(data)
        return churn[0] , round(churn_prob[0][1] , 4) * 100
    except Exception as e:
        print(f"Error in predicting cluster: {e}")