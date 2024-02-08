from PIL import Image
import numpy as np
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

a = np.array(Image.open('001.png'))
b = np.array(Image.open('002.png'))


Image.fromarray(a^b).save("Lemur.png")

