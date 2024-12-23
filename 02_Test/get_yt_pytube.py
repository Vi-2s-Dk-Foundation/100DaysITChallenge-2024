from pytube import Playlist, YouTube

p = Playlist("https://www.youtube.com/playlist?list=PLcTyOFH6d6WJhDvlOmVDSBjD18P_EmHzf")

print(f'Downloading: {p.title}')
print(f"Number of videos: {p.length}")

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#print(yt.title)
print(yt.thumbnail_url)

videos = p.videos

videos = []
for video_url in p.video_urls:
    yt = YouTube(video_url)
    print(type(yt))
    print(yt)
    video_info = {
#        'title': yt.title,
        'description': yt.description,
#        'length': yt.length,
        'url': video_url
    }
    videos.append(video_info)

print(*videos)
