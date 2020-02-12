import os
import yaml


class GetData:
    def get_yml_data(self, yaml_name):
        with open("./Data" + os.sep + yaml_name, "r") as f:
            return yaml.safe_load(f)
