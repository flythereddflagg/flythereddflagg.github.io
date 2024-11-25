# doing this with tkinter is a terrible idea

import tkinter as tk

SCREENH, SCREENW = 600, 800
FPS = 60

speed = 100 # pixels/sec
t_after = int(1/30*1000)
x, y = t_after/1000*speed, 0

def on_exit(tk_):
    tk_.running = False
    tk_.destroy()


def movement(main_window, event=None):
    game_screen.move(car, x, y)
    main_window.after(t_after, lambda: movement(main_window))


if __name__ == '__main__':
    main_window = tk.Tk()

    game_screen = tk.Canvas(
        master=main_window, 
        height=SCREENH, 
        width=SCREENW, bg="black"
    )
    game_screen.pack(expand=True, fill='both')
    main_window.geometry(f"{SCREENW}x{SCREENH}+100+100")
    main_window.resizable(False, False)
    main_window.protocol("WM_DELETE_WINDOW", lambda: on_exit(main_window))
    main_window.running = True

    blue_car_img = tk.PhotoImage(file="./blue_car.png")
    car = game_screen.create_image(50, 50, image=blue_car_img)
    movement(main_window)
    main_window.mainloop()

    # while main_window.running:
    #     # game_screen.delete("all")
    #     game_screen.move(car, 5, 5)
    #     main_window.update()
