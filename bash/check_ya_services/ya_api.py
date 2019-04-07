import argparse
import requests
import sys




def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--services", nargs='+')
    parser.add_argument("-v", "--addresses", nargs='+')
    parser.add_argument("-f", "--report_file")
    args = parser.parse_args()
    return (args.services, args.addresses,args.report_file)
    
    
    
if __name__ == "__main__":
    ya_services,ya_addresses,path = getargs()
    services = {}
    
    if len(ya_services) != len(ya_addresses):
        raise Exception("Check arguments")
        
    for i in range(len(ya_services)):
        services[ya_services[i]] = "https://" + ya_addresses[i]
        
    for k,v in services.items():
        with open(path,'a+') as f:
            try:
                r = requests.get(v)
                if r.status_code < 500:
                    f.write("{}|{}|SUCCESS\n".format(k,v))
                else:
                    f.write("{}|{}|FAILED\n".format(k,v))
            except Exception as err:
                r.raise_for_status()
                f.write("{}|{}|ERROR\n".format(k,v))
                sys.exit(1)

    sys.exit(0)