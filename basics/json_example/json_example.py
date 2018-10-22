# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
import json
import os
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
data = {
    "Employee": {
        "first": "Mario",
        "last": "Geneau"
    }
}
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
def saveJsonFile(json_file_name_without_ext, dict_to_save):
    with open(f"{os.getcwd()}/json_example/{json_file_name_without_ext}.json", "w") as write_file:
        json.dump(dict_to_save, write_file)
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
def loadjsonFile(json_file_name_without_ext):
    with open(f"{os.getcwd()}/json_example/{json_file_name_without_ext}.json", "r") as read_file:
        return json.load(read_file)
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# saveJsonFile("employees", data)
emp = loadjsonFile("employees")
emp["Employee"]["age"] = "47"
saveJsonFile("employees", emp)
# print(emp["Employee"])