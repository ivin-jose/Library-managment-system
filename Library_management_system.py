# IMPORTED MODULES
from tkinter import *
import tkinter as tk
import sqlite3
import datetime

window = Tk()
window.title('LIBRARY MANAGEMENT SYSTEM ')
window.geometry('650x580')

tmp_name = 'no data'
tmp_class = 'no data'
tmp_num = 'no data'
tmp_date = 'no data'

# DATABASE CREATION AND CONNECTION

conn = sqlite3.connect('library_database1.db')
c = conn.cursor()
'''creating tables in databse to store datas
just command this below table if error happend'''

#c.execute("""CREATE TABLE user_details1(
 #          bk_name text,
  #         bk_author text,
   #        bk_details text,
    #       usr_name text,
     #      usr_class text,
      #     usr_num text,
       #    usr_date text
        #   )""")


# ADDING BOOKS TO LIBRARY(DATABSE) BT
def adding_books():
    ''' window to  adding books'''
    adding_window = Tk()
    adding_window.geometry('400x400')
    adding_window.title('ADD NEW BOOKS')

    def destroy():
        adding_window.destroy()

    # LEBALS
    bk_name_lb = Label(adding_window, text=' BOOK NAME ', )
    bk_name_lb.grid(row=0, column=0, ipadx=20, pady=10)

    bk_atr_lb = Label(adding_window, text=' AUTHOR NAME ')
    bk_atr_lb.grid(row=1, column=0, ipadx=20, pady=10)

    bk_details_lb = Label(adding_window, text=' BOOK DETAILS ')
    bk_details_lb.grid(row=2, column=0, ipadx=20, pady=10)
    global add_bk_entry
    global add_atr_entry
    global add_details_entry

    # ENTRY BOXES
    add_bk_entry = Entry(adding_window, fg='darkgreen')
    add_bk_entry.grid(row=0, column=1, ipadx=20, pady=20)

    add_atr_entry = Entry(adding_window, fg='darkgreen')
    add_atr_entry.grid(row=1, column=1, ipadx=20, pady=15)

    add_details_entry = Entry(adding_window, fg='darkgreen')
    add_details_entry.grid(row=2, column=1, ipadx=20, pady=15)

    # BUTTONS

    save_bt = Button(adding_window, text='SAVE   DETAILS', width=40, fg='green', command=saving_data)
    save_bt.place(x=40, y=180)

    close_bt = Button(adding_window, text='  CLOSE  ', width=40, fg='red', command=destroy)
    close_bt.place(x=40, y=230)
    adding_window.mainloop()


def saving_data():
    '''saving book details to database'''
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO user_details1 VALUES(:bk_name,:bk_author,:bk_details,:usr_name,:usr_class,:usr_num,:usr_date)",
        # creating dictinory to store data
        {
            'bk_name': add_bk_entry.get(),
            'bk_author': add_atr_entry.get(),
            'bk_details': add_details_entry.get(),
            'usr_name': tmp_name,
            'usr_class': tmp_class,
            'usr_num': tmp_num,
            'usr_date': tmp_date
        })
    conn.commit()
    conn.close()
    add_bk_entry.delete(0, END)
    add_atr_entry.delete(0, END)
    add_details_entry.delete(0, END)


def showing_books():
    '''Displaying book details'''
    show_window = Tk()
    show_window.geometry('400x500')
    show_window.title('ALL  BOOKS')
    list_book = Listbox(show_window, width=45, height=25, highlightcolor='white', selectbackground='red',
                        font=('Italic', 13))
    list_book.delete(0, END)
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM user_details1")
    records = c.fetchall()
    for record in records:
        list_book.insert(END, str(record[7]) + ' ' + str(record[0]))
        list_book.place(x=800, y=220)
    list_book.grid(row=1, column=0)
    conn.commit()
    conn.close()
    show_window.mainloop()


