def assertListEqual(a: list[any], b: list[any]):
    if len(a) >= len(b):
        for e in a:
            if not e in b:
                raise AssertionError(f"{e} not in list: {b}")
    else:
        for e in b:
            if not e in a:
                raise AssertionError(f"{e} not in list: {a}")


def assertSublist(container, sublist):
    for e in sublist:
        if not e in container:
            raise AssertionError(f"{e} not in list: {container}")
