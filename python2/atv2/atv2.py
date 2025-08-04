from flask import Flask, request

app = Flask(__name__)

@app.route("/soma")
def soma():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is None or b is None:
        return "parametros 'a' e 'b' são obrigatorios", 400

    resultado =a + b 
    return str(resultado)

if __name__ == "__main__":
    app.run(debug=True)