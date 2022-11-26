def parse_data(puzzle_input: str) -> dict[str, list[str]]:
    network = {}
    for line in puzzle_input.replace(" ", "").splitlines():
        name, connections = line.split("<->")
        network[name] = connections.split(",")
    return network


def get_local_net(network: dict[str, list[str]], node_name: str) -> set[str]:
    seen_nodes = set()
    open_nodes = {node_name}

    while open_nodes:
        current_node = open_nodes.pop()
        seen_nodes.add(current_node)

        for con in network[current_node]:
            if con not in seen_nodes:
                open_nodes.add(con)

    return seen_nodes


def solution_1(puzzle_input: str) -> int:
    net = parse_data(puzzle_input)
    return len(get_local_net(net, "0"))


def solution_2(puzzle_input: str) -> int:
    net = parse_data(puzzle_input)
    node_names = set(net.keys())
    groups = []
    while node_names:
        group = get_local_net(net, node_names.pop())
        groups.append(group)
        node_names = node_names.difference(group)
    return len(groups)
