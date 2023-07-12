
from tkinter import *
import webview

tk = Tk()

a = "DAKO"

webview.create_window( '.:: DAKO System ::.', 'http://127.0.0.1/web/doctorlogin.php',width=999900, height=999900,resizable=False,x=-10, y=0, )

webview.start()