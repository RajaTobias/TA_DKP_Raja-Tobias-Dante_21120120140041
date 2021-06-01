from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 
from collections import deque

#global variable
antrian = deque()

#create button
class BuckysButton:
    def __init__(self):
        self.btn = Button(top, background="dark salmon", command = self.submit, text="SUBMIT", activebackground="green").place(x=120,y=150)
        self.btn1 = Button(top, background="dark salmon", command = self.delete, text="RESET", activebackground="red").place(x=180,y=150)

    def submit(self):
       harga=""
       if len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA")
        return
       if len(strnomor.get()) == 0:
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
       pesan = "Halo " + stringnama.get() + ", terimakasih telah melakukan pemesanan!"
       messagebox.showinfo("Greeting", pesan)

       antrian.append(self.submit)

    
       nwindow = Toplevel(top)
       nwindow.geometry("350x300")
       nwindow.title("Status anda")
       nwindow.config(background="light blue")
       lb1= Label(nwindow, text = "Nama : " +stringnama.get(),  background = "light blue").place(x = 0,y =10)
       lb2= Label(nwindow, text = "Nomor Telepon : " +strnomor.get(),  background = "light blue").place(x = 0,y =40)
       lb3= Label(nwindow, text = "DP yang harus dibayar : " +harga,  background = "light blue").place(x = 0,y =70)
       lb4= Label(nwindow, text = "Metode pembayaran : " +strmetode.get(),  background = "light blue").place(x = 0,y =100)
       lb5= Label(nwindow, text = "Silahkan kirim bukti pembayaran ke 08958183818",  background = "light blue").place(x = 0,y =150)
       lb6= Label(nwindow, text = "menggunakan nomor yang sudah didaftarkan", background = "light blue").place(x = 0,y =170)
       lb7= Label(nwindow, text = "dalam waktu 1x24 jam.",  background = "light blue").place(x = 0,y =190)
       lb8= Label(nwindow, text = "Setelah itu kami akan menghubungi anda",  background = "light blue").place(x = 0,y =210)
       lb9= Label(nwindow, text = "untuk menentukan jadwal terapi",  background = "light blue").place(x = 0,y =230)
       lb10= Label(nwindow, text = "Nomor antrian anda : " + str(len(antrian)),  background = "light blue").place(x = 0,y =250)
       lb11= Label(nwindow, text = "TERIMAKASIH",background="green").place(x = 120, y = 275)

    def delete(self):
        stringnama.set("")
        strnomor.set("")
        radio.set(0)
        strmetode.set("Metode pembayaran")



     
top = Tk()  
b = BuckysButton()
top.config(background="antique white")
top.geometry("300x210")
top.title("Terapi Cedera Olahraga")


#label
lbnama = Label(top, background="antique white",text = "Nama\t").place(x = 30,y = 10) 
lbnomor = Label(top, background="antique white", text = "No.Telepon\t").place(x = 30,y = 40)
lbkategori = Label(background="antique white", text = "Kategori\t:").place(x = 30, y=70)
lbmetode = Label(background="antique white", text = "Metode\t:").place(x=30, y=120)
notif = Label(top, background="antique white", text="",fg="red")
notif.place(x=110, y=180 )


#input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama).place(x = 110, y = 10) 
strnomor = StringVar()
inomor = Entry(top,width = 20, textvariable=strnomor).place(x = 110, y = 40) 

#create radio
radio = IntVar()
R1 = Radiobutton(top, background="antique white",text="Anak-anak (<18 tahun)", variable=radio, value=1).place(x=105, y=70)  
R2 = Radiobutton(top, background="antique white",text="Dewasa (≥18 tahun)", variable=radio, value=2).place(x=105, y=90)   

#combobox
strmetode = StringVar(value='Metode pembayaran') 
Cb = ttk.Combobox(top, width = 21, textvariable = strmetode, state="readonly")
Cb.place(x=110, y=120)

#combobox list 
Cb['values'] = ('BNI(0178239771)',
                'BRI(099954567156731)',
                'Mandiri(0189675388462)')

top.mainloop()
