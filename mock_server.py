# /usr/bin/env python
# -*- coding:utf-8 -*-
 
 
from flask import jsonify,Flask,request
 
app = Flask(__name__)    
app.config['JSON_AS_ASCII'] = False #返回中存在中文字符 



@app.route('/mock/login', methods=['POST'])   
def login():
    login_success = {
    "code": 0,
    "msg": "Login Success",
    }
    login_error = {
    "code": 1,
    "msg": "账号密码错误",
    }
    name=request.values.get('name')
    password=request.values.get('password')
    if name=='wj' and password=='123456':
        return jsonify(login_success)
    else:
        return jsonify(login_error)


delMsg={
    'code':0,
    'msg':'delete success'
}
@app.route('/mock/deleteMock', methods=['DELETE'])   
def delete_mock():
    return jsonify(delMsg)


putMsg={
    'code':0,
    'msg':'put success'
}
@app.route('/mock/putMock', methods=['PUT'])     
def put_mock():
    return jsonify(putMsg)
 
if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 5000,
        debug = True
        )
