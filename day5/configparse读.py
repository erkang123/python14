import configparser

conf = configparser.ConfigParser()

conf.read('example.ini')

print(conf.sections())
print(conf.defaults())
print(conf['bitbucket.org']['user'])
for k in conf['DEFAULT']:
    print(k)

conf.remove_section('bitbucket.org')
conf.write(open('i.cfg','w'))