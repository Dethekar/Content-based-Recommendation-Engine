from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger import swag_from
from recommendation_engine import recommended_shows #Importing engine function
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

#Avoid switching the order of 'title' and 'confidence' keys
app.config['JSON_SORT_KEYS'] = False

#Load the dataset. Only title column is needed for indexing
netflix_titles_df = pd.read_csv('netflix_titles.csv', usecols=[2])

tfidf_vect_pkl = pickle.load(open('tfidf_vectorizer.pickle', 'rb'))

#API endpoint
@app.route('/api/', methods=['POST'])
@swag_from('swagger_doc.yml')
def process_request():

    #Parse received JSON request
    user_input = request.get_json()

    #Extract show title
    title = user_input['title']

    #Call recommendation engine
    recommended_shows_dict = recommended_shows(title, netflix_titles_df, tfidf_vect_pkl)

    return jsonify(recommended_shows_dict)


if __name__ == '__main__':

    app.run()
