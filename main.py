import socket

UDP_IP = "192.168.1.255"
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def parser(d: bytes) -> None:
    string_data = d.decode()
    humidity, temp_f, pressure_hpa = string_data.split(';')

    print('Temperature: {:.2f}°F'.format(float(temp_f)))
    print('Humidity   : {:.2f}%'.format(float(humidity)))
    print('Pressure   : {:.2f}hPa\n'.format(float(pressure_hpa)))

try:
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)

        if data == b'syn':
            print('sending \'ack\'')
            sock.sendto(b'ack', addr)
        
        else:
            parser(data)
except KeyboardInterrupt:
    print("User cancelled program.")