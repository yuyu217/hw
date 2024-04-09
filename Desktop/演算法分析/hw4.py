def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0' or visited[x][y]:
        return 0 # 檢查目前位置是否越界或目前像素為0或已被造訪過
    visited[x][y] = True
    area = 1  
    area += dfs(grid, x-1, y, visited)
    area += dfs(grid, x+1, y, visited)
    area += dfs(grid, x, y-1, visited)
    area += dfs(grid, x, y+1, visited)
    area += dfs(grid, x-1, y-1, visited)
    area += dfs(grid, x-1, y+1, visited)
    area += dfs(grid, x+1, y-1, visited)
    area += dfs(grid, x+1, y+1, visited)
    return area

def find_connected_components(image):
    if not image or not image[0]:
        return []
    rows, cols = len(image), len(image[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)] # 初始化
    components = [] # 儲存每個連通區域的面積
    
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == '1' and not visited[i][j]:
                components.append(dfs(image, i, j, visited))
    return components

def process_input(height, width, image_data, image_number):
    if len(image_data) != height or any(len(row) != width for row in image_data):
        return "Error: Image dimensions do not match input dimensions."
    
    components = find_connected_components(image_data)
    output = f"Image #{image_number}\nNumber of Connected Components = {len(components)}\n"
    for i, area in enumerate(components, 1):
        output += f"Connected Component #{i} Area = {area}\n"
    return output

image_number = 1
while True:
    height, width = map(int, input("Enter the height and width of the image: ").split())
    if height == 0 and width == 0:
        break

    input_image_data = []
    print("Enter the image data row by row:")
    for _ in range(height):
        row = input()
        input_image_data.append(row)

    test_output = process_input(height, width, input_image_data, image_number)
    print(test_output)
    image_number += 1
