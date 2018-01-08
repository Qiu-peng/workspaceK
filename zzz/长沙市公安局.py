
import json
import requests
userinfo={'username':'SZAKT', 'password':'0834FBC820E17A2C5C2DA87F93487B36'}
login_resp = requests.post('https://113.240.245.124:8442/login/', cert=('clientShenzhenAoKenTe_cert.cer'), verify=False, data=userinfo)

login_resp.json()
headers = {'content-type': 'application/json',
           'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJcEFkZHJlc3MiOiIxMjAuMjUuNjAuMjAiLCJYUSI6W10sIlRDQyI6W10sImlkIjoiNTljMWUwNTA5MWQ1Nzk2MzBjYWQ0NjA3IiwiQ29udGFjdHMiOiLlu5bkuZTkuL0iLCJDb250YWN0TnVtYmVyIjoiMTg1NjkwODY0ODgiLCJVbml0QWRkcmVzcyI6IuaAu-mDqOWcsOWdgO-8mua3seWcs-W4guWNl-WxseWMuumrmOaWsOaKgOacr-W3peS4muadkeWNl-WMulIzLUHlha3lsYJcbumVv-aymeWIhuWFrOWPuOWcsOWdgO-8mumVv-aymeW4guW8gOemj-WMuua5mOaxn-S4rei3r-S4h-i-vuW5v-WcukMy5qCLMzcxMC0zNzEyIiwiRGlzcGxheU5hbWUiOiLmt7HlnLPluILlpaXogq_nibnnp5HmioDmnInpmZDlhazlj7giLCJpYXQiOjE1MTI2MTY2ODgsImV4cCI6MTUxMjcwNjY4OH0.EMyqQHeFPG5EiOcNgHkHCBGGV46edIQUTwh4HjHJmq0'
}

inoutdatas={
    "records": [
        {"RECORDID": "SZAKT-4156451",
         "TYPE": 0,
         "SJ": "2017-12-06 17:43:43",
         "XZQH": "雨花区",
         "SSFXSJDM": "430111000000",
         "SSFXSJMC": "雨花分局",
         "SSPCSDM": "430111470000",
         "SSPCSMC": "圭塘派出所",
         "TCC": "汇远大厦",
         "CLHP": "临A2JA13",
         "INFO": {"TCCXX": {"TCCDZ": "雨花区劳动东路5号"}}
         }
    ]
}

inout_resp = requests.post('https://113.240.245.124:8442/api/saveVehicleAccessRecord/',
                           headers=headers,
                           cert=('clientShenzhenAoKenTe_cert.cer'),
                           verify=False,
                           data=json.dumps(inoutdatas)
                          )
inout_resp.json()
