
import openai

BASE_PROMPT = """
Generate an SQL query for me.

Question: {question}
Hint: {evidence}
ONLY return the SQL query without any explanation, notes, or formatting. Do not include code blocks or any additional text.

"""

ENHANCED_PROMPT = """
Generate an SQL query for me.

Database schema in the form of CREATE_TABLE statements:

{database_schema}

Using valid SQL, answer the following question based on the tables provided above.

Hint: {evidence}
Question: {question}
ONLY return the SQL query without any explanation, notes, or formatting. Do not include code blocks or any additional text.

"""

class ChatGPTModel:
    def __init__(self, api_key, model_name):
        openai.api_key = api_key
        self.model_name = model_name

    def generate_query(self, question, evidence, schema_hint=None):
        if schema_hint:
            prompt = ENHANCED_PROMPT.format(
                question=question,
                evidence=evidence,
                database_schema=schema_hint
            )
        else:
            prompt = BASE_PROMPT.format(
                question=question,
                evidence=evidence
            )

        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response['choices'][0]['message']['content'].strip()
