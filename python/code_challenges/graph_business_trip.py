def direct_flights(graph, city_list):
    if len(city_list) == 0:
        return (False, 0)
    total_cost = 0
    graph_keys = graph.get_nodes()
    key_values = dict()
    neighbors = dict()
    for item in graph_keys:
        neigh_list = graph.get_neighbors(item)
        key_values.update({f"{item.value}": item})
        neighbors.update({f"{item.value}": neigh_list})
    if city_list[0] not in key_values:
        return (False, 0)
    index = 0
    for place in city_list:
        index += 1
        current_neighbors = neighbors[place]
        for edge in current_neighbors:
            if index == len(city_list):
                break
            if edge.vertex.value == city_list[index]:
                total_cost += edge.weight
                break

    if total_cost > 0:
        return (True, total_cost)
    else:
        return (False, 0)
