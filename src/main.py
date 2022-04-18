import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="KRL Updater")
        screensize = wx.DisplaySize()
        w = screensize[0] * 0.4
        h = screensize[1] * 0.3
        self.SetMinSize((w, h))
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
