from flask import Flask, jsonify, abort
from database import consultar

app = Flask(__name__)

sql = '''SELECT * FROM CURSO'''

#Obtem todos os usuários
@app.route('/usuarios',methods=['GET'])
def obter_usuarios():
    try:
        return jsonify(consultar(sql=sql))
    except(Exception) as error:
        return abort(500)

#rodar servidor
app.run(port=5000,host='localhost',debug=True)