from reportlab.pdfgen import canvas
import tkinter as tk
from reportlab.lib.pagesizes import letter, A4

my_path='PROPOSTA-DE-SERVICO.pdf' # update the path 
from reportlab.lib.units import inch

from template import my_temp # import the template
from input_data import client,date,service,service_value #tkinter

## comment below values if you are using above Tkinter window
#s_filename='D:\\images\\rabbit_face2.jpg'

c = canvas.Canvas(my_path, bottomup=1, pagesize=letter)
c=my_temp(c) # run the template
#c.drawImage(s_filename,2.2*inch,0.7*inch) #Add image

###### Adding Collected data ####
c.setFillColorRGB(0,0,1)
c.setFont("Helvetica", 10)
c.drawString(1.83*inch, 7.5*inch,client.get())
c.drawString(1.11*inch, 6.1*inch,date.get())    
c.drawString(1.5*inch, 5.8*inch,service.get())    
c.drawString(3.1*inch,5*inch,service_value.get())    
######
c.showPage()
c.save()