# -- coding: utf-8 --

from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext 
from tkinter.ttk import *
import os
import json
import fortune

default_conf = {
    'cookie_path' : './cookies/default_cookies.txt',
    'bg' : './backgrounds/neon.jpg',
    'enable_bg' : 0
    }

if os.path.exists('config.json') == False:
    open('config.json', 'w', encoding = "utf-8")
    with open('config.json', 'w') as conf:
        json.dump(default_conf, conf, indent = 4, sort_keys = True)

fortune_window = Tk()
fortune_window.withdraw()
icon = PhotoImage(file = 'res/icon.png')
fortune_window.title('Fortune')
fortune_window.iconphoto(False, icon)

def load_opt():
    options_window = Toplevel(fortune_window)
    options_window.iconphoto(False, PhotoImage(file='res/setting-icon.png'))

    # options_window.withdraw() # hide root window

    def select_cookie():
        cookie_path = filedialog.askopenfilename(title = "Select your cookie file:",
                                                 filetypes = [("Text", "*.txt"),
                                                              ("Data", "*.dat")])
        current_folder = os.path.dirname(os.path.abspath(__file__))
        current_folder = current_folder.replace('\\', '/', -1)
        cookie_path = cookie_path.replace(current_folder, '.', 1)

        with open('config.json', 'r', encoding = "utf-8") as conf:
            data = json.load(conf)
            data['cookie_path'] = cookie_path
            entry_cookie_path.delete(0, 'end')
            entry_cookie_path.insert(0, cookie_path)
            with open('config.json', 'w+', encoding = "utf-8") as conf:
                json.dump(data, conf, indent = 4, sort_keys = True)

    def select_bg():
        bg_path =  filedialog.askopenfilename(title = "Select your background image:",
                                                 filetypes = [("PNG", "*.png"),
                                                              ("JPG", "*.jpg"),
                                                              ("GIF", "*.gif"),
                                                              ("All Files", "*.*")])
        current_folder = os.path.dirname(os.path.abspath(__file__))
        current_folder = current_folder.replace('\\', '/', -1)
        bg_path = bg_path.replace(current_folder, '.', 1)
        with open('config.json', 'r', encoding = "utf-8") as conf:
            data = json.load(conf)
            data['bg'] = bg_path
            entry_bg_path.delete(0, 'end')
            entry_bg_path.insert(0, bg_path)
            with open('config.json', 'w+', encoding = "utf-8") as conf:
                json.dump(data, conf, indent = 4, sort_keys = True)

        '''
        try:
            conf = open('conf.cfg', 'w')
            conf.write(cookie_path)
        finally:
            if conf:
                conf.close()
        '''
    
    def add_cookie2file(text):
        with open('config.json', 'r', encoding = "utf-8") as conf:
            data = json.load(conf)
            cookie_path = data['cookie_path']
        with open(cookie_path, 'a', encoding = "utf-8") as cookie:
            cookie.write('%\n')
            cookie.write(text)
            text_box.delete('0.0','end')


    def import_from_file():
        with open('config.json', 'r', encoding = "utf-8") as conf:
            data = json.load(conf)
            cookie_path = data['cookie_path']
            
        path = filedialog.askopenfilename(title = "Select file to import:",
                                          filetypes = [("Text", "*.txt"),
                                                       ("Data", "*.dat")])
        with open(path, 'r', encoding = "utf-8") as file:
            cookies = file.read()

        with open(cookie_path, 'a', encoding = "utf-8") as cookie:
            cookie.write('%\n')
            cookie.write(cookies)

    def reset_bg():
        entry_bg_path.delete(0, 'end')
        entry_bg_path.insert(0, './backgrounds/neon.jpg')

        with open('config.json', 'r', encoding = "utf-8") as conf:
            data = json.load(conf)
            data['bg'] = './backgrounds/neon.jpg'
            with open('config.json', 'w+', encoding = "utf-8") as conf:
                json.dump(data, conf, indent = 4, sort_keys = True)

    ############################- Load option window -###################################
    options_window.attributes('-topmost', True)
    options_window.geometry('320x320')
    options_window.title('Options')
    options_window.attributes('-topmost', False)
    options_tabs = Notebook(options_window)
        
    frame_gen = Frame(options_tabs)
    frame_about = Frame(options_tabs)
    frame_appear = Frame(options_tabs)
    
    options_tabs.add(frame_gen, text = 'General')
    options_tabs.add(frame_appear, text = 'Appearance')
    options_tabs.add(frame_about, text = 'About')
    options_tabs.pack(padx = 10, pady = 5, fill = BOTH, expand = True)

    ############################- General -#############################
    label_cookie_path = Label(frame_gen, text = 'Set cookie path:')
    label_cookie_path.place(x = 10, y = 10)
    
    entry_cookie_path = Entry(frame_gen, width = 40)
    entry_cookie_path.place(x = 10, y = 30)
    with open('config.json', 'r', encoding = "utf-8") as conf:
        data = json.load(conf)
        cookie_path = data['cookie_path']
        entry_cookie_path.insert(0, cookie_path)
    
    browse_file = Button(frame_gen, text = '...', command = select_cookie)
    browse_file.place(x = 260, y = 28)
    browse_file.config(width = 3)
    
    label_add_cookie = Label(frame_gen, text = 'Add Cookie to file')
    label_add_cookie.place(x = 10, y = 55)
    '''
    scroll = Scrollbar(frame_gen)
    scroll.place(x = 50, y = 300)
    '''
    text_box = scrolledtext.ScrolledText(frame_gen, height = 9, width = 33)
    text_box.place(x = 10, y = 75)
    '''
    scroll.config(command=text_box.yview)   #bind the text box
    text_box.config(yscrollcommand=scroll.set)  #bind the scroll bar
    '''
    label_notice = Label(frame_gen,
                         text = 'Tip: Cookies should be separated by %')
    label_notice.place(x = 10, y = 230)
    
    add_cookie = Button(frame_gen,
                        text = 'Add',
                        command =
                        lambda: add_cookie2file(text_box.get('0.0', 'end')))
    
    add_cookie.place(x = 215, y = 250)

    import_from_file = Button(frame_gen,
                              text = 'Import from file...',
                              command = import_from_file)
    import_from_file.place(x = 110, y = 250)
    
    ###################################- Appearance -##############################################
    label_bg = Label(frame_appear, text = 'Set Background Image:')
    label_bg.place(x = 10, y = 10)

    rst_bg = Button(frame_appear, image = rst_ico, compound = LEFT, command = reset_bg)
    rst_bg.place(x = 235, y = 28)
    rst_bg.config(width = 0.5)

    entry_bg_path = Entry(frame_appear, width = 36)
    entry_bg_path.place(x = 10, y = 30)

    with open('config.json', 'r', encoding = "utf-8") as conf:
        data = json.load(conf)
        bg_path = data['bg']
        entry_bg_path.insert(0, bg_path)

    browse_bg = Button(frame_appear, text = '...', command = select_bg)
    browse_bg.place(x = 265, y = 28)
    browse_bg.config(width = 3)
    ###################################- About -###################################################
    label_icon = Label(frame_about, image = icon)
    label_icon.place(x = 10, y = 0)
    label_name = Label(frame_about, text = 'pyFortune-GUI', font = ('', 20))
    label_name.place(x = 80, y = 10)
    label_author = Label(frame_about,
                         text = """Author: Theodore Cooper
                                \nWebsite: https://theodorecooper.github.io/
                                \nGithub: @theodorecooper
                                \nEmail: ccooperr2005@gmail.com
                                \nBased on python 3.9.6, Windows 10(x64,21H1) & tkinter
                                """)
    label_author.place(x = 10, y = 70)
    ######################################################################################
    
    
        
def goto_options():
    load_opt()
    
with open('config.json', 'r', encoding = "utf-8") as conf:
    data = json.load(conf)
    cookie_path = data['cookie_path']

cookie = fortune.get_random_fortune(cookie_path)


Label(fortune_window,
      #width = 40,
      text = cookie,
      wraplength = 480,
      justify = 'left',
      font = ('', 15)).pack(side = LEFT, padx = 10, pady = 10),

# load icons
setting_ico = PhotoImage(file = r'res/setting-icon.png').subsample(20, 20)
exit_ico = PhotoImage(file = r"res/exit-icon.png").subsample(20, 20)
rst_ico = PhotoImage(file = r'res/rst-icon.png').subsample(35, 35)

Button(fortune_window,
       text = 'Options',
       image = setting_ico,
       compound = LEFT,
       command = goto_options).pack(side = TOP)

Button(fortune_window,
       text = 'Exit',
       image = exit_ico,
       compound = LEFT,
       command = exit).pack(side = TOP)

fortune_window.resizable(0, 0)
fortune_window.deiconify()

mainloop()
