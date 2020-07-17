#Karen Wu's Connect 4 Game

from tkinter import *

root = Tk()

background_image = PhotoImage(file='square-01.png')
ball_image = PhotoImage(file='glass_ball-77px-01.png')
green_ball_image= PhotoImage(file='glass_ball-77px-04.png')
port_hole=PhotoImage(file='port_hole_14-80px.png')

image_width = background_image.width()
image_height = background_image.height()

turn = 0
nrows = 6
ncols = 7
red_green_ball = (ball_image, green_ball_image)
busy=False
ball_list = []

for column in range(ncols):
    ball_list.append([])
    
canvas=Canvas(root, width=image_width*ncols,height=image_height*nrows,bg='black')

for row in range (nrows):
    for col in range(ncols):
        squares=canvas.create_image(col*image_width,row*image_height,image=background_image,anchor='nw')
for row in range (nrows):
    for col in range(ncols):
        canvas.create_image(col*image_width,row*image_height,image=port_hole,anchor='nw')

canvas.pack()

def on_mouse_press(event):
    global busy
    if busy:
        return
    busy = True
    column=event.x//image_width
    dx = column*image_width
    color = ('red', 'green')
    global turn
    turn = 1 - turn
    if len(ball_list[column]) < 6:
        ball=canvas.create_image(column*image_width, 0, image=red_green_ball[turn], anchor='nw')
        ball_list[column].append(ball)
        length_of_each_col = len(ball_list[column])
        stacked_drop_height=(nrows*image_height)-(image_height*length_of_each_col)
        canvas.lift(ball, squares)
        for i in range(stacked_drop_height):
            canvas.move(ball, 0, 1)
            canvas.after(1) 
            canvas.update()
    else:
        turn = -turn+1
        print ("You have stacked the maximum number of balls in this column. Try another column.")
    print("Balls in each column: ", ball_list)
    print("Mouse pressed on column #", column, ", turn = ", turn, ", color = ", color[turn], ", # of balls in this column: ", len(ball_list[column]))
    busy = False
    return


def pop_out(event):
    column=event.x//image_width
    row=event.y//image_height
    global busy
    if busy:
        return
    busy = True
    global turn
    turn = 1 - turn
    event.movey = 100
    if row==5 and len(ball_list[column]) > 0:
        for x in range (image_height):
            for i in range(len(ball_list[column])):
                canvas.move(ball_list[column][0], 0 ,1)
                canvas.move(ball_list[column][i], 0, 1)
                canvas.after(2)
                canvas.update()
        ball_list[column].pop(0)
    else:
        turn=-turn+1
    busy=False
    return

canvas.bind('<Button-1>', on_mouse_press)
canvas.bind('<Button-3>', pop_out)
root.title('CONNECT 4')    # do this before event thread is busy in loop

root.mainloop()
