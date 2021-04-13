# frame-rate-enhancement

This project aims to double frame rate of given input videos, resulting in improvement of dull, slow, jerky and slideshow-like appearance of low frame rate videos. Program produces an intermediate frame between two original consequitive frames by making approximations of motion difference between these. 

## Technologies Used

- Frame Interpolation
- Dense Optical Flow
- Inpainting
- OpenCV
- Python

This program is developed using Dense Optical Flow Techniques. The missing-valued pixel problem is occured in the pixels entering the scene for the first time - which mostly occur in borders. This problem occurred because of objects / object parts that did not exist in the
the previous frame could not be predicted by the frame interpolating function. To fix this problem temporarily, inpainting techniques used to fill empty pixels with values. 


## Launch and Run
Program is a Python program and can be compiled at any Python development environment. The "Paris - 8132.mp4" file must be in the same directory with the program in order to work with example input file and see the results. The output of the program will be saved as "Paris - 8132_enhanced_DEMO.mp4" under the same directory with input file similar with the video in the repository.Different input videos can be used by changing the video name in the related code segment.

## Preview of Program
Original
![alt text](https://github.com/isilsukorkmaz/frame-rate-enhancement/blob/main/original.gif "Original")

Enhanced
![alt text](https://github.com/isilsukorkmaz/frame-rate-enhancement/blob/main/enhanced.gif "Enhanced")

Results and generated frames can be found at [Drive link](https://drive.google.com/drive/u/0/folders/1J_XbfNyOSfYFTetqcm-HAedSk4tgoZ7V).
