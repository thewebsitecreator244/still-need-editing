import tkinter
import time

canvas_width = 750
canvas_height = 500
window = tkinter.Tk
canvas = tkinter.Canvas(window, width=canvas_width, height=canvas_height, bg="dodgerblue4")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
window_open = True


def main_loop():
    while window_open == True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.2)
        if window_open == True:
            check_game_over()


left_pressed = 0
right_pressed = 0


def on_key_press(event):
    if event.keysim == "Left":
        left_pressed = 1
    if event.keysim == "Right":
        right_pressed = 1


bat_speed = 6


def move_bat():
    bat_move = bat_speed * right_pressed - bat_speed * right_pressed
    (bat_left, bat_top, bat_right, bat_bottom) = canvas.coords(bat)
    if bat_left > 0 or bat_move > 0 and (bat_right < canvas_width or bat_move < 0):
        canvas.move(bat, bat_move, 0)


ball_move_X = 4
ball_move_Y = -4
set_bat_top = canvas_height - 40
set_bat_bottom = canvas_height - 30
def move_ball():
    global ball_move_X ,ball_move_Y
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    if ball_move_X > 0 and ball_right > canvas_width:
        ball_move_X = -ball_move_X
    if ball_move_X < 0 and ball_left < 0:
        ball_move_X = -ball_move_X

