from wsgiref.simple_server import make_server
from webob import Request,Response, dec, exc
import re

class Router:
    def __init__(self, prefix:str=''):
        self.__prefix = prefix.rstrip('/\\')
        self.__routetable = []

    @property
    def prefix(self):
        return self.__prefix

    def route(self, pattern, *methods):
        def wrapper(handler):
            self.__routetable.append((pattern, methods, handler))
            return handler
        return wrapper

    def get(self, pattern):
        return self.route(pattern, "GET")

    def post(self, pattern):
        return self.route(pattern, "POST")

    def match(self, request: Request):
        if not request.path.startswith(self.prefix):
            return

        for pattern,methods,handler in self.__routetable:
            if not methods or request.method.upper() in methods:
                response = handler(request)

                return response


class Application:
    ROUTERS = []

    # 注册服务器
    @classmethod
    def register(cls, router:Router):
        cls.ROUTERS.append(router)
        return router

    @dec.wsgify
    def __call__(self, request: Request):
        for router in self.ROUTERS:
            response = router.match(request)
            if response:
                return response

        raise exc.HTTPNotFound('您访问的页面被外星人劫持了')


idx = Router('/')
py = Router('/python')
Application.register(idx)
Application.register(py)


@idx.get('/')
def index(request:Request):
    res = Response()
    res.body = "<h1>欢迎你们</h1>".encode()
    return res

@py.get('/python')
def showpython(request:Request):
    res = Response()
    res.body = "<h1>python</h1>".encode()
    return res

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    server = make_server(host,port,Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
