from tensorflow.python.keras.preprocessing.text import Tokenizer
from src.text_classification.domain.classification_repository import ClassificationRepository
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis
import json
from keras_preprocessing.text import tokenizer_from_json
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

class OwnClassificationRepository(ClassificationRepository):

    def process(sentence_to_process:str, tokenizer: Tokenizer):
        tokenized_sentence = tokenizer.texts_to_sequences([sentence_to_process])
        expanded_sentence = pad_sequences(tokenized_sentence, padding='post', maxlen=286)
        return expanded_sentence
        
    def loadTokenizer(self):
        with open('tokenizer.json') as f:
            data = json.load(f)
        return tokenizer_from_json(data)
    
    
    def predict(self,message, model, tokenizer):
        processed = self.process(message, tokenizer)
        reshaped_sentence = tf.reshape(processed,[1,286])
        prediction = model.predict(reshaped_sentence)
        return prediction[0][0],prediction[0][1]
        
    def get_sentiment_analysis(self, text) -> SentimentAnalysis:
        try:
            tokenizer = self.loadTokenizer()
            model = load_model('G:\Python/text_classification_server/text_classification_model.h5')
            sad, other = self.predict(text, model, tokenizer)
            return SentimentAnalysis(sad,other)
        except:
            return None