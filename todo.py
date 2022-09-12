#app.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', method=['POST'])
def addTodo():
    # Access body information

if __name__ == "__main__":
    app.run(debug=True)


# All 4 of them pass information through query parameters and path parameters
# Query parameters: www.google.com?page=3&row=12345&user=joe
# Path parameters: www.google.com/someRootURL/3/12345/joe
# For Post and Put
    # Info will be passed in the body