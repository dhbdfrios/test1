import yaml, os

def read_yaml_data(file_name):
    with open("./data" + os.sep + file_name, "r",encoding="utf-8") as f:
        return yaml.load(f)

data_list = []
data = read_yaml_data("login.yaml")
# print(data)
for i in data.keys():
    # print(i)
    data2 = data.get(i)
    name = data2.get("name")
    passwd = data2.get("passwd")
    tag = data2.get("tag")
    toast_msg = data2.get("get_toast_msg")
    expect_msg = data2.get("expect_msg")
    data_list.append((name,passwd,tag,toast_msg,expect_msg))

print(data_list)


