#!/usr/bin/env python3
from TikTokApi import TikTokApi
from converter import Converter
import argparse
import time
import os

def downloadTikTok(url):
    api = TikTokApi()
    data = api.getTikTokByUrl(url)
    return api.get_Video_By_DownloadURL(data['itemInfo']['itemStruct']['video']['downloadAddr'])

def convertToWebM(video, args):
    conv = Converter()
    with open('temp.mp4', 'wb') as out:
        out.write(video)

    options = {
        'format': 'webm',
        'video': {
            'codec': 'vp8',
            'quality': args.quality,
            'max_bitrate': args.bitrate,
            'width': args.width,
            'height': -2
    }}
    if (args.audio):
        options['audio'] = {'codec': 'vorbis'}
    convert = conv.convert('temp.mp4', str(int(time.time()))+'.webm', options)

    for timecode in convert:
        print(f'\rConverting to WebM ({int(timecode*100)}%)', end =' ')
    print('\rConverting to WebM (100%)')

    if os.path.exists('temp.mp4'):
        os.remove('temp.mp4')
    
def main(args):
    for url in args.url:
        convertToWebM(downloadTikTok(url), args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='+', help='The URLs of the Tik Tok. Accept multiple URLs')
    parser.add_argument('-a', '--audio', action="store_true", help='Enables audio for the WebM')
    parser.add_argument('-q', '--quality', type=int, help='Quality of the webm. From 4 (best) to 63 (worst). Defaults to 20.')
    parser.add_argument('-b', '--bitrate', type=int, help='Bitrate. From 16 (min) to 15000 (max). Defaults to 1000.')
    parser.add_argument('-w', '--width', type=int, help='Width (in pixels) of the WebM')
    args = parser.parse_args()
    if args.quality is None:
        args.quality = 20
    if args.bitrate is None:
        args.bitrate = 1000
    if args.width is None:
        args.width = 0
    main(args)
