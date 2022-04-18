import wx


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        info_sizer = wx.BoxSizer(wx.HORIZONTAL)
        status_box = wx.StaticBox(self, wx.ID_ANY, size=(500, 300), label="Status:")
        status_box_sizer = wx.StaticBoxSizer(status_box, wx.VERTICAL)

        btn_data = [("Check updates", btn_sizer, self.check_updates),
                    ("Download files", btn_sizer, self.download_files)]
        for data in btn_data:
            label, sizer, handler = data
            self.btn_builder(label, sizer, handler)

        self.status_text = wx.StaticText(status_box, wx.ID_ANY, label="It works!", style=wx.ALIGN_CENTER)
        status_box_sizer.Add(self.status_text, wx.ID_ANY, wx.TOP, 10)

        krl_logo_img = wx.Image("../img/krl_logo.png", wx.BITMAP_TYPE_PNG)
        krl_logo_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(krl_logo_img))

        info_sizer.Add(krl_logo_bitmap, wx.ALL | wx.ALIGN_LEFT, 5)
        info_sizer.Add(status_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        authors_text = wx.StaticText(self, wx.ID_ANY, label="KRL Updater made by K. Szpieg && H. Szolc",
                                          style=wx.ALIGN_CENTER)
        font = wx.Font(9, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        authors_text.SetFont(font)

        main_sizer.Add(info_sizer, wx.ALIGN_TOP, 5)
        main_sizer.Add(authors_text, wx.ALIGN_CENTER, 5)
        main_sizer.Add(btn_sizer, wx.ALIGN_BOTTOM, 5)
        self.SetSizer(main_sizer)

    def btn_builder(self, label, sizer, handler):
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, handler)
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

    def check_updates(self, event):
        self.status_text.SetLabel("check updates btn")

    def download_files(self, event):
        self.status_text.SetLabel("download files btn")


class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(parent=None, title="KRL Updater")
        self.panel = MainPanel(self)
        screensize = wx.DisplaySize()
        w = screensize[0] * 0.20
        h = screensize[1] * 0.15
        self.SetMinSize(self.GetSize())
        size = (int(w), int(h))
        size2 = ((size[0] * 2), (size[1] * 2))
        self.SetInitialSize(size)
        self.SetMaxSize(size2)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
