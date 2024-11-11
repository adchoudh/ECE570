def evaluate(gpt_sql, gold_sql):
    return gpt_sql.strip().lower() == gold_sql.strip().lower()
