from __future__ import unicode_literals
import youtube_dl

song = input("link: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': 'C:\\Users\\Saniel\\Desktop\\%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([song])