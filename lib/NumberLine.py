from psychopy import visual,event
import wx,time,response1,myFuncN


def dialogresponse(myresponse):
    app = wx.App()
    dlg = response1.Response(myresponse)
    retval = dlg.ShowModal()
    if retval == wx.ID_OK:
        ss = dlg.text
    else:
        ss = dlg.text

    dlg.Destroy()
    # app.MainLoop()
    ss = ' '.join(ss.split())
    return ss
#------------------------------------------------------------------------------------
def timeOutScreen(w,hh):

    tempTxt1 = visual.TextStim(win=w, text='Time Out', height=hh / 12., pos=(0, hh / 20.),
                                                         color='Black',alignHoriz= 'center')
    tempTxt2 = visual.TextStim(win=w, text='Press any key to continue', height=hh / 20., pos=(0, -hh / 20.),
                                     color='Black',alignHoriz= 'center')
    tempTxt1.autoDraw = 1
    tempTxt2.autoDraw = 1
    w.flip()
    event.waitKeys()
    tempTxt1.autoDraw = 0
    tempTxt2.autoDraw = 0
def runNumberLine(w, Feats,ratio,dim,TimeOut,response):
    data ={}
    w1,h1 = dim[0],dim[1]
    leftR, rightR, centerR = ratio[0],ratio[1],ratio[2]
    ll,rr,cc = Feats[0],Feats[1],Feats[2]
    l1 = myFuncN.drawCompleteStim(w, ll[0], ll[1], ll[2],ll[3], ll[4][0],ll[4][1] , enclosed=0)
    r1 = myFuncN.drawCompleteStim(w, rr[0], rr[1], rr[2],rr[3], rr[4][0],rr[4][1] , enclosed=0)
    c1 = myFuncN.drawCompleteStim(w, cc[0], cc[1], cc[2],cc[3], cc[4][0],cc[4][1] , enclosed=0)
    c = [l1,r1,c1]
    newc = [item for sublist in c for item in sublist]

    low, high = round(leftR, 3) * 1000, round(rightR, 3) * 1000
    myRatingScale = visual.RatingScale(w, low=low, high=high, marker='triangle',
                                       tickMarks=[None], precision=1, stretch=1.2, tickHeight=1.5,
                                       labels=[2],
                                       markerColor='DarkRed', pos=(0, -h1 / 6),
                                       textColor="blue", textSize=1.2, lineColor='green', size=1,
                                       showAccept=True, showValue=False, acceptSize=0.8, acceptText='ClickMe',
                                       acceptPreText='clickLine')
    stime = time.time()

    if (TimeOut):
        while myRatingScale.noResponse and (time.time() - stime < TimeOut):
            myRatingScale.draw()
            w.flip()
        nR = myRatingScale.noResponse
    else:
        while myRatingScale.noResponse:
            # myItem.draw()
            myRatingScale.draw()
            w.flip()
        nR = myRatingScale.noResponse # true means no resposnse or not final click

    ptime = time.time() - stime
    data['Time_Played'] = ptime
    if myRatingScale.getRating() is None:
        data['Clicked_Ratio'] = 'NA'
    else:
        data['Clicked_Ratio'] = (myRatingScale.getRating()) / 1000.0

    for i in newc:
        i.autoDraw = 0
    myRatingScale.autoDraw = 0
    if nR:
        timeOutScreen(w, h1)
    if (response[0] == 11):
        res = dialogresponse(response[1])
        data['response'] = res
    else:
        data['response'] = ''
    return data
