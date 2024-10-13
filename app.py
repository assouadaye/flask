from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulation des utilisateurs
users = {
    "user1": "User 1",
    "user2": "User 2"
}

# Stockage des messages (une liste de tuples (utilisateur, message))
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupérer l'utilisateur et le message
        username = request.form.get("username")
        message = request.form.get("message")

        # Ajouter le message à la liste des messages
        if username and message:
            messages.append((users.get(username), message))

        return redirect(url_for("index"))

    return render_template("index.html", users=users, messages=messages)


if __name__ == "__main__":
    # Lancer le serveur Flask en écoutant sur toutes les interfaces réseau
    app.run(debug=True, host="0.0.0.0", port=5000)