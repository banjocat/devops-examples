import os
import socket
import subprocess


from behave import *


@given('a host defined in env BEHAVE_HOST')
def step_impl(context):
    context.host = os.environ.get('BEHAVE_HOST', '127.0.0.1')


@given('I can ping the host')
def step_impl(context):
    host = context.host
    response = subprocess.call(['ping', '-c 1', host])
    assert response == 0


@when('I check port ([0-9]+)')
def step_impl(context, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((context.host, int(port)))
    context.port_check = result


@then('The port is closed')
def step_impl(context):
    assert context.port_check != 0

