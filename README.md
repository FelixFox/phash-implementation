# pHash implementation

This is an implementation of pHash algorithm used to compare images in a given folder.
The project was created within RailsReactor test task 😊

# Usage

1. Clone this repo by `git clone https://github.com/FelixFox/phash-implementation`

2. Enter the `phash-implementation` folder

3. To get printed results of similar images search, type `python solution.py --path <folder with images>` in terminal.

# pHash algorithm description

The algorithm has next steps:

   1. Reducing size and color of a given image to 32x32 resolution.This is done to simplify the DCT calculation and other computations.
   
   2. Applying Discrete Cosine Transform (DCT). Like in JPEG, here DCT separates the image into frequencies and scalars
   
   3. Reducing DCT result. Making it from 32x32 to 8x8 by keeping top-left 8x8 square. This square is a representation of the lowest frequencies of the image.
   
   4. Computing the median value from 8x8 DCT result 
   
   5. Getting binary hash. Here we set the 64 hash bits to 0 or 1 depending on whether each of the 64 DCT values is above or below the median value. 
   
**The result represents rough relative scale of the frequencies to the median value. If the structure of the image changes a bit, the result will not vary**









author: Anastasiia Kriuchkovska

e-mail: staceyhooks0@gmail.com
