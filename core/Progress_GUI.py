import PySimpleGUI as sg
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, Canvas, Column, Col, Combo, Frame, FileBrowse, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Sizer

import cv2

from conf.config import *

def ViewGUI():
    sg.theme('LightGreen')

    col1 = Column([
        [Frame('base function',[[Column([[
                        Text(r'VideoFile',size=(10,1)),
                        InputText(''*15, key="VideoFile"),
                        FileBrowse(target='VideoFile', size=(10,1)),
                        Button('start',key='start', size=(10,1)),
                        Button('stop',key='stop', size=(10,1)),
                        Button('Exit',key= 'exit', size=(10,1)),]],
                   size=(800,45), pad=(0, 0))]])],
        [Frame('videoplay',[[Column([[Image(filename='', key='image',)]],
                   size=(800,500), pad=(0, 0))
               ]])]
    ], pad=(0,0))


    col2 = Column([
        [Frame('results',
               [[Column(
                   [
                       [Image(filename='', key='image1', size=(200,100)), Button('view', size=(6,1)), Button('close', size=(6,1))],
                       [Image(filename='', key='image2', size=(200,100)), Button('view', size=(6,1)), Button('close', size=(6,1))],
                       [Image(filename='', key='image3', size=(200,100)), Button('view', size=(6,1)), Button('close', size=(6,1))],
                       [Image(filename='', key='image4', size=(200,100)), Button('view', size=(6,1)), Button('close', size=(6,1))],
                       [Image(filename='', key='image5', size=(200,100)), Button('view', size=(6,1)), Button('close', size=(6,1))],
                   ]
               ,size=(400,560))
                 ]]
               )]
    ])

    layout = [[col1,col2]]
    # layout = [
    #     [sg.Text(r'机器视觉原型系统', size=(40,1), justification='center')],
    #     [sg.Text(r'VideoFile',size=(10,1)), sg.InputText(''*30, key="VideoFile"), sg.FileBrowse(size=(10,1)),
    #      sg.Button('start',key='start', size=(10,1)), sg.Button('stop',key='stop', size=(10,1)), sg.Button('end', key='end', size=(10,1)),
    #      sg.Button('Exit',key= 'exit', size=(10,1))],
    #     [sg.Image(filename='', key='image')],
    # ]

    window = sg.Window(
        '机器视觉',
        layout,
        location=(100,100),
        finalize=True
    )
    return window

def main():
    window = ViewGUI()
    event, values = window.read()
    videofile = filename

    videofile = values['VideoFile']
    if videofile == '':

    cap = cv2.VideoCapture(videofile)

    # picture_list = [window['image1'],window['image2'],window['image3'],window['image4'],window['image5']]

    while True:
        event, values = window.read(timeout=0)
        # print(event, values)
        if event in (None, 'Exit'):
            break

        if event == 'start':
            flag = True
            while flag:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)

                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                window['image'].update(data=imgbytes)
                if event == 'stop':
                    flag = False
                sg.popup()

    window.close()


if __name__=='__main__':
    main()