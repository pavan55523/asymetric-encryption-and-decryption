from tkinter import *
from tkinter import messagebox
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
from random import randint
from PIL import ImageTk, Image
import yagmail


# creating root object
root = Tk()

# defining size of window
root.geometry("1350x680")
C = Canvas(root, bg="white", height=100, width=1000)
C.grid(row=1,column=1)
filename = ImageTk.PhotoImage(Image.open("123.jpg"))
background_label = Label(root, image=filename,width=1350,height=680)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# setting up the title of window
root.title("MED:A NEW MODEL FOR MESSAGE ENCRIPTION AND DECRIPTER USING ALIEN KEY")
Tops = Frame(root, width = 1800, relief = SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, width = 2520, height = 2500,relief = SUNKEN)
f1.pack(side = TOP)
lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),
text = "Message Encrypter and Decrypter",
fg = "Black",bg = "white" , bd = 10, anchor='w')
lblInfo.grid(row = 0, column = 0)


rand = StringVar()
sand = StringVar()
spass = StringVar()
Sub = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
enc= StringVar()
kdec=StringVar()

# Function to reset the window
def Reset():
    rs=messagebox.askokcancel("RESET ???","Are you sure?")
    if rs==True:
        rand.set("")
        Sub.set("")
        Msg.set("")
        sand.set("")
        spass.set("")
        key.set("")
        mode.set("")
        Result.set("")
        enc.set("")
        kdec.set("")
        z=0
#reciver mail id
recievermail= Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Reciever mail id:",bd = 16,anchor = "w")
recievermail.grid(row = 1, column = 0)
txtMail= Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = rand, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtMail.grid(row = 1, column = 1)

#sender mail id
sendermail= Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Sender mail id:",bd = 16,anchor = "w")
sendermail.grid(row = 2, column = 0)
txtMail= Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = sand, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtMail.grid(row = 2, column = 1)

#sender password
senderpass= Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Sender password:",bd = 16,anchor = "w")
senderpass.grid(row = 3, column = 0)
txtMail= Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = spass, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtMail.grid(row = 3, column = 1)

#subject
lblSub = Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Subject: ", bd = 16, anchor = "w")
lblSub.grid(row = 4, column = 0)
subject = Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = Sub, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
subject.grid(row = 4, column = 1)

# body
lblMsg = Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Body: ", bd = 16, anchor = "w")
lblMsg.grid(row = 5, column = 0)
body = Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = Msg,bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
body.grid(row = 5, column = 1)

#key
lblkey = Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Enter Key:", bd = 16, anchor = "w")
lblkey.grid(row = 6, column = 0)
txtkey = Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = key, show='*',bd=10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtkey.grid(row = 6, column = 1)

#encoded text msg
lblenc = Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Enter cipertext:",
bd = 16, anchor = "w")
lblenc.grid(row = 1, column = 4)
txtenc = Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = enc, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtenc.grid(row = 1, column = 5)

#Key for decryption
lblkdec= Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Enter key for decryption:",
bd = 16, anchor = "w")
lblkdec.grid(row = 2, column = 4)
txtkdec= Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = kdec, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')
txtkdec.grid(row =2, column = 5)

#display decrypted message
lblService = Label(f1, font = ('Ms Serif', 16, 'bold'),
text = "Decrypted message:", bd = 8, anchor = "w")
lblService.grid(row = 3, column = 4)
txtService = Entry(f1, font = ('Ms Serif', 16, 'bold'),
textvariable = Result, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtService.grid(row = 3, column = 5)
import base64
# Function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i])+ord(key_c)) % 256)
        enc.append(enc_c)
        r=base64.urlsafe_b64encode("".join(enc).encode()).decode()
    return r

# Function to decode
def decode(kdec, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = kdec[i % len(kdec)]
        dec_c = chr((256 + ord(enc[i])-ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
z=0
       
def Ref():
#The mail addresses and password
    clear=Msg.get()
    print("Message= ",(Msg.get()))
    sender_email = sand.get()
    sender_password = spass.get()
    reciever_email = rand.get()
    subject = Sub.get()
    k=key.get()
    i=randint(1,10000000000000)
    c=str(i)+random.choice(string.ascii_letters)
    k=k+c
    yag = yagmail.SMTP(user=sender_email, password=sender_password)
    contents =[Msg.get()]
    bodymsg = encode(k,clear)+"   key="+k #this key is the final decryption key
    #print("bodymsg:",bodymsg)
    #print("k=:",k)
    yag.send(to=reciever_email, subject=subject, contents= bodymsg)
               
def dcode():
    s=decode(kdec.get(), enc.get())
    Result.set(decode(kdec.get(), enc.get()))

#encrypt and mail sending button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
font = ('Ms Serif', 16, 'bold'), width = 10,
text = "send email", bg = "SteelBlue3",
command = Ref).grid(row = 7, column = 1)

#Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
font = ('Ms Serif', 16, 'bold'), width = 10,
text = "Show Message", bg = "SteelBlue3",
command = dcode).grid(row = 7, column = 5)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
fg = "black", font = ('Ms Serif', 16, 'bold'),
width = 10, text = "Reset", bg = "red2",
command = Reset).grid(row = 8, column = 4)

# keeps window alive
root.mainloop()
