from flask import Flask, render_template

app = Flask(__name__, template_folder="MyTemplates")

posts = [
    {"name": "Sunny Kumar", "roll": "15079", "semester": 7},
    {"name": "Vaishali Kumar", "roll": "15078", "semester": 7},
    {"name": "Raj Bharti", "roll": "15080", "semester": 7}
]


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/account')
def account():
    return render_template("account.html", posts = posts, title="Student Account")

if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"), debug=True)
