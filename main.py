import mysql.connector
from flask import Flask, make_response, jsonify, request, render_template

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='10203040',
    database='aula_13_10'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


cursor = mydb.cursor(dictionary=True)


@app.route("/funcionarios", methods=['GET'])
def get_funcionarios():
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    return render_template("funcionarios.html", funcionarios=funcionarios)

@app.route('/funcionarios', methods=['POST'])
def create_funcionario():
    primeiro_nome = request.form.get('primeiro_nome')
    sobrenome = request.form.get('sobrenome')
    data_admissao = request.form.get('data_admissao')
    status_funcionario = request.form.get('status_funcionario')
    id_setor = request.form.get('id_setor')
    id_cargo = request.form.get('id_cargo')

    my_cursor = mydb.cursor()
    sql = "INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo)

    my_cursor.execute(sql, values)
    mydb.commit()

    mensagem = 'Funcionário cadastrado com sucesso.'

    return render_template("index.html", mensagem=mensagem)


@app.route('/')
def index():
    mensagem = request.args.get('mensagem')
    return render_template("index.html", mensagem=mensagem)

@app.route('/setor', methods=['POST'])
def create_setor():
    nome_setor = request.form.get('nome_setor')

    my_cursor = mydb.cursor()
    sql = "INSERT INTO setor (nome) VALUES (%s)"
    values = (nome_setor,)

    my_cursor.execute(sql, values)
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Setor cadastrado com sucesso.',
            nome_setor=nome_setor
        )
    )
@app.route('/cargos', methods=['GET'])
def get_cargos():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM cargos")
    cargos = my_cursor.fetchall()
    return render_template("index.html", cargos=cargos)

@app.route('/cargos', methods=['POST'])
def create_cargo():
    nome_cargo = request.form.get('nome_cargo')
    id_setor = request.form.get('id_setor')

    my_cursor = mydb.cursor()
    sql = "INSERT INTO cargos (nome, id_setor) VALUES (%s, %s)"
    values = (nome_cargo, id_setor)

    my_cursor.execute(sql, values)
    mydb.commit()

    mensagem = 'Cargo cadastrado com sucesso.'

    return render_template("index.html", mensagem=mensagem)




app.run()

#não foi nem um pouco facil , porém foi top demais esse projeto!
