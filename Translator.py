from flask import Flask, render_template, request

app = Flask(__name__)
my_words = {"hello": "Привет", "dog": "Собака", "cat": "Кошка", "apple": "Яблоко", "potato": "Картофель"}

@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"].lower()
        return render_template('result.html', word=my_words[word])

    return render_template('dict.html')

@app.route('/<word>')
def index(word):
    return render_template('dict.html', word=word)

if __name__ == '__main__':
    app.run()


