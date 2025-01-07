from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def score_server():
    with open('scores.txt', "r") as file:
        score = file.read()
        return render_template('index.html', score=score)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=5000, debug=True)