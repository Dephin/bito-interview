from flask import Flask, Response, jsonify


# 定义response返回类,自动解析json
# class JSONResponse(Response):
#     @classmethod
#     def force_type(cls, response, environ=None):
#         if isinstance(response, dict):  # 判断返回类型是否是字典(JSON)
#             response = jsonify(response)  # 转换
#         return super().force_type(response, environ)


app = Flask(__name__)
app.debug = True  # 开启debug
# app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api')
class Controller:
    @app.route('/people')
    def getPeopleData(self):
        foo.id=1
        pass

    @app.route('/people/update')
    def updatePeopleData(self):
        pass

    @app.route('/people/snapshot')
    def getPeopleSnapshopData(self):
        pass

    @app.route('/people/snapshot/update')
    def updatePeopleSnapshotData(self):
        pass


if __name__ == '__main__':
    app.run()
