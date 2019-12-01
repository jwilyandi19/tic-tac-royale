import tkinter.font as ttf
import tkinter as ttk

class Font:

    TitleFont = None
    NormalFont = None
    MenuButtonFont = None

    @staticmethod
    def Initialize(tk: ttk.Tk):
        Font.TitleFont = ttf.Font(tk, family="Roboto", size=20, weight="bold")
        Font.NormalFont = ttf.Font(tk, family="Roboto", size=12)
        Font.MenuButtonFont = ttf.Font(tk, family="Roboto", size=16)