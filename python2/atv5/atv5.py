from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [f"usuario{i}" for i in range(1, 100)]

@app.route("/")
def home():
    return "Bem-vindo, Davi! Vai em /users?page=1 pra ver a lista paginada."

@app.route("/users")
def listar_usuarios():
    page = int(request.args.get("page", 1))
    per_page = 10

    start = (page - 1) * per_page
    end = start + per_page
    paginados = usuarios[start:end]

    if not paginados:
        return jsonify({"error": "Página vazia, não há usuários aqui!"}), 404

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total_users": len(usuarios),
        "users": paginados
    })

if __name__ == "__main__":
    app.run(debug=True)
