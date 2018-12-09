import bluetooth
import pygame
import time


def init_ble():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found %d devices" % len(nearby_devices))
    print(nearby_devices)

    device_mac_addr = '0C:54:15:8D:60:98'
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((device_mac_addr, port))

    time.sleep(2)

    return sock


def init_pygame():
    pygame.init()
    # clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_mode((640, 480))
    # return clock


def read_keyboard():
    data = [0] * 6

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        print("SPEED UP")
        data[0] = 1
    elif keys[pygame.K_s]:
        print("SLOW DOWN")
        data[1] = 1

    if keys[pygame.K_UP]:
        print("FORWARD")
        data[2] = 1
    elif keys[pygame.K_DOWN]:
        print("BACKWARD")
        data[3] = 1

    if keys[pygame.K_LEFT]:
        print("LEFT")
        data[4] = 1
    elif keys[pygame.K_RIGHT]:
        print("RIGHT")
        data[5] = 1

    if keys[pygame.K_ESCAPE]:
        print("STOPPING")
        data = None

    return data


def process():
    init_pygame()
    sock = init_ble()

    while True:
        pygame.time.wait(500)

        data = read_keyboard()

        if not data:
            sock.close()
            return

        print(data)
        sock.send(str(data))
        pygame.event.pump()


def main():
    process()


if __name__ == '__main__':
    main()
