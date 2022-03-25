from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    name = "Lisa"
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    response = '''
    <html>
    <body>
        <h1>Hello, ''' + name + '''!</h1>
        <a href=“www.google.com”>not google</a>
        <ul>
        '''
    for i in city_names:
        response += f"<li> {i}"
    response += '''
        <ul>
    </body>
    </html>'''
    return response


app.run()
