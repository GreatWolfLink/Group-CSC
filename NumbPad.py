#### number pad ####
import tkinter as tk



class NumberPad():
    def __init__(self):

        text = ""

        window = tk.Tk()
        xspace=10
        yspace=10



        def Input(number):

            text = text + tk.StringVar().get()
            print(text)
    
        for row in range(1,5):
            tk.Grid.rowconfigure(window,row,weight=1)

        for column in range(1,3):
            tk.Grid.columnconfigure(window,row,weight=1)

        Label = tk.Label(window,text="",relief="solid",textvariable=text).grid(row=1,column=1,columnspan=3)
        One = tk.Button(window,text="1",command=lambda:Input("1")).grid(row=2,column=1,padx=xspace,pady=yspace)
        Two = tk.Button(window,text="2",command=lambda:Input("2")).grid(row=2,column=2,padx=xspace,pady=yspace)
        Three = tk.Button(window,text="3",command=lambda:Input("3")).grid(row=2,column=3,padx=xspace,pady=yspace)
        Four = tk.Button(window,text="4",command=lambda:Input("4")).grid(row=3,column=1,padx=xspace,pady=yspace)
        Five = tk.Button(window,text="5",command=lambda:Input("5")).grid(row=3,column=2,padx=xspace,pady=yspace)
        Six = tk.Button(window,text="6",command=lambda:Input("6")).grid(row=3,column=3,padx=xspace,pady=yspace)
        Seven = tk.Button(window,text="7",command=lambda:Input("7")).grid(row=4,column=1,padx=xspace,pady=yspace)
        Eight = tk.Button(window,text="8",command=lambda:Input("8")).grid(row=4,column=2,padx=xspace,pady=yspace)
        Nine = tk.Button(window,text="9",command=lambda:Input("9")).grid(row=4,column=3,padx=xspace,pady=yspace)
        Zero = tk.Button(window,text="0",command=lambda:Input("0")).grid(row=5,column=1,padx=xspace,pady=yspace)
        Decimal = tk.Button(window,text=".",command=lambda:Input(".")).grid(row=5,column=2,padx=xspace,pady=yspace)
        Negative = tk.Button(window,text="-",command=lambda:Input("-")).grid(row=5,column=3,padx=xspace,pady=yspace)


    
