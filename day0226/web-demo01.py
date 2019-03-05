"""
1.微程序，即一个web接口
2.搭建并运行服务器
3.浏览器访问
"""


# 程序接口
def index(env, respose):
    print(env)
    print(type(env))

    # QUERY_STRING获取的是使用get请求传递的参数
    print(env["QUERY_STRING"])
    # PATH_INFO获取的就是该页面的URI，我们就可以利用它来传递参数
    print(env["PATH_INFO"])

    respose("200 OK", [("Content-type", "text/html")])
    return [b"hello world"]


# 搭建服务器
from wsgiref.simple_server import make_server
# 创建服务器对象
httpd = make_server("", 8000, index)
print("服务中。。。。")
# 启动服务器，让服务器一直工作
httpd.serve_forever()
