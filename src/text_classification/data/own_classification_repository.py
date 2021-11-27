from keras_preprocessing.text import Tokenizer
from src.text_classification.domain.classification_repository import ClassificationRepository
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis
from src.text_classification.data.prediction_exception import PredictionException
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

class OwnClassificationRepository(ClassificationRepository):

    def __init__(self, tokenizer: Tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    def __process(self, sentence_to_process):
        tokenized_sentence = self.tokenizer.texts_to_sequences([sentence_to_process])
        expanded_sentence = pad_sequences(tokenized_sentence, padding='post', maxlen=307)
        return expanded_sentence
    
    
    def __predict(self, text):
        processed = self.__process(text)
        reshaped_sentence = tf.reshape(processed,[1,307])
        prediction = self.model.predict(reshaped_sentence)
        return prediction[0][0],prediction[0][1]
        
    def get_sentiment_analysis(self, text):
        try:
            sad, other = self.__predict(text)
            return SentimentAnalysis(sad,other)
        except:
            raise  PredictionException()