from flask import Flask, render_template, json, request
import openai

app = Flask(__name__)
chat_log = ""

FILENAME = 'requests.html'

@app.route('/')
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

    openai.api_key = "LALALALALLALA"
    completion = openai.Completion()

    start_chat_log = """The following is a conversation between a human and their friend AI. The AI is quite friendly, thoughtful, optimistic, and is good at listening.
                        Human: Hi
                        AI: Hey, how's it going?
                        Human: Alright. i guess I've been feeling kinda down lately
                        AI: I'm sorry to hear that. do you want to talk about it?"""

    question = request.form["question"]  # the input given by the user

    global chat_log

    '''Check if it's the first question?'''
    if not chat_log:
        chat_log = start_chat_log

    prompt = f"{chat_log}Human: {question}\nAI:"  # format the prompt

    # generate reponse from the API
    
    response = completion.create(
            prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=150)

    answer = response.choices[0].text.strip()

    print(answer)

    print('received request')

    return json.dumps({'answer': answer})


# if __name__ == '__main__':
#     app.run(debug=True)
