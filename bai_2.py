def Standardise(list_item: list[str]) -> list[str]:
    for i in range(0, len(list_item)):
        while " " in list_item[i]:
            list_item[i] = list_item[i].replace(" ", "")
        for letter in list_item[i]:
            letter = letter.capitalize()
    list_item.sort()
    return list_item


if "__main__" == __name__:
    li = ["sp-001", "SP-002", "sP-003"]
    li = Standardise(li)
    print(li)
