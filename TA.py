from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

#create button
class BuckysButton:
    def __init__(self):
        self.btn = Button(top, command = self.submit, text="SUBMIT", activebackground="green").place(x=120,y=170)

    def submit(self):
       harga=""
       if len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA")
        return
       if strnomor.get() == 0:
        messagebox.showerror("Error","BELUM MENGISI NOMOR")
        return
       if radio.get()== 0:
        messagebox.showerror("Error","BELUM MEMILIH KATEGORI")
        return
       elif radio.get() == 1:
        harga="Rp 60.000"
       elif radio.get() == 2:
        harga="Rp 100.000 "
       if strmetode.get() == 'Metode pembayaran':
        messagebox.showerror("Error","BELUM MEMILIH METODE PEMBAYARAN")
        return
       pesan = "Halo " + stringnama.get() + ", terimakasih telah memesan antrian!\nSilahkan melakukan pembayaran DP sebesar " + harga + " dengan metode pembayaran " + strmetode.get() + " dalam 1x24 jam"
       pesan1 = "Kirim bukti transfer ke nomor 08958183818 menggunakan nomor " + strnomor.get()+ ".\nJika sudah silahkan tunggu kami hubungi untuk menentukan jadwal terapi"
       messagebox.showinfo("Greeting", pesan)
       messagebox.showinfo("Greeting", pesan1)

 
top = Tk()  
b = BuckysButton()
top.geometry("300x200")
top.title("Terapi Cedera Olahraga")

#label
lbnama = Label(top, text = "Nama\t").place(x = 30,y = 10) 
lbnomor = Label(top, text = "No.Telepon\t").place(x = 30,y = 40)
lbkategori = Label(text = "Kategori\t:").place(x = 30, y=70)
lbmetode = Label(text = "Metode\t:").place(x=30, y=140)

#input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama).place(x = 110, y = 10) 
strnomor = StringVar()
inomor = Entry(top,width = 20, textvariable=strnomor).place(x = 110, y = 40) 

#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Anak-anak", variable=radio, value=1).place(x=105, y=70)  
R2 = Radiobutton(top, text="Dewasa", variable=radio, value=2).place(x=105, y=90)   

#combobox
strmetode = StringVar(value='Metode pembayaran') 
Cb = ttk.Combobox(top, width = 21, textvariable = strmetode, state="readonly")
Cb.place(x=110, y=140)

#combobox list 
Cb['values'] = ('BNI: 0178239771',
                'BRI: 099954567156731',
                'Mandiri: 0189675388462') 

top.mainloop()
