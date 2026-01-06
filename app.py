from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    owner_info = {
        "name": "Prinsh Patel",
        "whatsapp": "9726380301",
        "email": "prinshpatel113@gmail.com",
        "insta": "prinsh__patel__46",
        "fb_name": "Prinsh Patel"
    }
    return render_template('index.html', info=owner_info)

if __name__ == '__main__':
    app.run(debug=True)