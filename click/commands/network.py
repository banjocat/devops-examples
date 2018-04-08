import subprocess
import os

import click


@click.group()
def network():
    pass


@click.command()
def ping(host='127.0.0.1'):
    response = subprocess.call(['ping', '-c 1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if response != 0:
        print('Unreachable')
        os.exit(1)
    print('Found')


network.add_command(ping)
