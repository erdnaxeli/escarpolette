import socket

import netifaces
from zeroconf import ServiceInfo, Zeroconf


def register(port: int):
    zeroconf = Zeroconf()

    addresses = []
    for i in netifaces.interfaces():
        try:
            addresses.append(socket.inet_aton(netifaces.ifaddresses(i)[netifaces.AF_INET][0]["addr"]))
        except KeyError:
            pass

    name = "_escarpolette._tcp.local."
    service = ServiceInfo(
        "_escarpolette._tcp.local.", name=name, port=port, addresses=addresses
    )
    zeroconf.register_service(service)
