from flask import Flask
from flask_restful import Api
from src.text_classification.data.own_classification_repository import OwnClassificationRepository
from src.text_classification.data.own_classification_service import OwnClassificationService
from flask import request

app = Flask(__name__)
api = Api(app)
classificationRepository = OwnClassificationRepository()
classificationService = OwnClassificationService(classificationRepository)

@app.route('/text_classification', methods=['POST'])
def classify_text():
    message = request.args.get('message')
    analysis = classificationService.get_sentiment_analysis(message)
    if analysis != None:
        return analysis.toJson(), 200
    else:
        return {}, 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')