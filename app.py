from flask import Flask, request, abort, jsonify
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

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
    def retrieve_calculation():
        body = request.get_json()
        print
        operation_type = body.get('operation_type', None)
        firstInt = body.get('x', None)
        secondInt = body.get('y', None)

        result = 0
        try:
            if operation_type != None and firstInt != None and secondInt != None:
                operation_type = operation_type.lower()
                if (operation_type == "addition" or operation_type == "subtraction" or operation_type == "multiplication"):
                    if (str(type(firstInt)) != "<class 'int'>" and str(type(secondInt)) != "<class 'int'>"):
                        if operation_type == "addition":
                            result = firstInt + secondInt
                        elif operation_type == "subtraction":
                            result = firstInt - secondInt
                        elif operation_type == "multiplication":
                            result = firstInt * secondInt
                    else:
                        abort(400)
                else:
                    abort(400)
            else:
                abort(400)
        except Exception as e:
            abort(400)
        
        return jsonify({
            'slackUsername': 'laolu',
            'result': result,
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

    return app
