import json
from src.models.chatgpt_model import ChatGPTModel

def main():
    api_key = ""
    model_name = "gpt-4"
    
    with open("datasets/financial.json") as f:
        dataset = json.load(f)
    
    gpt_model = ChatGPTModel(api_key, model_name)
    
    results = []
    
    for data_point in dataset:
        question = data_point["question"]
        evidence = data_point["evidence"]
        
        gpt_sql = gpt_model.generate_query(question, evidence)
        
        result = {
            "question": question,
            "hint": evidence,  
            "gold_sql": data_point["SQL"],
            "gpt_sql": gpt_sql,
            "correct": gpt_sql.strip() == data_point["SQL"].strip()
        }
        
        results.append(result)
    
    with open("results_base.json", "w") as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    main()
