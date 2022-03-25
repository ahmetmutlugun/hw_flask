from flask import Flask

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']


@myobj.route("/")
def home():
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
