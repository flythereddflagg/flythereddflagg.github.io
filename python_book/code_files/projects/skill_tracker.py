import tkinter as tk
import json

SAVEFILE = 'data.json'
row_counter = 0
column_counter = 0

def add_to_frame(entry_text, time, coord=None):
    global row_counter
    global column_counter
    
    if coord:
        column, row  = coord
    else:
        row, column = row_counter, column_counter
    
    x0 = time
    y0 = 100
    x1 = 0
    y1 = 0
    
    if skill_dictionary == {}:  # first time
        skill_dictionary[entry_text] = []

    else:  # column_counter in (0, 1, 2, 3):
        skill_dictionary[entry_text] = []

    frame1.rowconfigure(row_counter, weight=1)
    frame1.columnconfigure(column_counter, weight=1)
    new_label = tk.Canvas(frame1, width=150, height=50)
    new_label.create_rectangle(x0, y0, x1, y1, fill="red")
    new_label.create_text(30, 27, text=entry_text)
    skill_dictionary.setdefault(entry_text, []).append(time)
    new_label.grid(
        row=row, column=column, padx=5, pady=10
    )
    column_counter += 1
    skill_dictionary.setdefault(entry_text, []).append(column_counter)
    skill_dictionary.setdefault(entry_text, []).append(row_counter)
    if column_counter == 3:
        column_counter = 0
        row_counter += 1



def add_to_frame_command():
    # print("add_to_frame called")
    entry_text = add_skill_entry.get()
    add_skill_entry.delete(0,tk.END)
    time = time_tracker.get()
    time_tracker.delete(0,tk.END)
    add_to_frame(entry_text, time)



if __name__ == '__main__':
    # make a new file if none exists
    try:
        open(SAVEFILE).close()
    except FileNotFoundError:
        with open(SAVEFILE, 'w') as f:
            json.dump({}, f)

    # setup gui
    main_window = tk.Tk()  # creates main window
    main_window.geometry('720x640+250-120')  # creates size of window

    # Make 4x4 grid
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)
    # add input box
    add_skill_entry = tk.Entry(main_window, bg="gray")
    add_skill_entry.grid(column=0, row=0, sticky="s")
    # add input box
    time_tracker = tk.Entry(main_window, bg="gray")
    time_tracker.grid(column=0, row=1, sticky="n")

    frame1 = tk.Frame(main_window, bg="white", height="300", width="300")
    frame1.grid_propagate(0)
    frame1.grid(row=0, column=1, rowspan=2)
    # submit button for both
    submit_button = tk.Button(
        main_window, text="Submit", command=add_to_frame_command)
    submit_button.grid(column=0, row=1, sticky="s")

    # extract data from file
    with open(SAVEFILE, 'r') as f:
        skill_dictionary = json.load(f)
        print("Printing file: ")
        for key, val in skill_dictionary.items():
            print(key, val)
            add_to_frame(key, val[0], coord=val[1:])

    main_window.mainloop()

    print("saving file")
    with open(SAVEFILE, 'w') as f:
        json.dump(skill_dictionary, f, indent=4)

