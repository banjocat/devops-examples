import os
import re

from jinja2 import Template

with open('./objects.cfg.j2') as f:
    template = Template(f.read())



def parse_envs():
    nagios_defines = {
            'host': [],
            'hostgroup': [],
            'service': [],
            'contact': [],
            'service': [],
            'contactgroup': [],
            'command': [],
            }
    for define in nagios_defines:
        regexp = re.compile('%s_\d+' % define)
        for env in os.environ:
            if regexp.match(env):
                config = get_host_config_dict(os.environ[env])
                nagios_defines[define].append(config)
    return nagios_defines


def get_host_config_dict(configs):
    host = {}
    configs_split = configs.split(';')
    for config in configs_split:
        (key, value) = config.split('=')
        host[key] = value
    return host


nagios_defines = parse_envs()
objectcfg = template.render(nagios_defines=nagios_defines)

print objectcfg



