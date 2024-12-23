import requests
from bs4 import BeautifulSoup

def get_channel_data(channel_url):
  """Fetches details about playlists and videos from a YouTube channel using direct HTTP requests.

  Args:
      channel_url: The URL of the YouTube channel.

  Returns:
      A dictionary containing playlist and video information.
  """

  response = requests.get(channel_url)
  soup = BeautifulSoup(response.text, 'html.parser')

  # Find the h1 element
  h1_element = soup.find('h1')

  channel_title = h1_element

  playlists = []
  for playlist in soup.find_all('ytd-playlist-renderer'):
      playlist_title = playlist.find('a', id='title-text').text.strip()
      playlist_url = playlist.find('a', id='title-text')['href']
      playlist_details = get_playlist_videos(playlist_url)
      playlists.append({
          'title': playlist_title,
          'url': playlist_url,
          'videos': playlist_details['videos']
      })

  return {
      'channel_title': channel_title,
      'playlists': playlists
  }

def get_playlist_videos(playlist_url):
  """Fetches details about videos in a YouTube playlist using direct HTTP requests.

  Args:
      playlist_url: The URL of the YouTube playlist.

  Returns:
      A dictionary containing a list of video details.
  """

  response = requests.get(playlist_url)
  soup = BeautifulSoup(response.text, 'html.parser')

  videos = []
  for video in soup.find_all('ytd-video-renderer'):
      video_title = video.find('a', id='video-title').text.strip()
      video_url = video.find('a', id='video-title')['href'].split('=')[1]  # Extract video ID from URL
      video_description = video.find('yt-formatted-string', id='description-text').text.strip()

      # **Extracting Thumbnail (Less Reliable):**
      # This method constructs a common thumbnail URL, but it might not always be accurate.
      thumbnail_url = "https://i.ytimg.com/vi/" + video_url + "/default.jpg"

      # **Extracting Duration (More Complex):**
      # Duration might require advanced techniques like JavaScript execution or analyzing video details.

      videos.append({
          'title': video_title,
          'url': video_url,  # Use video ID for better URLs
          'description': video_description,
          'thumbnail_url': thumbnail_url,
          'duration': None  # Placeholder for duration (requires further processing)
      })

  return {
      'playlist_title': soup.find('h1', id='title').text.strip(),  # Get playlist title within the playlist page
      'videos': videos
  }

# Replace with the actual YouTube channel URL
channel_url = "https://www.youtube.com/channel/UCUqY7E3BYnQiv8LCUPn8nMw"

channel_data = get_channel_data(channel_url)

print(channel_data)