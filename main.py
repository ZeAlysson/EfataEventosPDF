import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from textwrap import wrap
from input_data import *

my_path = 'PROPOSTA-DE-SERVICO.pdf'  # update the path

from template import my_temp  # import the template

# Function to draw wrapped text
def draw_wrapped_text(c, text, x, y, max_width, line_height):
    lines = wrap(text, width=max_width)
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height

c = canvas.Canvas(my_path, bottomup=1, pagesize=letter)
c = my_temp(c)  # run the template

###### Adding Collected data ####
c.setFillColorRGB(0, 0, 1)
c.setFont("Helvetica", 10)
c.drawString(1.83*inch, 7.5*inch, client.get())
c.drawString(1.11*inch, 6.1*inch, date.get())

# Draw services with bullet points
y_position = 5.8 * inch
for service in services:
    draw_wrapped_text(c, f"• {service}", 0.4*inch, y_position, 80, 12)
    y_position -= 0.2 * inch

c.drawString(3.1*inch, 5*inch, service_value.get())
######
c.showPage()
c.save()