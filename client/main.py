import tkinter as tki
import client.frame.home as fHomeMod
import client.asset.font as fontMod

def RunGUI():
    root = tki.Tk()
    fontMod.Font.Initialize(root)
    root.title("Tic Tac Royale")
    root.resizable(width=False, height=False)
    home = fHomeMod.Home(root)
    home.show()
    root.mainloop()

RunGUI()