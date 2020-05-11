'''
    计算[1,2,3,4,5]
'''
# def list_sum(my_list):
#     the_sum = 0
#     for num in my_list:
#         the_sum = the_sum + num
#     return the_sum

# def to_str(num,base):
#     convert_str = '0123456789ABCDEF'
#     if num < base:
#         return convert_str[num]
#
#     else:
#         return to_str(int(num/base),base) + convert_str[num % base]
#
# print(to_str(769,10))
# print(to_str(769,2))
# print(to_str(769,8))
# print(to_str(769,16))

from pythonds .basic.stack import Stack
s = Stack()
def to_str(num,base):
    convert_str = '0123456789ABCDEF'
    while num > 0:
        if num < base:
            s.push(convert_str[num])

        else:
            s.push(convert_str[num%base])
        num = num//base

    result = ''
    while not s.isEmpty():
        result = result + s.pop()

    return result

print(to_str(796,10))

