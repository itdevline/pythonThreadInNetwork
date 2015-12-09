import socket
from threading import Thread


def _scan(host_port, timeout):
    host, port = host_port.split(":")   # Split the string ":"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, int(port))) # secound argument convert to int (PORT)
        sock.close()    # Close the socket.
        print("Success connecting: " + host + ":" + port)
    except (socket.timeout, socket.error):
        print("Cannot connect to host: " + host + ":" + port)

if __name__ == "__main__":
    # host_list = ["host1:port1", "host2:port2"]
    hosts_list = ["www.python.org:8081", "www.python.org:8082", "www.python.org:8083", "www.python.org:80"]

    # Host check without thread
    
    for out_list in hosts_list:
        _scan(out_list,5)


    # Host check with thread at the same time
    """
    for out_list in hosts_list:
        pThread = Thread(target=_scan, args=(out_list,5,));     # set host list and timeout
        pThread.start()
    """