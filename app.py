from flask import Flask,render_template,url_for
app = Flask(__name__,template_folder='template')
posts=[
    {"Name":"Reshail khan",
    "Date":"04/15/2019",
    "Number":"Blog No.1",
    "Context":"This is our first data / context in a html file."
    },
    {"Name":"Shumail khan",
    "Date":"05/15/2019",
    "Number":"Blog No.2",
    "Context":"This is our second data / context in a html file."
    },
    {"Name":"Azam khan",
    "Date":"06/15/2019",
    "Number":"Blog No.3",
    "Context":"This is our third data / context in a html file."
    }

]
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About Page')

