# BurpSuite Logs Cleaner

Use this script to remove any out of scope requests from Burp Suite log file.

## Requirements

Python v3.x+

## Usage

```bash
Usage:  python parse_burp_logs.py -i /tmp/Burp.log -s google.com -o /tmp/cleaned_Burp.log

Options:
  -h, --help      show this help message and exit
  -i INPUT_FILE   BurpSuite Log file
  -s SCOPE        Scope e.g. www.google.com
  -o OUTPUT_FILE  Parsed BurpSuite Log file output
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
