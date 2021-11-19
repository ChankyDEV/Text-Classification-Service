from abc import ABC, abstractmethod
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis

class ClassificationRepository(ABC):
    
    @abstractmethod
    def get_sentiment_analysis(self,text) -> SentimentAnalysis : pass