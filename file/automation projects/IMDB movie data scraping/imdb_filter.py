import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import pandas as pd


def fetch_filtered_data(country=None, rating=None, release_date=None, director=None, language=None, genre=None):
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    query = "SELECT * FROM imdb_table WHERE 1=1"
    params = []

    if country:
        query += " AND Country_of_origin LIKE ?"
        params.append(f"%{country}%")

    if rating:
        query += " AND Rating >= ?"
        params.append(rating)

    if release_date:
        query += " AND Release_date > ?"
        params.append(release_date)

    if director:
        query += " AND Director LIKE ?"
        params.append(f"%{director}%")

    if language:
        query += " AND Language LIKE ?"
        params.append(f"%{language}%")

    if genre:
        query += " AND Genre LIKE ?"
        params.append(f"%{genre}%")

    cursor.execute(query, params)
    data = cursor.fetchall()

    conn.close()

    return data

def filter_data():
    country = country_var.get()
    rating = rating_var.get()
    release_date = release_date_var.get()
    director = director_var.get()
    language = language_var.get()
    genre = genre_var.get()


    filtered_data = fetch_filtered_data(country, rating, release_date, director, language, genre)

    if not filtered_data:
        messagebox.showinfo("No Results", "No movies found matching the given criteria.")
        return

    df = pd.DataFrame(filtered_data, columns=['Rank', 'Title', 'Rating', 'Release_date', 'Genre', 'Runtime', 'Director', 'Stars', 'Country_of_origin', 'Language', 'Budget'])

    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Export Successful", "Filtered data exported to Excel successfully.")


root = tk.Tk()
root.title("IMDb Data Filter")

filter_frame = ttk.Frame(root, padding="20")
filter_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(filter_frame, text="Country of Origin:").grid(row=0, column=0, sticky=tk.W)
country_var = tk.StringVar()
country_entry = ttk.Entry(filter_frame, textvariable=country_var)
country_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(filter_frame, text="Minimum Rating:").grid(row=1, column=0, sticky=tk.W)
rating_var = tk.DoubleVar()
rating_entry = ttk.Entry(filter_frame, textvariable=rating_var)
rating_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(filter_frame, text="Release After Date (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W)
release_date_var = tk.StringVar()
release_date_entry = ttk.Entry(filter_frame, textvariable=release_date_var)
release_date_entry.grid(row=2, column=1, sticky=tk.W)

ttk.Label(filter_frame, text="Director:").grid(row=3, column=0, sticky=tk.W)
director_var = tk.StringVar()
director_entry = ttk.Entry(filter_frame, textvariable=director_var)
director_entry.grid(row=3, column=1, sticky=tk.W)

ttk.Label(filter_frame, text="Language:").grid(row=4, column=0, sticky=tk.W)
language_var = tk.StringVar()
language_entry = ttk.Entry(filter_frame, textvariable=language_var)
language_entry.grid(row=4, column=1, sticky=tk.W)

ttk.Label(filter_frame, text="Genre:").grid(row=5, column=0, sticky=tk.W)
genre_var = tk.StringVar()
genre_entry = ttk.Entry(filter_frame, textvariable=genre_var)
genre_entry.grid(row=5, column=1, sticky=tk.W)

filter_button = ttk.Button(filter_frame, text="Filter", command=filter_data)
filter_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
