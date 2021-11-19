class SentimentAnalysis():
    
    def __init__(self, depression_factor, other_emotion_factor):
        self.depression_factor = depression_factor
        self.other_emotion_factor = other_emotion_factor
    
    def toJson(self):
        return {
            "sad": str(self.depression_factor),
            "other": str(self.other_emotion_factor)
        }