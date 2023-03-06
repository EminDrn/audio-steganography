import wave
from tkinter import *
from tkinter import filedialog
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
master = Tk()
canvas = Canvas(master,height=650, width=650)
canvas.pack()
master.title("Ses Steganografisi")

frame_mid1 = Frame(master,bg='')
frame_mid1.place(x= 20 , y=100,height=30,width=300)
dosya_yolu_text = Label(master,text='Şifrelenmiş Sesi Seçiniz ',font='Verdana 12  bold')
dosya_yolu_text.place(x=330 , y =60)

open_button = Button(master,text="Dosya Aç",command=lambda:[open_file(),get_path()],)
open_button.place(x=220,y=140,height=30,width=100)

path_label = Label(frame_mid1,bg='white',font='Verdana 8')
path_label.pack(side=LEFT)
gonderlicekMailAdresi = Text(master)

gonderlicekMailAdresi.place(x=20,y = 370 , width= 300, height=20)
ssw = gonderlicekMailAdresi.get(1.0,"end-1c")
print(ssw)


def prevPage():
    master.destroy()

Button(master,text="Programdan Çıkmak İçin Tıklayınız" , command=prevPage).pack(fill=X,expand=TRUE,side=LEFT)

frame_mid1 = Frame(bg = '')
frame_mid1.place(x=330,y = 100,height= 30 , width=300)


dosya_yolu_text = Label(text = 'Şifrelenecek sesi seçiniz',font='Verdana 12 bold')
dosya_yolu_text.place(x= 20,y = 60)

path = Label(frame_mid1 , font='Verdana 8',bg= 'white')
path.pack(side=LEFT)

open_button = Button(text="Dosya Aç", command=lambda: [coz()], )
open_button.place(x=530, y=140, height=30, width=100)

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[("Audio Files", '*.*')])
    if file:
        path_label.configure(text=file.name)


def mailGonder():
    FROM_ADDRESS = "emin87d@gmail.com"
    TO_ADDRESS = "emin001d@gmail.com"
    # E-posta mesajını oluşturun
    body = "https://drive.google.com/file/d/125sbqAHmix_ViFksItedUxaIZyPADU-e/view?usp=share_link"
    msg = MIMEMultipart("mixed")
    MIMEText(body)
    msg["Subject"] = "dednsdasadaseme"
    msg["Body"] = body
    msg["From"] = FROM_ADDRESS
    msg["To"] = TO_ADDRESS
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_ADDRESS = "emin87d@gmail.com"
    EMAIL_PASSWORD = "iogeycwivtstasrh"
    text_part = MIMEText(body)
    msg.attach(text_part)
    # E-posta mesajına dosya ekleyin
    part = MIMEApplication(open(get_path(), "rb").read())
    part.add_header("Content-Disposition", "attachment", filename=fp.replace("\\", "\\\\"))
    msg.attach(part)

    # E-posta sunucusuna bağlanın ve e-posta gönderin
    smtp_client = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp_client.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    smtp_client.quit()
def open_fileÇ():
    file = filedialog.askopenfile(mode='r', filetypes=[("Images Files", '*.*')])
    if file:
        filepath = os.path.abspath(file.name)
        path.configure(text=filepath)
        return file.name

#kodun çözüldüğü kısım
def coz():
    fp = open_fileÇ()
    text = decode(fp)
    decode_text.configure(text=text)
    #print(text)
#dosya yolunu yazma
new_file_path = ""
def get_path():
    file_path = (path_label["text"])
    fp = str(file_path)

    return fp
fp  =new_file_path
def display_text():
    txt = text_input.get(1.0, "end-1c")
    return txt

def gizle():
    encode(get_path(),display_text())

file_path_label = Label(frame_mid1, text=get_path(), font='Verdana 12 bold', bg='white')
file_path_label.pack(side=LEFT)

mesaj_text = Label(master, text='Gizlemek istediğiniz mesaj', font='Verdana 12 bold')
mesaj_text.place(x=20, y=180)

text_input = Text(master)
text_input.place(x=20,y=210,width=300,height=150)
send_button = Button(master, text="Şifrele", command=lambda: [gizle(),info(),mailGonder()])
send_button.place(x=200, y=410, height=30, width=100 )

# Butona basıldığında bilgi vermesi
frame_bottom = Frame(master, bg='#FFFFFF')
frame_bottom.place(x=20,y=580)
success = False
success_text = Label(frame_bottom, text="",font=('Helvetica 13 bold'))
success_text.pack()
def info():
    msg = 'İşleminiz başarıyla gerçekleşti.'
    success_text.configure(text=msg)

def checkFlip(data,a,b):
    #mantıksal and işlemi yapılır
    store = data & 12
    if store == 0 and (a == 0 and b == 0):
        return data
    elif store == 4 and (a == 0 and b == 1):
        return data
    elif store == 8 and (a == 1 and b == 0):
        return data
    elif store == 12 and (a == 1 and b == 1):
        return data
    else:
        return data ^ 3

def encode(ses,veri):
    print("\nEncoding Starts..")
    audio = wave.open(ses,mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string = str(veri)
   # print(string)
    string = string + int(((2*len(frame_bytes))-(len(string)*8*8))/8) *'#'
#ord fonksiynu parametre olarak aldığı değeri ASCII kodunun gösterir
#bin verilen değeri ikilik tabana dönüştürür
#ikilik tabanda gösterilen sayının gösteriminde 0b kullanılır
#lstrip 0b yi başından atar
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
   # print(bits)
    j = 0
    for i in range(0,len(frame_bytes),2):
        a = bits[i]
        b = bits[i+1]
        frame_bytes[j] = checkFlip(frame_bytes[j],a,b)
        frame_bytes[j] = frame_bytes[j] & 243
        #11110011
        if a==0 and b==1:
            frame_bytes[j] = frame_bytes[j] + 4
        elif a==1 and b==0:
            frame_bytes[j] = frame_bytes[j] + 8
        elif a==1 and b==1:
            frame_bytes[j] = frame_bytes[j] + 12
        j = j + 1
    frame_modified = bytes(frame_bytes)
    newAudio =  wave.open(ses, 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)

    newAudio.close()
    audio.close()
   # print(" |---->succesfully encoded inside"+ ses)


decode_text_msg = Label(text='Sesin içindeki gizlenmiş mesaj ',font='Verdana 12 bold')
decode_text_msg.place(x=330,y=180)

decode_frame = Frame(bg='white')

decode_frame.place(x=330,y=210,height=150,width=300)
decode_text = Label(decode_frame, bg='white', wraplength=550)
decode_text.pack(side=LEFT)



def decode(ses):
    print("\nDecoding Starts..")
    audio = wave.open(ses, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = []
    for i in range(len(frame_bytes)):
        frame_bytes[i] = frame_bytes[i] & 12
        if frame_bytes[i] == 0:
            extracted.append(0)
            extracted.append(0)
        elif frame_bytes[i] == 4:
            extracted.append(0)
            extracted.append(1)
        elif frame_bytes[i] == 8:
            extracted.append(1)
            extracted.append(0)
        elif frame_bytes[i] == 12:
            extracted.append(1)
            extracted.append(1)
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]
    return (decoded)
    audio.close()


master.mainloop()