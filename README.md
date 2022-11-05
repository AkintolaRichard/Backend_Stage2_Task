## HNG9 Second Task

**Track:** Backend

### :bulb: Study Material
[REST API TUTORIAL](https://www.gravitee.io/blog/rest-api-tutorial) 

### :bulb: Task Description
 - Using the same server setup from stage one
 - Create an (POST) api endoint that takes the following sample json:
 - { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
     - Operation can either be addition, subtraction or mutiplication
     - x can be a number and Integer datatype
     - y can be a number and Integer datatype
 - Based on the operation sent, perform a simple arithmetic operation on x and y
 - Return a response with the result of the operation and your slack username
 { “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }
 Push to GitHub

**Sample Input** `{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }`

**Sample Response Format** `{ “slackUsername”: String, “result”: Integer, “operation_type”: Enum.value }`

### :bulb:Task Duration: 3 Days

### :bulb:Submission Details:
Use the slack command `/grade` along with your hosted URL. If it passes/fails, you would know immediately.
`/grade https://yoururl.com`

### :bulb: Deadline: Saturday 5th Nov 2022 - 11:59PM WAT

### :bulb::bulb: Bonus
We will send in a random string to the `"operation_type"` field . This string will be an operation written in words, for example “Can you please add the following numbers together - 13 and 25.”
This string will not be revealed ahead of time. On marking day, we will reveal the string and test it against all scripts.

**Hint:** GPT-3 could help.



## HNG INTERNSHIP - SIMPLE CALCULATOR API

### Setting up

#### Install Dependencies

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

#### `GET '/'`

- The home page
- Request Arguments: none 
- Returns: An object with keys, `success, message`

```json
{
  "success": true, 
  "message": "Welcome to HNG 9 Stage 2 Task"
}
```

#### `POST '/api/v1.0/calculate'`

- Performs calculations `e.g multiplication, addition, subtraction` and also uses AI to answer calculation statements passed to the `operation_type` key value `e.g`
```json
{
    "operation_type": "I want to add",
    "x": 2,
    "y": 2
}
```
- Request Arguments: json 
```json
{
    "operation_type": "addition",
    "x": 2,
    "y": 2
}
```
- Returns: An object with keys, `result, slackUsername, operation_type`

```json
{
  "operation_type": "addition",
  "result": 4,
  "slackUsername": "username"
}
```
