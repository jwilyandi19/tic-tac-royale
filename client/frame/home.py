import tkinter as tki
import tkinter.font as tkf
import tkinter.ttk as ttk
import client.asset.font as fontMod

class Home:
    def __init__(self, root: tki.Tk):
        self.frame = ttk.Frame(root, width=800, height=600)
        title = ttk.Label(
            self.frame, 
            text="Tic Tac Royale",
            font=fontMod.Font.TitleFont)
        title.place(x=400-title.winfo_reqwidth()/2, y=20)
        nameFrame = self.buildNameFrame()
        nameFrame.place(x=400-nameFrame.winfo_reqwidth()/2, y=100)
        menuFrame = self.buildMenuFrame()
        menuFrame.place(x=400-menuFrame.winfo_reqwidth()/2, y=200)
        exitBtn = tki.Button(self.frame, text="Keluar", width=20)
        exitBtn.place(x=800 - exitBtn.winfo_reqwidth() - 20, y=600 - exitBtn.winfo_reqheight() - 20)
        self.frame.grid()
        self.hide()

    def buildNameFrame(self) -> tki.Widget:
        nameFrame = ttk.Frame(self.frame)
        nameEntry = ttk.Entry(nameFrame, width=20, font=fontMod.Font.NormalFont)
        nameEntry.grid(column=1, row=0, columnspan=2)
        nameLabel = ttk.Label(
            nameFrame,
            text="Name",
            font=fontMod.Font.NormalFont
            )
        nameLabel.grid(column=0, row=0, padx=10)
        nameLabel.update()
        return nameFrame

    def buildMenuFrame(self) -> tki.Widget:
        menuFrame = ttk.Frame(self.frame)
        newRoomBtn = tki.Button(menuFrame, text="Buat Ruangan", width=30, height=1, font=fontMod.Font.MenuButtonFont)
        newRoomBtn.pack(pady=5)
        joinRoomBtn = tki.Button(menuFrame, text="Ikuti Ruangan", width=30, height=1, font=fontMod.Font.MenuButtonFont)
        joinRoomBtn.pack(pady=5)
        viewBtn = tki.Button(menuFrame, text="Penonton", width=30, height=1, font=fontMod.Font.MenuButtonFont)
        viewBtn.pack(pady=5)
        menuFrame.update()
        return menuFrame

    def show(self):
        self.frame.grid()

    def hide(self):
        self.frame.grid_remove()
        
