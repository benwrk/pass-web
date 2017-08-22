import threading
import socket

class DiscoveryService(object):
    
    def __init__(self, listening_port, max_udp_size):
        self.listening_port = listening_port
        self.max_udp_size = max_udp_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', listening_port))
        self.mac_ip_map = {}
        self.discovery_thread = self.DiscoveryThread(0, self)

    def run(self):
        print('[DiscoveryService] Starting discovery thread.')
        self.discovery_thread.start()
    
    def stop(self):
        self.discovery_thread.safe_stop()

    class DiscoveryThread(threading.Thread):
        def __init__(self, id, server):
            threading.Thread.__init__(self)
            self.id = id
            self.server = server
            self.running = False
            self.daemon = True
                    
        def run(self):
            self.running = True
            while self.running:
                data, src = self.server.socket.recvfrom(self.server.max_udp_size)
                if not self.running:
                    break
                data_str = str(data, 'utf-8')
                if 'PASS_HANDSHAKE' in data_str:
                    mac = data_str.split('/!!/')[1]
                    ip_address, origin_port = src
                    print('[DiscoveryThread] Broadcast received: ' + mac + ' is located at ' + ip_address)
                    
                    # Add to dict!
                    self.server.mac_ip_map[mac] = ip_address

        def safe_stop(self):
            self.running = False
