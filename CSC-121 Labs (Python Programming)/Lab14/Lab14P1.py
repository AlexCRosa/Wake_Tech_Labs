#
# Alex Cesar Rosa
# 4/28/2024
# Grade calculator using Tkinter for GUI application
#

import tkinter


class CalculatorGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Grade Calculator")
        self.main_window.geometry("260x125")

        self.frame1 = tkinter.Frame(self.main_window)
        self.test_prompt = tkinter.Label(self.frame1, text="Tests Grade: ")
        self.test_entry = tkinter.Entry(self.frame1, width=10)
        self.test_prompt.pack(side="left")
        self.test_entry.pack(side="left")
        self.frame1.pack()

        self.frame2 = tkinter.Frame(self.main_window)
        self.grade_prompt = tkinter.Label(self.frame2, text="Labs Grade: ")
        self.lab_entry = tkinter.Entry(self.frame2, width=10)
        self.grade_prompt.pack(side="left")
        self.lab_entry.pack(side="left")
        self.frame2.pack()

        self.frame3 = tkinter.Frame(self.main_window)
        self.exam_prompt = tkinter.Label(self.frame3, text="Exams Grade: ")
        self.exam_entry = tkinter.Entry(self.frame3, width=10)
        self.exam_prompt.pack(side="left")
        self.exam_entry.pack(side="left")
        self.frame3.pack()

        self.frame4 = tkinter.Frame(self.main_window)
        self.grade_average = tkinter.Label(self.frame4, text="Grade Average: ")
        self.grade_average.pack(side="left")
        self.average_value = tkinter.StringVar()
        self.average_label = tkinter.Label(self.frame4, textvariable=self.average_value)
        self.average_value.set("-------")
        self.average_label.pack(side="left")
        self.frame4.pack()

        self.frame5 = tkinter.Frame(self.main_window)
        self.calc_average = tkinter.Button(self.frame5, text='Calculate', command=self.calc_avg)
        self.quit_button = tkinter.Button(self.frame5, text='Quit', command=self.main_window.destroy)
        self.calc_average.pack(side='left')
        self.quit_button.pack(side='left')
        self.frame5.pack()

        tkinter.mainloop()

    def calc_avg(self):
        try:
            test = float(self.test_entry.get()) * 0.20
            lab = float(self.lab_entry.get()) * 0.30
            exam = float(self.exam_entry.get()) * 0.50
            score = test + lab + exam

            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"

            self.average_value.set(f"{score:.1f} ({grade})")
        except ValueError:
            self.average_value.set("Error")


calculator_gui = CalculatorGUI()
