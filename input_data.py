import customtkinter as ctk
import os
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from boxmessages import validate_fields, show_warning, validate_date

ctk.set_appearance_mode("light")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

my_w = ctk.CTk()
my_w.geometry("1280x720")
my_w.title('Proposta de Serviço Efatá Eventos')
my_w.grid_rowconfigure(0, weight=1)
my_w.grid_columnconfigure(1, weight=1)

# load images with light and dark mode image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

# create navigation frame
navigation_frame = ctk.CTkFrame(my_w, corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(4, weight=1)

navigation_frame_label = ctk.CTkLabel(navigation_frame, text="  Image Example", image=logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

def change_appearance_mode_event(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)
        
def home_button_event():
    select_frame_by_name("Início")

def frame_2_button_event():
    select_frame_by_name("Observações")


appearance_mode_menu = ctk.CTkOptionMenu(navigation_frame, values=["Light", "Dark"],
                                                                command=change_appearance_mode_event)
appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

home_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Início",	
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=home_image, anchor="w", command=home_button_event)
home_button.grid(row=1, column=0, sticky="ew")

frame_2_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Observações",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=chat_image, anchor="w", command=frame_2_button_event)
frame_2_button.grid(row=2, column=0, sticky="ew")


# create home frame
home_frame = ctk.CTkFrame(my_w, corner_radius=0, fg_color="transparent")
home_frame.grid(row=0, column=0, sticky="nsew")
home_frame.grid_columnconfigure(0, weight=1)
home_frame.grid_columnconfigure(1, weight=3)  # Aumentar o peso da coluna do meio
home_frame.grid_columnconfigure(2, weight=1)
home_frame.grid_rowconfigure(0, weight=1)
home_frame.grid_rowconfigure(1, weight=1)
home_frame.grid_rowconfigure(2, weight=1)
home_frame.grid_rowconfigure(3, weight=1)
home_frame.grid_rowconfigure(4, weight=1)
home_frame.grid_rowconfigure(5, weight=1)

client = ctk.StringVar(value='')
date = ctk.StringVar(value='')
service_value = ctk.StringVar(value='')
services = []
s_filename = ''


# Cliente
l1 = ctk.CTkButton(home_frame, text='Cliente', image=add_user_image, compound="right", height=35, font=("Helvetica", 20))
l1.grid(row=1, column=0, padx=10, pady=0, sticky='e')
e1 = ctk.CTkEntry(home_frame, font=("Helvetica", 22), width=600, validate='focusout', height=35, textvariable=client)  # Aumentar largura
e1.grid(row=1, column=1, padx=10, pady=0, sticky='ew')

# Data
l2 = ctk.CTkButton(home_frame, text='Data', image=add_user_image, compound="right", height=35, font=("Helvetica", 20))
l2.grid(row=2, column=0, padx=10, pady=0, sticky='e')

def on_validate_date(P):
    if not validate_date(P):
        messagebox.showerror("Data Inválida", "Por favor, insira uma data válida no formato DD/MM/AAAA.")
        return False
    return True

vcmd_date = (home_frame.register(on_validate_date), '%P')
e2 = DateEntry(home_frame, font=("Helvetica", 22), textvariable=date, width=10, date_pattern='dd/mm/yyyy', validate='focusout', validatecommand=vcmd_date)  # Aumentar largura
e2.grid(row=2, column=1, padx=10, pady=0, sticky='w')


# Serviço
l3 = ctk.CTkButton(home_frame, text='Serviços', image=add_user_image, compound="right", height=35, font=("Helvetica", 20))
l3.grid(row=3, column=0, padx=10, pady=0, sticky='e')
e3 = ctk.CTkTextbox(home_frame, font=("Helvetica", 22), width=600, height=5)  # Aumentar largura e altura
e3.grid(row=3, column=1, padx=10, pady=0, sticky='ew')

def add_service():
    service_text = e3.get("1.0", ctk.END).strip()
    if service_text:
        services.append(service_text)
        e3.delete("1.0", ctk.END)
        messagebox.showinfo("Serviço Adicionado", "Serviço adicionado com sucesso!")

# Botão para adicionar serviço
b_add_service = ctk.CTkButton(home_frame, text='Adicionar Serviço', font=("Helvetica", 22), command=add_service)
b_add_service.grid(row=3, column=2, padx=0, pady=0)

# Valor total
l4 = ctk.CTkButton(home_frame, text='Valor Total', image=add_user_image, compound="right", height=35, font=("Helvetica", 20))
l4.grid(row=4, column=0, padx=10, pady=0, sticky='e')
e4 = ctk.CTkEntry(home_frame, font=("Helvetica", 22), textvariable=service_value, width=150, validate='focusout')  # Aumentar largura
e4.grid(row=4, column=1, padx=10, pady=0, sticky='w')



def upload_file():
    global img, s_filename
    f_types = [('Jpg Files', '*.jpg')]
    s_filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=s_filename)
    b4 = ctk.CTkButton(my_w, image=img)  # using Button 
    b4.grid(row=5, column=2, columnspan=2)

def on_generate():
    if not validate_fields(client, date, service_value):
        if not show_warning("Campos Vazios", "Alguns campos estão vazios ou incorretos. Deseja prosseguir?"):
            return
    my_w.destroy()

# Botão Gerar
b2 = ctk.CTkButton(home_frame, text='Gerar', font=("Helvetica", 22), command=on_generate)
b2.grid(row=5, column=1, padx=0, pady=(0, 20))

def on_enter(event):
    event.widget.insert(ctk.INSERT, "\n")

e3.bind("<Return>", on_enter)


# create second frame
second_frame = ctk.CTkFrame(my_w, corner_radius=0, fg_color="transparent")

def select_frame_by_name(name):
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "Início" else "transparent")
    frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Observações" else "transparent")

    # show selected frame
    if name == "Início":
        home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        home_frame.grid_forget()
    if name == "Observações":
        second_frame.grid(row=0, column=1, sticky="nsew")
    else:
        second_frame.grid_forget()
    
# select default frame
select_frame_by_name("Início")

my_w.mainloop()