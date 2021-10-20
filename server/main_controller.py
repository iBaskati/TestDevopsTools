from flask import Flask
app = Flask(__name__)


@app.route('/listOfNames', methods=['GET', 'POST'])
def get_list_of_names():
    return {"Name": "Testing devops tools", "None": "None"}


@app.route("/", methods=["GET", "POST"])
def home():
    return {"Page": "Home"}


def run_server(host, port, debug=True):
    app.run(host=host, port=port, debug=debug)
