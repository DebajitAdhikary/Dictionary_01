import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def load_dictionary():

    dictionary = {}
    with open('dictionary.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            dictionary[row[0]] = row[1]
    return dictionary

def search_word(word):
  
    dictionary = load_dictionary()
    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found in dictionary."

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    
    word = request.form['word']
    definition = search_word(word)
    return render_template('search.html', word=word, definition=definition)

    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
