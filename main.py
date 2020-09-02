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


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Task.query.get_or_404(task_id)

    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        # POST

        task.task_text = request.form['task_text']
        db.session.commit()

        return redirect('/')

    else:
        # GET

        return render_template('update.html', task=task)


if __name__ == '__main__':
    db.create_all()
    app.run()
