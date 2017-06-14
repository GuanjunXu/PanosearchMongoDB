# -*- coding: utf-8 -*-

import xlrd
import case_script
import json
import pymongo
import os
import time
from uiautomator import device as d

app_id = "PanoSearch"
imei = '862131030039861'
start_id = ''

host = '10.185.29.20'
port = 27017

client = pymongo.MongoClient(host, port)
db = client.preline_debug

cwd = os.getcwd()
result_path = cwd + '\\TestResult\\' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
os.makedirs(result_path)

def main_test():
    file_name = "case_tmp.xlsx"
    bk = xlrd.open_workbook(file_name)
    case_sheet = bk.sheet_names()[0]
    sh = bk.sheet_by_name(case_sheet)
    nrows = sh.nrows
    ncols = sh.ncols
    col_names = sh.row_values(0)
    os.chdir(result_path)
    for i in range(1, nrows):
        col_values = sh.row_values(i)
        k_v = dict(zip(col_names, col_values))
        print k_v['CaseNo'] + ' ' + k_v['FuncName'] + ' ... Running ...',
        if k_v['DocFind'] in ['app', 'ready', 'exit']:
            collection = db.app
        else:
            collection = db.event
        os.popen("adb shell am force-stop com.letv.android.quicksearchbox")
        collection.remove({"app_id":app_id,"imei":imei})
        try:
            exec('case_script.' + k_v['FuncName'] + '()') # Run test case
            time.sleep(6)
        except:
            pass
        find_par = eval(k_v['FindPar'])
        find_result = collection.find(find_par)
        test_result = 'FAIL'
        f_name_o = k_v['CaseNo'] + '_' + k_v['FuncName'] + '.txt'
        f = open(f_name_o, 'w')
        for data in find_result:
            data['_id'] = str(data['_id'])
            json_data = json.dumps(data, indent = 4)
            f.write(json_data)
            for sub_dic in data['props']:
                if k_v['EventPropsK'] in sub_dic.values():
                    props_index = data['props'].index(sub_dic)
                    if data['props'][props_index]["value"] == k_v['EventPropsV']:
                        test_result = 'PASS'
                    break

        f.close()
        os.rename(f_name_o, f_name_o[0:-4] + '_' + test_result + '.txt')
        print test_result

        


main_test()
# case_script.launchSlideUp()