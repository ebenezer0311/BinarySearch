# Binary Search Algo
class Solution:
    def search(self,nums,target):
        start=0
        end=len(nums)-1

        while start<=end:
            mid=start+(end-start)//2

            if nums[mid]==target:
                return mid
            
            elif target>nums[mid]:
                start=mid+1
                
            else:
                end=mid-1
                
        return -1

#implement lower bound

def lowerBound(arr,n,x):

    index=n
    start=0
    end=n-1

    while start<=end:
        mid=(start+end) // 2
        
        if arr[mid]>=x:
            index=mid
            end=mid-1
            
        else:
            start=mid+1
        
    return index

#implement upper bound
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    start=0
    end=n-1
    index=n
    while start<=end:

        mid=(start+end)//2

        if arr[mid]>x:
            index=mid
            end=mid-1
        else:
            start=mid+1

    return index
    
# insert positions
class Solution:
    def searchInsert(self,nums,target):
        start=0
        end=len(nums)-1
        index=len(nums)

        while start<=end:
            mid=(start+end)//2

            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                index=mid
                end=mid-1
            
            else:
                start=mid+1
        return index

# 	Floor/Ceil in Sorted Array

def ceilingInSortedArray(n, x, arr):
    arr.sort()
    start=0
    end=n-1
    floor=-1
    ceil=-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==x:
            floor=arr[mid]
            ceil=arr[mid]
            return "{} {}".format(floor, ceil)
        
        elif arr[mid]>x:
            ceil=arr[mid]
            end=mid-1
        else:
            floor=arr[mid]
            start=mid+1
            
    return "{} {}".format(floor,ceil)

#Find first and last position of element in Sorted array
class Solution:
    def searchRange(self,nums,target):
        def firstOcc(arr,n,x):
            start=0
            end=n-1
            first=-1

            while start<=end:
                mid=(start+end)//2
                if arr[mid]==x:
                    first=mid
                    end=mid-1
                
                elif arr[mid]<x:
                    start=mid+1
                else:
                    end=mid-1
            return first

        def lastOcc(arr,n,x):
            start=0
            end=n-1
            last=-1

            while start<=end:
                mid=(start+end)//2

                if arr[mid]==x:
                    last=mid
                    start=mid+1
                
                elif arr[mid]<x:
                    start=mid+1
                else:
                    end=mid-1

            return last

        n=len(nums)
        first=firstOcc(nums,n,target)
        if first==-1:
            return [-1,-1]
        last=lastOcc(nums,n,target)
        return [first,last]

# Number of occurrence
def count(arr,n,x):
    def firstOcc(arr,n,x):
        start=0
        end=n-1
        first=0

        while start<=end:
            mid=(start+end)//2
            if arr[mid]==x:
                first=mid
                end=mid-1
                
            elif arr[mid]<x:
                start=mid+1
            else:
                end=mid-1
        return first

    def lastOcc(arr,n,x):
        start=0
        end=n-1
        last=0

        while start<=end:
            mid=(start+end)//2

            if arr[mid]==x:
                last=mid
                start=mid+1
                
            elif arr[mid]<x:
                start=mid+1
            else:
                end=mid-1

        return last

        
    first=firstOcc(arr,n,x)
    last=lastOcc(arr,n,x)
    ans=last-first+1
    if ans==1:
        return 0
    return ans

# search in a sorted rotated array
class Solution:
    def search(self,nums,target):
        n=len(nums)
        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid

            elif nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1

            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1

# search in a sorted rotated array(duplicates)
class Solution:
    def search(self, nums: [int], target: int) -> bool:
        n=len(nums)
        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return True

            if nums[start]==nums[mid]==nums[end]:
                start+=1
                end-=1
                continue

            elif nums[start]<=nums[mid]:
                if nums[start]<=target<=nums[mid]:
                    end=mid-1
                else:
                    start=mid+1

            else:
                if nums[mid]<=target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return False

#Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            middle = left + (right - left) // 2
        
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
    
        return nums[left]
    
# Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        start,end=1,x

        while start<=end:
            mid=(start+end)//2

            if mid*mid==x:
                return mid
            
            elif mid*mid>x:
                end=mid-1
            
            else:
                start=mid+1
        
        return end


        

    


