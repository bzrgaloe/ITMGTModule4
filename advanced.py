def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    board_size = len(board)

    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]

    for column in range(board_size):
        if len(set([row[column] for row in board])) == 1 and board[0][column] != "":
            return board[0][column]

    down_diagonal = [board[pos][pos] for pos in range(board_size)]
    up_diagonal = [board[row][board_size - 1 - row] for row in range(board_size)]
    if len(set(down_diagonal)) == 1 and down_diagonal[0] != "":
        return down_diagonal[0]
    if len(set(up_diagonal)) == 1 and up_diagonal[0] != "":
        return up_diagonal[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    travel_time = 0

    while current_stop != second_stop:
        if (current_stop, second_stop) in route_map:
            travel_time += route_map[(current_stop, second_stop)]['travel_time_mins']
            break
        else:
            for key in route_map.keys():
                if key[0] == current_stop:
                    travel_time += route_map[key]['travel_time_mins']
                    current_stop = key[1]
                    break
    
    return travel_time
