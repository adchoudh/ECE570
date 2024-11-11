from src.evaluation.prompt_engineering import generate_prompt

def generate_prompt_with_hint(question, gold_sql, base_hint=""):
    hint = f"{base_hint} The query involves {analyze_sql_structure(gold_sql)}."
    return generate_prompt(question, hint)

def analyze_sql_structure(sql_query):
    if "JOIN" in sql_query:
        return "joining tables"
    if "WHERE" in sql_query:
        return "filtering criteria"
    if "COUNT" in sql_query:
        return "counting entries"
    return "basic SQL operations"
