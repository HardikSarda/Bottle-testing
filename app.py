from bottle import Bottle, run, template, request, static_file
import subprocess
import os

app = Bottle()


@app.route('/')
def home():
    return template('base')


@app.route('/submit', method='POST')
def submit():
    chromedriver_path = request.forms.get('chromedriver_path')
    base_url = request.forms.get('base_url')
    email = request.forms.get('email')
    password = request.forms.get('password')
    search_url = request.forms.get('search_url')

    # Update constants.py
    constants_content = f'''
CHROMEDRIVER_PATH = "{chromedriver_path}"
BASE_URL = "{base_url}"
EMAIL = "{email}"
PASSWORD = "{password}"
SEARCH_URL = "{search_url}"
    '''
    with open('constants.py', 'w') as f:
        f.write(constants_content)

    # Run main.py
        try:
            subprocess.run(["python", "main.py"], check=True)
            return static_file('company_data.csv', root='.', download='company_data.csv')
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e}"


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
