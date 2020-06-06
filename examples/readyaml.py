import yaml
with open("doc.yaml","r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
for section in cfg:
    print(section)
print(cfg['other']['preprocessing_queue'])


