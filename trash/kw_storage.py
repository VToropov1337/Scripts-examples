import json
import os
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="increase output key")
parser.add_argument("--val", help="increase output value")
args = parser.parse_args()



def gg():
    with open(storage_path, 'a+') as f:
        f.seek(0)
        tmp_file = f.read()
        f.seek(0)

        if len(tmp_file) == 0:
            string_to_json = json.dumps({args.key : [args.val]})
            hh_storage = json.loads(string_to_json)
            f.write(json.dumps(hh_storage))
        else:
            f.seek(0)
            tmp2_file = f.read()
            f.seek(0)
            hh = json.loads(tmp2_file)

            if args.key in hh.keys():
                hh[args.key].append(args.val)
                with open(storage_path, 'w') as f:
                    f.write(json.dumps(hh))

            else:
                with open(storage_path, 'w') as f:
                    hh.setdefault(args.key, [args.val])
                    f.write(json.dumps(hh))


if args.val == None:
    if os.path.isfile('/tmp/storage.data') == True:
        with open(storage_path, 'a+') as f:
            f.seek(0)
            tmp3_file = f.read()
            f.seek(0)
            hh = json.loads(tmp3_file)
            if args.key in hh:
                print(', '.join([str(i) for i in hh[args.key]]))
            else:
                print("None")
    else:
        if os.path.isfile('/tmp/storage.data') != True:
            print("None")
        else:
            with open(storage_path, 'a+') as f:
                f.seek(0)
                tmp3_file = f.read()
                f.seek(0)
                hh = json.loads(tmp3_file)
                if args.key in hh:
                    print(', '.join([str(i) for i in hh[args.key]]))
                else:
                    print("None")
else:
    gg()
