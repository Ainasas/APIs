
from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [
    {
        'id': 1, 'nome': 'Felipe', 'sobrenome': 'Penner'
    },
    {
        'id': 2, 'nome': 'João', 'sobrenome': 'Pedro'
    },
    {
        'id': 3, 'nome': 'Otavio', 'sobrenome': 'Santos'
    },
    
]


# Consultar(todos)
@app.route('/clientes',methods=['GET'])
def obter_clientes():
    return jsonify(clientes)

# Consultar(id)
@app.route('/clientes/<int:id>', methods=['GET'])
def obter_clientes_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)
# Editar
@app.route('/clientes/<int:id>',methods=['PUT'])
def editar_clientes_id(id):
    cliente_alterado = request.get_json()
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])
#Criar
@app.route('/clientes', methods = ['POST'])
def adicionar_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    
    return jsonify(clientes)

# Excluir
@app.route('/clientes/<int:id>', methods = ['DELETE'])
def excluir_cliente(id):
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]
            
    return jsonify(clientes)

app.run(port=5000,host='localhost',debug=True)