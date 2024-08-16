
import pandas as pd

def project_quotes(best_model, historical_quotes, distances_df, weeks=52):
    """ Esta função tem o objetivo de projetar cotações de frete para as próximas 52 semanas com base em um modelo treinado.
    
    Ela realiza as seguintes operações:
    1. Itera sobre todas as combinações únicas de origem e destino nas cotações históricas.
    2. Obtém a distância correspondente do DataFrame de distâncias.
    3. Utiliza o modelo treinado para prever o custo do frete para cada combinação.
    4. Cria um DataFrame com as projeções de frete para todas as combinações.
    """
    projected_quotes = []
    
    for origin in historical_quotes['id_city_origin'].unique():
        for destination in historical_quotes['id_city_destination'].unique():
            distance = distances_df[(distances_df['id_city_origin'] == origin) & 
                                    (distances_df['id_city_destination'] == destination)]['distance'].values[0]
            
            prediction = best_model.predict([[origin, destination, distance]])[0]
            
            projected_quotes.append({
                'id_city_origin': origin,
                'id_city_destination': destination,
                'freight_cost': prediction
            })
    
    return pd.DataFrame(projected_quotes)