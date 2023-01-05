
def get_dict_key(dic, value):
    targets = []
    while True:
        keys = list(dic.keys())
        values = list(dic.values())
        try:
            idx = values.index(value)
            target = keys[idx]
            targets.append(target)
            del dic[target]
        except ValueError:
            return targets


def manhattan(a, b):
    # Write your code here
    states = {
        'ORIGIN': 0,
        'TURN': 1,
        'HORIZONTAL': 2,
        'VERTICAL': 3,
        'INTERSACTION': 4
    }
    origin = [0, 0]
    current_position = origin
    map_states = {tuple(current_position): states['ORIGIN']}

    all_routes = a.copy()
    all_routes.extend(b)

    current_no = 0
    intersaction_routes = list()

    for route in all_routes:
        if route[0] == 'E':
            if current_position != origin:
                map_states[tuple(current_position)] = states['TURN']
            for _ in range(int(route[1])):
                current_position[0] += 1
                pos = tuple(current_position)
                if pos in map_states and map_states[pos] == states['VERTICAL']:
                    map_states[pos] = states['INTERSACTION']
                elif pos not in map_states:
                    map_states[tuple(current_position)] = states['HORIZONTAL']

        if route[0] == 'W':
            if current_position != origin:
                map_states[tuple(current_position)] = states['TURN']
            for _ in range(int(route[1])):
                current_position[0] -= 1
                pos = tuple(current_position)
                if pos in map_states and map_states[pos] == states['VERTICAL']:
                    map_states[pos] = states['INTERSACTION']
                elif pos not in map_states:
                    map_states[tuple(current_position)] = states['HORIZONTAL']

        if route[0] == 'N':
            if current_position != origin:
                map_states[tuple(current_position)] = states['TURN']
            for _ in range(int(route[1])):
                current_position[1] += 1
                pos = tuple(current_position)
                if pos in map_states and map_states[pos] == states['HORIZONTAL']:
                    map_states[pos] = states['INTERSACTION']
                elif pos not in map_states:
                    map_states[tuple(current_position)] = states['VERTICAL']

        if route[0] == 'S':
            if current_position != origin:
                map_states[tuple(current_position)] = states['TURN']
            for _ in range(int(route[1])):
                current_position[1] -= 1
                pos = tuple(current_position)
                if pos in map_states and map_states[pos] == states['HORIZONTAL']:
                    map_states[pos] = states['INTERSACTION']
                elif pos not in map_states:
                    map_states[tuple(current_position)] = states['VERTICAL']
        
        current_no += 1
        if current_no == len(a):
            current_position = origin
    
    intersaction_routes = get_dict_key(map_states, states['INTERSACTION'])
    
    min_value = 0
    for item in intersaction_routes:
        sum = abs(item[0]) + abs(item[1])
        if min_value == 0:
            min_value = sum
        else:
            if sum < min_value:
                min_value = sum
    
    return min_value


a = ['E8', 'N5', 'W5', 'S3']
b = ['N7', 'E6', 'S4', 'W4']
print(manhattan(a, b))
