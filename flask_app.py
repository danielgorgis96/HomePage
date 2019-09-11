from flask import Flask, render_template, request, send_file,redirect
app = Flask(__name__)


google_url_1 = 'https://www.google.com/search?sxsrf=ACYBGNRhJBkvdLe8ArRJVFzBX6SpJc4nlg%3A1568217277045&ei=vRh5Xae6AsvHwQLo2Kf4Dg&q='
google_url_2 = '&oq=dsd+sd+sd&gs_l=psy-ab.3..33i160.6831.7689..8280...0.0..0.96.577.9......0....1..gws-wiz.......35i39j35i39i19j0j0i131j0i10j0i203j0i22i30j0i13i30j0i13i10i30.BlDtZYHOQ44&ved=0ahUKEwjnjOrNkMnkAhXLY1AKHWjsCe8Q4dUDCAs&uact=5'

@app.route('/', methods=['GET','POST'])
def Menu_func():

    if request.method == 'POST':

        Input_str = str(request.form['GoogleSearch'])
        Input_str.replace(' ','+')
        
        return redirect(google_url_1+Input_str+google_url_2,code=302)

    return render_template('Frontpage.html')


if __name__ == "__main__":
    app.run(debug=True)