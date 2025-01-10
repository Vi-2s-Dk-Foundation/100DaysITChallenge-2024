from googleapiclient.discovery import build
import csv

# Replace with your actual API key
API_KEY = "AIzaSyCdiK4Pai6473NsIvIL8pnRbkeRD-qFMI4" 

def get_playlist_videos(playlist_id):
  """
  Fetches details of videos in a YouTube playlist using the Data API v3.

  Args:
    playlist_id: The ID of the YouTube playlist.

  Returns:
    A list of dictionaries, where each dictionary represents a video in the playlist
    and contains details like title, description, publishedAt, and duration.
  """

  youtube = build('youtube', 'v3', developerKey=API_KEY)

  request = youtube.playlistItems().list(
      part="snippet,contentDetails",  # Include contentDetails for duration
      playlistId=playlist_id,
      maxResults=50  # Adjust as needed
  )

  videos = []
  while request:
    response = request.execute()

    for item in response['items']:
      print(item)
      videos.append(item)
    #   video = {
    #       'title': item['snippet']['title'],
    #       'description': item['snippet']['description'],
    #       'publishedAt': item['snippet']['publishedAt'],
    #       'duration': item['contentDetails']['duration']  # Extract duration
    #   }
    #   videos.append(video)

    request = youtube.playlistItems().list_next(
        previous_request=request, previous_response=response
    )

  return videos

# Example usage
playlist_id = "PLcTyOFH6d6WIByisZGI1s2MYZOhAolu1s" 
playlist_videos = get_playlist_videos(playlist_id)

# Write data to CSV file
# with open('playlist_videos.csv', 'w', newline='') as csvfile:
#   fieldnames = ['Title', 'Description', 'Published At', 'Duration']
#   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#   writer.writeheader()
#   writer.writerows(playlist_videos)

# print("Video details saved to 'playlist_videos.csv'")