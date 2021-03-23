import tkinter as tk

window = tk.Tk()

lbl_header = tk.Label(text="CS 452 Dynamic Memory Allocation Project")
lbl_header.pack()


# frm_info = tk.Frame(master=window, width=200, height=100, bg="red")
frm_info = tk.Frame(master=window, width=200, height=100, bg="red")
frm_info.pack()

frm_memory_first_fit = tk.Frame(highlightbackground="black", highlightthickness=1,
                                master=window, width=200, height=100, bg="green")
frm_memory_first_fit.pack()

lbl_first_fit = tk.Label(frm_memory_first_fit, text="First Fit").pack()
# frm_memory_first_fit.pack()

frm_memory_best_fit = tk.Frame(
    master=window, width=200, height=100, bg="yellow")
frm_memory_best_fit.pack()

frm_memory_worst_fit = tk.Frame(
    master=window, width=200, height=100, bg="blue")
frm_memory_worst_fit.pack()

window.mainloop()
