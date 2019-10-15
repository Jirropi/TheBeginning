import json


sample_input = json.load(open("C:/Users/jirro/OneDrive/Desktop/Files/json_test.json"))
print(sample_input)
print(type(sample_input[0]))
print(sample_input[0]["device_type"])
for each in sample_input:
    print(each)