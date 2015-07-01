from flask import Flask, render_template
from tasks import add, greeting

app = Flask(__name__)

@app.route('/')
def test_app():
	return "Things are working"

@app.route('/celery')
def celery_task():
    add.delay(1,2)
    return "Task complete"

@app.route('/words')
def word_greeter():
    greeting.delay("some background tasks")
    return greeting("some background tasks")

if __name__ == '__main__':
	app.run(debug=True)
