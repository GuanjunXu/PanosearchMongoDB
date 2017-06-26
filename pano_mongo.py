import json
import pymongo
import os
import time

host = '10.185.29.20'
port = 27017
app_ver = "3.0.1"

client = pymongo.MongoClient(host, port)
db = client.preline_debug
collection = db.app

find_par = {"app_id":"PanoSearch","imei":"862131030039861"}
find_key = find_par.keys()
find_list = collection.find(find_par)

print len([i for i in find_list])
find_list = collection.find(find_par)
print len([i for i in find_list])

key_str = '_'.join(find_key)
path = key_str + '_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
os.mkdir(path)
dir_now = os.getcwd()
os.chdir(dir_now + '\\' + path)

for data in find_list:
    data['_id'] = str(data['_id'])
    f_name = '%s_%s.txt'%(key_str, str(data['_id']))
    print "Generate %s "%f_name,
    f = open(f_name, 'w')
    json_data = json.dumps(data,indent = 4)
    print "Writing... ",
    f.write(json_data)
    f.close()
    print "Done."