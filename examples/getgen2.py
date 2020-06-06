from readConfig import Config

filepath = 'enodeb_config.xml'
cfg_id = '77B0355D-EFAD-4124-8C91-C8324D77090C'
config = Config(filepath)
config.create_dict_xml()
print"hjhcbjhcc", config.get_config_dict(cfg_id)
