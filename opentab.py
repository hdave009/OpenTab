import webbrowser
import opentabdb as db
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("OpenTab")

course_text = StringVar()
url_text = StringVar()
url_selected = None


def populateURLList(urls):
    url_lb.delete(0, END)
    url_lb.insert(END, *urls)


def open_tabs_command():
    urls = db.get_course_urls(course_text.get())
    populateURLList(urls)
    for url in urls:
        try:
            webbrowser.open(url)
        except:
            continue


def view_urls_command():
    urls = db.get_course_urls(course_text.get())
    populateURLList(urls)


def add_urls_command():
    course = course_text.get()
    url = url_text.get()
    if (course == ''):
        messagebox.askokcancel(
            "Invalid entry", "Please enter a course and URL.")
    else:
        db.add_course_urls(course, [url])
        populateURLList([f"Added {course} and URL:", db.url_format(url)])


def onselect(e):
    global url_selected
    url_selected = url_lb.selection_get()


def del_url_command():
    course = course_text.get()
    if (course == ''):
        messagebox.askokcancel(
            "Invalid entry", "Please enter a course and select URL")
    else:
        db.del_url(course, url_selected)
        populateURLList(db.get_course_urls(course))


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

l1 = Label(window, text="Course")
l1.grid(row=0, column=0)

l2 = Label(window, text="URL")
l2.grid(row=0, column=2)

course_entry = Entry(window, textvariable=course_text)
course_entry.grid(row=0, column=1)

url_entry = Entry(window, textvariable=url_text)
url_entry.grid(row=0, column=3)

url_lb = Listbox(window, height=6, width=35)
url_lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

url_lb.configure(yscrollcommand=sb1.set)
sb1.configure(command=url_lb.yview)

url_lb.bind('<<ListboxSelect>>', onselect)
#url_lb.bind('<FocusOut>', lambda e: url_lb.selection_clear(0, END))

opentabs_btn = Button(window, text="Open Tabs", width=12,
                      command=open_tabs_command)
opentabs_btn.grid(row=2, column=3)

search_btn = Button(window, text="View URLs", width=12,
                    command=view_urls_command)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text="Add course/url",
                 width=12, command=add_urls_command)
add_btn.grid(row=4, column=3)

del_btn = Button(window, text="Delete course/url",
                 width=12, command=del_url_command)
del_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=12, command=window.destroy)
close_btn.grid(row=7, column=3)

window.mainloop()
