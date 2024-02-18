board = list( (input() , input() , input()) )

one = 0 
team = 0 

for row in board :  # check 3 rows 
    # check for one member win 
    if len(set(row)) == 1  :
        one += 1 

    # check for team win 
    if len(set(row)) == 2 : 
        team += 1 

for col in range(3) : # check 3 cols 
    # check for one member win
    if len(set([item[col] for item in board])) == 1 : 
        one += 1 
    
    # check for team win
    if len(set([item[col] for item in board])) == 2 : 
        team += 1 
    

# check first diagonal
if len(set([board[0][0] , board[1][1] , board[2][2] ]  )) == 1 :
    one += 1 
if len(set([board[0][0] , board[1][1] , board[2][2] ]  )) == 2 :
    team += 1 

# check second diagonal
if len(set([board[0][2] , board[1][1] , board[2][0] ]  )) == 1 :
    one += 1 
if len(set([board[0][2] , board[1][1] , board[2][0] ]  )) == 2 :
    team += 1 



print(one)
print(team)