def turn_right():
    turn_left()
    turn_left()
    turn_left()


detect_loop = 0
while not at_goal():
    if wall_on_right():
        detect_loop = 0
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        detect_loop += 1
        if detect_loop == 5:
            turn_left()
        turn_right()
        move()
