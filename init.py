from tensorflow.keras.models import load_model
from src.text_classification.data.own_classification_repository import OwnClassificationRepository
from src.text_classification.data.own_classification_service import OwnClassificationService
from keras_preprocessing.text import tokenizer_from_json
import json
from src.text_classification.domain.classification_repository import ClassificationRepository
from src.text_classification.domain.classification_service import ClassificationService
from typing import Union

class Initializer:
    def __init__(self, model_path, tokenizer_path):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path

    def initialize(self) -> Union[ClassificationService, ClassificationRepository]:
        tokenizer = self.__load_tokenizer()
        model = self.__load_model()
        classificationRepository = OwnClassificationRepository(tokenizer=tokenizer, model=model)
        classificationService = OwnClassificationService(classificationRepository)
        return classificationService, classificationRepository 

    
    def __load_tokenizer(self):
        with open(self.tokenizer_path) as f:
            data = json.load(f)
        return tokenizer_from_json(data)

    def __load_model(self):
        return load_model(self.model_path)