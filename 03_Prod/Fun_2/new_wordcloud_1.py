from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from random import randint

# Load the Christmas tree image mask
tree_mask = np.array(Image.open("team2.png")) 

# Invert the mask (black becomes white, white becomes black)
inverted_mask = 255 - tree_mask

# Prepare the text data
names = """
Holy Venom
Krismond Studios
Content Circle K
Ole Tyme Designs
Richard Lovings
Henry Bonney
VeenaSriVenkat
Shivneri art1
eemeelyo
Furry pets Plus other funny videos
Vehicle Insights
KedeiBC Tv
Doctor Specific 💜
Therapy Dog Troy
Buzz CapitalTV
Ellen Tokpa
Ketech tube
Grand Music Events | formații nuntă București |
MarkandJu Workouts for over 40's & 50's
Crazy Life Homestead
Chidemy Gaming
Timber
m80
The World of Krish
DIGIMARKX AI
onesire
Danalache Sebastian
mara jin
Rino
Nile Nonsense
Hari Doss
tunde adeniran
Africstyle Fashion
belad2000
Dele Adeniji
Gerard T
Desta Getaw
Muhammad Fahim Anwar
don ekolson
rene fadriquela
Murat Arziman
Grigoris Mavridis
Vikash Malik
Benjamin Odenigbo
Jesper Juhl Hansen
Lali
Design Scape
Anoop S Hari
de_prince_alsina Fiftness
Praise
K D
meombe likine
Gayani Athauda
Heinrich Edimo
Arsene Denis-Gabriel
Ako Nana Kelly
Conrad
JORDAN and JAYDEN SQL
Julio Mondjeli
I futurity Buila
yasir riaz
"""

# Create a WordCloud object with the Christmas tree mask
wordcloud = WordCloud(
    # background_color="white",
    mask=tree_mask,
    max_words=200,
    stopwords=STOPWORDS,
    contour_width=3,
    repeat=True,
    contour_color="white",
    colormap="prism", 
    min_font_size=20,  
    max_font_size=25,  
).generate(names)

# Convert wordcloud to numpy array
wordcloud_array = wordcloud.to_array() 

# Get the dimensions of the wordcloud array
try:
    height, width, third = wordcloud_array.shape 
except ValueError:
    print("Error: Unexpected shape for wordcloud_array.")
    print("Shape:", wordcloud_array.shape) 

# Add snow effect
for _ in range(1500):
    x = randint(0, width - 1)
    y = randint(0, height - 1)
    wordcloud_array[y, x] = 255

# Display the generated image
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud_array, interpolation="bilinear")
plt.axis("off")
plt.show()