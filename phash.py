"""
Author: Anastasia Kriuchkovska
E-mail: staceyhooks0@gmail.com

This is an implementation of PHash algorithm for computing image hash.

    The algorithm has next steps:

    1. Reducing size and color of a given image to 32x32 resolution.This is done to simplify the DCT calculation and other computations.
    2. Applying Discrete Cosinus Transform (DCT). Like in JPEG, here DCT separates the image into frequencies and scalars
    3. Reducing DCT result. Making it from 32x32 to 8x8 by keeping top-left 8x8 square. This square is a representation of the lowest frequencies of the image.
    4. Computing the median value from 8x8 DCT result 
    5. Getting binary hash. Here we set the 64 hash bits to 0 or 1 depending on whether each of the 64 DCT values is above or below the median value. 
        The result represents rough relative scale of the frequencies to the median value. If the structure of the image changes a bit, the result will not vary

"""

import math
from PIL import Image
import numpy as np


class PHash:
    def __init__(self):
        self.size = 32
        self.hash_size = 8
        self.coefs = self.__init_coefs()

    def __init_coefs(self):
        coef = []
        for i in range(32):
            coef.append(1)

        coef[0] = 1 / math.sqrt(2)
        return coef


    def get_hash(self, image: Image):
        image_gray = image.convert("L").resize((self.size, self.size), Image.ANTIALIAS)
        
        pixels = np.asarray(image_gray)
        print("Applying DCT...")
        dct_values = self.__dct(pixels)
        binary_hash_np = self.__get_binary_hash(dct_values)
        
        return binary_hash_np

    def __dct(self, input_vals):
        res = np.ones(shape=(self.size, self.size))
        
        for u in range(self.size):
            for v in range(self.size):
                sum = 0.0
                for i in range(self.size):
                    for j in range(self.size):
                        dct_part = self.__compute_dct_part(u, v, i, j, input_vals[i][j])
                        sum += dct_part
                sum *= (self.coefs[u] * self.coefs[v]) / 4.0
                
                
                res[u][v] = float(sum)
        return res

    def __compute_dct_part(self, u, v, i, j, input_value):
        result = (
            math.cos(((2 * i + 1) / (2.0 * self.size)) * u * math.pi)
            * math.cos(((2 * j + 1) / (2.0 * self.size)) * v * math.pi)
            * input_value
        )
        return result

    def __get_binary_hash(self, dct_result):
        dct_low = dct_result[:self.hash_size, :self.hash_size]
        med = np.median(dct_low)
        diff = dct_low>med
        return diff

 

    # def _binary_array_to_hex(arr):
    #     """
    #     internal function to make a hex string out of a binary array.
    #     """
    #     bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    #     width = int(numpy.ceil(len(bit_string)/4))
    #     return '{:0>{width}x}'.format(int(bit_string, 2), width=width)



