# -*- coding: utf-8 -*-

import xlrd
import case_script
import json
import pymongo
import os
import time
import shutil

app_id = "PanoSearch"
imei = '861579030145560'
start_id = ''

test_priority = ["P0", "P1", "P2"]
test_version = ["2.5.0", "3.0.0", "3.0.2"]

host = '10.185.29.20' #'10.149.14.93' # '10.185.29.20' # 
port = 27017

gaps = 2
single_case = None

case_not_run = 1 # Skip uiautomator scripts if not 1

client = pymongo.MongoClient(host, port)
db = client.preline_debug #phone # preline_debug

cwd = os.getcwd()
result_path = cwd + '\\TestResult\\' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
os.makedirs(result_path)

def mainTest():
    file_name = "case_tmp_ver302.xlsx"
    bk = xlrd.open_workbook(file_name)
    case_sheet = bk.sheet_names()[0]
    sh = bk.sheet_by_name(case_sheet)
    nrows = sh.nrows
    ncols = sh.ncols
    col_names = sh.row_values(0)
    os.chdir(result_path)
    start_line, end_line = 1, nrows
    start_time = time.time()
    print "-*-*-*- Start: %s -*-*-*-\nResult path as: %s"%(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(start_time)), result_path)
    if single_case != None:
        start_line, end_line = single_case - 1, single_case
    for i in range(start_line, end_line):
        col_values = sh.row_values(i)
        k_v = dict(zip(col_names, col_values))
        if k_v['Ver'] not in test_version or k_v['Priority'] not in test_priority:
            continue
        try:
            k_v['CaseNo'] = int(k_v['CaseNo'])
        except:
            pass
        time.sleep(20)
        print str(i+1) + '\t' + str(k_v['CaseNo']) + '\t' + k_v['FuncName'] + '\t... Running ...\t',
        if k_v['EventType'] in ['run', 'ready', 'exit']:
            collection = db.app
        else:
            collection = db.event
        test_result = 'NoData'
        t_r = 'NoData'
        if case_not_run == 1:
            case_script.exitPano()
            collection.remove({"app_id":app_id,"imei":imei}) # Clear history
            try:
                exec('case_script.' + k_v['FuncName'] + '()') # Run test case
                time.sleep(gaps)
            except:
                t_r = 'Err'
        find_par = eval(k_v['FindPar'])
        find_result = collection.find(find_par)
        broken_count = 0
        while len([item for item in find_result]) == 0:
            find_result = collection.find(find_par)
            time.sleep(gaps)
            broken_count += 1
            if broken_count > 10:
                t_r = 'FindDBFailed'
                break
        time.sleep(gaps)
        find_result = collection.find(find_par)
        f_name_o = str(k_v['CaseNo']) + '_' + k_v['FuncName'] + '.txt'
        f = open(f_name_o, 'w')
        fail_reason = ''
        find_result_list = []
        for data in find_result:
            data['_id'] = str(data['_id'])
            json_data = json.dumps(data, indent = 4)
            f.write(json_data)
            find_result_list.append(data)
        f.close()
        props = []
        for prop in k_v['EventProps'].split(','):
            if '=' in prop:
                prop = dict([prop.split('=')])
            props.append(prop)
        data_props_list = []
        for f_data in find_result_list:
            for sub_dic in f_data['props']:
                data_props_list.append(sub_dic)
        err_list = []
        for p in props:
            ppc = 0
            test_result = 'PASS'
            for pp in data_props_list:
                if type(p) != dict and p in pp.values():
                    p_index = data_props_list.index(pp)
                    if data_props_list[p_index]["value"] != None:
                        test_result = 'PASS'
                        break
                elif type(p) == dict and p.keys()[0] in pp.values():
                    p_index = data_props_list.index(pp)
                    if data_props_list[p_index]["value"] == p.values()[0]:
                        test_result = 'PASS'
                        break
                ppc += 1
                if ppc == len(data_props_list):
                    err_list.append(p)
                    fail_reason = '\n\n-*-*-*-*- ' + str(err_list) + ' has error -*-*-*-*-'
                    test_result = 'FAIL'
                    ppc = 0
            if test_result == 'FAIL':
                t_r = 'FAIL'
                continue
        f = open(f_name_o, 'a')
        f.write(fail_reason)
        f.close()
        try:
            os.rename(f_name_o, f_name_o[0:-4] + '_' + t_r + '.txt')
        except:
            os.rename(f_name_o, f_name_o[0:-4] + '_' + test_result + '.txt')
        print test_result
        if test_result != 'PASS':
            if case_not_run == 1:
                case_script.captureScreenAndPull(f_name_o, result_path)
            f_reg = open('regression_test.txt', 'a')
            f_reg.write('%s,'%i)
            f_reg.close()
    end_time = time.time()
    print "-*-*-*- End: %s -*-*-*-\nDuration: %s"%(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(end_time)), end_time - start_time)
        
