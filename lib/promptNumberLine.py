import wx
import wx.calendar as cal
import datetime

class DatePicker(wx.DatePickerCtrl):
    def __init__(self, parent, dt, style=wx.DP_DEFAULT):
        super(DatePicker, self).__init__(parent, dt=dt, style=style)
        #self.SetInitialSize((120, -1))

class MyPrompt(wx.Dialog):
    ParticipantID = []
    SessionNumber = []
    ParticipantAge = []
    ParticipantGrade = []
    TimeOut = []
    InputFiles = []
    EventDate = []
    CheckBoxesStates = {'color':False}

    def __init__(self):
        wx.Dialog.__init__(self, None, wx.ID_ANY, title='Welcome')
        #add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        title = wx.StaticText(self.panel, wx.ID_ANY, 'Welcome to NumberLine Game')

        bmp = wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER, (16, 16))
        inputPIDIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelPID = wx.StaticText(self.panel, wx.ID_ANY, 'Participant ID')
        self.inputTxtPID = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        inputSNUMIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelSNUM = wx.StaticText(self.panel, wx.ID_ANY, 'Session #        ')
        self.inputTxtSNUM = wx.TextCtrl(self.panel, wx.ID_ANY,'')

        inputAgeIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelAge = wx.StaticText(self.panel, wx.ID_ANY, 'Age                    ')
        self.inputTxtAge = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        inputGradeIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelGrade = wx.StaticText(self.panel, wx.ID_ANY, 'Grade                ')
        self.inputTxtGrade = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        inputTimeoutIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelTimeout = wx.StaticText(self.panel, wx.ID_ANY, 'Timeout(s)      ')
        self.inputTxtTimeout = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        inputFilesIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelFiles = wx.StaticText(self.panel, wx.ID_ANY, 'Files(by \' ; \')     ')
        self.inputTxtFiles = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        self.colorOptCheckBox = wx.CheckBox(self.panel, wx.ID_ANY, 'Color')
        self.colorOptCheckBox.SetValue(False)
        self.colorOptCheckBox.Bind(wx.EVT_CHECKBOX, self.onColor)

        today = datetime.date.today().strftime('%B %d, %Y')
        labelDateDspIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelDateDisplay = wx.StaticText(self.panel, wx.ID_ANY, 'Today\'s date: '+today)
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        labelDateDisplay.SetFont(font)


        okBtn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
        # self.calendar.Bind(cal.EVT_CALENDAR_DAY, self.onCalSelected)

        topSizer          = wx.BoxSizer(wx.VERTICAL)
        titleSizer        = wx.BoxSizer(wx.HORIZONTAL)
        inputPIDSizer     = wx.BoxSizer(wx.HORIZONTAL)
        inputSNUMSizer    = wx.BoxSizer(wx.HORIZONTAL)
        inputAgeSizer     = wx.BoxSizer(wx.HORIZONTAL)
        inputGradeSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputTimeoutSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFilesSizer   = wx.BoxSizer(wx.HORIZONTAL)
        infoDateDspSizer  = wx.BoxSizer(wx.HORIZONTAL)


        colorChkBoxSizer  = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer          = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)

        inputPIDSizer.Add(inputPIDIco, 0, wx.ALL, 5)
        inputPIDSizer.Add(labelPID, 0, wx.ALL, 5)
        inputPIDSizer.Add(self.inputTxtPID, 1, wx.ALL|wx.EXPAND, 5)

        inputSNUMSizer.Add(inputSNUMIco, 0, wx.ALL, 5)
        inputSNUMSizer.Add(labelSNUM, 0, wx.ALL, 5)
        inputSNUMSizer.Add(self.inputTxtSNUM, 1, wx.ALL|wx.EXPAND, 5)

        inputAgeSizer.Add(inputAgeIco, 0, wx.ALL, 5)
        inputAgeSizer.Add(labelAge, 0, wx.ALL, 5)
        inputAgeSizer.Add(self.inputTxtAge, 1, wx.ALL|wx.EXPAND, 5)

        inputGradeSizer.Add(inputGradeIco, 0, wx.ALL, 5)
        inputGradeSizer.Add(labelGrade, 0, wx.ALL, 5)
        inputGradeSizer.Add(self.inputTxtGrade, 1, wx.ALL|wx.EXPAND, 5)

        inputTimeoutSizer.Add(inputTimeoutIco, 0, wx.ALL, 5)
        inputTimeoutSizer.Add(labelTimeout, 0, wx.ALL, 5)
        inputTimeoutSizer.Add(self.inputTxtTimeout, 1, wx.ALL | wx.EXPAND, 5)

        inputFilesSizer.Add(inputFilesIco, 0, wx.ALL, 5)
        inputFilesSizer.Add(labelFiles, 0, wx.ALL, 5)
        inputFilesSizer.Add(self.inputTxtFiles, 1, wx.ALL|wx.EXPAND, 5)


        colorChkBoxSizer.Add(self.colorOptCheckBox, 1, wx.ALL|wx.EXPAND, 5)


        infoDateDspSizer.Add(labelDateDspIco, 0, wx.ALL, 5)
        infoDateDspSizer.Add(labelDateDisplay, 0, wx.ALL, 5)

        # inputDateSizer.Add(inputDateIco, 0, wx.ALL, 5)
        # inputDateSizer.Add(self.labelDate, 0, wx.ALL, 5)
        # inputDateSizer.Add(self.calendar, 0, wx.ALL, 0)

        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self.panel,), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputPIDSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputSNUMSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputAgeSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputGradeSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputTimeoutSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFilesSizer, 0, wx.ALL|wx.EXPAND, 5)

        topSizer.Add(colorChkBoxSizer, 0, wx.ALL|wx.EXPAND, 5)

        topSizer.Add(infoDateDspSizer, 0, wx.ALL|wx.EXPAND, 5)
        # topSizer.Add(inputDateSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)

    # def onCalSelected(self, event):
    #     date = self.calendar.GetDate()
    #     day = date.GetDay()
    #     month = date.GetMonth()+1
    #     year = date.GetYear()
    #     ds = "%02d/%02d/%d" % (month, day, year)
    #     if len(MyPrompt.EventDate) == 0:
    #         MyPrompt.EventDate.append(ds)
    #     else:
    #         MyPrompt.EventDate[0] = ds
    #     self.labelDate.SetLabel(ds)

    # Checkboxes handlers

    def onColor(self, event):
        sender = event.GetEventObject()
        isChecked = sender.GetValue()
        if isChecked:
            print 'color'
            MyPrompt.CheckBoxesStates['color'] = True
        elif not sender.IsChecked:
            MyPrompt.CheckBoxesStates['color'] = False


    def onOK(self, event):
        # Do something
        print 'onOK handler'
        if len(MyPrompt.ParticipantID) == 0:
            MyPrompt.ParticipantID.append(self.inputTxtPID.GetValue())
        else:
            MyPrompt.ParticipantID[0] = self.inputTxtPID.GetValue()

        if len(MyPrompt.SessionNumber) == 0:
            MyPrompt.SessionNumber.append(self.inputTxtSNUM.GetValue())
        else:
            MyPrompt.SessionNumber[0] = (self.inputTxtSNUM.GetValue())

        if len(MyPrompt.ParticipantAge) == 0:
            MyPrompt.ParticipantAge.append(self.inputTxtAge.GetValue())
        else:
            MyPrompt.ParticipantAge[0] = (self.inputTxtAge.GetValue())

        if len(MyPrompt.ParticipantGrade) == 0:
            MyPrompt.ParticipantGrade.append(self.inputTxtGrade.GetValue())
        else:
            MyPrompt.ParticipantGrade[0] = (self.inputTxtGrade.GetValue())

        if len(MyPrompt.InputFiles) == 0:
            MyPrompt.InputFiles.append(self.inputTxtFiles.GetValue())
        else:
            MyPrompt.InputFiles[0] = (self.inputTxtFiles.GetValue())

        if len(MyPrompt.EventDate) == 0:
            ds = datetime.datetime.today().strftime('%Y-%m-%d')
            MyPrompt.EventDate.append(ds)

        if len(MyPrompt.TimeOut) == 0:
            MyPrompt.TimeOut.append(self.inputTxtTimeout.GetValue())
        else:
            MyPrompt.TimeOut[0] = self.inputTxtTimeout.GetValue()
        # else:
        #     MyPrompt.EventDate[0] = (self.EventDate.GetValue())

        self.EndModal(wx.ID_OK) #returns numeric code to caller

    #    print MyPrompt.ParticipantID
    #    print MyPrompt.SessionNumber
    #    print MyPrompt.ParticipantAge
    #    print MyPrompt.ParticipantGrade
    #    print MyPrompt.InputFiles
    #    print MyPrompt.EventDate

    def onCancel(self, event):
        self.EndModal(wx.ID_CANCEL) #returns numeric code to caller
        # self.Destroy()
        # self.closeProgram()

    def closeProgram(self):
        self.Close()

# Run the program
if __name__ == '__main__':
    app = wx.App()
    dlg = MyPrompt()
    retval = dlg.ShowModal()
    if retval == wx.ID_OK:
        # print len(dlg.TimeOut) is always 1
        # print dlg.TimeOut[0]==''
        # print dlg.CheckBoxesStates
        # print dlg.ParticipantGrade
        if (dlg.TimeOut[0]):
            s1= int(dlg.TimeOut[0])
        else:
            s1= 0

        print s1
        dlg.Destroy()
    app.MainLoop()
