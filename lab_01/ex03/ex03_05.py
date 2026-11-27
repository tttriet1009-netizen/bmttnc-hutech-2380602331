def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
print("Số lần xuất hiện của các phần tử:", dem_so_lan_xuat_hien(input_string.split()))
