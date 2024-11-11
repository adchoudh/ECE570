import json
import os
import pandas as pd

def load_dataset(dataset_path):
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)
    return dataset

def load_schema_descriptions(schema_folder_path):
    schema_descriptions = {}
    for file_name in os.listdir(schema_folder_path):
        if file_name.endswith('.csv'):
            table_name = file_name.split('.')[0]
            file_path = os.path.join(schema_folder_path, file_name)
            schema_descriptions[table_name] = pd.read_csv(file_path)
    return schema_descriptions
