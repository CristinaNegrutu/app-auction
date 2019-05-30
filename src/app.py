from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)  # '__main__'
app.secret_key = "cristina"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/developers')
def developers():
    return render_template('developers.html')


@app.route('/clients')
def clients():
    return render_template('clients.html')


@app.route('/developer/project/view')
def developer_project_view():
    return render_template('developer_project_view.html')

@app.route('/client/project/view')
def client_project_view():
    return render_template('client_project_view.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=4988, debug=True)
