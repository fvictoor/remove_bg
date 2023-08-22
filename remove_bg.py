from rembg import remove
from tkinter import *
from tkinter import filedialog, messagebox
from pkg_resources import resource_filename
from PIL import Image

def btn_clicked():
    filetypes = (('All files', '*.*'), ('Image', '*.png') )
    input_path = filedialog.askopenfilename( title='Open a file', initialdir='/',filetypes=filetypes)
    print (input_path)
    
    #file = resource_filename(__name__,input_path)
    output_path = filedialog.asksaveasfilename(filetypes=filetypes)

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path+'.png')
    messagebox.showinfo(message="Background removido com sucesso!")
    
# Cria a Tela
window = Tk()
window.geometry("682x384") #Largura x Altura
window.configure(bg = "#ffffff")
window.title("Remove Background")
canvas = Canvas(window, bg = "#ffffff", height = 560, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

#Importa o icone
# Importa icone
icon_img = resource_filename(__name__,r"img\\icon.ico")
window.iconbitmap(False, icon_img)
canvas = Canvas(window, bg = "#ffffff", height = 560, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

# Importa Imagem de Backgroung
background_img = resource_filename(__name__,r"img\\background.png" )
background_img = PhotoImage(file = background_img)
background = canvas.create_image(340, 190.0, image=background_img)

# Importa o Botão
img0 = resource_filename(__name__,r"img\img0.png" )
img0 = PhotoImage(file = img0)
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0,  command = btn_clicked, relief = "flat")
b0.place( x = 225, y = 185, width = 220, height = 40)

window.resizable(False, False)
window.mainloop()


