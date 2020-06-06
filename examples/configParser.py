import configparser

config = configparser.ConfigParser()
config.read('cfg.cfg')

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']
print(host, user, passwd, db)
