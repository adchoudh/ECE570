# hint_generator.py

import sqlparse
import re

def load_schema_info(schema_folder):
    """
    Loads schema information from the CSV files located in the specified folder.
    """
    schema_info = {}
    # Load each CSV file as a table's schema
    for table_name in ["account", "district", "client", "card", "loan", "trans", "order", "disp"]:
        with open(f"{schema_folder}/{table_name}.csv", "r") as f:
            # Read column names and descriptions from each file
            lines = f.readlines()
            columns = [line.split(",")[0].strip() for line in lines[1:]]
            schema_info[table_name] = columns
    return schema_info

def extract_tables(sql_query):
    """
    Extracts table names from a SQL query.
    """
    parsed = sqlparse.parse(sql_query)[0]
    tables = []
    aliases = {}
    for token in parsed.tokens:
        if token.ttype is None and token.is_group:
            for sub_token in token.tokens:
                if sub_token.ttype is None and isinstance(sub_token, sqlparse.sql.Identifier):
                    identifier_str = str(sub_token).lower()
                    if 'join' in identifier_str or 'from' in identifier_str:
                        table_name = identifier_str.split()[-1]
                        tables.append(table_name)
                        if " as " in identifier_str:
                            alias = identifier_str.split(" as ")[1].strip()
                            aliases[alias] = table_name
                        else:
                            aliases[table_name] = table_name
    return tables, aliases

def generate_enhanced_hint(evidence, gold_sql, schema_info):
    """
    Generates an enhanced hint by combining the provided evidence with extracted schema info.
    """
    tables, aliases = extract_tables(gold_sql)
    
    # Build the hint by incorporating table and column details
    hint_details = []
    for table in tables:
        table_name = aliases.get(table, table)  # Get the actual table name if an alias is used
        if table_name in schema_info:
            column_list = schema_info[table_name]
            hint_details.append(f"Table '{table_name}': columns are {', '.join(column_list)}")
        else:
            hint_details.append(f"Table '{table_name}' not found in schema.")

    enhanced_hint = f"{evidence} | Additional hint: {'; '.join(hint_details)}"
    return enhanced_hint
