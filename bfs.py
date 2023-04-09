import copy

pacman_x, pacman_y = list(map(int, input().split()))
food_x, food_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))
grid = []
node_expanded = []
queue = []
answer_routes = None

for i in range(0, n):
    grid.append(list(map(str, input())))
    
input_grid=copy.deepcopy(grid)
#FOR DEFINING PATH AT INITIAL LOCATION OF PACMAN
input_grid[pacman_x][pacman_y]="-"
print(input_grid[pacman_x][pacman_y])

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
#directions = [[0, 1], [1, 0],[-1, 0], [0, -1]]

queue.append([pacman_x, pacman_y, []])
while len(queue) > 0:
    x, y, r = queue.pop(0)
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
            queue.append([next_x, next_y, routes])

print(str(len(node_expanded)))
for point in node_expanded:
    print(str(point[0]) + " " + str(point[1]))

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