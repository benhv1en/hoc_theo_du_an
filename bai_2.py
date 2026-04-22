def Standardise(list_item: list[str]) -> list[str]:
    for item in list_item:
        while " " in item:
            item.replace(" ", "")
        item.capitalize()
