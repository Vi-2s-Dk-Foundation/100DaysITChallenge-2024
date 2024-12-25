from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the Christmas tree image mask
tree_mask = np.array(Image.open("christmas-tree.png"))  # Replace "christmas_tree.png" with the actual path

# Prepare the text data
names = """
Jingle Bells
Silent Night
Deck the Halls
We Wish You a Merry Christmas
The Twelve Days of Christmas
Frosty the Snowman
Rudolph the Red-Nosed Reindeer
Nativity
Jesus
Mary
Joseph
Angels
Wise Men
Bethlehem
Christmas
Holidays
Festive
Cheerful
Joyful
Merry
Happy
Peace
Love
Giving
Sharing
Traditions
Family
Friends
Celebrations
"""

# Create a WordCloud object with the Christmas tree mask
wordcloud = WordCloud(
    background_color="white",
    mask=tree_mask,
    max_words=50,
    stopwords=STOPWORDS,
    contour_width=3,
    contour_color="green",
    colormap="winter"  # Use a wintery colormap
).generate(names)

# Add some "snow" effect
def snow(image):
    """
    Adds a snow effect to the image.
    """
    from random import randint
    for _ in range(500):  # Adjust the number of snowflakes
        x = randint(0, image.shape[1])
        y = randint(0, image.shape[0])
        image[y, x] = 255  # Set pixel to white for snowflake
    return image

wordcloud.to_array()  # Convert wordcloud to numpy array
wordcloud_with_snow = snow(wordcloud)

# Display the generated image
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud_with_snow, interpolation="bilinear")
plt.axis("off")
plt.show()