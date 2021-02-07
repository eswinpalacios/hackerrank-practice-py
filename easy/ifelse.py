def if_else(n=0):
    rest = n % 2
    if rest > 0:
        return "Weird"
    elif rest == 0 and n in range(2, 6):
        return "Not Weird"
    elif rest == 0 and n in range(6, 21):
        return "Weird"
    else:
        return "Not Weird"


print(if_else(20))
