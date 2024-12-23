from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_youtube_channel(channel_url):
    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
    driver.get(channel_url)

    # Scroll down to load more videos (adjust the scroll count as needed)
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    videos = soup.find_all('ytd-video-renderer')

    video_data = []
    for video in videos:
        title = video.find('a', id='video-title').text.strip()
        description = video.find('yt-formatted-string', id='description-text').text.strip()
        duration = video.find('span', id='video-time').text.strip()
        url = video.find('a', id='video-title')['href']
        video_data.append({
            'title': title,
            'description': description,
            'duration': duration,
            'url': 'https://www.youtube.com' + url
        })

    return video_data

# Replace with the actual channel URL
channel_url = "https://www.youtube.com/channel/UCUqY7E3BYnQiv8LCUPn8nMw"


# API_KEY = "AIzaSyCdiK4Pai6473NsIvIL8pnRbkeRD-qFMI4"
# channel_id = UCUqY7E3BYnQiv8LCUPn8nMw

video_data = scrape_youtube_channel(channel_url)

# Print the extracted data
for video in video_data:
    print(video)