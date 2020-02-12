import pytest, yaml


def get_yaml():
    data_l = []
    with open("G:\\Users\Lenovo\PycharmProjects\sh_app13_day10_1\Data\sum.yml", "r") as f:
        data = yaml.safe_load(f)
        # print("data={}".format(data))
        for i in data.values():
            data_l.append(tuple(i.values()))
    print(data_l)
    return data_l
print(get_yaml())


