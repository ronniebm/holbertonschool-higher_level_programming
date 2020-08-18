#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):

    _l = list(list_of_integers)
    size = len(_l)
    PEAK = 0

    if size == 0:
        return None

    elif size == 1:
        return _l[0]

    elif size == 2:
        return max(_l)

    # caso cuando la lista es impar.
    if size % 2 == 1:
        mid = (size // 2)
        # print(l)
        # print("mid = " + str(mid))

        for i in range(0, mid + 1):
            # print("***ciclo#" + str(i) + "***")

            val1 = _l[mid - i]
            val2 = _l[mid + i]

            if i == 0:
                if _l[mid] >= _l[mid - 1] and _l[mid] >= _l[mid + 1]:
                    # print("yahoo")
                    return _l[mid]

            elif i < mid:

                if val1 >= _l[mid - i - 1] and val1 >= _l[mid - i + 1]:
                    # print("jmm1")
                    return val1

                elif val2 >= _l[mid + i - 1] and val2 >= _l[mid + i + 1]:
                    # print("jmm2")
                    return val2

            elif i == mid:

                if val1 >= _l[mid - i + 1]:
                    return val1

                elif val2 >= _l[mid + i - 1]:
                    return val2

    # caso cuando la lista es par
    elif size % 2 == 0:
        max = (size // 2) - 1
        pl = max
        pr = (size // 2)
        # print(l)
        # print("pointer left = " + str(pl))
        # print("pointer right = " + str(pr))

        for i in range(0, max):
            # print("***ciclo#" + str(i) + "***")
            # print("**")

            val1 = _l[pl - i]
            val2 = _l[pr + i]

            if i < max:
                if val1 >= _l[pl - i - 1] and val1 >= _l[pl - i + 1]:
                    # print("jmm1")
                    # print(l[pl - 1])
                    return val1

                elif val2 >= _l[pr + i - 1] and val2 >= _l[pr + i + 1]:
                    # print("jmm2")

                    return val2

            elif i == max:
                if _l[pl] >= _l[pl + i]:
                    return _l[pl]

                elif _l[pr] >= _l[pr - i]:
                    return _l[pr]
