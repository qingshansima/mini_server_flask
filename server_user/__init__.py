from flask import Flask,jsonify
from server_user.config import DevConfig

#App初始化
app=Flask(__name__)
#环境配置
app.config.from_object('server_user.config.DevConfig')

@app.route('/startInfo',methods=['GET'])
def start_info():
    return jsonify({
        'code':'000000000000',
        'message':'OK'
    })