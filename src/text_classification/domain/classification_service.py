from abc import ABC, abstractmethod
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis

class ClassificationService(ABC):
    
    @abstractmethod
    def get_sentiment_analysis(self, text:str): pass