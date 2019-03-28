import pytest
import json
import requests
import time
import re


def file_clean(pathtofile):
    with open(pathtofile, 'w') as logfile:
        logfile.close()


def file_parse(pathtofile):
    with open(pathtofile, 'r') as logfile:
        regex = re.findall(r'(?<=WARNING\s\s\|\s)[\w\s,()%]*(?=\n)', logfile.read())
        logfile.close()
        return regex


def win_dict(test_input):
    d = dict(instance_type=test_input[0],
             instance_name=test_input[1],
             server_connection_report=test_input[2],
             server_mem_report=test_input[3],
             server_cpu_report=test_input[4],
             processes_report=dict(test_input[5])
             )
    time.sleep(0.01)
    j = json.dumps(d)
    return j

def win_dict_procrep_no_dict(test_input):
    d = dict(instance_type=test_input[0],
             instance_name=test_input[1],
             server_connection_report=test_input[2],
             server_mem_report=test_input[3],
             server_cpu_report=test_input[4],
             processes_report=test_input[5]
             )
    time.sleep(0.01)
    j = json.dumps(d)
    return j


def mt5_dict(test_input):
    d = dict(instance_type=test_input[0],
             instance_name=test_input[1],
             server_connection_report=test_input[2],
             balance_operations=test_input[3],
             server_quotes_delay_report=dict(test_input[4])
             )
    time.sleep(0.01)
    j = json.dumps(d)
    return j


def post_send(j):
    ip = "http://192.168.1.8:55555"

    headrs = {'Content-Type': 'application/json'}

    requests.post(ip, data=j, headers=headrs)




logfilepath = str(r'C:\Users\Tester\Documents\TASKS\MON-2\MON_Server_v102\LOGS\2019-03-27-client.log')


data_mail_check_no_access = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "-1", "-1", "-1", {"mtsrv": 9}],
                 'not accessible',
                 id='mail WIN NOT ACCESSIBLE')
                            ]

data_mail_check_no_access_no_dict = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "-1", "0", "-1", "-1"],
                 'not accessible',
                 id='mail WIN NOT ACCESSIBLE')
                            ]

data_mail_check_total_m_limit = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "10", {"mtsrv": 9}],
                 'Memory usage is 51%, limit is 50%',
                 id='mail WIN memory limit reached -1'),
#    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "51", "10", {"mtsrv": 9}],
#                 'Memory usage is 51%, limit is 50%',
#                 id='mail WIN memory limit reached 50')
                            ]

data_mail_check_total_cpu_limit = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "40", {"mtsrv": 9}],
                 'CPU usage is 40%, limit is 35%',
                 id='mail WIN cpu limit reached 40'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "34", {"mtsrv": 9}],
                 'CPU usage is 34%, limit is 35%',
                 id='mail WIN cpu limit reached 34')
                                ]

data_mail_check_process_cpu_limit = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "34", {"mtsrv": 10}],
                 'Memory usage is 10 MB, limit is 10 MB',
                 id='mail ps mtsrv cpu limit reached 10'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "34", {"mtsrv": 11}],
                 'Memory usage is 11 MB, limit is 11 MB',
                 id='Process mtsrv Memory reached limit'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", "49", "34", {"mtsrv": -1}],
                 'Process mtsrv is not found',
                 id='Process mtsrv is not found'),
                                     ]


