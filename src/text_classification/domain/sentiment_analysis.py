class SentimentAnalysis():
    
    def __init__(self, depression_factor, non_depression_factor):
        self.depression_factor = depression_factor
        self.non_depression_factor = non_depression_factor
    
    def to_json(self):
        return {
            "depressed": str(self.depression_factor),
            "non-depressed": str(self.non_depression_factor)
        }