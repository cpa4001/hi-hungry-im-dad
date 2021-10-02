from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
      if request.form.get('action1') == 'GIVE ME A DAD JOKE!!':
         render_template('home.html')
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

#background process happening without any refreshing
def do_something():
    print ("Hello")
    return

if __name__ == '__main__':
   app.run(debug=True)
   
