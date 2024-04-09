from collections import deque

def get_steps_to_goal_b_target(capacity_a, capacity_b, goal):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), steps = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # 檢查水桶B是否達到目標
        if b == goal:
            return steps + ["Success"]

        actions = [
            ((capacity_a, b), steps + ["Fill A"]),  # 將水桶 A 裝滿
            ((a, capacity_b), steps + ["Fill B"]),  # 將水桶 B 裝滿
            ((0, b), steps + ["Empty A"]),          # 將水桶 A 倒空
            ((a, 0), steps + ["Empty B"]),          # 將水桶 B 倒空
            ((max(a - (capacity_b - b), 0), min(b + a, capacity_b)), steps + ["Pour A B"]),  # 將水桶 A 的水倒入水桶 B
        ]

        for new_state, new_steps in actions:
            if new_state not in visited:
                queue.append((new_state, new_steps))

    return ["No solution found"]

if __name__ == "__main__":
    while True:
        input_str = input("Enter the capacities of bucket A, bucket B, and the target amount (0 0 0 to exit): ")
        a, b, goal = map(int, input_str.split())

        if a == 0 and b == 0 and goal == 0:
            break

        steps = get_steps_to_goal_b_target(a, b, goal)
        for step in steps:
            print(step)
