from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def Menu_func():
    return render_template('Frontpage.html')


if __name__ == "__main__":
    app.run(debug=True)