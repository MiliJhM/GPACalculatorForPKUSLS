import os
import tkinter
from tkinter import filedialog

import pandas as pd

from generator import generate
from praser import prase

if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()
    while True:
        file_path = filedialog.askopenfilename(filetypes=[("Excel", ".xlsx")])
        if file_path.endswith(".xlsx"):
            input = pd.read_excel(file_path)
            try:
                input = prase(input)
            except:
                print("Cannot prase the file, check the file format.")
                continue
            result = generate(input)
            break
        else:
            print("Cannot open file or file is not supported.(need .xlsx file)")
    root.deiconify()
    max_w, max_h = root.maxsize()
    root.geometry(f'500x300+{int((max_w - 500) / 2)}+{int((max_h - 300) / 2)}')
    root.resizable(width=False, height=False)
    
    # 居中打印result（换算绩点、优秀率、优良率、及格率）到root窗口
    tkinter.Label(root, text="换算绩点").grid(row=0, column=0)
    tkinter.Label(root, text="优秀率").grid(row=0, column=1)
    tkinter.Label(root, text="优良率").grid(row=0, column=2)
    tkinter.Label(root, text="及格率").grid(row=0, column=3)
    for i in range(len(result)):
        tkinter.Label(root, text=result.iloc[i, 3]).grid(row=i + 1, column=0)
        tkinter.Label(root, text=result.iloc[i, 0]).grid(row=i + 1, column=1)
        tkinter.Label(root, text=result.iloc[i, 1]).grid(row=i + 1, column=2)
        tkinter.Label(root, text=result.iloc[i, 2]).grid(row=i + 1, column=3)
    root.mainloop()
