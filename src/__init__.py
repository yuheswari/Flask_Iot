import json

def get_config(key):
    config_file="/home/yuheswari2525/IOT/config.json"
    file=open(config_file,"r")
    config =json.loads(file.read())
    file.close()

    if key in config:
        return config[key]
    else:
        raise Exception("key {} is not found in config.json".format(key)) # type: ignore
    