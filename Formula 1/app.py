import profile


app= Flask(__name__, template_folder='template')
db=SQL('sqlite:///TSPF.db')


@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template(