#!/usr/bin/env python3
import os.path
import subprocess
from base64 import b64encode


def _write_secret(name, fpath):
    with open(fpath, 'rt') as f:
        secret_data = f.read()

    secret_data_b64 = b64encode(secret_data.encode()).decode()
    secret_yaml = '\n  {}: {}'.format(
        os.path.basename(fpath), secret_data_b64
    )

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
    _write_secret(
        'authority1-keystore',
        'authority1/keystore/UTC--2018-05-07T22-54-50.644182705Z--'
        'e236d5c0d5ea75d866c56b9966a9b9f35bdb3ad0'
    )
    _write_secret(
        'authority2-keystore',
        'authority2/keystore/UTC--2018-05-07T22-58-06.079818290Z--'
        '8084b0f2cc92c2672db34b6df9656d2889dfa85e'
    )


_main()
