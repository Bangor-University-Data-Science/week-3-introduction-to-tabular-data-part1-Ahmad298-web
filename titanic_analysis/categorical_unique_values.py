import pandas as pd

def display_unique_values(df, categorical_features):
    unique_values = {}
    
    for feature in categorical_features:
       unique_values[feature] = df[feature].unique().tolist()
    
    
    return unique_values

if __name__ == "__main__":
    df = pd.read_csv('data/titanic.csv') 

    categorical_features = ['Sex', 'Embarked']  
    
    unique_values = display_unique_values(df, categorical_features)