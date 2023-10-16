def singleTimeAppaer(list):
    response = []
    for i in list:
        appearance = 0
        for k in list:
            if k == i:
                appearance = appearance+1
                if appearance > 1:
                    response.append(i)

    set_dif = set(list).symmetric_difference(set(response))
    return set_dif


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 111, 12, 33, 44, 55, 66,
           77, 1, 12, 33, 44, 55, 66, 77, 2, 3, 4, 222]
    print(f'Elements those appear only once in list {singleTimeAppaer(lst)}')
