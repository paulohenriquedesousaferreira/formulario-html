from flask import Flask, request
import pywhatkit as kit
from datetime import datetime, timedelta

app = Flask(__name__)

# Rota principal para o formulário
@app.route('/')
def home():
    return '''
    <form action="/enviar" method="POST">
        Nome: <input type="text" name="nome"><br>
        Telefone: <input type="text" name="telefone"><br>
        Data de Nascimento: <input type="date" name="dataNascimento"><br>
        Estado Civil: <input type="text" name="estadoCivil"><br>
        CPF: <input type="text" name="cpf"><br>
        FGTS: <input type="text" name="fgts"><br>
        Filhos: <input type="text" name="filhos"><br>
        <button type="submit">Enviar</button>
    </form>
    '''

# Rota para enviar as informações do formulário para o WhatsApp
@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    data_nascimento = request.form['dataNascimento']
    estado_civil = request.form['estadoCivil']
    cpf = request.form['cpf']
    fgts = request.form['fgts']
    filhos = request.form['filhos']

    # Formata a mensagem
    mensagem = f"Novo cadastro:\n\nNome: {nome}\nTelefone: {telefone}\nData de Nascimento: {data_nascimento}\nEstado Civil: {estado_civil}\nCPF: {cpf}\nFGTS: {fgts}\nFilhos: {filhos}"

    # Calcula o horário de envio (3 minutos depois do momento atual)
    agora = datetime.now()
    hora_envio = agora + timedelta(minutes=3)  # Ajuste para 3 minutos depois
    hora = hora_envio.hour
    minuto = hora_envio.minute

    # Envia a mensagem para o WhatsApp
    kit.sendwhatmsg("+5561981969785", mensagem, hora, minuto)  # Defina o número e o horário calculado

    return 'Formulário enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
