from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt


def plot(tags, mask_filename, ):
    data = ' '.join(tags)
    mask = imread(mask_filename, flatten=True)
    word_cloud = WordCloud(
        width=720,
        height=720,
        background_color='white',
        font_path='微软雅黑.ttc',
        mask=mask
    ).generate(data)
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.imsave()
