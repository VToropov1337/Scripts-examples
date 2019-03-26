import json_delta
import json

with open('test1.json','r') as f:
    v1 = json.loads(f.read())
    
    
with open('test2.json','r') as f2:
    v2 = json.loads(f2.read())

diff = json_delta.diff(v1, v2, verbose=False)

for i in diff:
    print(i)
