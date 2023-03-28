from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home():
    title = "Home"
    css_route = "css/home.css"
    return render_template("home.html", title=title, css_route=css_route)


if __name__ == '__main__':
    app.run(debug=True)