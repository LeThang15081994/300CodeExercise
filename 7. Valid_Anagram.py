# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

''' 
Cách 1
def isAnagram(str1, str2):

        if len(str1) != len(str2): # so sánh độ dài hai chuỗi.
             return False

        res1 = sorted(str1) # Sử dụng sorted để sắp xếp lại chuỗi 1.
        res2 = sorted(str2) # Sử dụng sorted để sắp xếp lại chuỗi 2.
        if res1 == res2: # So sánh hai list.
            return True
        else:
            return False
'''

# Cách 2: kiểm tra tần xuất lặp lại của các ký tự trong chuỗi

def isAnagram(str1, str2):
    if len(str1) != len(str2): # so sánh độ dài hai chuỗi.
            return False
    
    count = [0] * 26 # tạo một list count để đếm tần xuất xuất hiện trong chuỗi s và t với các ký tự từ a - z

    for char_str1, char_str2 in zip(str1,str2):
         count[ord(char_str1) - ord('a')] += 1 # Tăng đếm số ký tự trong chuỗi str1
         count[ord(char_str2) - ord('a')] -= 1 # Giảm đếm số ký tự trong chuỗi str2

    return all(index == 0 for index in count) # Kiểm tra xem tất cả các giá trị trong bảng đếm có bằng 0 hay không



if __name__ == "__main__":
    str1 = input("Nhập String 1: ")
    str2 = input("Nhập String 2: ")
    
    print(isAnagram(str1, str2))