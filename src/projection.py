
import pandas as pd

def project_quotes(best_model, historical_quotes, distances_df, weeks=52):
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