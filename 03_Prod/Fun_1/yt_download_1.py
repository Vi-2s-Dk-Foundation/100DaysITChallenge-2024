from pytube import YouTube
from tqdm import tqdm 

def download_video(url):
  try:
    yt = YouTube(url)
    #print(f"Downloading: {yt.title}")

    # Get highest resolution video stream
    stream = yt.streams.get_highest_resolution() 

    # Download with progress bar using tqdm
    with tqdm(total=stream.filesize, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
      stream.download(chunk_size=1024, callback=lambda s, c, b: pbar.update(c))

    print(f"Download complete.")

  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  video_url = input("Enter the YouTube video URL: ")
  download_video(video_url) # https://www.youtube.com/watch?v=bA0bfVGMTCE