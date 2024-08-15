# main.py
from data_processing import load_data, preprocess_data
from expansion import train_xgboost_model, expand_quotes
from projection import project_quotes
import os

def main():
    # Carregar dados
    freight_df = load_data('../data/freight_costs.csv')
    distances_df = load_data('../data/distances.csv')
    
    # Pré-processar dados
    processed_df = preprocess_data(freight_df, distances_df)
    
    # Treinar modelo XGBoost
    best_model = train_xgboost_model(processed_df)
    
    # Expandir cotações
    target_destinations = [1501303, 1506807, 3205309, 3548500, 4118204, 4207304, 4216206, 4315602]
    expanded_quotes = expand_quotes(best_model, distances_df, target_destinations)
    expanded_quotes.to_csv('../output/historical_quotes.csv', index=False)
    
    # Projetar cotações para as próximas 52 semanas
    projected_quotes = project_quotes(best_model, expanded_quotes, distances_df)
    projected_quotes.to_csv('../output/projected_quotes.csv', index=False)

if __name__ == "__main__":
    main()