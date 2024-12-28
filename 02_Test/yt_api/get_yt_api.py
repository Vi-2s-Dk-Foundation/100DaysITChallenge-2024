import requests
import pandas as pd

def get_channel_videos(channel_id, api_key):
  """Fetches videos from a YouTube channel using direct HTTP requests.

  Args:
    channel_id: The ID of the YouTube channel.
    api_key: Your YouTube Data API key.

  Returns:
    A tuple of video dictionary {plalist title, playlist ID, playlist description, playlist thumbnail} and playlist ID (to use as input for the next function).
  """

  base_url = "https://www.googleapis.com/youtube/v3/search"
  params = {
      "part": "snippet",
      "channelId": channel_id,
      "key": api_key,
      "type": "playlist",
      "maxResults": 50
  }

  response = requests.get(base_url, params=params)
  data = response.json()

  #print("Checking out the items...")
  #print(data['items'])

  videos = {}
  playlist_id_list = []
  for item in data['items']:
      dict_key = item['snippet']['title']
      playlist_id_list.append(item['id']['playlistId'])
      videos[dict_key] = [item['snippet']['title'], item['id']['playlistId'], item['snippet']['description'], item['snippet']['thumbnails']['default']['url']]

  return videos, playlist_id_list

def get_playlist_videos(api_key, playlist_id, part="snippet"):
  """Fetches video details from a YouTube playlist using the YouTube Data API v3.

  Args:
      api_key: Your YouTube Data API key.
      playlist_id: The ID of the YouTube playlist.
      part: The part of the playlist item resource to retrieve (default: snippet).

  Returns:
      A list of dictionaries containing video details {ID & Title}, or an empty list if there's an error.
  """

  base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
  params = {
      "part": part,
      "playlistId": playlist_id,
      "key": api_key,
      "maxResults": 50  # Adjust this as needed (maximum is 50)
  }

  try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    
    print(data["items"])

    if "items" not in data:
      print(f"No items found for playlist ID: {playlist_id}")
      return []

    videos = []
    for item in data["items"]:
      video_id = item["snippet"]["resourceId"]["videoId"]
      title = item["snippet"]["title"]

      videos.append({
          "videoId": video_id,
          "title": title
      })

    return videos

  except requests.exceptions.RequestException as e:
    print(f"Error fetching playlist videos: {e}")
    return []

  # API_KEY = "AIzaSyCdiK4Pai6473NsIvIL8pnRbkeRD-qFMI4"
  # channel_id = UCUqY7E3BYnQiv8LCUPn8nMw

channel_id = "UCUqY7E3BYnQiv8LCUPn8nMw"
api_key = "AIzaSyCdiK4Pai6473NsIvIL8pnRbkeRD-qFMI4"

plist, pid_list = get_channel_videos(channel_id, api_key)

all_videos=[]
for each_id in pid_list:
  videos = get_playlist_videos(api_key, each_id)
  all_videos.append([videos, each_id])
#print(*videos)

for playlist in plist:
  print(playlist)

# Create a Pandas DataFrame from the playlist
df = pd.DataFrame(plist)
df_plist = df.transpose()

print(df_plist.info)
print(df_plist.head)
print(df_plist.describe)

# Write the Playlist DataFrame to a csv file
df_plist.to_csv('new_play_data.csv', index=False)

# Create a Pandas DataFrame from the videos in each playlist
df_videos = pd.DataFrame(all_videos)
#df_videos = df.transpose()

print(df_videos.info)
print(df_videos.head)
print(df_videos.describe)

# Write the DataFrame to a csv file
df_videos.to_csv('new_all_videos_data.csv', index=False)
