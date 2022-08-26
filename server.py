from flask import Flask, render_template, redirect, session 
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "cookies"

@app.route('/')
def main():
    if 'count' not in session:  #if it is not getting data from count it displays 0
        session['count'] = 0
    else:
        session['count'] += 1  #if count is selected it adds one
    return render_template('index.html')


@app.route('/destroy_session')
def destroy():
    session.clear()  #this is clearing the session data
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)