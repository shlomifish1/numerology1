import tkinter
from tkinter import *
import personal_y
import name

class FullDates:

    def __init__(self):
        self.real_year = None
        self.real_month = None
        self.full_list = None
        self.shana_ishit = None
        self.bd_month = None
        self.forth_pick_end = None
        self.forth_pick_start = None
        self.third_pick_start = None
        self.second_pick_start = None
        self.first_pick_start = None
        self.forth_challenge = None
        self.third_challenge = None
        self.second_challenge = None
        self.first_challenge = None
        self.first_pick = None
        self.second_pick = None
        self.third_pick = None
        self.forth_pick = None
        self.final_number_destiny = None
        self.p_year = None
        self.p_month = None
        self.p_day = None
        self.full_date_short = None
        self.date_button_canvas = None
        self.date_button = None
        self.second_photo = None
        self.first_photo = None
        self.entry_canvas_last_name = None
        self.entry_last_name = None
        self.entry_canvas_first_name = None
        self.entry_first_name = None
        self.entry_canvas_date = None
        self.canvas = None
        self.entry_date = None
        self.final_number = None
        self.day_convert_list = None
        self.month_convert_list = None
        self.year_convert_list = None
        self.year = None
        self.month = None
        self.day = None
        self.fulldate_list = None
        self.down_day_convert_list = None

#צמצום המספרים למספר אחד
    def short_numbers(self, args):
        lista = [x for x in str(args)]
        list_map = map(int, lista)
        convert_list = list(list_map)
        sum_number = sum(convert_list)
        if sum_number > 9:
            self.short_numbers(sum_number)
        else:
            self.final_number = sum_number

#צמצום היעוד ל2 ספרות עבור שיעורי הנשמה
    def short_numbers_for_destiny(self, args):
        lista = [x for x in str(args)]
        list_map = map(int, lista)
        convert_list = list(list_map)

        self.final_number = sum(convert_list)

    def print_final_details(self):
        self.canvas.delete(self.entry_canvas_date, self.entry_canvas_first_name,
                           self.entry_canvas_last_name,self.date_button_canvas)
        self.second_photo = PhotoImage(file="image/second_page.png")
        self.canvas.create_image(0, 0, image=self.second_photo, anchor="nw")

        print_full_date_short = self.canvas.create_text(815, 150, fill="white", text=self.full_date_short,
                                                        font=("Ariel", 25, "italic"))
        self.short_numbers(self.day)
        self.p_day = self.final_number

        self.short_numbers(self.month)
        self.p_month = self.final_number

        self.short_numbers(self.year)
        self.p_year = self.final_number

        self.short_numbers(self.final_number_destiny)
        self.final_number_destiny = self.final_number

        # ------------------------------הדפסה של תאריכים ----------------------------

        print_full_date = self.canvas.create_text(580,100, fill='white', text=f" {self.p_day} / {self.p_month} / {self.p_year}", font=("Ariel", 25, "italic"))
        #print:
        print_destiny_final = self.canvas.create_text(770, 150, fill="white", text=f" {self.final_number_destiny} /", font=("Ariel", 25, "italic",))
        self.shana_ishit = personal_y.This_Year().shana_ishit(day=self.p_day, month=self.p_month, bd_month=self.bd_month)
        print_shana_ishit = self.canvas.create_text(790, 425, fill="white", text=self.shana_ishit, font=("Ariel", 25, "italic",))
        print_shana_nisteret = self.canvas.create_text(790, 479, fill="white", text=f" {personal_y.This_Year().shana_nisteret(self.final_number_destiny, self.shana_ishit)} / {self.final_number_destiny}", font=("Ariel", 25, "italic",))
        print_age = self.canvas.create_text(795, 525, fill= "white", text= personal_y.This_Year().calculet_age(bd_month=self.real_month, year_of_birth=self.real_year),font=("Ariel", 25, "italic",))


#------------------------------הדפסה של   פסגות והאתגרים ----------------------------

        p_peak1 = self.canvas.create_text(90, 135, fill='white', text=name.NamesData().sum_num(self.first_pick),  font=("Ariel", 25, "italic"))
        p_peak2 = self.canvas.create_text(90, 185, fill='white', text=name.NamesData().sum_num(self.second_pick), font=("Ariel", 25, "italic"))
        p_peak3 = self.canvas.create_text(90, 235, fill='white', text=name.NamesData().sum_num(self.third_pick), font=("Ariel", 25, "italic"))
        p_peak4 = self.canvas.create_text(90, 285, fill='white', text=name.NamesData().sum_num(self.forth_pick), font=("Ariel", 25, "italic"))
        p_challenge1 = self.canvas.create_text(230, 135, fill='white', text=abs(name.NamesData().sum_num(self.first_challenge)), font=("Ariel", 25, "italic"))
        p_challenge2 = self.canvas.create_text(230, 185, fill='white', text=abs(name.NamesData().sum_num(self.second_challenge)), font=("Ariel", 25, "italic"))
        p_challenge3 = self.canvas.create_text(230, 235, fill='white', text=abs(name.NamesData().sum_num(self.third_challenge)), font=("Ariel", 25, "italic"))
        p_challenge4 = self.canvas.create_text(230, 285, fill='white', text=abs(name.NamesData().sum_num(self.forth_challenge)), font=("Ariel", 25, "italic"))


