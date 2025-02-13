import customtkinter as ctk
import os
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from boxmessages import validate_fields, show_warning, validate_date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from template import my_temp
from textwrap import wrap

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("green")  

my_w = ctk.CTk()
my_w.geometry("1280x720+0+0")
my_w.title('Proposta de Serviço Efatá Eventos')
my_w.grid_rowconfigure(0, weight=1)
my_w.grid_columnconfigure(1, weight=1)


# load images with light and dark mode image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "efata_bgd.png")), size=(160, 150))
proposta_image = ctk.CTkImage(Image.open(os.path.join(image_path, "ps.png")), size=(480, 160))
client_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(30, 30))
date_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "calendar.png")), size=(30, 30))
service_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "service.png")), size=(30, 30))
value_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "dollars.png")), size=(30, 30))
add_service_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "add.png")), size=(35, 30))
home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))


# create navigation frame
navigation_frame = ctk.CTkFrame(my_w, corner_radius=0, fg_color="gray95")
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(4, weight=1)

navigation_frame_label = ctk.CTkLabel(navigation_frame, text="", image=logo_image, compound="center")
navigation_frame_label.grid(row=0, column=0, padx=0, pady=0)

def change_appearance_mode_event(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)
        
def home_button_event():
    select_frame_by_name("Início")

# def frame_2_button_event():
#     select_frame_by_name("Observações")


home_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Início",	
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=home_image, anchor="w", command=home_button_event)
home_button.grid(row=1, column=0, sticky="ew")


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

client = ctk.StringVar(value='Jovem Pan')
date = ctk.StringVar(value='')
service_value = ctk.StringVar(value='1000')
services = []
s_filename = ''

home_frame_propose_image_label = ctk.CTkLabel(home_frame, text="", image=proposta_image)
home_frame_propose_image_label.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

# Cliente
l1 = ctk.CTkButton(home_frame, text='Cliente', image=client_icon, compound="right", height=35, font=("Helvetica", 20), 
                   fg_color="gray85", text_color="gray30", hover_color="gray75")
l1.grid(row=1, column=0, padx=10, pady=0, sticky='e')
e1 = ctk.CTkEntry(home_frame, font=("Helvetica", 22), width=600, validate='focusout', height=35, textvariable=client)  # Aumentar largura
e1.grid(row=1, column=1, padx=10, pady=0, sticky='ew')

# Data
l2 = ctk.CTkButton(home_frame, text='Data', image=date_icon, compound="right", height=35, font=("Helvetica", 20), 
                   fg_color="gray85", text_color="gray30", hover_color="gray75")
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
l3 = ctk.CTkButton(home_frame, text='Serviços', image=service_icon, compound="right", height=35, font=("Helvetica", 20), 
                   fg_color="gray85", text_color="gray30", hover_color="gray75")
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
b_add_service = ctk.CTkButton(home_frame, text='Adicionar', font=("Helvetica", 18), command=add_service, image=add_service_icon, compound="right")
b_add_service.grid(row=3, column=2, padx=0, pady=0)

# Valor total
l4 = ctk.CTkButton(home_frame, text='Valor', image=value_icon, compound="right", height=35, font=("Helvetica", 20), 
                   fg_color="gray85", text_color="gray30", hover_color="gray75")
l4.grid(row=4, column=0, padx=10, pady=0, sticky='e')
e4 = ctk.CTkEntry(home_frame, font=("Helvetica", 22), textvariable=service_value, width=150, validate='focusout')  # Aumentar largura
e4.grid(row=4, column=1, padx=10, pady=0, sticky='w')


def on_generate():
    if not validate_fields(client, date, service_value):
        if not show_warning("Campos Vazios", "Alguns campos estão vazios ou incorretos. Deseja prosseguir?"):
            return
        
    client_name = client.get()
    
    default_filename = f"proposta_servico_{client_name}.pdf"

    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=default_filename)
    if not file_path:
        return  # Se o usuário cancelar, não fazer nada
    
    # Function to draw wrapped text
    def draw_wrapped_text(c, text, x, y, max_width, line_height):
        lines = wrap(text, width=max_width)
        for line in lines:
            c.drawString(x, y, line)
            y -= line_height

    c = canvas.Canvas(file_path, bottomup=1, pagesize=letter)
    c = my_temp(c)  # run the template

    # Adicionar dados coletados
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 10)
    c.drawString(1.83*inch, 7.5*inch, client.get())
    c.drawString(1.11*inch, 6.1*inch, date.get())

    # Desenhar serviços com pontos de bala
    y_position = 5.8 * inch
    for service in services:
        draw_wrapped_text(c, f"• {service}", 0.4*inch, y_position, 80, 12)
        y_position -= 0.3 * inch

    c.drawString(3.5*inch, 4.5*inch, service_value.get())
    c.showPage()
    c.save()
    services.clear()
    messagebox.showinfo("PDF Gerado", "O PDF foi gerado com sucesso!")
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
    #frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Observações" else "transparent")

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