# ISSUEING BOOK TO USER  BT
def issue_book():
    '''issue new book'''
    issue_window = Tk()
    issue_window.geometry('400x500')
    issue_window.title('ISSUE BOOKS')

    def destroy():
        issue_window.destroy()

    conn = sqlite3.connect('library_database.db')
    c = conn.cursor()
    # LEBALS

    bk_id_lb = Label(issue_window, text=' BOOK ID  ')
    bk_id_lb.grid(row=0, column=0, ipadx=20, pady=10)

    bk_name_lb = Label(issue_window, text=' BOOK NAME ')
    bk_name_lb.grid(row=2, column=0, ipadx=20, pady=10)
    bk_dtls_lb = Label(issue_window, text=' AUTHOR  ')
    bk_dtls_lb.grid(row=3, column=0, ipadx=20, pady=10)

    bk_dtls_lb = Label(issue_window, text=' BOOK DETAILS ')
    bk_dtls_lb.grid(row=4, column=0, ipadx=20, pady=10)

    bk_stdname_lb = Label(issue_window, text=' STUDENT NAME ')
    bk_stdname_lb.grid(row=5, column=0, ipadx=20, pady=10)

    bk_stdclass_lb = Label(issue_window, text=' STUDENT CLASS ')
    bk_stdclass_lb.grid(row=6, column=0, ipadx=20, pady=10)

    bk_stdid_lb = Label(issue_window, text=' STUDENT ID NUMBER ')
    bk_stdid_lb.grid(row=7, column=0, ipadx=20, pady=10)

    bk_stddate_lb = Label(issue_window, text=' DATE ')
    bk_stddate_lb.grid(row=8, column=0, ipadx=20, pady=10)

    global issue_bkid_entry
    global issue_bkname_entry
    global issue_bkathr_entry
    global issue_bkdtls_entry
    global issue_stdname_entry
    global issue_stdclass_entry
    global issue_stdnum_entry
    global issue_date_entry
    # ENTRY BOXES
    issue_bkid_entry = Entry(issue_window)
    issue_bkid_entry.grid(row=0, column=1, ipadx=20, pady=10)

    issue_bkname_entry = Entry(issue_window)
    issue_bkname_entry.grid(row=2, column=1, ipadx=20, pady=10)

    issue_bkathr_entry = Entry(issue_window)
    issue_bkathr_entry.grid(row=3, column=1, ipadx=20, pady=10)

    issue_bkdtls_entry = Entry(issue_window)
    issue_bkdtls_entry.grid(row=4, column=1, ipadx=20, pady=10)

    issue_stdname_entry = Entry(issue_window)
    issue_stdname_entry.grid(row=5, column=1, ipadx=20, pady=10)

    issue_stdclass_entry = Entry(issue_window)
    issue_stdclass_entry.grid(row=6, column=1, ipadx=20, pady=10)

    issue_stdnum_entry = Entry(issue_window)
    issue_stdnum_entry.grid(row=7, column=1, ipadx=20, pady=10)

    issue_date_entry = Entry(issue_window)
    issue_date_entry.grid(row=8, column=1, ipadx=20, pady=10)

    # BUTTONS
    enter_bt = Button(issue_window, text='ENTER', width=23, fg='blue',
                      command=inserting_issue_data)  # command=save_data)
    enter_bt.grid(row=1, column=1)

    save_bt = Button(issue_window, text='SAVE   DETAILS', width=40, fg='green', command=save_data)  # )
    save_bt.place(x=40, y=380)

    close_bt = Button(issue_window, text='  CLOSE  ', width=40, fg='red', command=destroy)
    close_bt.place(x=40, y=430)
    issue_window.mainloop()


# inserting data to issuebook//issue_book() SUB
def inserting_issue_data():
    '''inserting  book details to entryboxes'''
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    issue_bkname_entry.delete(0, END)
    issue_bkathr_entry.delete(0, END)
    issue_bkdtls_entry.delete(0, END)
    issue_date_entry.delete(0, END)
    oid_id = issue_bkid_entry.get()
    c.execute('SELECT * FROM user_details1 WHERE oid = ' + oid_id)
    records = c.fetchall()
    for record in records:
        issue_bkname_entry.insert(0, record[0])
        issue_bkathr_entry.insert(0, record[1])
        issue_bkdtls_entry.insert(0, record[2])
    # DATE AND TIME
    date_nows = datetime.datetime.now()
    date_now = date_nows.strftime('%d-%m-%Y')
    # print(datetime.today().strftime("%I:%M %p"))
    time_hrs = datetime.datetime.today().strftime("%I:%M %p")
    issue_date_entry.insert(END, date_now + ', ' + time_hrs)


