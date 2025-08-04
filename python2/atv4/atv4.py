from flask import Flask, request

app = Flask(__name__)

def log_request():
    print(f"[LOG] método: {request.method} | rota: {request.path}, IP: {request.remote_addr}")

@app.route("/")
def home():
    log_request()
    return "tchau pipoka!"

if __name__ == "__main__":
    app.run(debug=True)    