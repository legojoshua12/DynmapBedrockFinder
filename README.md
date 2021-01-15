# DynmapBedrockFinder
 A bedrock pillar locator using the dynmap plugin. Designed for civilizationcraft trade goodie location quickly.
## Required Libraries
 - Opencv
 - OS
 - Numpy
 - Pillow
 - Requests
 
## How to use
To configure for proper use, use the config file in the src directory to edit the range of the search as well as the link for the dynmap pull from source. As long as the tiles follow the same link format, the script will pull and merge all the searched image tiles into one large image.

## Todo
Add more efficient recognition algorithm for higher accuracy and quicker recognition time
 - Check out this example: https://github.com/EdjoLabs/image-match