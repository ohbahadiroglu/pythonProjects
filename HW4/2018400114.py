
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
game_on=True
game_over = False

score=0
time=0
if y%2==0:
    position=y//2-1
else:
    position=y//2
cluster_air=[]
for i in range(x):
    line=list()
    for j in range(y):
        line.append("*")
    cluster_air.append(line)
for i in range(g):
    blankline = list()
    for j in range(y):
        blankline.append(" ")
    cluster_air.append((blankline))
empty=[]
for i in range(y):
    empty.append(" ")
##board printer
if x==0:
    print("YOU WON!")
for line in cluster_air:
    for cell in line:
        print(cell,end="")
    print()
print(position*" "+"@"+" "*(y-position-1))
print("-"*72)
if x==0:
    print(f"YOUR SCORE: {score}")
    game_on=False



while game_on:


    action = input("Choose your action!\n")
    action = action.lower()

    if action=="exit":
        ##board
        for line in cluster_air:
            for cell in line:
                print(cell, end="")
            print()
        print(position * " " + "@" + " " * (y - position-1))
        print("-" * 72)
        print(f"YOUR SCORE: {score}")
        game_on=False

    elif action=="left":
        time+=1
        if position>0:
            position-=1
        if time != 0 and time % 5 == 0:
            for cell in cluster_air[-1]:
                if cell == "*":
                    print("GAME OVER")
                    for line in cluster_air:
                        for cell in line:
                            print(cell, end="")
                        print()
                    print(position * " " + "@" + " " * (y - position-1))
                    print("-" * 72)

                    print(f"YOUR SCORE: {score}")
                    game_on = False
                    game_over=True
                    break

            else:
                cluster_air.pop()
                empty = []
                for i in range(y):
                    empty.append(" ")
                cluster_air.insert(0, empty)
        if game_over==False:
            for line in cluster_air:
                for cell in line:
                    print(cell, end="")
                print()
            print(position * " " + "@" + " " * (y - position-1))
            print("-" * 72)


    elif action=="right":
        time += 1
        if position < y-1 :
            position += 1
        if time != 0 and time % 5 == 0:
            for cell in cluster_air[-1]:
                if cell == "*":
                    print("GAME OVER")
                    for line in cluster_air:
                        for cell in line:
                            print(cell, end="")
                        print()
                    print(position * " " + "@" + " " * (y - position-1))
                    print("-" * 72)

                    print(f"YOUR SCORE: {score}")
                    game_on = False
                    game_over=True
                    break
            else:
                cluster_air.pop()
                empty = []
                for i in range(y):
                    empty.append(" ")
                cluster_air.insert(0, empty)

        if game_over==False:
            for line in cluster_air:
                for cell in line:
                    print(cell, end="")
                print()
            print(position * " " + "@" + " " * (y - position-1))
            print("-" * 72)


    elif action=="fire":
        game_won = False
        time+=1
        for i in range(len(cluster_air)-1,-1,-1):
            if cluster_air[i][position]=="*":
                cluster_air[i][position] = " "
                try:
                    cluster_air[i+1][position] = " "
                except:
                    pass
                score+=1
                if score==x*y:
                    game_won=True
                if game_won:
                    print("YOU WON!")
                    for line in cluster_air:
                        for cell in line:
                            print(cell, end="")
                        print()
                    print(position * " " + "@" + " " * (y - position-1))
                    print("-" * 72)
                    print(f"YOUR SCORE: {score}")
                    game_on=False
                    break
                if time != 0 and time % 5 == 0:
                    for cell in cluster_air[-1]:
                        if cell == "*":
                            print("GAME OVER")
                            for line in cluster_air:
                                for cell in line:
                                    print(cell, end="")
                                print()
                            print(position * " " + "@" + " " * (y - position-1))
                            print("-" * 72)

                            print(f"YOUR SCORE: {score}")
                            game_on = False
                            game_over=True
                            break
                    else:
                        cluster_air.pop()
                        empty = []
                        for i in range(y):
                            empty.append(" ")
                        cluster_air.insert(0, empty)


                if game_over==False:
                    for line in cluster_air:
                        for cell in line:
                            print(cell, end="")
                        print()
                    print(position * " " + "@" + " " * (y - position-1))
                    print("-" * 72)
                break

            cluster_air[i][position]="|"
            if i+1<len(cluster_air):
                cluster_air[i+1][position] = " "


            for line in cluster_air:
                for cell in line:
                    print(cell, end="")
                print()
            print(position * " " + "@" + " " * (y - position-1))
            print("-" * 72)
            if cluster_air[0][position]=="|":
                cluster_air[0][position] = " "
                if time != 0 and time % 5 == 0:
                    for cell in cluster_air[-1]:
                        if cell == "*":
                            print("GAME OVER")
                            for line in cluster_air:
                                for cell in line:
                                    print(cell, end="")
                                print()
                            print(position * " " + "@" + " " * (y - position-1))
                            print("-" * 72)
                            print(f"YOUR SCORE: {score}")
                            game_on = False
                            break
                    else:
                        cluster_air.pop()
                        empty = []
                        for i in range(y):
                            empty.append(" ")
                        cluster_air.insert(0, empty)
                for line in cluster_air:
                    for cell in line:
                        print(cell, end="")
                    print()
                print(position * " " + "@" + " " * (y - position-1))
                print("-" * 72)

    else:
        time+=1
        game_over = False
        if time != 0 and time % 5 == 0:
            for cell in cluster_air[-1]:
                if cell == "*":
                    print("GAME OVER")
                    for line in cluster_air:
                        for cell in line:
                            print(cell, end="")
                        print()
                    print(position * " " + "@" + " " * (y - position-1))
                    print("-" * 72)

                    print(f"YOUR SCORE: {score}")
                    game_on = False
                    game_over = True
                    break
            else:
                cluster_air.pop()
                cluster_air.insert(0, [" " for i in range(x)])
        if game_over == False:
            for line in cluster_air:
                for cell in line:
                    print(cell, end="")
                print()
            print(position * " " + "@" + " " * (y - position-1))
            print("-" * 72)




# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
