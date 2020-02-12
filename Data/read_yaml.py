import yaml
with open("./aa.yaml","r",encoding="utf-8") as f:
    value=yaml.safe_load(f)
    print("value={}".format(value))
    print("类型={}".format(type(value)))