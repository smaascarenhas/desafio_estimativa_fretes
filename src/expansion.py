
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error


def train_xgboost_model(df):
    """ Essa função tem o objetivo de treinar um modelo XGBoost para prever custos de frete.
        Ela realiza as seguintes etapas:
        1. Prepara os dados, separando features e target.
        2. Divide os dados em conjuntos de treino e teste.
        3. Define um intervalo de busca para hiperparâmetros.
        4. Utiliza o (Random Search) para otimização de hiperparâmetros.
        5. Treina o modelo com os melhores hiperparâmetros encontrados.
        6. Avalia o modelo usando RMSE e MAPE para os conjuntos de treino e teste.
        7. Calcula a importância das features usando permutation importance.
        8. Retorna o melhor modelo treinado.
    """
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
    """ Essa função tem o objetivo de expandir as cotações de frete para todas as combinações
        de origens no Mato Grosso e destinos específicos.
        Ela realiza as seguintes etapas:
        1. Identifica todas as origens únicas no Mato Grosso.
        2. Para cada combinação de origem e destino alvo:
           - Recupera a distância correspondente.
           - Usa o modelo treinado para prever o custo do frete.
        3. Compila todas as previsões em um DataFrame.
        4. Retorna o DataFrame com as cotações expandidas.
    """
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