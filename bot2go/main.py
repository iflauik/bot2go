import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Bot2go</h1><p>Welcome." \
           "<br>Haha, I'm a robot, and I don't need to eat." \
           "<br>I am interested only in electricity." \
           "<br>Nevertheless, I might help you to book your favorite place.</p>"


app.run()
