
# Re-direct Python print output to pop-up window

The code in this repository adapts [a way](https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget) to redirect output from Python print statements to a pop-up window using the [Tcl/Tk](https://www.tcl.tk/) [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) framework, which is accessed through the Python package [*tkinter*](https://docs.python.org/3/library/tkinter.html).

If it is run in a terminal, the code will produce print statements in both the terminal and in the pop-up window.

All the Python packages used in the code are included in the Python standard library, so the code should work with any recent version of Python.  An Anaconda environment is included in case one has any problems running it.

## Run with Anaconda

In the *src* directory, you can [run these commands](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html):

```code
conda env create -f environment.yml

conda activate py3_11

python redirect_print.py
```