# updating the issue datas //issue_book() SUB
def save_data():
    '''saving details of  book to database'''
    record_id = issue_bkid_entry.get()
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    c.execute("""UPDATE user_details1 SET
    bk_name = :book,
    bk_author = :author,
    bk_details = :details,
    usr_name = :usrname,
    usr_class = :usrclass,
    usr_num = :usrnum,
    usr_date = :usrdate

    WHERE oid = :oid
    """,
              {
                  'book': issue_bkname_entry.get(),
                  'author': issue_bkathr_entry.get(),
                  'details': issue_bkdtls_entry.get(),
                  'usrname': issue_stdname_entry.get(),
                  'usrclass': issue_stdclass_entry.get(),
                  'usrnum': issue_stdnum_entry.get(),
                  'usrdate': issue_date_entry.get(),
                  'oid': record_id
              })
    conn.commit()
    conn.close()
    issue_bkid_entry.delete(0, END)
    issue_bkname_entry.delete(0, END)
    issue_bkathr_entry.delete(0, END)
    issue_bkdtls_entry.delete(0, END)
    issue_stdname_entry.delete(0, END)
    issue_stdclass_entry.delete(0, END)
    issue_stdnum_entry.delete(0, END)
    issue_date_entry.delete(0, END)


# window of issued book BT
def removing_book():
    '''window for removing isseud book'''
    rm_issue_window = Tk()
    rm_issue_window.geometry('400x500')
    rm_issue_window.title('REMOVE ISSUED BOOKS')

    def destroy():
        rm_issue_window.destroy()

    conn = sqlite3.connect('library_database.db')
    c = conn.cursor()

    # LEBALS
    bk_id_lb = Label(rm_issue_window, text=' BOOK ID  ')
    bk_id_lb.grid(row=0, column=0, ipadx=20, pady=10)

    bk_name_lb = Label(rm_issue_window, text=' BOOK NAME ')
    bk_name_lb.grid(row=2, column=0, ipadx=20, pady=10)
    bk_name_lb = Label(rm_issue_window, text=' AUTHOR ')
    bk_name_lb.grid(row=3, column=0, ipadx=20, pady=10)

    bk_dtls_lb = Label(rm_issue_window, text=' BOOK DETAILS ')
    bk_dtls_lb.grid(row=4, column=0, ipadx=20, pady=10)

    bk_stdname_lb = Label(rm_issue_window, text=' STUDENT NAME ')
    bk_stdname_lb.grid(row=5, column=0, ipadx=20, pady=10)

    bk_stdclass_lb = Label(rm_issue_window, text=' STUDENT CLASS ')
    bk_stdclass_lb.grid(row=6, column=0, ipadx=20, pady=10)

    bk_stdid_lb = Label(rm_issue_window, text=' STUDENT ID NUMBER ')
    bk_stdid_lb.grid(row=7, column=0, ipadx=20, pady=10)

    bk_stddate_lb = Label(rm_issue_window, text=' DATE ')
    bk_stddate_lb.grid(row=8, column=0, ipadx=20, pady=10)

    global rm_issue_bkid_entry
    global rm_issue_bkname_entry
    global rm_issue_bkathr_entry
    global rm_issue_bkdtls_entry
    global rm_issue_stdname_entry
    global rm_issue_stdclass_entry
    global rm_issue_stdnum_entry
    global rm_issue_date_entry

    # ENTRY BOXES
    rm_issue_bkid_entry = Entry(rm_issue_window, fg='red')
    rm_issue_bkid_entry.grid(row=0, column=1, ipadx=20, pady=10)

    rm_issue_bkname_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_bkname_entry.grid(row=2, column=1, ipadx=20, pady=10)
    rm_issue_bkathr_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_bkathr_entry.grid(row=3, column=1, ipadx=20, pady=10)

    rm_issue_bkdtls_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_bkdtls_entry.grid(row=4, column=1, ipadx=20, pady=10)

    rm_issue_stdname_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_stdname_entry.grid(row=5, column=1, ipadx=20, pady=10)

    rm_issue_stdclass_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_stdclass_entry.grid(row=6, column=1, ipadx=20, pady=10)

    rm_issue_stdnum_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_stdnum_entry.grid(row=7, column=1, ipadx=20, pady=10)

    rm_issue_date_entry = Entry(rm_issue_window, fg='darkgreen')
    rm_issue_date_entry.grid(row=8, column=1, ipadx=20, pady=10)

    # BUTTONS
    enter_bt = Button(rm_issue_window, text='ENTER', width=23, fg='blue', command=inserting_details)
    enter_bt.grid(row=1, column=1)

    save_bt = Button(rm_issue_window, text='REMOVE DETAILS', width=40, bg='green', fg='white',
                     command=deleting_book)  # )
    save_bt.place(x=40, y=380)

    close_bt = Button(rm_issue_window, text='  CLOSE  ', width=40, bg='red', fg='white', command=destroy)
    close_bt.place(x=40, y=430)

    rm_issue_window.mainloop()
    conn.commit()
    conn.close()


