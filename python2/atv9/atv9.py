from flask import Flask, request, jsonify, send_file
from io import BytesIO

app = Flask(__name__)

# Dicionário para armazenar arquivos na memória
arquivo_memoria = {}

@app.route("/")
def home():
    return "Envie um arquivo com POST /upload para armazenar em memória e GET /download/<nome> para baixar."

@app.route("/upload", methods=["POST"])
def upload_arquivo():
    if 'arquivo' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    arquivo = request.files['arquivo']
    if arquivo.filename == '':
        return jsonify({"error": "Nome do arquivo vazio"}), 400
    
    conteudo = arquivo.read()
    arquivo_memoria[arquivo.filename] = conteudo

    return jsonify({"message": f"Arquivo '{arquivo.filename}' armazenado com sucesso"}), 201

@app.route("/download/<nome_arquivo>", methods=["GET"])
def download_arquivo(nome_arquivo):
    conteudo = arquivo_memoria.get(nome_arquivo)
    if not conteudo:
        return jsonify({"error": "Arquivo não encontrado"}), 404
    
    return send_file(
        BytesIO(conteudo),
        download_name=nome_arquivo,  # <- aqui é o novo nome do parâmetro
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
