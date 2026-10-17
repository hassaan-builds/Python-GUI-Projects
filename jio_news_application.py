
import requests
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import Request, urlopen
import io
import webbrowser

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GNEWS_API_KEY")


class NewsApp:

    def __init__(self):
        # Create GUI
        self.load_gui()

        # Fetch news
        try:
            url = (
                "https://gnews.io/api/v4/top-headlines"
                f"?country=pk&lang=en&apikey={API_KEY}"
            )

            response = requests.get(url, timeout=15)
            response.raise_for_status()

            data = response.json()
            self.articles = data.get("articles", [])

            if not self.articles:
                self.show_message("No news articles available.")
            else:
                self.load_news_items(0)

        except requests.RequestException as e:
            print("API Error:", e)
            self.show_message("Could not fetch news. Check internet.")

        except ValueError as e:
            print("Data Error:", e)
            self.show_message("Could not read news data.")

        # Start GUI only once
        self.root.mainloop()

    def load_gui(self):
        # Main window
        self.root = Tk()
        self.root.title("NEWS HUB")
        self.root.geometry("350x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#080B12")

        # Professional Header
        self.header = Label(
            self.root,
            text="NEWS HUB",
            font=("Arial", 22, "bold"),
            bg="#101820",
            fg="#00D9FF",
            pady=15
        )
        self.header.pack(fill=X)

        # Small subtitle
        subtitle = Label(
            self.root,
            text="YOUR DAILY NEWS",
            font=("Arial", 9, "bold"),
            bg="#101820",
            fg="#AAB8C5",
            pady=4
        )
        subtitle.pack(fill=X)

        self.header_area = [self.header, subtitle]

    def clear(self):
        # Keep header; remove previous news widgets
        for widget in self.root.pack_slaves():
            if widget not in self.header_area:
                widget.destroy()

    def show_message(self, message):
        # Display an error or information message
        label = Label(
            self.root,
            text=message,
            bg="#080B12",
            fg="white",
            font=("Arial", 12),
            wraplength=300,
            justify="center"
        )
        label.pack(expand=True, pady=20)

    def load_news_items(self, index):
        # Clear previous article but keep header
        self.clear()

        article = self.articles[index]

        # Load article image
        img_url = article.get("image")

        try:
            if not img_url:
                raise ValueError("Image URL not available")

            req = Request(
                img_url,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            raw_data = urlopen(req, timeout=10).read()

            im = Image.open(io.BytesIO(raw_data))
            im = im.convert("RGB")
            im = im.resize((330, 220))

            photo = ImageTk.PhotoImage(im)

            image_label = Label(
                self.root,
                image=photo,
                bg="#080B12"
            )
            image_label.image = photo
            image_label.pack(pady=(12, 5))

        except Exception as e:
            print("Image Error:", e)

            image_label = Label(
                self.root,
                text="Could not load image",
                bg="#202020",
                fg="white",
                font=("Verdana", 12, "bold"),
                width=35,
                height=8
            )
            image_label.pack(pady=(12, 5))

        # Article title
        heading = Label(
            self.root,
            text=article.get("title", "No title available"),
            bg="#080B12",
            fg="#00D9FF",
            wraplength=320,
            justify="center",
            font=("Arial", 15, "bold")
        )
        heading.pack(padx=10, pady=(10, 12))

        # Article description
        description = article.get("description") or "No description available"

        details = Label(
            self.root,
            text=description,
            bg="#080B12",
            fg="#D4D9E2",
            wraplength=320,
            justify="center",
            font=("Arial", 10)
        )
        details.pack(padx=10, pady=(0, 10))

        # Navigation buttons
        frame = Frame(self.root, bg="#080B12")
        frame.pack(side=BOTTOM, fill=X, pady=12)

        if index > 0:
            prev_button = Button(
                frame,
                text="PREV",
                width=9,
                height=2,
                bg="#182635",
                fg="white",
                activebackground="#00D9FF",
                command=lambda: self.load_news_items(index - 1)
            )
            prev_button.pack(side=LEFT, padx=(8, 3))

        read_button = Button(
            frame,
            text="READ MORE",
            width=11,
            height=2,
            bg="#007C91",
            fg="white",
            activebackground="#00D9FF",
            command=lambda: self.open_link(article.get("url"))
        )
        read_button.pack(side=LEFT, padx=3)

        if index < len(self.articles) - 1:
            next_button = Button(
                frame,
                text="NEXT",
                width=9,
                height=2,
                bg="#182635",
                fg="white",
                activebackground="#00D9FF",
                command=lambda: self.load_news_items(index + 1)
            )
            next_button.pack(side=LEFT, padx=3)

    def open_link(self, url):
        if url:
            webbrowser.open(url)
        else:
            print("Article URL not available")


# Run application
if __name__ == "__main__":
    app = NewsApp()
