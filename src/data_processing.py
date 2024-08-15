# data_processing.py
import pandas as pd
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path, sep=';', decimal=',')
    if 'id_city_origin' in df.columns and 'id_city_destination' in df.columns:
        df['id_city_origin'] = df['id_city_origin'].astype(int)
        df['id_city_destination'] = df['id_city_destination'].astype(int)
    if 'freight_cost' in df.columns:
        df['freight_cost'] = df['freight_cost'].astype(float)
    if 'distance' in df.columns:
        df['distance'] = df['distance'].astype(float)
    return df

def preprocess_data(freight_df, distances_df):
    # Criar um dicionário de distâncias para lookup rápido
    distance_dict = distances_df.set_index(['id_city_origin', 'id_city_destination'])['distance'].to_dict()
    
    # Função para obter a distância
    def get_distance(origin, destination):
        return distance_dict.get((origin, destination), np.nan)
    
    # Adicionar coluna de distância ao freight_df
    freight_df['distance'] = freight_df.apply(lambda row: get_distance(row['id_city_origin'], row['id_city_destination']), axis=1)
    
    return freight_df 