testdata_win = [
    pytest.param(["WIN", "LOCALHOST4 (300)", "-1", 27, 0, {"mtsrv": 10}],
                 'not accessible',
                 id='WIN-MT4 NOT ACCESSIBLE'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", 27, 0, {"mtsrv": 10}],
                 'Process mtsrv memory usage limit is reached',
                 id='MT4 Memory Limit Reached'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", 27, 0, {"mtsrv": 10}],
                 'Memory usage is 10 MB, limit is 10 MB',
                 id='Memory Usage Is'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", 50, 0, {"mtsrv": 5}],
                 'Memory usage is 50%, limit is 50%',
                 id='MT4 CPU Usage Percentage'),
    pytest.param(["WIN", "LOCALHOST4 (300)", "0", 50, 35, {"mtsrv": 5}],
                 'CPU usage is 35%, limit is 35%',
                 id='CPU Usage Reached'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "-1", 27, 0, {"mt5trade64": 10}],
                 'not accessible',
                 id='WIN-MT5 NOT ACCESSIBLE'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5access64": 10}],
                 'Memory usage is 10 MB, limit is 10 MB',
                 id="MT5ACCESS Memory Limit Is"),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5access64": 10}],
                 'Process mt5access64 memory usage limit is reached',
                 id='MT5 Memory Limit Reached'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5trade64": 10}],
                 'Memory usage is 10 MB, limit is 10 MB',
                 id='MT5TRADE Memory Limit Is'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5trade64": 10}],
                 'Process mt5trade64 memory usage limit is reached',
                 id='MT5TRADE Memory Limit Reached'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5history64": 10}],
                 'Memory usage is 10 MB, limit is 10 MB',
                 id='MT5HISTORY Memory Limit Is'),
    pytest.param(["WIN", "LOCALHOST5 (300)", "0", 50, 0, {"mt5history64": 10}],
                 'Process mt5history64 memory usage limit is reached',
                 id='MT5HISTORY Memory Limit Reached'),
                         ]

testdata_win_no_alerts = [
    (["WIN", "LOCALHOST4 (300)", "0", 27, 0, {"mtsrv": 9}], 'not accessible'),
    (["WIN", "LOCALHOST4 (300)", "0", 27, 0, {"mtsrv": 9}], 'Process mtsrv memory usage limit is reached'),
    (["WIN", "LOCALHOST4 (300)", "0", 27, 0, {"mtsrv": 9}], 'Memory usage is 9 MB, limit is 10 MB'),
    (["WIN", "LOCALHOST4 (300)", "0", 49, 0, {"mtsrv": 9}], 'Memory usage is 49%, limit is 50%'),
    (["WIN", "LOCALHOST4 (300)", "0", 49, 34, {"mtsrv": 9}], 'CPU usage is 34%, limit is 35%'),
    (["WIN", "LOCALHOST5 (300)", "0", 27, 0, {"mt5trade64": 9,
                                              "mt5access64": 9,
                                              "mt5history64": 9}],
     'not accessible'),
    (["WIN", "LOCALHOST5 (300)", "0", 27, 0, {"mt5trade64": 9,
                                              "mt5access64": 9,
                                              "mt5history64": 9}],
     'Memory usage is 10 MB, limit is 10 MB'),
    (["WIN", "LOCALHOST5 (300)", "0", 27, 0, {"mt5trade64": 9,
                                              "mt5access64": 9,
                                              "mt5history64": 9}],
     'Process mt5access64 memory usage limit is reached'),
    (["WIN", "LOCALHOST5 (300)", "0", 27, 0, {"mt5trade64": 9,
                                              "mt5access64": 9,
                                              "mt5history64": 9}],
     'Process mt5trade64 memory usage limit is reached'),
    (["WIN", "LOCALHOST5 (300)", "0", 27, 0, {"mt5trade64": 9,
                                              "mt5access64": 9,
                                              "mt5history64": 9}],
     'Process mt5history64 memory usage limit is reached'),
                         ]

