from tkinter import *
from tkinter import messagebox
import csv
import time
from pathlib import Path
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class Record_Manager:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Record Manager")

        self.field_names = ['date', 'Kota', 'Marble', 'Granite', 'Lokhand', 'Lokhand-Stock', 'Kapachi', 'Kapachi-Stock',
                            'Cement', 'Cement-Stock1', 'Cement-Stock2', 'Chokatha', 'Chokhatha-Stock', 'Patra', 'Wall',
                            'Floor', 'Sanatairy']

        # Initialize self.data by reading existing data from the CSV file
        self.csv_filename = f"record_{time.strftime('%Y-%m-%d')}.csv"
        self.load_data_from_csv()  # Load existing data if the file exists

        bg_color = "#074463"
        title = Label(self.root, text="Record Manager", bd=12, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        self.Kota = IntVar()
        self.Marble = IntVar()
        self.Granite = IntVar()
        self.Lokhand = IntVar()
        self.Lokhand_Stock = IntVar()
        self.Kapachi = IntVar()
        self.Kapachi_Stock = IntVar()
        self.Cement = IntVar()

        self.Cement_Stock1 = IntVar()
        self.Cement_Stock2 = IntVar()
        self.Chokatha = IntVar()
        self.Chokhatha_Stock = IntVar()
        self.Patra = IntVar()
        self.Wall = IntVar()
        self.Floor = IntVar()
        self.Sanatairy = IntVar()

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F2.place(x=55, y=80, width=675, height=465)

        box11_lbl = Label(F2, text="Kota", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=15, pady=15, sticky="w")
        box11_txt = Entry(F2, width=30, textvariable=self.Kota, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        box12_lbl = Label(F2, text="Marble", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        box12_txt = Entry(F2, width=30, textvariable=self.Marble, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        box13_lbl = Label(F2, text="Granite", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        box13_txt = Entry(F2, width=30, textvariable=self.Granite, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        box14_lbl = Label(F2, text="Lokhand", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        box14_txt = Entry(F2, width=30, textvariable=self.Lokhand, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        box15_lbl = Label(F2, text="Lokhand-Stock", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        box15_txt = Entry(F2, width=30, textvariable=self.Lokhand_Stock, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        box16_lbl = Label(F2, text="Kapachi", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        box16_txt = Entry(F2, width=30, textvariable=self.Kapachi, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        box17_lbl = Label(F2, text="Kapachi-Stock", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        box17_txt = Entry(F2, width=30, textvariable=self.Kapachi_Stock, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        box18_lbl = Label(F2, text="Cement", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        box18_txt = Entry(F2, width=30, textvariable=self.Cement, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F3.place(x=800, y=80, width=675, height=465)

        box21_lbl = Label(F3, text="Cement-Stock1", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=15, pady=15, sticky="w")
        box21_txt = Entry(F3, width=30, textvariable=self.Cement_Stock1, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        box22_lbl = Label(F3, text="Cement-Stock2", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        box22_txt = Entry(F3, width=30, textvariable=self.Cement_Stock2, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        box23_lbl = Label(F3, text="Chokatha", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        box23_txt = Entry(F3, width=30, textvariable=self.Chokatha, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        box24_lbl = Label(F3, text="Chokhatha-Stock", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        box24_txt = Entry(F3, width=30, textvariable=self.Chokhatha_Stock, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        box25_lbl = Label(F3, text="Patra", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        box25_txt = Entry(F3, width=30, textvariable=self.Patra, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        box26_lbl = Label(F3, text="Wall", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        box26_txt = Entry(F3, width=30, textvariable=self.Wall, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        box27_lbl = Label(F3, text="Floor", font=("times new roman", 15, "bold"), bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        box27_txt = Entry(F3, width=30, textvariable=self.Floor, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        box28_lbl = Label(F3, text="Sanatairy", font=("times new roman", 15, "bold"), bg=bg_color,fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        box28_txt = Entry(F3, width=30, textvariable=self.Sanatairy, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Options", font=("times new roman", 16, "bold"), pady=18,fg="gold", bg=bg_color)
        F6.place(x=55, y=556, relwidth=0.92, height=215)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=50, width=890, relwidth=0.13, height=115)

        s_btn = Button(btn_F, text="Save Record", bg="cadetblue", command=self.save_bill, fg="white", bd=2, pady=15,width=15, font="arial 14 bold").grid(row=0, column=2, padx=15, pady=15)

        Add_row_btn = Button(btn_F, text="Add New Record", command=self.create_csv_file, bg="cadetblue", fg="white",bd=2, pady=15, width=15, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=15)

        Create_btn = Button(btn_F, text="Create New File", command=self.create_csv_file, bg="cadetblue", fg="white",bd=2, pady=15, width=15, font="arial 14 bold").grid(row=0, column=4, padx=5, pady=15)

        Clear_btn = Button(btn_F, text="Clear Boxes", command=self.clear_data, bg="cadetblue", fg="white", bd=2,pady=15, width=15, font="arial 14 bold").grid(row=0, column=5, padx=5, pady=15)

        Total_btn = Button(btn_F, text="Total All Records", command=self.calculate_totals, bg="cadetblue", fg="white",bd=2, pady=15, width=15, font="arial 14 bold").grid(row=0, column=6, padx=5, pady=15)

    def load_data_from_csv(self):
        try:
            with open(self.csv_filename, 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                self.data = [row for row in reader]
        except FileNotFoundError:
            self.data = []

    def create_csv_file(self):

        today = time.strftime("%Y-%m-%d")
        # Specify the full path to save the CSV file to D:/record
        self.csv_filename = f"D:/record1/record_{today}.csv"
        csv_path = Path(self.csv_filename)

        # this is for daily records_2023-24 file if it is not exist then it create one
        self.total_file = "D:/record1/daily_records_2023-24.csv"
        csv_total = Path(self.total_file)

        if not csv_total.is_file():
            with open(csv_total, 'w', newline='') as csv_file:
                pass

        if not csv_path.is_file():
            with open(csv_path, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
                writer.writeheader()

    def save_bill(self):
        op = messagebox.askyesno("Save Record", "Do you want to save the Record?")
        if op > 0:
            record = {
                'date': time.strftime("%Y-%m-%d"),
                'Kota': self.Kota.get(),
                'Marble': self.Marble.get(),
                'Granite': self.Granite.get(),
                'Lokhand': self.Lokhand.get(),
                'Lokhand-Stock': self.Lokhand_Stock.get(),
                'Kapachi': self.Kapachi.get(),
                'Kapachi-Stock': self.Kapachi_Stock.get(),
                'Cement': self.Cement.get(),
                'Cement-Stock1': self.Cement_Stock1.get(),
                'Cement-Stock2': self.Cement_Stock2.get(),
                'Chokatha': self.Chokatha.get(),
                'Chokhatha-Stock': self.Chokhatha_Stock.get(),
                'Patra': self.Patra.get(),
                'Wall': self.Wall.get(),
                'Floor': self.Floor.get(),
                'Sanatairy': self.Sanatairy.get(),
            }

            with open(self.csv_filename, 'a', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
                writer.writerow(record)

            self.data.append(record)  # Add the new record to self.data

            print("Record saved successfully.")
            print(time.strftime("%Y-%m-%d"))
            messagebox.showinfo("Saved", f"File Name : 'record_{time.strftime('%Y-%m-%d')}' saved successfully")

        else:
            return
        self.clear_data()

    def calculate_totals(self):
        # Today's file path
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_path = f"D:/record1/record_{current_date}.csv"
        output_file = "D:/record1/daily_records_2023-24.csv"

        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Calculate the sum of specified columns
            column_sums = df[self.field_names[1:]].sum()
            current_datetime = datetime.now().strftime("%Y-%m-%d")

            # Create a new dictionary with the results
            result_dict = {'date': current_date}
            result_dict.update({field: column_sums[i - 1] for i, field in enumerate(self.field_names[1:], start=1)})
            print(result_dict)

            # Open the CSV file for writing with DictWriter
            with open(output_file, mode='a', newline='') as csv_file:
                fieldnames = self.field_names
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Write the header row if the file is empty
                if csv_file.tell() == 0:
                    writer.writeheader()

                # Write the data from the dictionary
                writer.writerow(result_dict)

            messagebox.showinfo("Total All", "Column totals saved to 'daily_records_2023-24.csv'.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear Data?")
        if op > 0:
            self.Kota.set(0)
            self.Marble.set(0)
            self.Granite.set(0)
            self.Lokhand.set(0)
            self.Lokhand_Stock.set(0)
            self.Kapachi.set(0)
            self.Kapachi_Stock.set(0)
            self.Cement.set(0)

            self.Cement_Stock1.set(0)
            self.Cement_Stock2.set(0)
            self.Chokatha.set(0)
            self.Chokhatha_Stock.set(0)
            self.Patra.set(0)
            self.Wall.set(0)
            self.Floor.set(0)
            self.Sanatairy.set(0)


root = Tk()
obj = Record_Manager(root)
root.mainloop()
