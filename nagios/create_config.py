'''
This script is what parses the environmental variables
It then outputs the nagios config file
'''
import os
import re

from jinja2 import Template

with open('./objects.cfg.j2') as f:
    template = Template(f.read())



def parse_envs():
    '''
    Goes through all the environmental variables
    Any matching a nagios define it adds
    for jinja2 to use
    '''
    nagios_defines = {}
    regexp = re.compile('([a-z]+)_\d+')
    for env in os.environ:
        match = regexp.match(env)
        if not match:
            continue
        define_name = match.groups(0)[0]
        # Create the key as an array if doesnt exist yet
        if define_name not in nagios_defines:
            nagios_defines[define_name] = []
        config = get_host_config_dict(os.environ[env])
        nagios_defines[define_name].append(config)
    return nagios_defines


def get_host_config_dict(configs):
    '''
    Takes one environmental variable
    and splits it into a map
    '''
    host = {}
    configs_split = configs.split(';')
    for config in configs_split:
        (key, value) = config.split('=')
        host[key] = value
    return host


nagios_defines = parse_envs()
objectcfg = template.render(nagios_defines=nagios_defines)

print objectcfg



