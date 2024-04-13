# ValueError: Circular reference detected in Python

import json

a_dict = {}

a_dict['site'] = 'bobbyhadz.com'

a_dict['nested'] = a_dict.copy()


json_string = json.dumps(a_dict)

# 👇️ {"site": "bobbyhadz.com", "nested": {"site": "bobbyhadz.com"}}
print(json_string)