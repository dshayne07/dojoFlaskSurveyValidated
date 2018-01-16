from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key="oiwajefoaiwnegwboughuao"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    error = False
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") # just pass a string to the flash function
        error = True
    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        error = True
    elif len(request.form['comment']) > 120:
        flash("Comment is too long!")
        error = True
    if not error:
        flash(request.form)
        return redirect("/display_results")

    return redirect('/') # either way the application should return to the index and display the message

@app.route("/display_results")
def display():
    return render_template("results.html")

app.run(debug=True)