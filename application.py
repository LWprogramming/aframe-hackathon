from flask import Flask, render_template, json, request, jsonify, session
from flask_session import Session
from tempfile import mkdtemp
import openai

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

chat_log = ""
FILENAME = 'requests.html'

@app.route('/', methods=["GET", "POST"])
def hello():
    '''The display page for the user'''

    return render_template(FILENAME)

@app.route('/index')
def index():
    '''The display page for the user'''
    return render_template("index.html")


@app.route("/reply", methods=['POST'])
def reply():
    '''Processses the input from user and returns it back to the html page'''

    openai.api_key = "nice try"
    completion = openai.Completion()

    # getting post request from requests.html
    question = ([i for i in request.form.keys()][0])
    print("human input: " + question)
    
    global chat_log

    '''Check if it's the first question?, i.e., the chat log is empty'''
    if not chat_log:
        # reading the promts file for initial training data
        prompt_file = open('prompts.txt', 'r')
        start_chat_log = prompt_file.read()
        propmt_file.close()
        
        # storing the initial prompts to chat_log
        chat_log = start_chat_log

    # format the prompt
    prompt = f"{chat_log}\nHuman: {question}\nAI:"  

    # generate reponse from the API
    response = completion.create(
            prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=150)

    # extract answer from response
    answer = response.choices[0].text.strip()

    # storing the chat logs
    chat_log = prompt + answer

    # printing chat logs
    print("------------------")
    print(chat_log)
    print("------------------")

    print(answer)

    print('received request')

    # returning the answer
    return jsonify({'answer': answer})


# if __name__ == '__main__':
#     app.run(debug=True)
