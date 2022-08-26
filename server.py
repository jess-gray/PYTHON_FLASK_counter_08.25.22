from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "cookies"

@app.route('/')
def main():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1 
    return render_template('index.html')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)