def mystery(start=0):
    elems = [start]

    def some_function(elem=None):
        if isinstance(elem, int):
            elems.append(elem + elems[-1])

        if isinstance(elem, str):
            if elem.strip().isnumeric():
                num = int(elem.strip())
                if num % 2 == 0:
                    num *= 2
                else:
                    num = -num

                elems.append(num + elems[-1])
            else:
                num = len(elem)
                if num % 2 == 0:
                    if elems[-1] % 2 == 1 and elems[-1] != 5:
                        elems.append(elems[-1] - num)
                    else:
                        elems.append(elems[-1] + num)
                else:
                    if num % 3 == 0 or (num % 5 == 0 and elems[-1] != 0):
                        elems.append(elems[-1] - num)
                    else:
                        elems.append(elems[-1] + num)

        return elems[-1]
    return some_function
