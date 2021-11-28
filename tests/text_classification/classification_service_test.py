import unittest
from src.text_classification.data.prediction_exception import PredictionException
from src.text_classification.data.own_classification_service import OwnClassificationService
from src.text_classification.data.own_classification_repository import OwnClassificationRepository
from unittest.mock import Mock
from src.text_classification.domain.failure import Failure
from keras_preprocessing.text import tokenizer_from_json
from tensorflow.keras.models import load_model
import json

from src.text_classification.domain.sentiment_analysis import SentimentAnalysis


class TestClassificationService(unittest.TestCase):
    
    
    def __prepareRepo(self):
        model_path = 'G:\Python/text_classification_server/src/text_classification/data/model/90_percent_changed_classes.h5'
        tokenizer_path = 'G:\Python/text_classification_server/src/text_classification/data/model/tokenizer.json'
        with open(tokenizer_path) as f:
            data = json.load(f)
        tokenizer = tokenizer_from_json(data)
        model = load_model(model_path)
        return OwnClassificationRepository(tokenizer, model)
    
    def setUp(self):
        repository = self.__prepareRepo()
        self.repository = repository
        self.service = OwnClassificationService(repository)
    
    def test_bad_scenario(self):
        self.repository.get_sentiment_analysis = Mock(side_effect=PredictionException())
        result = self.service.get_sentiment_analysis('test message');
        self.assertTrue(type(result) is Failure)

    def test_correct_scenario(self):
        analysis = SentimentAnalysis(0.5,0.5)
        self.repository.get_sentiment_analysis = Mock(return_value=analysis)
        result = self.service.get_sentiment_analysis('test message');
        self.assertEqual(result, analysis)
        
if __name__ == '__main__':
    unittest.main()