def arrangeFiles(dir_work, new_dir):
    file_list = os.listdir(result_path)
    try:
        os.mkdir(new_dir)
    except:
        pass
    for f in file_list:
        if f[-8:-4] == 'PASS':
            shutil.move(f, new_dir)

def regressionTest():
    print '===== Regression Test Start ====='
    f_reg = open('regression_test.txt','r')
    reg = f_reg.readline()
    reg_list = reg.split(',')
    reg_list.remove('')
    file_name = r"..\..\case_tmp.xlsx"
    bk = xlrd.open_workbook(file_name)
    case_sheet = bk.sheet_names()[0]
    sh = bk.sheet_by_name(case_sheet)
    nrows = sh.nrows
    ncols = sh.ncols
    col_names = sh.row_values(0)
    os.chdir(result_path)
    for j in reg_list:
        col_values = sh.row_values(int(j))
        k_v = dict(zip(col_names, col_values))
        try:
            k_v['CaseNo'] = int(k_v['CaseNo'])
        except:
            pass
        print str(int(j)+1) + '\t' + str(k_v['CaseNo']) + '\t' + k_v['FuncName'] + '\t... Running ...\t',
        if k_v['EventType'] in ['run', 'ready', 'exit']:
            collection = db.app
        else:
            collection = db.event
        test_result = 'NoData_regression'
        t_r = 'NoData_regression'
        if case_not_run == 1:
            case_script.exitPano()
            collection.remove({"app_id":app_id,"imei":imei}) # Clear history
            try:
                exec('case_script.' + k_v['FuncName'] + '()') # Run test case
                time.sleep(gaps)
            except:
                t_r = 'Err_regression'
        find_par = eval(k_v['FindPar'])
        find_result = collection.find(find_par)
        broken_count = 0
        while len([item for item in find_result]) == 0:
            find_result = collection.find(find_par)
            time.sleep(gaps)
            broken_count += 1
            if broken_count > 10:
                t_r = 'FindDBFailed_regression'
                break
        time.sleep(gaps)
        find_result = collection.find(find_par)
        f_name_o = str(k_v['CaseNo']) + '_' + k_v['FuncName'] + '_regression.txt'
        f = open(f_name_o, 'w')
        fail_reason = ''
        find_result_list = []
        for data in find_result:
            data['_id'] = str(data['_id'])
            json_data = json.dumps(data, indent = 4)
            f.write(json_data)
            find_result_list.append(data)
        f.close()
        props = []
        for prop in k_v['EventProps'].split(','):
            if '=' in prop:
                prop = dict([prop.split('=')])
            props.append(prop)
        data_props_list = []
        for f_data in find_result_list:
            for sub_dic in f_data['props']:
                data_props_list.append(sub_dic)
        err_list = []
        for p in props:
            ppc = 0
            for pp in data_props_list:
                if type(p) != dict and p in pp.values():
                    p_index = data_props_list.index(pp)
                    if data_props_list[p_index]["value"] != None:
                        test_result = 'PASS'
                        break
                elif type(p) == dict and p.keys()[0] in pp.values():
                    p_index = data_props_list.index(pp)
                    if data_props_list[p_index]["value"] == p.values()[0]:
                        test_result = 'PASS'
                        break
                ppc += 1
                if ppc == len(data_props_list):
                    err_list.append(p)
                    fail_reason = '\n\n-*-*-*-*- ' + str(err_list) + ' has error -*-*-*-*-'
                    test_result = 'FAIL_regression'
                    ppc = 0
            if test_result == 'FAIL_regression':
                t_r = 'FAIL_regression'
                continue
        f = open(f_name_o, 'a')
        f.write(fail_reason)
        f.close()
        try:
            os.rename(f_name_o, f_name_o[0:-4] + '_' + t_r + '.txt')
        except:
            os.rename(f_name_o, f_name_o[0:-4] + '_' + test_result + '.txt')
        print test_result
        if test_result != 'PASS':
            if case_not_run == 1:
                case_script.captureScreenAndPull(f_name_o, result_path)
    print '===== Regression Test End ====='
        
mainTest()
arrangeFiles(result_path, 'PASS')
try:
    ff = open('regression_test.txt','r')
    regressionTest()
except:
    pass
arrangeFiles(result_path, 'PASS')