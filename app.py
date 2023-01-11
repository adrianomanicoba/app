from flask import Flask

app = Flask(__name__)

# criar a 1ª página do site

# route

# função
@app.route("/")
def homepage():
    return "<p>Esse é meu 1º </p>site ****Adriano**** teste"
# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do render
