from src.text_classification.domain.classification_service import ClassificationService
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis
from src.text_classification.domain.classification_repository import ClassificationRepository

class OwnClassificationService(ClassificationService):
    
    def __init__(self, repository: ClassificationRepository):
        self.repository = repository
    
    def get_sentiment_analysis(self, text: str) -> SentimentAnalysis:
        return self.repository.get_sentiment_analysis(text)
        
      