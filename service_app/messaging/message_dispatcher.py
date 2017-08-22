from service_app.messaging.discovery_service import DiscoveryService
import socket

svc_listening_port = 1256
svc_max_udp_size = 1024
box_listening_port = 1257

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MessageDispatcher(object, metaclass=Singleton):
    def __init__(self):
        print('[MessageDispatch] Initializing discovery service...')
        self.discovery_svc = DiscoveryService(svc_listening_port, svc_max_udp_size)
        self.discovery_svc.run()
        print('[MessageDispatch] Discovery service started.')

    def dispatch_message(self, message):
        boxes = message.send_to.all()
        b_message = str(message.message).encode('utf-8')
        b_duration = str(message.duration).encode('utf-8')
        b_type = str(message.type).encode('utf-8')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        all_included = True
    
        print('[MessageDispatch] Dispatching ' + str(message))
        for box in boxes:
            print('[MessageDispatch] Sending to ' + str(box))
            b_packet = b'PASS_MSG/!!/' + b_type + b'/!!/' + b_message + b'/!!/' + b_duration
            print(b_packet.decode('utf-8'))
            if box.mac_address in self.discovery_svc.mac_ip_map.keys():
                box_ip = self.discovery_svc.mac_ip_map.get(box.mac_address)
                sock.sendto(b_packet, (box_ip, box_listening_port))
            else:
                print('[MessageDispatch] Not found! The system does not have the IP address of ' + box.mac_address)
                all_included = False

        return all_included
