
import copy

pacman_x, pacman_y = list(map(int, input().split()))
food_x, food_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))
grid = []
node_expanded = []
stack = []
answer_routes = None
cyclic_nodes=[]

for i in range(0, n):
    grid.append(list(map(str, input())))


def isValid(x, y, N, M):
     
    if (x < N and x >= 0 and
        y < M and y >= 0):
        return True
         
    return False
 
# Function which will check whether the given grid consist of a cycle or not
def isCycle(x, y, arr, visited, parentX, parentY,n,m):
     
    # Mark the current vertex as visited
    visited[x][y] = True
    cyclic_nodes.append([x,y])
     
    N, M = n, m
     
    # Loop for generate all possibilities of adjacent cells and checking them
    for direction in directions:
        newX = x + direction[0]
        newY = y + direction[1]
         
        if (isValid(newX, newY, N, M) and
            arr[newX][newY] == arr[x][y] and
               not (parentX == newX and
                    parentY == newY)):
                            
            # Check if there exist cycle then return true
            if visited[newX][newY]:
               
                # Return True as the cycle exists
                return True
                 
            # If the cycle is not found then keep checking recursively
            else:
                check = isCycle(newX, newY, arr,
                                visited, x, y,N,M)
                if check:
                    return True
        
   
                
                        
                     
    # If there was no cycle, taking x and y as source then return false
    return False
 
# Function to detect Cycle in a grid
def detectCycle(arr,n,m):
     
    N, M = n,m
     
    # Initially all the cells are unvisited
    visited = [[False] * M for _ in range(N)]
 
    # Variable to store the result
    cycle = False
 
    # As there is no fixed position of the cycle we have to loop through all the elements
    for i in range(N):
         
        # If cycle is present and we have already detected it, then break this loop
        if cycle == True:
            break
 
        for j in range(M):
             
            # Taking (-1, -1) as source nodes parent
            if visited[i][j] == False:
                if(arr[i][j]=="%"):
                    continue
                
                cycle = isCycle(i, j, arr,
                                visited, -1, -1,N,M)
                                
             
            # If we have encountered a cycle then break this loop
            if cycle == True:
                break
     
    # Cycle was encountered
    if cycle == True:
        #print("Yes")
        return True
         
    # Cycle was not encountered
    else:
        #print("No")
        return False







###########################################################################    
#FOR STORING THE INPUT ARRAY
input_grid=copy.deepcopy(grid)
check_grid=copy.deepcopy(grid)

#FOR DEFINING PATH AT INITIAL LOCATION OF PACMAN
input_grid[pacman_x][pacman_y]="-"
check_grid[pacman_x][pacman_y]="-"

print(input_grid[pacman_x][pacman_y])

#directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
directions = [[1, 0],[0, 1], [-1, 0], [0, -1]]           #Gets to the food

stack.append([pacman_x, pacman_y, []])
while len(stack) > 0:
    x, y, r = stack.pop()
    routes = copy.deepcopy(r)
    routes.append([x, y])

    node_expanded.append([x, y])

    if x == food_x and y == food_y:
        if answer_routes == None:
            answer_routes = routes
            break

    for direction in directions:
        next_x, next_y = x + direction[0], y + direction[1]
        if next_x < 0 or next_x >= n or next_y < 0 and next_y >= n:
            continue

        if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
            grid[next_x][next_y] = '='
            stack.append([next_x, next_y, routes])

print(str(len(node_expanded)))
for point in node_expanded:
    print(str(point[0]) + " " + str(point[1]))

print("**Printing answer routes for pacman****")
print(str(len(answer_routes) - 1))
for point in answer_routes:
    print(str(point[0]) + " " + str(point[1]))
    
print("**Printing answer routes for pacman****")

print("*************") 
for point in answer_routes:
    l_x=point[0]
    l_y=point[1]
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            if(i==l_x and j==l_y):
               print("P", end = ' ')
            else:
               print(input_grid[i][j], end = ' ')
      
        print('',sep='\n')
        
    print("///////////////////////////////")

t=detectCycle(check_grid,n,m)
print(t)    
print("*********")
for point in cyclic_nodes:
    print(str(point[0]) + " " + str(point[1]))


for point in cyclic_nodes:
    l_x=point[0]
    l_y=point[1]
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            if(i==l_x and j==l_y):
               print("P", end = ' ')
            else:
               print(input_grid[i][j], end = ' ')
      
        print('',sep='\n')
        
    print("///////////////////////////////")