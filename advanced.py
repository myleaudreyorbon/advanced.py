'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see `advanced_sample_data.py` for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def relationship_status(from_member, to_member, social_graph):
    following_from_member = social_graph.get(from_member, {}).get("following", [])
    following_to_member = social_graph.get(to_member, {}).get("following", [])

    # Check if from_member follows to_member
    if to_member in following_from_member:
        # Check if to_member also follows from_member
        if from_member in following_to_member:
            return "friends"
        else:
            return "follower"
    # Check if to_member follows from_member
    elif from_member in following_to_member:
        return "followed by"
    else:
        return "no relationship"

social_graph = {
"@bongolpoc":{"first_name":"Joselito",
                "last_name":"Olpoc",
                "following":[
                ]
},
"@joaquin":  {"first_name":"Joaquin",
                "last_name":"Gonzales",
                "following":[
                    "@chums","@jobenilagan"
                ]
},
"@chums" : {"first_name":"Matthew",
            "last_name":"Uy",
            "following":[
                "@bongolpoc","@miketan","@rudyang","@joeilagan"
            ]
},
"@jobenilagan":{"first_name":"Joben",
                "last_name":"Ilagan",
            "following":[
                "@eeebeee","@joeilagan","@chums","@joaquin"
                ]
},
"@joeilagan":{"first_name":"Joe",
                "last_name":"Ilagan",
                "following":[
                "@eeebeee","@jobenilagan","@chums"
                ]
},
"@eeebeee":  {"first_name":"Elizabeth",
                "last_name":"Ilagan",
                "following":[
                "@jobenilagan","@joeilagan"
                ]
},
}

from_member = "@joaquin"
to_member = "@jobenilagan"
print(relationship_status(from_member, to_member, social_graph))


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see `advanced_sample_data.py` for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner, or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(len(board)):
        # Check rows
        if len(set(board[i])) == 1 and board[i][0] != "-":
            return board[i][0]
        # Check columns
        if len(set(row[i] for row in board)) == 1 and board[0][i] != "-":
            return board[0][i]
    
    # Check diagonals
    if len(set(board[i][i] for i in range(len(board)))) == 1 and board[0][0] != "-":
        return board[0][0]
    if len(set(board[i][len(board) - 1 - i] for i in range(len(board)))) == 1 and board[0][len(board) - 1] != "-":
        return board[0][len(board) - 1]
    
    return "NO WINNER"

# Sample tic-tac-toe boards
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

# Example usage
print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see `advanced_sample_data.py` for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        # Check if there is a direct route between current_stop and second_stop
        if (current_stop, second_stop) in route_map:
            total_time += route_map[(current_stop, second_stop)]["travel_time_mins"]
            break
        
        # Find the next stop in the route_map
        found = False
        for route in route_map:
            if route[0] == current_stop:
                total_time += route_map[route]["travel_time_mins"]
                current_stop = route[1]
                found = True
                break

        # If no route is found, return -1
        if not found:
            return -1

    return total_time

# Example usage:
route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

first_stop = "admu"
second_stop = "upd"
print(eta(first_stop, second_stop, route_map))