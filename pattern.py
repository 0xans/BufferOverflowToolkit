import sys, argparse, itertools
from colorama import Fore, init, Style
init()
info = f'{Fore.YELLOW + Style.BRIGHT}[!]{Fore.RESET + Style.RESET_ALL}'
sucess = f'{Fore.GREEN + Style.BRIGHT}[+]{Fore.RESET + Style.RESET_ALL}'
error = f'{Fore.RED + Style.BRIGHT}[-]{Fore.RESET + Style.RESET_ALL}'

def create(length, sets):
    if sets:
        sets_list = [list(s) for s in sets.split(',')]
        pattern = ''.join(''.join(p) for p in itertools.product(*sets_list))
    else:
        sets_list = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789']
        pattern = ''.join(''.join(p) for p in itertools.product(*sets_list))
    
    if length > len(pattern):
        print(f"{error} The requested length exceeds the maximum pattern length.")
        sys.exit(1)
    return pattern[:length]

def main():
    parser = argparse.ArgumentParser(description="Generate a pattern")
    parser.add_argument('-l', '--length', required=True, type=int, help="The pattern length")
    parser.add_argument('-s', '--sets', required=False, type=str, help="Custom Pattern Sets (e.g: ABC,def,123)")
    args = parser.parse_args()
    length = args.length
    sets = args.sets

    pattern = create(length, sets)
    print(f'{sucess} Created pattern:\n{pattern}')
if __name__ == '__main__':
    main()