Tik tok now requires to be logged in in order to download videos, so this script doesn't currently work. Let me know if you're interested in a fix.

# tiktok2webm
Downloads Tik Toks from urls and converts them to WebMs. Written for 4chan. Can create both soundless and with sound WebMs

# Setup
## Cross platform
Requires ffmpeg to be installed. Also required some python modules to be installed
```
$ pip install -r requirements.txt
```
The script can then be ran from the CLI
```
python3 tiktok2webm.py URL 
```
The first run might take a while.

## Compiled Windows binary
A Windows binary is provided, and with it isn't necessary to setup a Python environment. It still requires ffmpeg to be installed.

Open `cmd.exe` and execute 
```
tiktok2webm.exe URL 
```
You can also drag and drop the `.exe` in the terminal, but please note that the WebMs will be downloaded in the folder your terminal is open in.

# Usage
```
$ python3 tiktok2webm.py --help
usage: tiktok2webm.py [-h] [-a] [-q QUALITY] [-b BITRATE] [-w WIDTH] url [url ...]

positional arguments:
  url                   The URL of the Tik Tok

optional arguments:
  -h, --help            show this help message and exit
  -a, --audio           Enables audio for the WebM
  -q QUALITY, --quality QUALITY
                        Quality of the webm. From 4 (best) to 63 (worst). Defaults to 20.
  -b BITRATE, --bitrate BITRATE
                        Bitrate. From 16 (min) to 15000 (max). Defaults to 1000.
  -w WIDTH, --width WIDTH
                        Width (in pixels) of the WebM
```

You can play with the quality/bitrate/image size to adjust the file size.

Multiple Tik Toks can be downloaded by providing multiple ULRs at once.
