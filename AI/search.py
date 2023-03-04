from queue import PriorityQueue, Queue
from settings import *
from math import *


class Node:

    def __init__(self, state, action=None, parent=None, g_cost=0, f_cost=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.g_cost = g_cost
        self.f_cost = f_cost

    def __eq__(self, other):
        return self.state == other.state and self.action == other.action and self.parent == other.parent and self.g_cost == other.g_cost and self.f_cost == other.f_cost

    def __hash__(self):
        return hash((self.state, self.action, self.parent, self.g_cost, self.f_cost))

    def __lt__(self, other):
        return self.f_cost < other.f_cost


class State:

    def __init__(self, y, x, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.direction == other.direction

    def __hash__(self):
        return hash((self.x, self.y, self.direction))


class Search:

    def __init__(self, points_grid, game=None):
        self.game = game
        self.points_grid = points_grid

    def heuristic(self, state, goal_state):
        return abs(state.x - goal_state.x + abs(state.y - goal_state.y))

    def graph_search_AStar(self, initial_state, goal_state):

        # data structure for prioritizing best nodes to visit is PriorityQueue
        fringe = PriorityQueue()

        # first node has no parent and no action, its g(n) is 0 and f(n) = g(n) + h(n) is just heuristics
        init_node = Node(initial_state, None, None, 0, self.heuristic(initial_state, goal_state))

        # add initial node on fringe
        fringe.put((0, init_node))

        # tracking nodes
        fringe_track = {init_node}

        # explored states
        explored = []

        while not fringe.empty():

            node = fringe.get()[1]

            fringe_track.remove(node)

            if self.goal_test(node.state, goal_state):
                return self.get_actions(node)

            explored.append(node.state)

            for action, state, cost in self.successor(node):

                g_cost = node.g_cost + cost

                x_node = Node(state, action, node, g_cost, g_cost + self.heuristic(state, goal_state))

                f_cost = g_cost + self.heuristic(state, goal_state)

                if x_node not in fringe_track and state not in explored:
                    # nie zastepuje bezposrednio ale wezel ktory ma mniejszy f_cost czyli powinien byc zglebiany szybciej, trafi przed te gorsze
                    fringe.put( (f_cost, x_node) )
                    fringe_track.add(x_node)

        return False

    # main loop for BFS graph search
    def graph_search_BFS(self, initial_state, goal_state):
        # first node has no parent and no action which leads to this node
        init_node = Node(initial_state, g_cost=0)

        # put first node on fringe
        fringe = [init_node]

        # explored states
        explored = []

        # while there are nodes to visit - proceed
        while fringe:

            # get node
            node = fringe.pop(0)

            # check if state stored in that node is desired state
            if self.goal_test(node.state, goal_state):
                return self.get_actions(node)

            # add visited state to explored
            explored.append(node.state)

            # get possible actions and states from successor
            for action, state, cost in self.successor(node):

                # if node is not in fringe and state from successor is not explored yet add this node to fringe
                if node not in fringe and state not in explored:

                    g_cost = node.g_cost + cost

                    # create node which stores state from successor
                    x_node = Node(state, action, node, g_cost)

                    fringe.append(x_node)

        return False

    # successor for bfs and *
    def successor(self, node):

        # extract state from node
        state = node.state

        # 90 degree right state
        right_state = State(state.y, state.x, (state.direction + 1) % 4)

        # storing temporarily node as list - cost of turn is 1
        right_node = ["Right", right_state, 1]

        # 90 degree left state - cost of turn is 1
        left_state = State(state.y, state.x, 3 if state.direction == 0 else state.direction - 1)

        # storing temporarily node as list
        left_node = ["Left", left_state, 1]

        # always two nodes are possible because we can turn in both sides
        nodes = [right_node, left_node]

        # forward state
        y = state.y
        x = state.x

        # check in which direction we move
        if state.direction == 0:
            y = y - 1
        elif state.direction == 1:
            x = x + 1
        elif state.direction == 2:
            y = y + 1
        elif state.direction == 3:
            x = x - 1

        # assume that next location is
        place = None

        # check if next location is not outside borders
        if 0 <= y < TILES_HEIGHT and 0 <= x < TILES_WIDTH:
            place = self.points_grid[y][x]

        # if place is still None, that means we would go out of border, if place is found, we must check if its
        # available for move
        if place is not None and place.is_available:
            # new state we reach after moving forward
            forward_state = State(y, x, state.direction)

            # default g_cost
            g_cost = 1

            # check cost of that location
            if place.is_obstacle:
                g_cost = 10

            # node storing that state
            forward_node = ["Forward", forward_state, g_cost]

            # include that node
            nodes.append(forward_node)

        # return all nodes - always 2 or 3
        return nodes

    # goal test is basically checking if we reached desired location
    def goal_test(self, state, goal_state):
        if state.x == goal_state.x and state.y == goal_state.y:
            return True
        else:
            return False

    # traversing backwards by parent attribute and getting actions
    def get_actions(self, node):
        actions = []
        # information about moves forward - additional
        moves_forward = 0
        # information about turns - additional
        turns = 0
        # node is desired location is g_cost of that node is actually cost of whole path
        parent = node
        while True:

            action = parent.action
            parent = parent.parent

            if action is None:
                break

            if action == "Forward":
                moves_forward = moves_forward + 1
            else:
                turns = turns + 1

            actions.append(action)

        actions.reverse()

        # if there is no game declared we use search class for GA and we are interested in distances
        if(self.game == None):
            # ignore turns left/right at start for estimating path cost by cost script
            path_cost = node.g_cost
            for action in actions:

                if action == "Forward":
                    break

                if action != "Forward":
                    path_cost += -1

            return path_cost

        else:
            print(actions)
            self.game.player._drive(actions)
            print("[ SEARCH LOG ] Path cost: " + str(node.g_cost))
            print("[ SEARCH LOG ] Obstacles destroyed: " + str( (node.g_cost - len(actions)) // 9))
            print("[ SEARCH LOG ] Moves forward: " + str(moves_forward))
            print("[ SEARCH LOG ] Turns: " + str(turns))
            print("[ SEARCH LOG ] Actions overall: " + str(len(actions)))
            return actions
