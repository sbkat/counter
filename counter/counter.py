from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret n safe"

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/count', methods=["POST"])
def count():
    if "add" in request.form:
        session["count"] -= 1
        session["adding_views"] += 2
    elif "reset" in request.form:
        session["count"] = 0
        session["adding_views"] = 0
    session.modified = True
    return redirect ('/')

@app.route('/custom_count', methods=["POST"])
def custom_count():
    num = request.form['num']
    session["count"] -= 1
    session['adding_views'] += int(num)
    return redirect ('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)