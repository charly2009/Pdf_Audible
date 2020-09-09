from tkinter import*
from ttkthemes import ThemedTk
import pyttsx3
import PyPDF2
import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

root =ThemedTk(theme="radiance")
root.geometry('500x400')
root.title('AudioBook')
root.iconbitmap('age.ico')
#root.config(background='yellow')

global file

playlistbox = Listbox(root, width= 40, background='yellow')

playlistbox.pack(pady=30, padx=30)
playlist = []
def delete():
    try:
        global selected
        selected = playlistbox.curselection()
        selected = int(selected[0])
        playlistbox.delete(selected)

        choices=messagebox.askquestion('Warning', 'Are You Sure To Delete The File ')
        if choices == 'yes':
            messagebox.showinfo('w','thanks')
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    except:
        pass

def open():
    try:
        global filename_path
        global filename
        #load.configure(text='hello')
        filename_path= filedialog.askopenfilenames(defaultextension='.pdf', filetypes=[('PDF FILE' ,'*.pdf') ])
        filename = filename_path
        file = os.path.basename(filename[0])
        #messagebox.showinfo('Files Uploaded', file)

        add_to_playlist(file)
    except:
        messagebox.showwarning('Error', ' Please upload a file')


def add_to_playlist(file):

    index = 0
    playlistbox.insert(index, file)
    index += 1

global selected_song

def read():

    try:
        selected= playlistbox.curselection()
        filet = playlistbox.get(selected)
        pdfreader = PyPDF2.PdfFileReader(filet)
        pages = pdfreader.numPages  ## check the numbers of page
        page = pdfreader.getPage(35)  ## get the page 10
        text = page.extractText()  # extract text from page 10
        print(f'there are {pages}  pages ')  ## print it
        print(text)
        speaker = pyttsx3.init()  # speaker initiliazer
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', 105)
        speaker.setProperty('voices','')  # changing index, changes voices. o for male
        speaker.save_to_file(text, 'test.mp3')  # it in mp3 format audio
        speaker.say(text)  # read it

        speaker.runAndWait()

    except:
            messagebox.showwarning('Error', 'Please select a file ')


load = ttk.Button(root, text='Upload', command= open)
load.pack(padx=100)

deletebuttton = ttk.Button(root, text='Delete', command= delete)
deletebuttton.pack(padx=100)

readbuttton = ttk.Button(root, text='Read', command= read)
readbuttton.pack(padx=100)


root.mainloop()

