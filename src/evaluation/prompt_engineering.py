from src.hint_generator import generate_enhanced_hint

def get_base_hint(evidence):

    return evidence

def get_enhanced_hint(evidence, gold_sql):

    enhanced_hint = generate_enhanced_hint(gold_sql)
    
    combined_hint = f"{evidence} | Additional hint: {enhanced_hint}"
    return combined_hint
