from flask import Flask, render_template, request

app = Flask(__name__)


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['jk_request'] == 'GIVE ME A DAD JOKE!!':
            # request dad joke from python script
            # get the string put it in render_template
            dadjoke = "Hi Hungry"
            return render_template('home.html', dadjoke=dadjoke)
    ##      elif  request.form.get('action2') == 'VALUE2':
    ##         pass # do something else
    ##      else:
    ##         pass # unknown
    ##   elif request.method == 'GET':
    ##      return render_template('home.html', form=form)
    return render_template('home.html')

@app.route('/christian')
def christian():
    return 'This is Christian\'s  route'

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/button')
def button():
    return render_template("button.html")


if __name__ == '__main__':
    app.run(debug=True)
