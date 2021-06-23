from app import app
from database.models import IbmUser, Config
from database import DB
import requests
import json
import time

@app.route('/custom_original', methods=['POST'])
def add_user():
    
    config = Config.query.filter_by().first()
    ibm_user_index = config.ibm_user_index

    user = IbmUser.query.filter_by(id=ibm_user_index).first()
    if user is None:
        config.ibm_user_index = config.ibm_user_index + 1
        DB.session.commit()
        return add_user()
    new_id = req_url(user.tel)
    if new_id == 0 or new_id is None:
        config.ibm_user_index = config.ibm_user_index + 1
        DB.session.commit()
        return add_user()
        
    DB.session.commit()
    hidata_reg(new_id, user.tel)
    return {
        "tel": user.tel,
        "index": config.ibm_user_index
    }

@app.route('/count')
def get_count():
    
    config = Config.query.filter_by().first()
    ibm_user_index = config.ibm_user_index
    return {
        "index": ibm_user_index,
        "total": 280262
    }

def req_url(m):
    kw = {
        'm': m
    }
    headers = {
        'client': 'h5',
        'version': '2.2.6'
    }
    response = requests.put(
        app.config['RDHY_GEN_URL'], params=kw, headers=headers
    )
    response_datas = json.loads(response.text)
    return response_datas['data']

def hidata_reg(user_id, tel):
    data = {
        "common":{
            "ip": "0.0.0.0",
            "port": "80",
            "appId": app.config['HIDATA_APPID'],
            "platformId": "2",
            "appVersion": "V1.0",
            "eventLogVersion": "V1.0",
            "deviceId": "",
            "deviceType": "1",
            "deviceModel": "PC",
            "operateSystem": "Mac",
            "operateSystemVersion": "MacIntel",
            "screenSize": "2560*1440",
            "browserName": "chrome/90.0.4430.85",
            "browserVersion": "90",
            "logType": "2"
        },
        "event":{
            "sourceId":"10001",
            "eventId": "3",
            "eventTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
			"userId": user_id,			       # 用户id 
			"account": tel,  		           # 注册账号
			"passwd": "",                      # 注册密码
			"name": "", 		               # 注册姓名
			"nickname": "",   	               # 注册别名
			"registerType": "2", 			   # 注册方式（1：工号；2：手机；3：微信；4：qq;5:微博6：邮箱）
			"img": "",	                       # 注册头像 
			"age": "0",						   # 注册年龄 
			"sex": "0",						   # 性别：0：无；1：男；2：女； 
			"birthday": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # 生日  
			"trade": "123"
            }
        }
    
    response = requests.post(app.config['HIDATA_URL'], data=json.dumps(data), headers={
        'Content-Type': 'application/json;charset=UTF-8'
    })
    # response_datas = json.loads(response.text)
    return bool(response.text)
    
    