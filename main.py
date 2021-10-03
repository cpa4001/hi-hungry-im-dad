from flask import Flask, render_template, request
import random
import csv


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['jk_request'] == 'GIVE ME A DAD JOKE!!':
            dadjoke = ""
            # request dad joke from python script
            # get the string put it in render_template
            filename = "generated_jokes.csv"

            with open(filename) as f:
                reader = csv.reader(f)
                chosen_row = str(random.choice(list(reader))).replace('[', '').replace(']','')
                return render_template('home.html', dadjoke=chosen_row)

            return render_template('home.html', dadjoke=dadjoke)
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
