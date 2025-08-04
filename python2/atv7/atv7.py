from flask import Flask, request, jsonify
app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return "API de usuários rodando! Use POST /add_usuarios pra adicionar e GET /users pra listar ou filtrar."



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

@app.route("/users")
def listar_usuarios():
    nome_filtro = request.args.get("nome")
    
    if nome_filtro:
        filtrados = [u for u in usuarios if nome_filtro.lower() in u.get("nome", "").lower()]
    else:
        filtrados = usuarios

    return jsonify({
        "total_users": len(filtrados),
        "usuarios": filtrados
    })

if __name__ == '__main__':
    app.run(debug=True)
