import os
import json
import tempfile
import argparse






parser = argparse.ArgumentParser(description='Simple k-w storage')
parser.add_argument('--key', type=str, help='input a key')
parser.add_argument('--value', type=str, help='input a value')
args = parser.parse_args()
print(args.key,args.value)



storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open (storage_path,'a') as f:
    kw = json.dumps({args.key:args.value})
    f.write(kw)
    
    
    
with open(storage_path,'r') as f2:
    print(f2.read())
    
    




