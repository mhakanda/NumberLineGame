import wx
import wx.calendar as cal
import datetime

class Response(wx.Dialog):
    text=[]
    def __init__(self,myword):
        pp = .7
        size = (wx.GetDisplaySize()[0] * pp, wx.GetDisplaySize()[1] * pp)
        wx.Dialog.__init__(self, None, wx.ID_ANY, title='Response',size=size)
        #add a panel so it looks correct on all platforms
        # self.panel = wx.Panel(self, wx.ID_ANY,size=size)
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        font1 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        font2 = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True)
        # font3 = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True)

        # st = wx.StaticText(panel, -1, "Please write your response")
        st = wx.StaticText(panel, -1, myword)
        # st.SetBackgroundColour('green')
        st.SetFont(font1)
        vbox.Add(st, 1, wx.ALIGN_CENTER | wx.ALL, 9)
        ps = 500*pp
        self.tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(ps, ps))
        # self.tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, 300))
        # tc.SetBackgroundColour('green')
        # st.SetFont(font3)
        vbox.Add(self.tc, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)

        # okBtn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        # cancelBtn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')
        # self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        # self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        b1 = wx.Button(panel, wx.ID_ANY, "Submit", size=(120, 10))
        # b1 = wx.Button(panel, wx.ID_ANY, "Submit")
        # b1 = wx.Button(panel, wx.ID_ANY, label="Submit", size=(120, 10))
        b1.SetFont(font2)
        # c1 = wx.Button(panel, wx.ID_ANY, "Cancle", size=(120, 10))
        # c1.SetFont(font2)
        # hbox.Add(b1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        # hbox.Add(c1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        # vbox.Add(hbox, 10, wx.ALIGN_CENTER | wx.ALL, 5)
        vbox.Add(b1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        # vbox.Add(b1, 1, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALL, 5)
        b1.Bind(wx.EVT_BUTTON, self.submitNow)

        panel.SetSizer(vbox)
        self.Center()
        # self.Show()
    # def onCancel(self, event):
    #     self.EndModal(wx.ID_CANCEL) #returns numeric code to caller
    #     # self.Destroy()
    #     # self.closeProgram()
    #
    # def closeProgram(self):
    #     self.Close()
    def submitNow(self, event):
        # self.text.append(self.tc.GetValue())
        self.text = self.tc.GetValue()
        # self.text = self.tc.GetValue()
        self.EndModal(wx.ID_OK)
        # self.Close()
# Run the program
if __name__ == '__main__':
    app = wx.App()
    dlg = Response('Please')
    retval = dlg.ShowModal()
    if retval == wx.ID_OK:
        ss = dlg.text
    else:
        ss = dlg.text

    dlg.Destroy()
    app.MainLoop()
    # ss = ss.replace('\n',' ')
    # ss = ss.replace('\t', ' ')
    ss = ' '.join(ss.split())

    print type(ss)