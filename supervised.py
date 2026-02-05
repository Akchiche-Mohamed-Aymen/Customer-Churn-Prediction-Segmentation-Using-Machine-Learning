import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
from imblearn.over_sampling import RandomOverSampler

def imbalanced_to_balanced(X , y):
    oversample = RandomOverSampler(sampling_strategy='minority' , random_state=42 )
    X_resampled, y_resampled = oversample.fit_resample(X, y)
    return X_resampled , y_resampled
def model_evaluation(y , y_pred):
    accuracy = round(accuracy_score(y, y_pred) , 4)
    precision = round(precision_score(y, y_pred),4)
    recall = round(recall_score(y, y_pred) , 4)
    f1 = round(f1_score(y, y_pred) , 4)
    print(f"Accuracy: {accuracy * 100}")
    print(f"Precision: {precision * 100}")
    print(f"Recall: {recall * 100}")
    print(f"F1-Score: {f1 * 100}")
data = pd.read_csv("data_for classification.csv")
X = data.drop(columns=["churn"])
y = data["churn"]
X_res , y_res = imbalanced_to_balanced(X,y)
print(len(y) , len(y_res))
X_train, X_test, y_train, y_test = train_test_split(X_res , y_res, test_size=0.3,shuffle=True , random_state=42)
model = RandomForestClassifier(n_estimators=20,min_samples_leaf=7,max_depth=10, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Evaluate model
model_evaluation(y_test , y_pred)

'''save model in classification.pkl file'''
import pickle
with open('random_forest_clf.pkl', 'wb') as f:
    pickle.dump(model, f)
