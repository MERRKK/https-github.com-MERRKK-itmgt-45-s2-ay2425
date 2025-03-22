'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
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
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # Check if from_member comes from to_member (assume it is false first baseline)
    from_follows_to = False
    if from_member in social_graph and "following" in social_graph[from_member]:
        if to_member in social_graph[from_member]["following"]:
            from_follows_to = True
    
    # Check if to_member comes from from_member (assume it is false first baseline)
    to_follows_from = False
    if to_member in social_graph and "following" in social_graph[to_member]:
        if from_member in social_graph[to_member]["following"]:
            to_follows_from = True
    
    # Determine relationship status based on who follows whom sequencing
    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Determine size of the board based on #
    n = len(board)
    
    # Check rows (ensure if all elements are the same symbol in a column/row via set command)
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]
    
    # Check columns 
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if len(set(column)) == 1 and column[0] != "":
            return column[0]
    
    # Check top left to bottom right diagonal 
    diagonal1 = [board[i][i] for i in range(n)]
    if len(set(diagonal1)) == 1 and diagonal1[0] != "":
        return diagonal1[0]
    
    # Check opposite diagonal line
    diagonal2 = [board[i][n-i-1] for i in range(n)]
    if len(set(diagonal2)) == 1 and diagonal2[0] != "":
        return diagonal2[0]
    
    # If there is no winner found, just return output
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
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

    # 1 Cycle Conducted if start and end route are at the same stop! 
    if first_stop == second_stop:
        # Calculate total time for the entire route
        total_time = 0
        for leg in route_map:
            total_time += route_map[leg]['travel_time_mins']
        return total_time
    
    # Otherwise, Find the path from first_stop to second_stop
    current_stop = first_stop
    total_time = 0
    
    next_stops = {}
    for leg in route_map:
        start, end = leg
        next_stops[start] = {
            'next': end, 
            'time': route_map[leg]['travel_time_mins']
        }
        
    # Travel until the second stop
    while current_stop != second_stop:
        # Get info for the next leg
        leg_info = next_stops[current_stop]        
        # Add travel time
        total_time += leg_info['time']       
        # Move to the next stop
        current_stop = leg_info['next']
    
    return total_time
