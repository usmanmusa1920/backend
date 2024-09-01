import socket


def port_scanner(target, ports):
    get_host_name = socket.gethostbyname(target)
    print(f"Scanning {target} ({get_host_name})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result =  sock.connect_ex((get_host_name, port))

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()


# here i booted jupyter-lab server on port 8888, flask server on 5000 & django server on port 8000, while the port 7000 is off.
port_scanner("127.0.0.1", [8888, 5000, 7000, 8000])
