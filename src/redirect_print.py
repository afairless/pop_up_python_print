
import sys
import time
from time import sleep
import tkinter as tk


def tkinter_textbox(
    font_type: str='texgyreheros', font_size: int=12, font_style: str='bold'
    ) -> tk.Tk:
    """
    Creates a tkinter GUI window with a textbox that receives and prints output 
        from any print statements
    The window has a button that lets the user close the window

    This function can be called as:

        root = tkinter_textbox()

    To include output from print statements in a loop, one can include this 
        line in the loop:

        root.update()


    Adapted from:
        https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget
    """

    # having 3 levels of nested functions is convoluted, but the function 
    #   'copy_redirect_print' needs to be in the same scope as the variable
    #   'textbox'
    def copy_redirect_print(func):
        def inner(input_str):
            try:
                textbox.insert(tk.END, input_str)
                textbox.see('end')
                # textbox.see(tk.END)
                return func(input_str)
            except:
                return func(input_str)
        return inner

    sys.stdout.write = copy_redirect_print(sys.stdout.write)

    root = tk.Tk()
    font_tuple = (font_type, font_size, font_style)
    textbox = tk.Text(root, font=font_tuple)
    textbox.pack()
    button1 = tk.Button(
        root, text='Close', font=font_tuple, command=root.destroy)
    button1.pack()

    return root


def main():

    root = tkinter_textbox()

    a_list = ['meow', 'moo', 'bark', 'quack', 'oink']
    for i in range(len(a_list)):
        print(a_list[i])
        root.update()
        sleep(0.2)

    for i in range(20):
        print(i)
        root.update()

    print(f'meow now {time.ctime(time.time())}')

    root.mainloop()


if __name__ == '__main__':
    main()