testdata_mt5 = [
    pytest.param(["MT5", "MT5 (300)", '-1', 0, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'not accessible',
                 id='MT5 NOT ACCESSIBLE'),
    pytest.param(["MT5", "MT5 (300)", 0, -1, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'balance operations failed',
                 id='MT5 Balance operation Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 999}],
                 'Symbol EURCAD delay limit is reached',
                 id='Quotes EURCAD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 999}],
                 'Delay is 1000 sec, limit is 1000 sec',
                 id='Quotes EURCAD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 1000, "EURGBP": 999}],
                 'Symbol EURUSD delay limit is reached',
                 id='Quotes EURUSD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 1000}],
                 'Symbol EURGBP delay limit is reached',
                 id='Quotes EURGBP Delay Alert'),
                         ]

testdata_mt5_no_alerts = [
    pytest.param(["MT5", "MT5 (300)", "0", 0, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'not accessible',
                 id='str MT5 ACCESSIBLE'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'not accessible',
                 id='int MT5 ACCESSIBLE'),
    pytest.param(["MT5", "MT5 (300)", 0, "0", {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'balance operations failed',
                 id='str MT5 Balance operation Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'balance operations failed',
                 id='int MT5 Balance operation Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 1000, "EURGBP": 1000}],
                 'Symbol EURCAD delay limit is reached',
                 id='Quotes EURCAD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 1000, "EURGBP": 1000}],
                 'Delay is 1000 sec, limit is 1000 sec',
                 id='Quotes EURCAD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 1000, "EURGBP": 999}],
                 'Symbol EURUSD delay limit is reached',
                 id='Quotes EURUSD Delay Alert'),
    pytest.param(["MT5", "MT5 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 1000}],
                 'Symbol EURGBP delay limit is reached',
                 id='Quotes EURGBP Delay Alert'),
                         ]


testdata_mt4 = [
    pytest.param(["MT4", "MT4 (300)", '-1', 0, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'not accessible',
                 id='MT4 NOT ACCESSIBLE'),
    pytest.param(["MT4", "MT4 (300)", 0, -1, {"EURCAD": 999, "EURUSD": 999, "EURGBP": 999}],
                 'balance operations failed',
                 id='MT4 Balance operation Alert'),
    pytest.param(["MT4", "MT4 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 999}],
                 'Symbol EURCAD delay limit is reached',
                 id='MT4 Quotes EURCAD Delay Alert'),
    pytest.param(["MT4", "MT4 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 999}],
                 'Delay is 1000 sec, limit is 1000 sec',
                 id='MT4 Quotes EURCAD Delay Alert'),
    pytest.param(["MT4", "MT4 (300)", 0, 0, {"EURCAD": 999, "EURUSD": 1000, "EURGBP": 999}],
                 'Symbol EURUSD delay limit is reached',
                 id='MT4 Quotes EURUSD Delay Alert'),
    pytest.param(["MT4", "MT4 (300)", 0, 0, {"EURCAD": 1000, "EURUSD": 999, "EURGBP": 1000}],
                 'Symbol EURGBP delay limit is reached',
                 id='MT4 Quotes EURGBP Delay Alert')
                         ]


@pytest.mark.parametrize('test_input, expected', testdata_win)
def test_wincore_positive(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', testdata_win_no_alerts)
def test_wincore_no_alerts(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)

    assert any(expected in s for s in regex) is False


@pytest.mark.parametrize('test_input, expected', testdata_mt5)
def test_mt5_positive(test_input, expected):

    file_clean(logfilepath)

    j = mt5_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', testdata_mt4)
def test_mt4_positive(test_input, expected):

    file_clean(logfilepath)

    j = mt5_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)

    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', testdata_mt5_no_alerts)
def test_mt5_no_alerts(test_input, expected):

    file_clean(logfilepath)

    j = mt5_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is False


@pytest.mark.parametrize('test_input, expected', data_mail_check_no_access)
def test_mail_no_access(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', data_mail_check_total_m_limit)
def test_mail_memory_limit(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', data_mail_check_total_cpu_limit)
def test_mail_cpu_limit(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


@pytest.mark.parametrize('test_input, expected', data_mail_check_process_cpu_limit)
def test_mail_prc_limit(test_input, expected):

    file_clean(logfilepath)

    j = win_dict(test_input)

    post_send(j)

    regex = file_parse(logfilepath)
    assert any(expected in s for s in regex) is True


