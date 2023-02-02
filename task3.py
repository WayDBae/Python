lis = [11,8,12,1,100]
def find_min(lis):
    min_element=lis[0]
    for element in lis:
        if element < min_element:
            min_element = element
    return min_element
print(find_min(lis))
