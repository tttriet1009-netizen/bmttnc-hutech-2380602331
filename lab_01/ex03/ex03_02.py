def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(",")]
print("List sau khi đảo ngược:", dao_nguoc_list(numbers))
