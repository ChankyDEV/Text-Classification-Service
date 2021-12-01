from flask import Flask
from flask_restful import Api
from flask import request
from init import Initializer
from src.text_classification.domain.sentiment_analysis import SentimentAnalysis

app = Flask(__name__)
api = Api(app)

initializer = Initializer(model_path = 'G:\Python/text_classification_server/src/text_classification/data/model/model_2021-11-28_best.h5',
                         tokenizer_path = 'G:\Python/text_classification_server/src/text_classification/data/model/tokenizer.json')
classificationService, classificationRepository = initializer.initialize()

@app.route('/text_classification', methods=['POST'])
def classify_text():
    message = request.args.get('message')
    analysis = classificationService.get_sentiment_analysis(message)
    if type(analysis) == SentimentAnalysis:
        return analysis.to_json(), 200
    else:
        return {
            "message": "Something went wrong while trying to classify your message. Please try again later."
            }, 404


if __name__ == '__main__':
    app.run()