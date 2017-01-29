import os
from jinja2 import Template

with open('./objects.cfg.j2') as f:
    template = Template(f.read())

def get_host_config_dict():
    result = []
    for i in xrange(0, 1000):
        key = 'SERVER_%s' % i
        if key not in os.environ:
            break
        host = {}
        configs = os.environ[key]
        configs_split = configs.split(';')
        for config in configs_split:
            (key, value) = config.split('=')
            host[key] = value
        result.append(host)
    return result


hosts = get_host_config_dict()
objectcfg = template.render(hosts=hosts)

print objectcfg



