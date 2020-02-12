import pytest
from Base.getData import GetData


def get_yaml():
    data_l = []
    # with open("G:\\Users\Lenovo\PycharmProjects\sh_app13_day10_1\Data\sum.yml","r") as f:
    # with open(r"./Data/sum.yml", "r") as f:
    # with open(r"./Data"+os.sep+"sum.yml", "r") as f:
    data=GetData().get_yml_data("sum.yml")
    # data=yaml.safe_load(f)
    # print("data={}".format(data))
    for i in data.values():
        data_l.append(tuple(i.values()))
    print(data_l)
    return data_l


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_yaml())
    def test_s(self, a, b, c):
        """计算两个数之和等于第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
