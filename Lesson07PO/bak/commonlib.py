import yaml
yaml.warnings({'YAMLLoadWarning': False})
def load_eles(page):
    with open('eles_cfg.yaml', 'r') as f:
        datas = yaml.load(f.read())
    return datas[page]


