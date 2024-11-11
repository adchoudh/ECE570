from src.evaluation.correction_logic import SQLCorrection

class SQLCorrectionModel:
    def __init__(self):
        self.corrector = SQLCorrection()

    def correct_query(self, generated_sql):
        return self.corrector.correct_query(generated_sql)
