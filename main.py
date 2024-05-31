import socket

UDP_IP = ""
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
#sock.settimeout(5)

def parser(d: bytes) -> None:
    string_data = d.decode()
    humidity, temp_f, pressure_hpa = string_data.split(';')

    print('Temperature: {:.2f}°F'.format(float(temp_f)))
    print('Humidity   : {:.2f}%'.format(float(humidity)))
    print('Pressure   : {:.2f}hPa\n'.format(float(pressure_hpa)))

try:
    print('Starting application...')
    while True:
        data, addr = sock.recvfrom(1024)
        print(f'Addr: {addr}')
        print(f"Received message: {data}")

        if data == b'syn':
            print('sending \'ack\'')
            sock.sendto(b'ack', addr)
        else:
            parser(data)
except TimeoutError as e:
    print(f'Socket Timed out: {e}')
except KeyboardInterrupt:
    print("User cancelled program.")
