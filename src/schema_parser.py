import os
import pandas as pd

def load_schema_info(schema_dir):
    schema_info = {}
    for file_name in os.listdir(schema_dir):
        if file_name.endswith(".csv"):
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(schema_dir, file_name)
            schema_info[table_name] = pd.read_csv(file_path)
    return schema_info

def generate_hint(schema_info, relevant_tables):
    hints = []
    for table in relevant_tables:
        if table in schema_info:
            columns = schema_info[table]
            column_hints = f"Table {table}: " + ", ".join(
                f"{row['original_column_name']} ({row['column_description']})"
                for _, row in columns.iterrows() if 'original_column_name' in row and 'column_description' in row
            )
            hints.append(column_hints)
    return " | ".join(hints)
