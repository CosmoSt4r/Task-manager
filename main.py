from app import app
from database import db, Task
from flask import render_template, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # POST

        task_text = request.form['task_text']
        new_task = Task(task_text)

        db.session.add(new_task)
        db.session.commit()
        return redirect('/')

    else:
        # GET

        tasks = Task.query.order_by(Task.created).all()
        return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
