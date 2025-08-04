from flask import Flask, request, jsonify
app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return "API de usuários rodando! Use POST /add_usuarios pra adicionar e GET /usuarios pra listar."


@app.route('/add_usuarios', methods=['POST'])
def add_usuarios():

    novo_usuario = request.get_json()
     
    if not novo_usuario:
        return jsonify({"error": "Nenhum usuário encontrado"}), 400
    
    usuarios.append(novo_usuario)

    return jsonify({
        "message": "Usuário adicionado com sucesso",
        "usuarios": usuarios,
        "total_usuarios": len(usuarios)
    }), 201

@app.route("/usuarios")
def listar_usuarios():
    return jsonify({
        "total_usuarios": len(usuarios),
        "usuarios": usuarios
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
