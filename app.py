from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def get_data():
    with open('dictionary.csv') as f:
        reader = csv.reader(f)
        data = {rows[0]:rows[1:] for rows in reader}
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = get_data()
    search_word = request.form['search_word']
    if search_word in data:
        result = [search_word] + data[search_word]
    else:
        result = []
    return render_template('search.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
