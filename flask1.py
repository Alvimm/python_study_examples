from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/')
@app.route('/user/<name>')
def hello_world(name='User'):
    return render_template('user.html', received_name=name)


@app.route('/sum/')
@app.route('/sum/<num01>/<num02>')
def sum_num(num01=0, num02=0):
    result = float(num01) + float(num02)
    return str(result)


'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Received post! Login!'
    else:
        return 'Received get! Display login FORM.'
'''
if __name__ == '__main__':
    app.run(debug=True)
