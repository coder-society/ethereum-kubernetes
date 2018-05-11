#!/usr/bin/env python3
import subprocess
import json
from base64 import b64encode


def _write_secret(name, fname):
    with open(fname, 'rt') as f:
        secret_data = f.read()

    secret_data_b64 = b64encode(secret_data.encode()).decode()
    secret_yaml = '\n  {}: {}'.format(fname, secret_data_b64)

    with open('kubernetes/{}-secret.yaml'.format(name), 'w') as f:
        f.write("""\
apiVersion: v1
kind: Secret
metadata:
  name: {}
type: Opaque
data: {}
""".format(name, secret_yaml))


def _main():
    with open('secrets.json', 'rt') as f:
        secrets = json.load(f)

    for i in range(1, 3):
        command_str_tpl = r'source authority/.env.authority{0} && ' \
            'envsubst \$AUTHORITY_NAME,\$NFS_SERVER,\$NFS_PATH,\$NETWORK_ID,' \
            '\$BOOT_NODE_ID,\$AUTHORITY_ADDRESS < ' \
            'authority/authority.template.yaml > kubernetes/authority{0}.yaml'
        command_str = command_str_tpl.format(i)
        subprocess.check_call(command_str, shell=True)

    _write_secret('authority1-password', 'authority1-password.txt')
    _write_secret('authority2-password', 'authority2-password.txt')
    _write_secret('genesis', 'genesis.json')
    _write_secret('boot', 'boot.key')


_main()
