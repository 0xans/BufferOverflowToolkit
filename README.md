# Buffer Overflow Toolkit
## Name: Buffer Overflow Toolkit
## Author: 0xans
## Contact: Instagram: [0x.ans](https://instagram.com/0x.ans)

```
  ____         __ _____           _ _  ___ _   
 | __ )  ___  / _|_   _|__   ___ | | |/ (_) |_ 
 |  _ \ / _ \| |_  | |/ _ \ / _ \| | ' /| | __|
 | |_) | (_) |  _| | | (_) | (_) | | . \| | |_ 
 |____/ \___/|_|   |_|\___/ \___/|_|_|\_\_|\__|
                                          @0xans
```

## Usage:
- **Bad Characters Detection:**
  ```sh
  python3 badchars.py -b <badchars>
  ```
- **Buffer Overflow Exploit:**
  ```sh
  python3 exploit.py <ip> <port> -o <offset> -p <prefix>
  ```
- **Fuzzing for Buffer Overflows:**
  ```sh
  python3 fuzzer.py <ip> <port> -n <initial_size> -x <step>
  ```
- **Pattern Creation and Offset Detection:**
  ```sh
  python3 pattern.py -l <length> -s <sets>
  python3 offset.py -v <value> -l <length> -s <sets>
  ```
- **Listener for Reverse Shells:**
  ```sh
  python3 listener.py <ip> <port>
  ```
- **Interacting with Exploited Targets:**
  ```sh
  python3 interactor.py <ip> <port> -t <timeout>
  ```

## Tool Descriptions:
### Bad Characters Detection
Generates all byte values from `\x00` to `\xff` as a formatted string, excluding specified bad characters.

### Buffer Overflow Exploit
Script to create and send a buffer overflow payload to a specified IP and port.

### Fuzzer
Fuzzes a target application to determine the payload size that causes a crash.

### Pattern Creation
Generates a unique pattern to help identify the offset of the buffer overflow.

### Offset Detection
Locates the exact offset in the buffer using a generated pattern.

### Listener
Sets up a listener to catch incoming connections, useful for reverse shells.

### Interactor
Interacts with an exploited target, sending and receiving messages.

## Options:
- `-h, --help`: Show help message and exit.
- `-b, --badchars <badchars>`: Specify bad characters to exclude.
- `-u, --url <url>`: Target URL (for some scripts).
- `-x, --origin <origin>`: Custom origin header (for some scripts).
- `-p, --proxy <proxy>`: Specify the proxy parser.
- `-c, --cookie <cookie>`: Cookie session.
- `-v, --verbose <verbose>`: Verbose mode (e.g., -v 1,3).
- `-a, --all_pages`: Search for all site pages (for some scripts).
- `-w, --wordlist <wordlist>`: Wordlist file containing URLs.
- `-o, --output_file <output_file>`: Output file to save potential vulnerabilities.
- `-o, --offset <offset>`: Offset value.
- `-n, --initial_size <initial_size>`: Initial payload size.
- `-x, --step <step>`: Payload size increment step.
- `-t, --timeout <timeout>`: Timeout duration.
- `-s, --sets <sets>`: Custom pattern sets.
- `-l, --length <length>`: Pattern length.
- `-p, --prefix <prefix>`: Prefix string.

## Example Usages:
**To detect bad characters:**
```sh
python3 badchars.py -b \x00\x0a
```

**To perform a buffer overflow exploit:**
```sh
python3 exploit.py 192.168.0.1 8080 -o 1024 -p A
```

**To fuzz a target:**
```sh
python3 fuzzer.py 192.168.0.1 8080 -n 100 -x 100
```

**To create a pattern:**
```sh
python3 pattern.py -l 3000
```

**To find the offset of a pattern:**
```sh
python3 offset.py -v 386F4332 -l 3000
```

**To set up a listener:**
```sh
python3 listener.py 0.0.0.0 4444
```

**To interact with an exploited target:**
```sh
python3 interactor.py 192.168.0.1 8080 -t 5
```

For more details on usage and options, refer to the help message provided by each tool.

## Issue?
- DM me on Instagram
- If you have questions about the tool, you can add me on Instagram: [0x.ans](https://instagram.com/0x.ans)
