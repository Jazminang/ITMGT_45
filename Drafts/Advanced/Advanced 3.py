def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
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
    current_stop = first_stop
    total_time = 0
    
    while current_stop != second_stop:
        if (current_stop, second_stop) in route_map:
            total_time += route_map[(current_stop, second_stop)]['travel_time_mins']
            break
        
        next_stop_options = [(current_stop, stop) for stop in route_map if current_stop == stop[0]]
        
        if not next_stop_options:
            return "Invalid route"
        
        next_stop_options.sort(key=lambda x: route_map[x]['travel_time_mins'])
        next_stop = next_stop_options[0][1]
        total_time += route_map[next_stop_options[0]]['travel_time_mins']
        current_stop = next_stop

    return total_time

legs = {
     ("upd","admu"): {
         "travel_time_mins": 10
     },
     ("admu","dlsu"): {
         "travel_time_mins": 35
     },
     ("dlsu","upd"): {
         "travel_time_mins": 55
     }
}

# Example usage
first_stop = "upd"
second_stop = "admu"
time = eta(first_stop, second_stop, legs)
print("ETA:", time, "minutes")
