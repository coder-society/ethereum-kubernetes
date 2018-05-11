#!/usr/bin/env python3
import os.path
import shutil


_DATA_DIR = '/var/data/ethereum'
_KEYSTORE_DIR = '/var/data/keystore'

if not os.path.isdir(_DATA_DIR):
    raise Exception('{} must exist'.format(_DATA_DIR))
if not os.path.isdir(_KEYSTORE_DIR):
    raise Exception('{} must exist'.format(_KEYSTORE_DIR))

if not os.path.exists(os.path.join(_DATA_DIR, 'keystore')):
    print('Initializing keystore dir')
    shutil.copytree(_KEYSTORE_DIR, os.path.join(_DATA_DIR, 'keystore'))
else:
    print('Keystore dir already exists, no need to initialize it')
