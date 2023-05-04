import tkinter



def main():
    
    tk = tkinter.Tk()
    tk.geometry("400x300")
    m_enab = int()
    what_we_have_text = tkinter.Label(text = "Що ми маємо?   Відміть відповідні велечини")
    m = tkinter.Checkbutton(text = "Маса",variable=m_enab)
    
    
    
    what_we_have_text.grid(column=0,row=0)
    m.grid(column=0,row=1,sticky="w")
    tk.mainloop()
    
    
if __name__ == "__main__":
    main()