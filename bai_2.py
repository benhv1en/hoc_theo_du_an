def Standardise(list_item: list[str]) -> list[str]:
    for i in range(0, len(list_item)):
        while " " in list_item[i]:
            list_item[i] = list_item[i].replace(" ", "")
        list_item[i] = list_item[i].upper()
    list_item.sort(reverse=True)
    return list_item


if "__main__" == __name__:
    li = ["sp-002", "SP-001", "sP-003"]
    li = Standardise(li)
    print(li)
