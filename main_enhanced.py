import json
from src.models.chatgpt_model import ChatGPTModel
from src.schema_parser import load_schema_info 
from src.hint_generator import generate_enhanced_hint 

def main():
    api_key = ""
    model_name = "gpt-4"
    
    with open("datasets/financial.json") as f:
        dataset = json.load(f)
    schema_info = load_schema_info("database_description")
    
    gpt_model = ChatGPTModel(api_key, model_name)
    
    results = []
    for data_point in dataset:
        question = data_point["question"]
        evidence = data_point["evidence"]
        gold_sql = data_point["SQL"]
        
        schema_hint = generate_enhanced_hint(evidence, gold_sql, schema_info)
        
        gpt_sql = gpt_model.generate_query(question, evidence, schema_hint)
        
        result = {
            "question": question,
            "hint": evidence,
            "schema_hint": schema_hint,
            "gold_sql": gold_sql,
            "gpt_sql": gpt_sql,
            "correct": gpt_sql.strip() == gold_sql.strip()
        }
        results.append(result)

    with open("results_enhanced.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()
