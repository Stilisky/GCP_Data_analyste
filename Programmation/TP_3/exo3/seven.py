
def seven_seg(number):
    rows = [' ', '|', '_']
    
    if number == 0:
        # print(rows[0] + '\n' + rows[1] + '\n' + rows[2])
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[1] + rows[0] + rows[1] + '\n' + rows[1] + rows[2] + rows[1])
    elif number == 1:
        print(rows[0] +rows[0] +rows[0] + '\n' + rows[0] + rows[0] + rows[1] + '\n' + rows[0] + rows[0] + rows[1])
        # print(rows[0][:1] +rows[0][:1] +rows[0][:1] + '\n' + rows[0][:1] + rows[0][:1] + rows[1][2:] + '\n' + rows[0][:1] + rows[0][:1] + rows[2][2:])
    elif number == 2:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
        # print(rows[0] + '\n' + rows[0][:1] + rows[2][1:2] + rows[1][2:] + '\n' + rows[1][0:1] + rows[2][1:2] + rows[0][2:])
    elif number == 3:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[0] + rows[2] + rows[1])
    elif number == 4:
        print(rows[0] + rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    elif number == 5:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    elif number == 6:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    elif number == 7:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    elif number == 8:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    elif number == 9:
        print(rows[0] +rows[2] +rows[0] + '\n' + rows[0] + rows[2] + rows[1] + '\n' + rows[1] + rows[2] + rows[0])
    else:
        print('NONE')


        
