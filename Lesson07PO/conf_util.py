import yaml
yaml.warnings({'YAMLLoadWarning': False})
def get_locators(yamlfile):
    with open(yamlfile,'r') as f:
        txt=f.read()
        res=yaml.load(txt)
        return res

if __name__ == '__main__':
    res=get_locators('locators.yml')
    print(res)