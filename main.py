'''
Module to receive and connect to a UDP stream for Weather from ESP 32
'''

import socket
from os import remove

UDP_IP = ""
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

count = 0

def write_data(data: bytes) -> None:
    with open('/data/.weather.lock', 'w') as lock, open('/data/.weather.dat', 'a') as w_data:
        lock.write('Locking\n')
        string_data = data.decode()
        humidity, temp_f, pressure_hpa = string_data.split(';')
        w_data.write('-'*10 + '\n')
        w_data.write(f'{humidity}\n')
        w_data.write(f'{temp_f}\n')
        w_data.write(f'{pressure_hpa}\n')
    
    remove('/data/.weather.lock')

def parser(d: bytes) -> None:
    global count 
    count += 1
    string_data = d.decode()
    humidity, temp_f, pressure_hpa = string_data.split(';')

    print(f'Packet Count: {count}')
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
            write_data(data)
except TimeoutError as e:
    print(f'Socket Timed out: {e}')
except KeyboardInterrupt:
    print("User cancelled program.")
