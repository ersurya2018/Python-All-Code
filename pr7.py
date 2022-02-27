def largest(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max
a=largest([10,3,3,4,5,6,90])
print(a)