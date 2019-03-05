def main(env, response):
    response("200 OK", [("Content-type", "text/html")])
    # print(env["PATH_INFO"])
    path = env["PATH_INFO"][1:]

    if path == "findall":
        return findall(env, response)
    elif path == "allgood":
        return allgood(env, response)
    elif path == "delete":
        return delete(env, response)
    elif path == "index":
        return index(env, response)


def index(env, response):
    listA = open("temp/index1.html", "r", encoding="utf-8")
    listr = listA.read()
    return [listr.encode("utf-8")]


def findall(env, response):
    listA = open("temp/findall.html", "r", encoding="utf-8")
    listr = listA.read()
    return [listr.encode("utf-8")]


def allgood(env, response):
    listB = open("temp/allgood.html", "r", encoding="utf-8")
    listr2 = listB.read()
    return [listr2.encode("utf-8")]


def delete(env, response):
    listC = open("temp/delete.html", "r", encoding="utf-8")
    listr3 = listC.read()
    return [listr3.encode("utf-8")]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd1 = make_server("", 8000, main)
    print("无常普。。。")
    httpd1.serve_forever()


