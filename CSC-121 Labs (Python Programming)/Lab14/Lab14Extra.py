#
# Alex Cesar Rosa
# 4/28/2024
# Cash register using Tkinter for GUI application
#

import tkinter


class CashRegister:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Cash Register")
        self.main_window.geometry("250x150")

        self.frame1 = tkinter.Frame(self.main_window)
        self.workbook_prompt = tkinter.Label(self.frame1, text="Workbooks: ")
        self.workbook_entry = tkinter.Entry(self.frame1, width=10)
        self.workbook_prompt.pack(side="left")
        self.workbook_entry.pack(side="left")
        self.frame1.pack()

        self.frame2 = tkinter.Frame(self.main_window)
        self.textbook_prompt = tkinter.Label(self.frame2, text="Textbooks: ")
        self.textbook_entry = tkinter.Entry(self.frame2, width=10)
        self.textbook_prompt.pack(side="left")
        self.textbook_entry.pack(side="left")
        self.frame2.pack()

        self.frame3 = tkinter.Frame(self.main_window)
        self.magazine_prompt = tkinter.Label(self.frame3, text="Magazines: ")
        self.magazine_entry = tkinter.Entry(self.frame3, width=10)
        self.magazine_prompt.pack(side="left")
        self.magazine_entry.pack(side="left")
        self.frame3.pack()

        self.frame4 = tkinter.Frame(self.main_window)
        self.discount_checkbox = tkinter.BooleanVar(value=False)
        self.checkbox = tkinter.Checkbutton(self.frame4, text="25% Discount", variable=self.discount_checkbox)
        self.checkbox.pack(side="left")
        self.frame4.pack()

        self.frame5 = tkinter.Frame(self.main_window)
        self.total_purchase = tkinter.Label(self.frame5, text="Total:")
        self.total_purchase.pack(side="left")
        self.total_value = tkinter.StringVar()
        self.total_label = tkinter.Label(self.frame5, textvariable=self.total_value)
        self.total_value.set("-------")
        self.total_label.pack(side="left")
        self.frame5.pack()

        self.frame6 = tkinter.Frame(self.main_window)
        self.calc_average = tkinter.Button(self.frame6, text='Calculate', command=self.calc_total)
        self.quit_button = tkinter.Button(self.frame6, text='Quit', command=self.main_window.destroy)
        self.calc_average.pack(side='left')
        self.quit_button.pack(side='left')
        self.frame6.pack()

        tkinter.mainloop()

    def calc_total(self):
        try:
            WORKBOOK_PRICE = 8.50
            TEXTBOOK_PRICE = 24.00
            MAGAZINE_PRICE = 5.95

            workbook = int(self.workbook_entry.get())
            textbook = int(self.textbook_entry.get())
            magazine = int(self.magazine_entry.get())

            total_purchase = (workbook * WORKBOOK_PRICE) + (textbook * TEXTBOOK_PRICE) + (magazine * MAGAZINE_PRICE)

            if self.discount_checkbox.get() == True:
                total_purchase = total_purchase * 0.75
                self.total_value.set(f"${total_purchase:.2f}")
            elif self.discount_checkbox.get() == False:
                self.total_value.set(f"${total_purchase:.2f}")
        except ValueError:
            self.total_value.set("Error")


cash_register_gui = CashRegister()