#------------------------------הדפסה של גילאי תחילת הפסגות והאתגרים ----------------------------
        self.first_pick_start = int(27 - self.final_number_destiny)
        self.second_pick_start = int(self.first_pick_start + 9)
        self.third_pick_start = int(self.second_pick_start + 9)
        self.forth_pick_start = int(self.third_pick_start + 9)
        self.forth_pick_end = int(self.forth_pick_start + 9)

        p_psagot_date1 = self.canvas.create_text(370, 135, fill='white', text=f" {self.first_pick_start} - {self.second_pick_start} ", font=("Ariel", 25, "italic"))
        p_psagot_date2 = self.canvas.create_text(370, 185, fill='white', text=f" {self.second_pick_start} - {self.third_pick_start} ", font=("Ariel", 25, "italic"))
        p_psagot_date3 = self.canvas.create_text(370, 235, fill='white', text=f" {self.third_pick_start} - {self.forth_pick_start} ", font=("Ariel", 25, "italic"))
        p_psagot_date4 = self.canvas.create_text(370, 285, fill='white', text=f" {self.forth_pick_start} - {self.forth_pick_end} ", font=("Ariel", 25, "italic"))

    # ------------------------------הדפסה של נתוני השם, עיצורים והאוי ----------------------------
        n_data = name.NamesData()
        first_name_str = self.entry_first_name.get()
        first_name_str = n_data.letter(first_name_str)
        full_name_str = self.entry_last_name.get() + self.entry_first_name.get()
        full_name_print = n_data.letter(full_name_str)

        p_first_name = self.canvas.create_text(800, 209, fill='white', text=first_name_str, font=("Ariel", 25, "italic"))
        p_full_name = self.canvas.create_text(635, 265, fill='white', text=full_name_print, font=("Ariel", 25, "italic"))

        itzurim_str = n_data.letter(list(filter(n_data.itzurim, full_name_str)))
        aiv_print =n_data.letter(list(filter(n_data.aiv, full_name_str)))
        p_itzurim = self.canvas.create_text(825, 320, fill='white', text=itzurim_str, font=("Ariel", 25, "italic"))
        p_aiv = self.canvas.create_text(870, 375, fill='white', text=aiv_print, font=("Ariel", 25, "italic"))

    def bd_split(self):
        self.fulldate_list = [x for x in str(self.entry_date.get())]
        self.day = self.fulldate_list[0:2]
        self.day = map(int, self.day)
        self.day = sum(self.day)

        self.month = self.fulldate_list[2:4]
        self.month = map(int, self.month)
        self.month = sum(self.month)

        self.year = self.fulldate_list[4:]
        self.year = map(int, self.year)
        self.year = sum(self.year)

        self.bd_month = self.fulldate_list[2:4]
        self.bd_month = f"{self.bd_month[0]}{self.bd_month[1]}"
        self.bd_month = int(self.bd_month)

        #חישוב שנה מלאה וחודש מלא
        self.full_list = [x for x in (self.entry_date.get())]
        self.real_month = self.full_list[2:4]
        self.real_month = f"{self.real_month[0]}{self.real_month[1]}"
        self.real_month = int(self.real_month)
        self.real_year = self.full_list[4:]
        self.real_year = f"{self.real_year[0]}{self.real_year[1]}{self.real_year[2]}{self.real_year[3]}"
        self.real_year = int(self.real_year)

        #חישוב פסגות
        self.short_numbers(self.day)
        self.p_day = self.final_number

        self.short_numbers(self.month)
        self.p_month = self.final_number

        self.short_numbers(self.year)
        self.p_year = self.final_number
        self.first_pick = int(self.p_day + self.p_month)
        self.second_pick = int(self.p_day + self.p_year)
        self.third_pick = int(self.first_pick + self.second_pick)
        self.forth_pick = int(self.p_month + self.p_year)

        #חישוב אתגרים

        self.first_challenge = abs(self.p_day - self.p_month)
        self.second_challenge = abs(self.p_day - self.p_year)
        self.third_challenge = abs(self.first_challenge - self.second_challenge)
        self.forth_challenge = self.p_month - self.p_year

        self.full_date_short = self.fulldate_list
        self.full_date_short = map(int, self.full_date_short)
        self.full_date_short = sum(self.full_date_short)

        self.final_number_destiny = self.full_date_short
        self.print_final_details()

    def get_date(self):
        window = Tk()

        self.first_photo = PhotoImage(file="image/first_page.png")
        self.canvas = Canvas(width=1000, height=600)
        self.canvas.create_image(0, 0, image=self.first_photo, anchor="nw")
        self.canvas.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)

        # Entry
        var = tkinter.StringVar()

        max_len = 8

        def on_write(*args):
            s = var.get()

            if len(s) > max_len:
                var.set(s[:max_len])

        var.trace_variable("w", on_write)

        #Entry
        self.entry_date = Entry(window, font=('Ariel 20'), textvariable=var)
        self.entry_canvas_date = self.canvas.create_window(600, 140, window=self.entry_date, width=135, height=40)
        self.entry_first_name = Entry(window, font=('Ariel 20'), )
        self.entry_canvas_first_name = self.canvas.create_window(600, 230, window=self.entry_first_name, width=135, height=40)
        self.entry_last_name = Entry(window, font=('Ariel 20'))
        self.entry_canvas_last_name = self.canvas.create_window(600, 300, window=self.entry_last_name, width=135, height=40)

        # Button
        self.date_button = Button(window, command=self.bd_split, text="לחץ לאישור", width=10, height=2)
        self.date_button_canvas = self.canvas.create_window(500, 410, window=self.date_button)

        #----------להגדיר אנטר----------
        # window.bind('<Return>', self.bd_split())

        window.mainloop()