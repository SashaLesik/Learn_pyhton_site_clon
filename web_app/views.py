from web_app import app
@app.route('/')
def index():
    return 'hello, word'