def convert(number):
    res = ""
    values = {3: "Pling", 5: "Plang", 7:"Plong"}
    for key, value in values.items():
        if number % key == 0:
            res += value

    if res == '':
        return str(number)
    else:
        return res
