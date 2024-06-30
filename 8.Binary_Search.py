# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


def search( nums, target):

    left, right = 0 , len(nums) - 1 # Đặt phạm vi tìm kiếm 

    while left <= right:      # kiểm tra phạm vi có còn hợp lệ
        mid = (left + right) // 2 # tìm giá trị mid của mảng

        if nums[mid] == target: # so sánh giá trị tại vị trí mid với target
            return mid          # trả về ngay lập tức giá trị tìm được
        elif nums[mid] < target: # so sánh giá trị tại vị trí mid với target
            left = mid + 1     # cập nhật lại giá trị phạm vi bên trái
        else:
            right = mid - 1 # cập nhật lại giá trị phạm vi bên trái
    
    return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2
    print(search(nums, target))