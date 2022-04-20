import wx
import krl_ftpservices as krl


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        info_sizer = wx.BoxSizer(wx.HORIZONTAL)
        box_w = screensize[0] * 0.14
        box_h = screensize[1] * 0.1
        box_size = (int(box_w), int(box_h))
        status_box = wx.StaticBox(self, wx.ID_ANY, size=box_size, label="Status:")
        status_box_sizer = wx.StaticBoxSizer(status_box, wx.VERTICAL)

        # Create buttons
        check_updates_btn = wx.Button(self, label="Check updates")
        check_updates_btn.Bind(wx.EVT_BUTTON, self.check_updates)

        self.download_files_btn = wx.Button(self, label="Download files")
        self.download_files_btn.Bind(wx.EVT_BUTTON, self.download_files)
        self.download_files_btn.Disable()

        btn_sizer.Add(check_updates_btn, 0, wx.ALL | wx.CENTER, 5)
        btn_sizer.Add(self.download_files_btn, 0, wx.ALL | wx.CENTER, 5)

        # Create Status box
        self.status_text = wx.StaticText(status_box, wx.ID_ANY, label="It works!", style=wx.ALIGN_CENTER)
        status_box_sizer.Add(self.status_text, wx.ID_ANY, wx.TOP, 10)

        # Add KRL logo
        img_scale = size[0] - box_size[0] + 15

        krl_logo_img = wx.Image("../img/krl_logo.png", wx.BITMAP_TYPE_PNG)
        krl_logo_img = krl_logo_img.Scale(img_scale, img_scale, wx.IMAGE_QUALITY_HIGH)
        krl_logo_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(krl_logo_img))

        # Set up top section (logo and box)
        info_sizer.Add(krl_logo_bitmap, wx.ALL | wx.ALIGN_LEFT, 5)
        info_sizer.Add(status_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        # Add authors
        authors_text = wx.StaticText(self, wx.ID_ANY, label="KRL Updater made by K. Szpieg && H. Szolc",
                                     style=wx.ALIGN_CENTER)
        font = wx.Font(9, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        authors_text.SetFont(font)

        # Set up window's elements
        main_sizer.Add(info_sizer, wx.ALIGN_TOP, 5)
        main_sizer.Add(authors_text, wx.ALIGN_CENTER, 5)
        main_sizer.Add(btn_sizer, wx.ALIGN_BOTTOM, 5)
        self.SetSizer(main_sizer)

    def check_updates(self, event):
        krl.connect_to_ftp_server()
        self.download_files_btn.Enable()
        wx.MessageBox("Updates loaded...", 'Info', wx.OK | wx.ICON_INFORMATION)

    def download_files(self, event):
        krl.download_btn_functionality()
        wx.MessageBox("Update download successfully", 'Info', wx.OK | wx.ICON_INFORMATION)


class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(parent=None, title="KRL Updater")
        self.panel = MainPanel(self)
        self.SetMinSize(size)
        size2 = ((size[0] * 2), (size[1] * 2))
        self.SetInitialSize(size)
        self.SetMaxSize(size2)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    screensize = wx.DisplaySize()
    w = screensize[0] * 0.2
    h = screensize[1] * 0.15
    size = (int(w), int(h))
    frame = MainFrame()
    app.MainLoop()
