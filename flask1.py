from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/')
def mrb_page():
    return "This is mrb home page"
@ app.route('/host')
def host_page():
    return render_template("file:///C:/Users/ELCOT/PycharmProjects/webpage/homepg.html")

if __name__ == "__main__":
  app.run()