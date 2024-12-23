from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_youtube_playlist(playlist_url):
    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
    driver.get(playlist_url)

    # Scroll down to load more playlists (adjust as needed)
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    playlist_title = soup.find('h1', id='video-title').text.strip()
    playlist_description = soup.find('yt-formatted-string', id='description-text').text.strip()

    # Extract video information (adjust selectors as needed)
    videos = soup.find_all('ytd-playlist-video-renderer')
    video_data = []
    for video in videos:
        video_title = video.find('a', id='video-title').text.strip()
        video_url = video.find('a', id='video-title')['href']
        video_data.append({'title': video_title, 'url': video_url})

    return {
        'title': playlist_title,
        'description': playlist_description,
        'videos': video_data
    }

# Replace with the actual playlist URL
playlist_url = "https://youtube.com/playlist?list=PLcTyOFH6d6WIByisZGI1s2MYZOhAolu1s&si=2_6DBZF1bzR3KhUV"

playlist_info = scrape_youtube_playlist(playlist_url)
print(playlist_info)