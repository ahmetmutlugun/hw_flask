from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    name = "Lisa"
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    return '''
    <html>
    <body>
        <h1>Hello, ''' + name + '''!</h1>
        <a href=“www.google.com”>not google</a>
        <ul>
            <li> ''' + city_names[0] + '''
            <li> ''' + city_names[1] + '''
            <li> ''' + city_names[2] + '''
            <li> ''' + city_names[3] + '''
        <ul>
    </body>
    </html>'''


app.run()
