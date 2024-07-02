import socket, argparse
from colorama import Fore, init, Style
init()
info = f'{Fore.YELLOW + Style.BRIGHT}[!]{Fore.RESET + Style.RESET_ALL}'
success = f'{Fore.GREEN + Style.BRIGHT}[+]{Fore.RESET + Style.RESET_ALL}'
error = f'{Fore.RED + Style.BRIGHT}[-]{Fore.RESET + Style.RESET_ALL}'

def check(ip, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        print(f"{success} Successfully connected to {ip}:{port}")
        return True
    except Exception as e:
        print(f"{error} Unable to connect to {ip}:{port} - {e}")
        return False
    except KeyboardInterrupt:
        return
    finally:
        s.close()
        print(f"{info} Connection closed")

def interact(s, ip, port, log_file=None):
    try:
        print(f"{success} Connected to {ip}:{port}")

        with open(log_file, 'a') if log_file else None as log:
            while True:
                message = input(f"{info} Enter message ('exit' or 'quit' to close): ")
                if message.lower() in ["exit", "quit"]:
                    break
                s.sendall(message.encode())
                response = s.recv(1024)
                print(f"{success} Received response: {response.decode()}")
                if log:
                    log.write(f"Sent: {message}\nReceived: {response.decode()}\n")
    except Exception as e:
        print(f"{error} An error occurred: {e}")
    finally:
        s.close()
        print(f"{info} Connection closed")


def main():
    parser = argparse.ArgumentParser(description="Check and interact with a target.")
    parser.add_argument('ip', type=str, help='Target IP address')
    parser.add_argument('port', type=int, help='Target port')
    parser.add_argument('-t', '--timeout', type=int, default=5, help='Timeout in seconds (default: 5)')
    parser.add_argument('-c', '--check', action='store_true', help='Check if the port is open without sending a pattern')
    parser.add_argument('-s', '--send', type=str, help='Pattern to send')

    args = parser.parse_args()
    if args.check:
        check(args.ip, args.port, args.timeout)
    elif args.send:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(args.timeout)
            s.connect((args.ip, args.port))
            s.sendall(args.send.encode())
            print(f"{success} Sent pattern: {args.send}")
            response = s.recv(1024)
            print(f"{success} Received response: {response.decode()}")
        except Exception as e:
            print(f"{error} An error occurred: {e}")
        finally:
            s.close()
            print(f"{info} Connection closed")
    else:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(args.timeout)
            s.connect((args.ip, args.port))
            interact(s, args.ip, args.port)
        except Exception as e:
            print(f"{error} Unable to connect to {args.ip}:{args.port} - {e}")
if __name__ == '__main__':
    main()