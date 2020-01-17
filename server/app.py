'''Web server application.'''

import json

from flask import Flask, request

from utils import authenticate, dir_init, db_init

app = Flask(__name__)

# Make sure we have a database ready to rock n roll
db = db_init()

# Add directories required on the server
dir_init()

@app.route('/')
def check():
    '''Send a response to let machines know server is up.'''

    return {
        'message': 'Server is up and running!',
        'status': 'OK',
    }

@app.route('/upload_manifest', methods=['POST'])
def upload_manifest():
    '''Target uploads a list of all client files.

    Parameters
    ----------
    name : str
        Name of the machine.
    token : str
        Authentication token.
    data : json string
        JSON string containing the list of files for each client
        machine on the target.
    '''

    # Make sure we trust this machine as a target
    name = request.form['name']
    token = request.form['token']
    if not authenticate(name, token, role='target'):
        return False

    # Get the manifests for each client
    manifests = json.loads(request.form['data'])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
