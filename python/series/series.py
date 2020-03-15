def slices(series, length):
    if length > len(series) or length <= 0: raise ValueError("Length error.")
    return [series[i:(i+length)] for i in range(len(series)+1) if len(series[i:(i+length)]) == length]


