# HNG INTERNSHIP - SIMPLE CALCULATOR API

## Setting up

## Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

### Run the Server

From within the app directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=development
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Documentation Example

`POST '/api/v1.0/calculate'`

- Performs simple calculations `(multiplication, addition, subtraction)`
- Request Arguments: json 
```json
{
    "operation_type": "addition",
    "x": 2,
    "y": 2
}
```
- Returns: An object with keys, `result, slackUsername`

```json
{
  "result": 4, 
  "slackUsername": "laolu"
}
```
