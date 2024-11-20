#calculator 

def calculator(input_str):
    pieces = input_str.split(" ")
    while "*" in pieces:
        split_point = pieces.index("*")
        pieces[split_point - 1] =  int(pieces[split_point - 1]) * int(pieces[split_point + 1])
        pieces.pop(split_point + 1)
        pieces.pop(split_point)

    result = int(pieces[0])
    pieces.pop(0)
    while len(pieces) > 0:
        if pieces.pop(0) == "+":
            result += int(pieces.pop(0))
        else:
            result -= int(pieces.pop(0))
    return result

def calculator(input_str):
    pieces = input_str.split(" ")
    if len(pieces) == 1:
        return int(pieces[0])
    
    if "+" in pieces:
        split_point = pieces.index("+")
        return calculator(" ".join(pieces[:split_point])) + calculator(" ".join(pieces[split_point + 1:]))
    if "-" in pieces:
        split_point = pieces.index("-")
        return calculator(" ".join(pieces[:split_point])) - calculator(" ".join(pieces[split_point + 1:]))
    
    if pieces[1] == "*":
        return calculator(pieces[0]) * calculator(" ".join(pieces[2:]))