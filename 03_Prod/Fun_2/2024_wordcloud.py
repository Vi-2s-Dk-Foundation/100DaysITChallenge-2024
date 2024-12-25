from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the Christmas tree image mask
tree_mask = np.array(Image.open("christmas-tree.png")) 

# Prepare the text data
text = """
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
    max_words=100,
    stopwords=STOPWORDS,
    contour_width=3,
    contour_color="red",
    min_font_size=8,
).generate(text)

# Create a color function
image_colors = ImageColorGenerator(tree_mask) 

# Apply the color function to the wordcloud
wordcloud.recolor(color_func=image_colors)

# Display the generated image
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()