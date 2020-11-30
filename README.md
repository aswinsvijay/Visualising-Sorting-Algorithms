# Visualising Sorting Algorithms

Sorting algorithms visualised using bar graph with pygame module.

The environment can be tweaked by modifying the `config.py` file.
* `w,h` - width and height of the window
* `fps` - frame rate of the animation, use 0 for interactive mode
* `n` - number of elements in the list to sort.

The default parameters are read from `config.py`. Using command line arguments will override these parameters.  
If the positional argument for sort algorithm is not specified, a menu is presented followed by a prompt to choose the required algorithm.  
For more help use `python3 main.py --help` (replace `python3` with the python binary that is installed on your system)  