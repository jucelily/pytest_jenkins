import yaml
data={'Search_Data': {'search_test_002': {'except': {'value': '你好'},  'value': '你好'},
                      'search_test_001': {'except': [4, 5, 6], 'value': 456}}}
with open("./data4.yaml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)