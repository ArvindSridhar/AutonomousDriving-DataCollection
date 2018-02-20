from flask import *
app = Flask(__name__)
 
@app.route("/")
def index():
    #url_for('static', filename='app.css')
    return render_template('index.html')