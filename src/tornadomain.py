from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from flask_app import  app


#定义处理类型
# class IndexHandler(tornado.web.RequestHandler):
#     #添加一个处理get请求方式的方法
#     def get(self):
#         #向响应中，添加数据
#         self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')

if __name__ == '__main__':
    app.debug = True
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(80)
    IOLoop.instance().start()
    #创建一个应用对象
    # app = tornado.web.Application([(r'/',IndexHandler)])
    #绑定一个监听端口
    # app.listen(8888)
    #启动web程序，开始监听端口的连接
    # tornado.ioloop.IOLoop.current().start()
