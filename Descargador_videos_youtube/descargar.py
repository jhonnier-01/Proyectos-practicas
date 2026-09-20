import yt_dlp

url = input("Ingresa el enlace del video: ")

opciones = {
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '/home/especiales/Descargas/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'js_runtimes': {
        'deno': {'path': '/home/especiales/.deno/bin/deno'}
    },
    'extractor_args': {
        'youtube': {
            'player_client': ['web', 'mweb']
        }
    }
}

with yt_dlp.YoutubeDL(opciones) as ydl:
    ydl.download([url])

print("\n¡Descarga completada en la carpeta Descargas!")
