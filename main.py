from flask import *
import ml
import os
from dotenv import load_dotenv

load_dotenv()


first_name = os.getenv("first_name")
full_name = os.getenv("full_name")
email = os.getenv("email")
phone = os.getenv("phone")

model = ml.AI()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("main.html", first_name = first_name, full_name = full_name, email=email, phone=phone)

@app.route("/ai", methods=["GET", "POST"])
def ai():
    response=''
    if request.method == "POST":
        user_input = request.form["user_input"]
        print(user_input)
        response = model.chatbot_response(user_input)
    return render_template("ai.html", response=response)

@app.route("/ai/devs", methods=["GET"])
def let_user_use_ai():
    return model.chatbot_response(request.args.get('sentence'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from env or default to 5000
    app.run(host="0.0.0.0", port=port)
