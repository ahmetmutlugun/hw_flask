from flask import Flask

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']


@myobj.route("/")
def home():
    response = f'''
    <html>
    <body>
        <h1>Welcome''' + name + '''!</h1>
        <ahref="www.google.com">notgoogle</a>
        <ul>
        '''
    for i in city_names:
        response += f"<li>{i}</li>"
    response += '''
        <ul>
    </body>
    </html>'''
    return response

