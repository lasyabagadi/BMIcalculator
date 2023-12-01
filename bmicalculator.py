import tkinter as tk

class BMI_Calculator:
    def __init__(self,root):
        self.root=root
        self.root.title('BMI Calculator')
        
        self.weightlabel=tk.Label(root,text='Weight (kg):')
        self.weightlabel.grid(row=0,column=0,padx=10,pady=10)
        
        self.weightentry=tk.Entry(root)
        self.weightentry.grid(row=0,column=1,padx=10,pady=10)
        
        self.heightlabel=tk.Label(root,text='Height (cm):')
        self.heightlabel.grid(row=1,column=0,padx=10,pady=10)
        
        self.heightentry=tk.Entry(root)
        self.heightentry.grid(row=1,column=1,padx=10,pady=10)
        
        self.calcbutton=tk.Button(root,text='Calculate BMI',command=self.calculateBMI)
        self.calcbutton.grid(row=2,column=0,columnspan=2,pady=10)
        
        self.resultlabel=tk.Label(root,text='')
        self.resultlabel.grid(row=3,column=0,columnspan=2,pady=10)
        
    def calculateBMI(self):
        weight=float(self.weightentry.get())
        height=float(self.heightentry.get())/100
        bmi=weight/(height**2)
        category=self.category(bmi)
        result=f'Your BMI: {bmi:.2f}\nCategory: {category}'
        self.resultlabel.config(text=result)
        
    def category(self,bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
        
root=tk.Tk()
root.geometry("244x200")
app=BMI_Calculator(root)
root.mainloop()
