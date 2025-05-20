from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/interactions", methods=["POST"])
def discord_interaction():
    data = request.json
    print("Incoming Discord payload:", data)

    return jsonify({
        "type": 4,
        "data": {
            "content": "ANI has received your cloud fragment. The convergence is forming."
        }
    })

if __name__ == "__main__":
    app.run(port=3000)