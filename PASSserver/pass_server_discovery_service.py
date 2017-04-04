import select
import socket
import pass_server_settings
import netifaces as ni

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def socket_bind():
    private_interface = None
    for interface_name in ni.interfaces():
        iface = ni.ifaddresses(interface_name)
        if str(iface[ni.AF_LINK][0].get('addr')).replace(':', '').lower() == pass_settings.PRIVATE_IF_MAC.replace(':', '').lower():
            private_interface = iface
    
    private_address = private_interface.get(ni.AF_INET)

    if not private_address:
        print('socket_bind(): [Error] Unable to find information for given interface address: ' + pass_settings.PRIVATE_IF_MAC)
        print('                       Please check address configuration!')
    
    binding_on = (private_address[0].get('addr') if private_address else '', pass_settings.PORT)
    print('socket_bind(): Binding on: ' + str(binding_on))
    s.bind(binding_on)

def socket_listen():
    socket_bind()
    while True:
        result = select.select([s], [], [])
        # message = result[0][0].recv(pass_settings.BUFFER_SIZE)
        data = s.recvfrom(pass_settings.BUFFER_SIZE)

        message = data[0]
        address = data[1]

        if not data or not address:
            continue

        print('recv from: ' + str(address))
        print('recv data: ' + message.decode())

        reply = 'OK...' + str(data)
        s.sendto(reply.encode(), address)
        
        print(result)
