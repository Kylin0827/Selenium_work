import yaml
yaml.warnings({'YAMLLoadWarning': False})
def load_eles(page):
    with open('page_eles_cfg.yaml', 'r') as f:
        datas = yaml.load(f.read())
    return datas[page]

if __name__ == '__main__':
    # unittest.main()
    print(load_eles('LoginPage'))
