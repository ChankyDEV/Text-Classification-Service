class SentimentAnalysis():
    
    def __init__(self, depression_factor, other_emotion_factor):
        self.depression_factor = depression_factor
        self.other_emotion_factor = other_emotion_factor
    
    def to_json(self):
        return {
            "depressed": str(self.depression_factor),
            "non-depressed": str(self.other_emotion_factor)
        }