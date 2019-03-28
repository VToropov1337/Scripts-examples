import os
import re

path = 'path/to/file/with/extension/example.json'

file = os.path.basename(path).replace('.json','')
file2 = re.search('[ \w-]+?(?=\.)',path)

print(file,file2.group(0))
