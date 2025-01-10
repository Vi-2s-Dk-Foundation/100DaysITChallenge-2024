from bs4 import BeautifulSoup
import requests

def get_h1_text(url):
  """
  Fetches and returns the text content of the first <h1> element 
  found on the given webpage.

  Args:
      url: The URL of the webpage to scrape.

  Returns:
      The text content of the first <h1> element, or None if no <h1> 
      element is found.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, 'html.parser')

    h1_element = soup.find('h1')
    if h1_element:
      return h1_element.text.strip() 
    else:
      return None

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    return None

if __name__ == "__main__":
  url = "https://www.whoscored.com" 

  h1_text = get_h1_text(url)

  if h1_text:
    print(f"H1 text: {h1_text}")
  else:
    print("No <h1> element found on the page.")

# if __name__ == "__main__":
#   url = "https://www.whoscored.com/LiveScores"

#   h1_text = get_h1_text(url)

#   if h1_text:
#     print(f"H1 text: {h1_text}")
#   else:
#     print("No <h1> element found on the page.")