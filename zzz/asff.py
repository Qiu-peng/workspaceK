import json
import requests
import hashlib
import time
import httplib2

def in2outTime():
    def fun():
        with open('login_token.json', 'r') as f:
            data = f.read()
            data = json.loads(data)
            intime = data[1]
            intime = intime['intime']

        outtime = time.time()
        times = int(outtime) - intime
        if times >= 24*60*60:
            carInout_login()

    return fun

timedata = []
def carInout_login():
    # detail = {'kind': 'login#data'}

    password = 'akt@sz'
    # 加密大写
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    encrypt_passwd = m.hexdigest()
    encrypt_passwd = encrypt_passwd.upper()
    print(encrypt_passwd)

    loginurl = 'http://113.240.245.124:8482/login/'
    query_data = {
        'username': 'SZAKT',
        'password': encrypt_passwd
    }

    response = requests.post(loginurl, data=query_data)
    error_code = response.json().get('error_code')
    error_message = response.json().get('error_message')
    token = response.json().get('token')
    print(token)
    print(error_code)
    print(error_message)

    intime = int(time.time())
    # data = json.dumps(token)

    timedata.append({
        'token': token,
        'intime': intime
    })
    dataTransmit()
    # with open('login_token.json', 'w', encoding='utf-8') as f:
    #     f.write(data)

    # detail['error_code'] = error_code
    # detail['error_message'] = error_message
    # return Response(detail)


# @in2outTime
def dataTransmit():

    # with open('login_token.json', 'r') as f:
    #     data = f.read()
    #     data = json.loads(data)
    #     token = data[0]
    #     token = token['token']
    if timedata:
        print("文件：%s"%timedata)
        token = timedata[0]["token"]
        print(token)
        ssfurl = "http://113.240.245.124:8482/api/saveVehicleAccessRecord/"
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }

        data = {
            "records": [
                {"RECORDID": "SZAKT-1475291",
                 "TYPE": 0,
                 "SJ": "2017-11-16 17:31:25",
                 "XZQH": "雨花区",
                 "SSFXSJDM": "430111000000",
                 "SSFXSJMC": "雨花分局",
                 "SSPCSDM": "430111460000",
                 "SSPCSMC": "洞井派出所",
                 "TCC": "高升家园小区",
                 "CLHP": "湘J2U589",
                 "INFO": {"TCCXX": {"TCCDZ": "测试"}}
                 }
            ]

        }

        response = requests.post(ssfurl, headers=headers, data=json.dumps(data))
        error_code = response.json().get('error_code')
        error_message = response.json().get('error_message')
        print(error_code)
        print(error_message)
    else:
        carInout_login()

if __name__ == '__main__':
    carInout_login()
    # in2outTime()
    # dataTransmit()