#!flask/bin/python
import json
from flask import Flask, jsonify,request

app = Flask(__name__)

def get_args(args1,args2):
    argss = args1+args2
    return argss


# passwd sign in
# from flask.ext.httpauth import HTTPBasicAuth
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# get 请求 响应结果 返回字典
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})
#
# # 按照 id来执行不同的功能
from flask import abort

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    task = [item for item in task]
    # task = {}
    # for item in tasks:
    #     if item['id'] == task_id:
    #         task[task_id] = item
    # if len(task) == 0:
    #     abort(404)

    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})

# 友好显示 404错误
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# def test():
#     for i in range(1,1000):
#         i = i * 3
#
#     a = {'AAAA' : i}
#
#     return a
# @app.route('/todo/api/v1.0/test', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': test()})
from flask import url_for

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    # python2 python3 区别之 map 数组和迭代器的区别
    task = [item for item in map(make_public_task, tasks)]
    return jsonify({'tasks': task})

# zabbix的方法
# 根据传入的参数调用不同的功能

@app.route('/zabbix',methods=['GET','POST'])
@auth.login_required
def get_zabbix():

    data = request.args
    json_dumps = json.dumps(data)
    print(json_dumps)
    return json_dumps


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
