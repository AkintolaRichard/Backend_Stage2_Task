import os
import openai
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

<<<<<<< HEAD
operation_types = {"addition": "+", "subtraction": "-", "multiplication": "*"}

openai.api_key = os.environ.get("API_KEY")

@app.route('/')
def index():
    return jsonify({
        'success': True,
        'message': 'Welcome to HNG 9 Stage 2 Task'
    })

@app.route('/api/v1.0/calculate', methods=['POST'])
def get_simple_calculation():
    body = request.get_json()

    result = None
    operation_type = None
    body_data_operation = body.get("operation_type", None)

    if body_data_operation != None:
        body_data_operation = body_data_operation.lower()
    
    if body_data_operation in operation_types:
        operation_type = body_data_operation
=======
    CORS(app, resources={r'/api/*': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,DELETE,OPTIONS'
        )
        return response


    @app.route('/api/v1.0/calculate', methods=['POST'])
    @cross_origin()
    def retrieve_calculation():
        body = request.get_json()
>>>>>>> 2cdfc131d52d249b35d8270c20165be4bcb0e016

        firstInt = body.get('x', None)
        secondInt = body.get('y', None)
        if firstInt != None and secondInt != None:
            result = eval(f'{firstInt}{operation_types[operation_type]}{secondInt}')

    else:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"{body_data_operation} \n\n| solution | operation_type |",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        _, result, operation_type, _ = [
            x.strip() for x in response.choices[0].text.split("\n")[-1].split("|")
            ]

    return jsonify({
        'slackUserName': 'laolu',
        'result': int(result),
        'operation_type': operation_type
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
        }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
    }), 422

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
    }), 400

@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405

@app.errorhandler(500)
def not_successful(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Request Not Successful'
    }), 500


if __name__ == '__main__':
    app.run()
