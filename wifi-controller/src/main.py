import socket
import pygame
from time import sleep


def init_pygame():
    pygame.init()
    # clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_mode((640, 480))
    # return clock


def read_keyboard():
    data = ['0'] * 6
    data[0] = '1'

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_w]:
    #     # print("SPEED UP")
    #     data[0] = '1'
    # elif keys[pygame.K_s]:
    #     # print("SLOW DOWN")
    #     data[1] = '1'

    if keys[pygame.K_UP]:
        # print("FORWARD")
        data[1] = '1'
        data[0] = '0'
    elif keys[pygame.K_DOWN]:
        # print("BACKWARD")
        data[0] = '0'
        data[2] = '1'

    if keys[pygame.K_LEFT]:
        # print("LEFT")
        data[0] = '0'
        data[3] = '1'
    elif keys[pygame.K_RIGHT]:
        # print("RIGHT")
        data[0] = '0'
        data[4] = '1'

    if keys[pygame.K_CAPSLOCK]:
        data[5] = '1'

    if keys[pygame.K_ESCAPE]:
        # print("STOPPING")
        data = None

    return ''.join(data)


def process():
    init_pygame()

    host = '192.168.43.94'
    # host = "127.0.0.1"
    port = 2137
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))
    last_sent = None

    counter = 0
    delta = 10000
    while True:
        counter += 1
        delta += 1

        data = read_keyboard()

        if not data:
            sock.close()
            return

        if data != last_sent and delta > 95000:
            counter = 0
            delta = 0
            sock.sendto(data.encode(), (host, port))
            print("CHANGE ", data)
            last_sent = data
        elif counter > 1000000:
            counter = 0
            sock.sendto(data.encode(), (host, port))
            print("KEEP ALIVE ", data)

        pygame.event.pump()


def main():
    process()


if __name__ == '__main__':
    main()
