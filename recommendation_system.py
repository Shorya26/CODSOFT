import tkinter as tk
from tkinter import ttk
import pandas as pd
import random

df = pd.read_csv("realistic_recommendations.csv")

class RecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Smart Recommendation System")
        self.root.geometry("600x500")
        self.root.configure(bg="#f5f5f5")

        self.category = None

        # Title
        title = tk.Label(
            root, text="🤖 Welcome to Recommendation Bot",
            font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333"
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            root, text="What would you like recommendations for?",
            font=("Arial", 13), bg="#f5f5f5"
        )
        subtitle.pack(pady=5)

        # Category buttons
        self.buttons_frame = tk.Frame(root, bg="#f5f5f5")
        self.buttons_frame.pack(pady=15)

        style = {"width": 15, "height": 2, "font": ("Arial", 11, "bold")}

        tk.Button(self.buttons_frame, text="🎬 Movies", bg="#4CAF50", fg="white",
                  command=lambda: self.select_category("movie"), **style).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(self.buttons_frame, text="📚 Books", bg="#2196F3", fg="white",
                  command=lambda: self.select_category("book"), **style).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.buttons_frame, text="🛒 Products", bg="#FF9800", fg="white",
                  command=lambda: self.select_category("product"), **style).grid(row=0, column=2, padx=10, pady=10)

        # Genre/category selection
        self.genre_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5")
        self.genre_dropdown = ttk.Combobox(root, state="readonly", width=30, font=("Arial", 11))
        self.genre_button = tk.Button(root, text="Show Recommendations ✅", bg="#673AB7", fg="white",
                                      font=("Arial", 11, "bold"), command=self.show_recommendations)

        # Results area (scrollable)
        self.results_frame = tk.Frame(root, bg="#f5f5f5")
        self.text_area = tk.Text(self.results_frame, wrap="word", width=65, height=12,
                                 font=("Arial", 11), bg="#ffffff", fg="#333")
        self.scrollbar = tk.Scrollbar(self.results_frame, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.reset_button = tk.Button(root, text="🔄 Reset", bg="#f44336", fg="white",
                                      font=("Arial", 11, "bold"), command=self.reset_app)

    def select_category(self, category):
        self.category = category
        genres = sorted(df[df["category"] == category]["genre"].unique())

        if category == "movie":
            self.genre_label.config(text="🎬 Select a Movie Genre:")
        elif category == "book":
            self.genre_label.config(text="📚 Select a Book Genre:")
        else:
            self.genre_label.config(text="🛒 Select a Product Category:")

        self.genre_label.pack(pady=10)
        self.genre_dropdown["values"] = genres
        self.genre_dropdown.current(0)
        self.genre_dropdown.pack(pady=5)
        self.genre_button.pack(pady=10)

    def show_recommendations(self):
        choice = self.genre_dropdown.get()
        items = df[(df["category"] == self.category) & (df["genre"] == choice)]["title"].tolist()
        recs = random.sample(items, min(5, len(items)))

        if self.category == "movie":
            result = "🎬 Recommended Movies:\n\n- " + "\n- ".join(recs)
        elif self.category == "book":
            result = "📚 Recommended Books:\n\n- " + "\n- ".join(recs)
        else:
            result = "🛒 Recommended Products:\n\n- " + "\n- ".join(recs)

        self.results_frame.pack(pady=15)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, result)
        self.text_area.pack(side=tk.LEFT, fill="both", expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.reset_button.pack(pady=10)

    def reset_app(self):
        self.genre_label.pack_forget()
        self.genre_dropdown.pack_forget()
        self.genre_button.pack_forget()
        self.results_frame.pack_forget()
        self.text_area.pack_forget()
        self.scrollbar.pack_forget()
        self.reset_button.pack_forget()
        self.category = None


if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationApp(root)
    root.mainloop()
