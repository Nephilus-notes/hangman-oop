# char = 'a'
# print(char.isalpha())
# # while a_list:
# #     print('fuck uyearh')
# #     # break

# print('I see')


import tkinter as tk

root = tk.Tk()


window_width = 600
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}'
)

# placing a label on the root window
message = tk.Label(root, text="Sup suckas")
message.pack()

root.mainloop()