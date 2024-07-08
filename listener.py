import socket, argparse, sys, time
from colorama import Fore, init, Style
init()
info = f'{Fore.YELLOW + Style.BRIGHT}[!]{Fore.RESET + Style.RESET_ALL}'
success = f'{Fore.GREEN + Style.BRIGHT}[+]{Fore.RESET + Style.RESET_ALL}'
error = f'{Fore.RED + Style.BRIGHT}[-]{Fore.RESET + Style.RESET_ALL}'

def listener(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip, port))
        s.listen(1)
        print(f"{success} Listening on {ip}:{port}")
        conn, addr = s.accept()
        print(f"{success} Connection received from {addr[0]}:{addr[1]}")
        while True:
            try:

                ans = conn.recv(1024).decode()
                sys.stdout.write(ans)
                command = input(f"")
                command += '\n'
                if command.strip().lower() == 'exit':
                    print(f"{info} Closing connection...")
                    conn.close()
                    break
                conn.send(command.encode())
                time.sleep(0.5)
                _line = ans.split('\n')[-1]
                sys.stdout.write('\033[A' + _line + '\n')
            except KeyboardInterrupt:
                print(f"{info} Interrupted by user. Closing connection...")
                conn.close()
                break
            except Exception as e:
                print(f"{error} An error occurred: {str(e)}")
                conn.close()
                break
    except KeyboardInterrupt:
        print(f"{info} Interrupted by user. Exiting...")
    except socket.timeout:
        print(f"{error} Connection timed out.")
    except Exception as e:
        print(f"{error} An error occurred: {str(e)}")
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description="Listener Script")
    parser.add_argument("ip", nargs='?', default='0.0.0.0', help="Listener IP address")
    parser.add_argument("port", type=int, help="Listener port")
    args = parser.parse_args()
    listener(args.ip, args.port)

if __name__ == '__main__':
    main()
