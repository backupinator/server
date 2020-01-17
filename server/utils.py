'''Utilities for server.'''

import pathlib
import json

import peewee # pylint: disable=E0401

from models import ServerBaseModel
from models import ServerClient as Client
from models import ServerTarget as Target
from models import ServerFile as File
from models import ServerBackup as Backup

def db_init():
    '''Set up the database.'''

    MODELS = (Client, Target, File, Backup)
    db_name = ServerBaseModel._meta.database.database
    db = peewee.SqliteDatabase(db_name)
    db.bind(MODELS)
    db.create_tables(MODELS)

    return db

def dir_init():
    '''Make sure directories exist.

    We need the following directories:

    - manifests : list of files on each target
    - locker : holds all files
    - machines : holds all the tokens and info about known machines.
    '''

    paths = ['manifests', 'locker', 'machines']
    for p in paths:
        path0 = pathlib.Path(p)
        if not path0.exists():
            path0.mkdir(parents=True, exist_ok=True)

def add_machine(name, token, roles):
    '''Add a known machine to the server's list.'''

    data = {
        'name': name,
        'token': token,
        'roles': roles,
    }

    path0 = (pathlib.Path('machines') / name).with_suffix('.json')
    with open(path0, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def remove_machine(name):
    '''Remove known machine from server's list.'''
    path0 = (pathlib.Path('machines') / name).with_suffix('.json')

    try:
        path0.unlink()
    except FileNotFoundError:
        pass

def authenticate(name, token, role='any'):
    '''Make sure the machine connecting is a known machine.'''

    # If it's not a known machine, deny
    path0 = (pathlib.Path('machines') / name).with_suffix('.json')
    if not path0.exists():
        return False

    # Load everything we know about the machine...
    with open(path0, 'r') as f:
        data = json.load(f)

    # Only allow if an allowed role is being asked for
    if not (role == 'any' or role in data['roles']):
        return False

    # If it's known and has the correct token, allow
    if token == data['token']:
        return True
    return False

if __name__ == '__main__':
    pass
