from flask import Flask, render_template, request
from model import Model

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def inserir():
    nome=''
    telefone=''
    endereco=''
    data_nascimento=''
    resultado_comando =''
    model = Model()

    if request.method == 'POST':
        nome = request.form['inputNome']
        telefone = request.form['inputTelefone']
        endereco = request.form['inputEndereco']
        data_nascimento_inserida = request.form['inputDataNascimento']

        resultado_comando = model.inserir(nome, telefone, endereco, data_nascimento_inserida)

    return  render_template("index.html", tituloIndex="Inserir", resultado=resultado_comando)


if __name__ == "__main__":
    app.run(debug=True, port=5000)