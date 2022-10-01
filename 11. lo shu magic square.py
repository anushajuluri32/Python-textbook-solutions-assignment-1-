'''
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18.
 The Lo Shu Magic Square has the following properties:
•	 The grid contains the numbers 1 through 9 exactly.
•	 The sum of each row, each column, and each diagonal all add up to the same number. 
This is shown in Figure 7-19.
In a program you can simulate a magic square using a two-dimensional list. 
Write a function that accepts a two-dimensional list as an argument and 
determines whether the list is a Lo Shu Magic Square.
 Test the function in a program
'''

def magicSquare(grid):
    '''
    a00     a01     a02
    a10     a11     a12
    a20     a21     a22
    '''
    r0=sum(grid[0])
    r1=sum(grid[1])
    r2=sum(grid[2])
    dij=grid[0][0]+grid[1][1]+grid[2][2]
    din_j=grid[2][0]+grid[1][1]+grid[0][2]
    c0=grid[0][0]+grid[1][0]+grid[2][0]
    c1=grid[0][1]+grid[1][1]+grid[2][1]
    c2=grid[0][2]+grid[1][2]+grid[2][2]
    if r0==r1==r2==dij==din_j==c0==c1==c2:
        return 1
    else:
        return 0

print("Enter elements in 3-D Grid:  ")
print("Note: Enter numbers only between 1 and 9")
grid=[]
for i in range(3):
    row=list(map(int,input().split()))
    grid.append(row)
flag=magicSquare(grid)
if flag==1:
    print("Given 3x3 grid is a Lo Shu Magic Square")
else:
    print("Given 3x3 grid is not a Lo Shu Magic Square")



    









