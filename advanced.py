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
    following_from_member = social_graph.get(from_member, {}).get('following', [])
    following_to_member = social_graph.get(to_member, {}).get('following', [])

    # Check if from_member follows to_member
    if to_member in following_from_member:
        # Check if to_member also follows from_member
        if from_member in following_to_member:
            return 'friends'
        else:
            return 'follower'
    # Check if to_member follows from_member
    elif from_member in following_to_member:
        return 'followed by'
    else:
        return 'no relationship'


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
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if len(set([board[row][col] for row in range(len(board))])) == 1 and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board)-1-i] for i in range(len(board))]
    if len(set(diagonal1)) == 1 and diagonal1[0] != '':
        return diagonal1[0]
    if len(set(diagonal2)) == 1 and diagonal2[0] != '':
        return diagonal2[0]

    # No winner
    return 'NO WINNER'

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
