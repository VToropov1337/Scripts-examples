import requests
import argparse



def get_args():
    parser = argparse.ArgumentParser(description='some sites')
    parser.add_argument('-f', type=str, help='site')
    args = parser.parse_args()
    return args.f


if __name__ == "__main__":
    get_args()
    arr1 = get_args()
    print('response is')
    print(requests.get(arr1).status_code)