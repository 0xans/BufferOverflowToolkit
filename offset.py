import sys, argparse, itertools
from colorama import Fore, init, Style
init()
info = f'{Fore.YELLOW + Style.BRIGHT}[!]{Fore.RESET + Style.RESET_ALL}'
success = f'{Fore.GREEN + Style.BRIGHT}[+]{Fore.RESET + Style.RESET_ALL}'
error = f'{Fore.RED + Style.BRIGHT}[-]{Fore.RESET + Style.RESET_ALL}'

def create(length, sets):
    if sets:
        pattern = ''.join([''.join(p) for p in itertools.product(*sets)])
    else:
        pattern = ''.join([''.join(p) for p in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789')])
    return pattern[:length]

def find_offset(buffer, value, start=0):
    try:
        return buffer.index(value, start)
    except ValueError:
        return None
    except KeyboardInterrupt:
        return
        
def locate_offset(opts):
    value = opts.value
    length = opts.length
    sets = [s for s in opts.sets.split(',')] if opts.sets else []
    if len(value) >= 8 and value.isdigit():
        value = int(value, 16)
    elif len(value) == 4:
        value = int.from_bytes(value.encode(), 'little')
    else:
        value = int(value, 16)

    buffer = create(length, sets)
    value_bytes = value.to_bytes(4, 'little').decode('latin-1')
    pos = find_offset(buffer, value_bytes)
    if pos is not None:
        print(f"{success} Exact match at offset {pos}")
        found = True
        return
    else:
        found = False
        sys.stderr.write(f"{error} No exact matches, looking for likely candidates\n")
        for idx in range(4):
            for c in range(256):
                nvb = value.to_bytes(4, 'little')
                nvb = nvb[:idx] + bytes([c]) + nvb[idx + 1:]
                nvi = int.from_bytes(nvb, 'little')
                pos = find_offset(buffer, nvi.to_bytes(4, 'little').decode('latin-1'))
                if pos is not None:
                    mle = value - int.from_bytes(buffer[pos:pos + 4].encode('latin-1'), 'little')
                    mbe = value - int.from_bytes(buffer[pos:pos + 4].encode('latin-1'), 'big')
                    print(f"{success} Possible match at offset {pos} (adjusted [ little-endian: {mle} | big-endian: {mbe} ] ) byte offset {idx}")
                    found = True
        if found:
            sys.exit(0)
        for idx in [0, 2]:
            for c in range(65536):
                nvb = value.to_bytes(4, 'little')
                nvb = nvb[:idx] + c.to_bytes(2, 'little') + nvb[idx + 2:]
                nvi = int.from_bytes(nvb, 'little')
                pos = find_offset(buffer, nvi.to_bytes(4, 'little').decode('latin-1'))
                if pos is not None:
                    mle = value - int.from_bytes(buffer[pos:pos + 4].encode('latin-1'), 'little')
                    mbe = value - int.from_bytes(buffer[pos:pos + 4].encode('latin-1'), 'big')
                    print(f"{success} Possible match at offset {pos} (adjusted [ little-endian: {mle} | big-endian: {mbe} ] )")
                    found = True
    while pos is not None:
        print(f"{success} Exact match at offset {pos}")
        pos = find_offset(buffer, value_bytes, pos + 1)
        found = True
        return

def main():
    parser = argparse.ArgumentParser(description="Locate a pattern offset")
    parser.add_argument('-v', '--value', type=str, required=True, help="The value to Locate")
    parser.add_argument('-l', '--length', required=True, type=int, help="The pattern length")
    parser.add_argument('-s', '--sets', required=False, type=str, help="Custom Pattern Sets (e.g: ABC,def,123)")
    args = parser.parse_args()
    locate_offset(args)
if __name__ == '__main__':
    main()
