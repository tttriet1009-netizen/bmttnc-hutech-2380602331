def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(",")]
print("List:", numbers)
print("Tuple từ List:", tao_tuple_tu_list(numbers))
