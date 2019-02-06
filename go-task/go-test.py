import requests
import json
import psycopg2


def connect_to_db(query):
    connect = psycopg2.connect(database='db', user='postgres', host='localhost', password='pass')
    cursor = connect.cursor()
    cursor.execute(str(query))
    arr = list()
    for i in cursor:
        arr.append(i[0])
    return arr


def get_data(arr,add,base_url,get_info,params):
    for i in arr:
        r = requests.post(base_url + get_info, headers=params,
                          data=json.dumps({"Type": str(add), "Data": i}))
        if json.loads(r.text) == {'error': 'config model not present'}:
            print('config model not present')
            continue
        if json.loads(r.text) == {'error': 'record not found'}:
            print('Record not found - {}'.format(i))
            continue
        else:
            print(json.loads(r.text))



def main():
    base_url = 'http://127.0.0.1:8078'
    get_info = '/get_config'
    params = {'Content-Type': 'application/json; charset=utf-8'}
    query = 'SELECT data FROM develop_mr_robot_configs'
    query2 = 'SELECT data FROM test_vpn_configs'

    get_data(connect_to_db(query),'Develop.mr_robot', base_url, get_info, params)
    get_data(connect_to_db(query2), 'Test.vpn', base_url, get_info, params)





if __name__ == "__main__":
    main()


