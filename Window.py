# import tkinter as tk
import tkinter

window = tkinter.Tk()

window.geometry("500x500")
window.resizable(False, False)
window.title("CS 452 Dynamic Memory Allocation Project")
# window = tk.Tk()

# lbl_header = tkinter.Label(text="CS 452 Dynamic Memory Allocation Project")
# lbl_header.place(x=1, y=1)


# lbl_header.pack()


frm_info = tkinter.Frame(window, width=100, height=300, bg="blue")
frm_info.place(x=1, y=100)

lbl_process_size = tkinter.Label(
    master=frm_info, text="Next Process Size to be allocated:")
lbl_process_size.place(x=10, y=10)


# frm_info = tkinter.Frame(window, width=200, height=100, bg="red")

# frm_info.place(100, 100)


# frm_memory_first_fit = tk.Frame(highlightbackground="black", highlightthickness=1,
#                                 master=window, width=200, height=100, bg="green")
# frm_memory_first_fit.pack()

# lbl_first_fit = tk.Label(frm_memory_first_fit, text="First Fit").pack()
# # frm_memory_first_fit.pack()

# frm_memory_best_fit = tk.Frame(
#     master=window, width=200, height=100, bg="yellow")
# frm_memory_best_fit.pack()

# frm_memory_worst_fit = tk.Frame(
#     master=window, width=200, height=100, bg="blue")
# frm_memory_worst_fit.pack()

window.mainloop()