def inserting_details():
    '''inserting isseud book details to entry boxes'''
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    rm_issue_bkname_entry.delete(0, END)
    rm_issue_bkathr_entry.delete(0, END)
    rm_issue_bkdtls_entry.delete(0, END)
    rm_issue_stdname_entry.delete(0, END)
    rm_issue_stdclass_entry.delete(0, END)
    rm_issue_stdnum_entry.delete(0, END)
    rm_issue_date_entry.delete(0, END)
    oid_id = rm_issue_bkid_entry.get()
    c.execute('SELECT * FROM user_details1 WHERE oid = ' + oid_id)
    records = c.fetchall()
    for record in records:
        rm_issue_bkname_entry.insert(0, record[0])
        rm_issue_bkathr_entry.insert(0, record[1])
        rm_issue_bkdtls_entry.insert(0, record[2])
        rm_issue_stdname_entry.insert(0, record[3])
        rm_issue_stdclass_entry.insert(0, record[4])
        rm_issue_stdnum_entry.insert(0, record[5])
        rm_issue_date_entry.insert(0, record[6])
    conn.commit()
    conn.close()


def deleting_book():
    '''deleting issued book deatils from database'''
    record_id = rm_issue_bkid_entry.get()
    conn = sqlite3.connect('library_database1.db')
    c = conn.cursor()
    c.execute("""UPDATE user_details1 SET
        bk_name = :book,
        bk_author = :author,
        bk_details = :details,
        usr_name = :usrname,
        usr_class = :usrclass,
        usr_num = :usrnum,
        usr_date = :usrdate

        WHERE oid = :oid
        """,
              {
                  'book': rm_issue_bkname_entry.get(),
                  'author': rm_issue_bkathr_entry.get(),
                  'details': rm_issue_bkdtls_entry.get(),
                  'usrname': tmp_name,
                  'usrclass': tmp_class,
                  'usrnum': tmp_num,
                  'usrdate': tmp_date,
                  # oid needs to add from delte_box
                  'oid': record_id
              })
    conn.commit()
    conn.close()
    rm_issue_bkid_entry.delete(0, END)
    rm_issue_bkname_entry.delete(0, END)
    rm_issue_bkathr_entry.delete(0, END)
    rm_issue_bkdtls_entry.delete(0, END)
    rm_issue_stdname_entry.delete(0, END)
    rm_issue_stdclass_entry.delete(0, END)
    rm_issue_stdnum_entry.delete(0, END)
    rm_issue_date_entry.delete(0, END)


# IMAGE
# image1 = Image.open(r"C:\Users\user\Pictures\project designs\library1.jpg")
# test = ImageTk.PhotoImage(image1)
# label1 = tk.Label(image=test,width=736,height=200)
# label1.image = test
# label1.place(x=280, y=0)

# LABELS
title_label = Label(window, text='NEW LIBRARY   MANAGEMENT  SOFTWARE', bg='red', fg='black', font=('Italic', 28))
title_label.pack()
title_label.place(x=220, y=70)

quts_label = Label(window, text='"THERE IS NO FREIND\n AS LOYAL AS THE\n BOOK" ', font=('Italic', 17), fg='orange')
quts_label.pack()
quts_label.place(x=500, y=160)

# BUTTONS,
all_books_button = Button(text='ALL BOOKS', width=35, height=2, bg='orange', fg='black', command=showing_books)
all_books_button.pack()
all_books_button.place(x=500, y=300)

order_book_button = Button(text='ISSUE BOOKS', width=35, height=2, bg='orange', fg='black', command=issue_book)
order_book_button.pack()
order_book_button.place(x=500, y=360)

remove_book_button = Button(text='REMOVE ISSUED BOOK', width=35, height=2, bg='orange', fg='black',
                            command=removing_book)
remove_book_button.pack()
remove_book_button.place(x=500, y=420)

add_book_button = Button(text='ADD BOOKS', width=35, height=2, bg='orange', fg='black', command=adding_books)
add_book_button.pack()
add_book_button.place(x=500, y=480)

conn.commit()
conn.close()
window.mainloop()

