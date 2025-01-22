from reportlab.lib.units import inch
def my_temp(c):
    c.translate(inch,inch)
    c.drawImage('efata.jpg', 2.5*inch, 8*inch, width=100, height=90) # image file 
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0, 7.5*inch, "PROPOSTA DE SERVIÇO – ")
    #####
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0, 7*inch, "EFATÁ EVENTOS") 
    
    ######
    c.setFont("Helvetica", 10)
    c.drawString(0, 6.8*inch, "CNPJ: 47.284.248/0001-95")
    c.drawString(0, 6.6*inch, "Sede: Rua Álvaro Jose Da Costa, Nº 517, Fazendinha, CEP 81.330-460, Curitiba - PR")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0, 6.1*inch, "SERVIÇO PARA ")
    c.drawString(1.8*inch, 5*inch, "VALOR TOTAL: R$")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(2*inch, 2*inch, "FORMAS DE PAGAMENTO:")
    c.setFont("Helvetica", 10)
    c.drawString(2*inch, 1.8*inch, "PIX")
    c.drawString(2*inch, 1.6*inch, "CARTÃO DE CRÉDITO")
    c.drawString(2*inch, 1.4*inch, "FATURADO(Negociável)")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(2*inch, 1*inch, "CONTATO:") 
    c.setFont("Helvetica", 10)
    c.drawString(2*inch, 0.8*inch, "Instagram: @eventos.efata")
    c.drawString(2*inch, 0.6*inch, "Email: eventos.efata@hotmail.com")
    c.drawString(2*inch, 0.4*inch, "Telefone: (41) 98512-2438")
       
 
    return c