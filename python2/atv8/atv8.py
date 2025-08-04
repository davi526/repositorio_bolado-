from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return "API DE HORA ONLINE RODADNO! USE /hora PARA VER A HORA ATUAL." \

@app.route("/hora")
def hora_atual():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    return jsonify({"hora": hora_formatada})

if __name__ == '__main__':
    app.run(debug=True)




    #datatime ate que e bacana seria util pra saber a hora em que o ususrio efetuou a resrva ne?
    