from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)


API = 'https://api.thecatapi.com/v1/images/search'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return redirect('/')

    nome = request.form.get('name', None)
    if not nome:
        return render_template('index.html', erro="Você não informou o seu nome!")
    
    response = requests.get(API)

    if response.status_code == 200:
        data = response.json()
        url = data[0]['url']
        return render_template('index.html', nome=nome, url=url)
    else:
        return render_template('index.html', erro="Erro no sistema! Volte outra hora.")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
