from flask import Flask, render_template

app = Flask(__name__)

FILENAME = 'requests.html'

@app.route('/')
def hello():
    return render_template(FILENAME)

if __name__ == '__main__':
    app.run(debug=True)
