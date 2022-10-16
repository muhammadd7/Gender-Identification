from tkinter import ttk
import tkinter as tk
from tkinter.constants import RIGHT 
from tkinter import *
import pickle
from tkinter import messagebox
import pandas as pd

root = Tk()       
root.geometry('500x500')	
root.title("Model Predictions")
Label(root, text ="Gender Identification using KNN & Perceptron", font=150).pack()

class Predictions(object):
    
    def __init__(self):
        self.sex = IntVar()
        self.weight = IntVar()
        self.height = IntVar()
        self.hair_length = IntVar()
        self.beard = IntVar()
        self.hijab = IntVar()
        self.bald = IntVar()
        self.physicalActivity = IntVar()
        self.cooking = IntVar()
        self.ownpet = IntVar()
        self.wearjewlery = IntVar()
        self.hairdye = IntVar()
        self.piercing = IntVar()
        self.contactlense = IntVar()
        self.i = IntVar() #Basically Links Any Radiobutton With The Variable=i.

    def AddAttributes(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Employee")
        newWindow.geometry("1000x700")
        Label(newWindow, text ="Add Sex").place(x=100, y=20)
        Label(newWindow, text="Add Height:").place(x=100, y=60)
        Label(newWindow, text="Add Weight:").place(x=100, y=100)
        Label(newWindow, text="Add Hair Length:").place(x=100, y=140)
        Label(newWindow, text="Add Beard:").place(x=100, y=180)
        Label(newWindow, text="Add Hijab:").place(x=100, y=220)
        Label(newWindow, text="Add Bald:").place(x=100, y=260)
        Label(newWindow, text="Add Physical Activities:").place(x=100, y=300)
        Label(newWindow, text="Cooking:").place(x=100, y=340)
        Label(newWindow, text="Own a Pet:").place(x=100, y=380)
        Label(newWindow, text="Wear Jewlery:").place(x=100, y=420)
        Label(newWindow, text="Hair Dye:").place(x=100, y=460)
        Label(newWindow, text="Piercing:").place(x=100, y=500)
        Label(newWindow, text="Wear Contact Lense:").place(x=100, y=540)
        

        ei = Entry(newWindow, textvariable=self.sex)
        nam = Entry(newWindow, textvariable=self.height)
        cni = Entry(newWindow, textvariable=self.weight)
        cont = Entry(newWindow, textvariable=self.hair_length)
        des = Entry(newWindow, textvariable=self.beard)
        jd = Entry(newWindow, textvariable=self.hijab)
        bd = Entry(newWindow, textvariable=self.bald)
        add = Entry(newWindow, textvariable=self.physicalActivity)
        cit = Entry(newWindow, textvariable=self.cooking)
        se = Entry(newWindow, textvariable=self.ownpet)
        sd = Entry(newWindow, textvariable=self.wearjewlery)
        vd = Entry(newWindow, textvariable=self.hairdye)
        ad = Entry(newWindow, textvariable=self.piercing)
        dd = Entry(newWindow, textvariable=self.contactlense)
        r1 = Radiobutton(newWindow, text="Perceptron", value=1, variable=self.i)
        r2 = Radiobutton(newWindow, text="Knn", value=2, variable=self.i)


        ei.place(x=300, y=20)
        nam.place(x=300, y=60)
        cni.place(x=300, y=100)
        cont.place(x=300, y=140)
        des.place(x=300, y=180)
        jd.place(x=300, y=220)
        bd.place(x=300, y=260)
        add.place(x=300, y=300)
        cit.place(x=300, y=340)
        se.place(x=300, y=380)
        sd.place(x=300, y=420)
        vd.place(x=300, y=460)
        ad.place(x=300, y=500)
        dd.place(x=300, y=540)
        r1.place(x=300, y=580)
        r2.place(x=300, y=620)
        r1.pack(side = RIGHT, ipadx=150)
        r2.pack(side = RIGHT)
        submit = Button(newWindow, text = 'Submit', command = self.SubmitAttributes)
        submit.place(x=200,y=660) 

    def SubmitAttributes(self):
        data = {
            'SEX':[self.sex.get()],
            'Height':[self.height.get()],
            'Weight':[self.weight.get()],
            'Hair length':[self.hair_length.get()],
            'Beard':[self.beard.get()],
            'Hijab':[self.hijab.get()],
            'Bald':[self.bald.get()],
            'Physical Activity':[self.physicalActivity.get()],
            'Cooking':[self.cooking.get()],
            'Own a pet':[self.ownpet.get()],
            'Wear Jewelery':[self.wearjewlery.get()],
            'Hair Dye':[self.hairdye.get()],
            'Piercing':[self.piercing.get()],
            'Wear Contact Lens':[self.contactlense.get()]
        }
        X_test = pd.DataFrame(data)
        if(self.i.get() == 1):
            pickled_model_svm = pickle.load(open('KNN_Model.pkl', 'rb'))
            predicted_KNN = pickled_model_svm.predict(X_test)
            messagebox.showinfo("KNN Prediction is: ", predicted_KNN )
        else:
            pickled_model_svm = pickle.load(open('Perceptron.pkl', 'rb'))
            predictedperceptron = pickled_model_svm.predict(X_test)
            messagebox.showinfo("Perceptron Prediction is: ", predictedperceptron )
        return 0
     

a = Predictions()
prediction = Button(root, text="Add Attributes for Predictions", padx=10, pady=5,  bg="#263D42", fg='white', command=a.AddAttributes)
prediction.place(x=150, y=250)

root.mainloop()