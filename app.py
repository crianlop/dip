import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
root = tk.Tk()  # create root window
root.title("Proyecto DIP")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = tk.Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

def loadPreview():
    filename = filedialog.askopenfilename()
    imagenOriginal=Image.open(filename)
    imagenOriginal.thumbnail((350,350))
    image = ImageTk.PhotoImage(imagenOriginal)
    preview.configure(image=image)
    preview.image=image
   
# Create frames and labels in left_frame
cargar=tk.Button(left_frame,text="Cargar imagen",command=loadPreview).grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
imagenOriginal=Image.open("imagen.jpg")
imagenOriginal.thumbnail((350,350))
image = ImageTk.PhotoImage(imagenOriginal)
#original_image = image.subsample(3,3)  # resize image using subsample

preview=tk.Label(left_frame,image=image)
preview.grid(row=1, column=0, padx=5, pady=5)

# Display image in right_frame
final=tk.Label(right_frame, image=image)
final.grid(row=0,column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = tk.Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
tk.Label(tool_bar, text="Aplicar ruido").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
tk.Label(tool_bar, text="Filtro de restaurado").grid(row=0, column=1, padx=5, pady=3, ipadx=10)



def aplicar():
    newImagen=preview.image
    final.configure(image=newImagen)
    final.image=newImagen



# Example labels that could be displayed under the "Tool" menu
tk.Button(tool_bar, text="Sal y pimienta",command=aplicar).grid(row=1, column=0, padx=5, pady=5)
tk.Button(tool_bar, text="Gasussiano",command=aplicar).grid(row=2, column=0, padx=5, pady=5)
tk.Button(tool_bar, text="Restaurar 1",command=aplicar).grid(row=1, column=1, padx=5, pady=5)
tk.Button(tool_bar, text="Restarurar 2",command=aplicar).grid(row=2, column=1, padx=5, pady=5)

root.bind("<Return>", loadPreview)
root.bind("<Return>", aplicar)
root.mainloop()