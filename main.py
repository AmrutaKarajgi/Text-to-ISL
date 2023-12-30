from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='')

def get_sigml_file(word):
    sigml_directory = os.path.join('static', 'SignFiles')
    sigml_file_path = os.path.join(sigml_directory, word + ".sigml")
    print(sigml_file_path)
    if os.path.isfile(sigml_file_path):
        print("File found")
        return word + ".sigml"
    else:
        print("File not found")
        return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_word():
    word = "about"  # Retrieve the word from the form data; default to None if not found

    # Check if the word is provided and is not an empty string
    if word and word.strip():
        # Convert the word to lowercase
        word = word.lower()
        sigml_file = get_sigml_file(word)

        if sigml_file:
            # Return the SigML file if found
            return send_from_directory('static/SignFiles', sigml_file)
        else:
            # Return a message if no SigML file is found for the word
            return f"No SigML file found for the word: {word}", 404
    else:
        # Return an error message if no word is provided in the request
        return "No word provided in the request", 400

@app.route('/static/sigml/<path:path>')
def serve_signfiles(path):
    return send_from_directory('static/sigml', path)

if __name__== "_main_":
    app.run(debug=True)