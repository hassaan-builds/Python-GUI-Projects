import requests
from tkinter import*
from PIL import ImageTk,Image
from urllib.request import Request, urlopen
import io
import webbrowser
import os
from dotenv import load_dotenv
load_dotenv()


class NewsApp:

    def __init__(self):
#fetch data
        self.data = requests.get(
            "https://gnews.io/api/v4/top-headlines",
            params={
                "country": "pk",
                "lang": "en",
                "apikey": os.getenv("GNEWS_API_KEY")
            }
        ).json()
        print(self.data)
       
        #initial Gui load
        self.load_gui()
      
        #load the first news item
        self.load_news_items(0)

 
    def load_gui(self):
        self.root=Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.configure(background="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_items(self,index):
        #clear the screen for the news items
        self.clear()
        #image
        
# Image
        img_url = self.data["articles"][index].get("image")
        try:
            if img_url:
                req = Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
                raw_data = urlopen(req, timeout=10).read()

                im = Image.open(io.BytesIO(raw_data))
                im = im.resize((350, 250))

                photo = ImageTk.PhotoImage(im)
                label = Label(self.root, image=photo, bg="black")
                label.image = photo
                label.pack()
            else:
                raise ValueError("Image URL not available")
            
        except Exception as e:
            print("Image Error:", e)
            label = Label(
                self.root,
                text="Could not load image",
                bg="#202020",
                fg="white",
                font=("Verdana", 12, "bold"),
                width=35,
                height=12
            )
            label.pack()



        heading=Label(self.root,text=self.data["articles"][index]["title"],bg="black",
                      fg="white",wraplength=350,justify="center")
        heading.pack(pady=(10,20))
        heading.configure(font=("verdana",15))


        
        details=Label(self.root,text=self.data["articles"][index]["description"],bg="black",
                      fg="white",wraplength=350,justify="center")
        details.pack(pady=(2,20))
        details.configure(font=("verdana",12,"bold"))


        frame=Frame(self.root,bg="black")
        frame.pack(expand="True",fill=BOTH)


        if index!=0:
            prev=Button(frame,text="prev",width=16,height=3,command=lambda:self.load_news_items
                        (index-1))
            prev.pack(side=LEFT)


        read=Button(frame,text="Read More",width=16,height=3,command=lambda:self.open_link
                    (self.data["articles"][index]["url"]))
        read.pack(side=LEFT)


        if index !=len(self.data["articles"])-1:
            next=Button(frame,text="Next",width=16,height=3,command=lambda:self.load_news_items
                        (index+1))
            next.pack(side=LEFT)


        self.root.mainloop()

    def open_link(self,url):
      webbrowser.open(url)
    

obj=NewsApp()
