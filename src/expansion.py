
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error


def train_xgboost_model(df):
    features = ['id_city_origin', 'id_city_destination', 'distance']
    X = df[features]
    y = df['freight_cost']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Definindo o espaço de busca para os hiperparâmetros
    param_dist = {
        'n_estimators': [500, 1000, 1500],
        'max_depth': [5, 7, 9],
        'learning_rate': [0.01, 0.1, 0.3],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0]
    }
    
    # Criando o modelo base
    base_model = XGBRegressor(random_state=42)
    
    # Realizando a Random Search
    random_search = RandomizedSearchCV(base_model, param_distributions=param_dist, 
                                       n_iter=10, cv=3, random_state=42, n_jobs=-1)
    random_search.fit(X_train, y_train)
    
    # Obtendo o melhor modelo
    best_model = random_search.best_estimator_

    # Avaliação do modelo
    train_pred = best_model.predict(X_train)
    test_pred = best_model.predict(X_test)
    
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

    train_mape = mean_absolute_percentage_error(y_train, train_pred)
    test_mape = mean_absolute_percentage_error(y_test, test_pred)

    print(f"Melhores parâmetros: {random_search.best_params_}")
    print(f"RMSE train: {train_rmse}")
    print(f"RMSE test: {test_rmse}")
    print(f"MAPE train: {train_mape:.4f}")
    print(f"MAPE test: {test_mape:.4f}")
    
    # Calculando a importância das features
    perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=10, random_state=42)
    
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': perm_importance.importances_mean
    }).sort_values('importance', ascending=False)
    
    print("\nImportância das Features:")
    print(feature_importance)
    
    return best_model

def expand_quotes(model, distances_df, target_destinations):
    all_mt_origins = distances_df['id_city_origin'].unique()
    
    expanded_quotes = []
    for origin in all_mt_origins:
        for destination in target_destinations:
            distance = distances_df[(distances_df['id_city_origin'] == origin) & 
                                    (distances_df['id_city_destination'] == destination)]['distance'].values[0]
            
            prediction = model.predict([[origin, destination, distance]])[0]
            
            expanded_quotes.append({
                'id_city_origin': origin,
                'id_city_destination': destination,
                'freight_cost': prediction
            })
    
    return pd.DataFrame(expanded_quotes)