from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/test')
def test():
    return u'hello world'


if __name__ == '__main__':
    app.run()
