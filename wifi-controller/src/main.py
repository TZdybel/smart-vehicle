import socket
import pygame
import time


def init_wifi(host, port):
    # host_addr = '198.168.0.1'
    # port = 2137
    # sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # sock.connect((device_mac_addr, port))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))

    time.sleep(2)

    return s


def init_pygame():
    pygame.init()
    # clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_mode((640, 480))
    # return clock


def read_keyboard():
    data = ['0'] * 6

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        print("SPEED UP")
        data[0] = '1'
    elif keys[pygame.K_s]:
        print("SLOW DOWN")
        data[1] = '1'

    if keys[pygame.K_UP]:
        print("FORWARD")
        data[2] = '1'
    elif keys[pygame.K_DOWN]:
        print("BACKWARD")
        data[3] = '1'

    if keys[pygame.K_LEFT]:
        print("LEFT")
        data[4] = '1'
    elif keys[pygame.K_RIGHT]:
        print("RIGHT")
        data[5] = '1'

    if keys[pygame.K_ESCAPE]:
        print("STOPPING")
        data = None

    return ''.join(data)


def process():
    init_pygame()

    # host = '192.168.10.1'
    host = "127.0.0.1"
    port = 8002
    sock = init_wifi(host, port)

    while True:
        # pygame.time.wait(500)

        data = read_keyboard()

        if not data:
            sock.close()
            return

        print(data)
        sock.sendto(data.encode(), (host, port))
        pygame.event.pump()


def main():
    process()


if __name__ == '__main__':
    main()
