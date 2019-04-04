from flask import Flask, render_template, redirect, url_for, request
import db_iface

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))


@app.route('/index.html')
def index():
    all_tasks = db_iface.retrieve()
    return render_template('index.html', tasks=all_tasks)


@app.route('/newtask', methods=['POST'])
def insert_new():
    nuovo = request.form['new_task']
    db_iface.insert(nuovo)
    return redirect(url_for('index'))


@app.route('/delete/<idt>')
def delete(idt):
    db_iface.remove(idt)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
