import pandas as pd
from sklearn.preprocessing import StandardScaler

def scaler(X_test):
    df = pd.read_csv('C:/Users/acer/Desktop/Web App/data/heart.csv')
    X = df.iloc[:,:-1]
    scaler = StandardScaler()
    X_scale = scaler.fit_transform(X)
    X_test_scale = scaler.transform(X_test)
    
    return X_test



