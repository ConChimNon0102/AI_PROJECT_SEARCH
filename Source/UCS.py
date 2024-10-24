from utils import *
import heapq

# Uniform Cost Search (UCS) Algorithm
def ucs(problem):
    start_node = Node(problem.initial_state)

    frontier = [(start_node.f, start_node)]
    explored = {str(start_node.state): (0, None)}

    while frontier:
        current_cost, node = heapq.heappop(frontier)

        if problem.goal_test(node.state):
            return solution(node)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)

            if child not in explored or child.f < explored[child][0]:
                explored[child] = (child.f, node)
                heapq.heappush(frontier, (child.f, child))
    
    return None