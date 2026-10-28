from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# Task 2: HTML generated directly, no template
@app.route('/')
def index():
    return """
    <p>Maria G.: IDK (I Don't Know)</p>
    <p>James T.: TBH (To Be Honest)</p>
    <p>Sam L.: FYI (For Your Information)</p>
    """
# Task 3: template route
@app.route('/eunur')
def eunur():
    acronym = "TL;DR (Too Long; Did not Read)"
    return render_template('template.html', acronym=acronym)
# Task 4: Bootstrap image page
@app.route('/image')
def image():
    return render_template('image.html')
