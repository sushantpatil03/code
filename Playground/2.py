import random
import time

def merge_sort(arr):
    if  len(arr)<=1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half,right_half)

def merge(left, right):
    res = []
    i = j = 0
    
    while i<len(left) and j<len(right):
        if  left[i]<right[j]:
            res.append(left[i])
            i += 1
        else: 
            res.append(right[j])
            j+=1
            
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x>pivot]
    mid = [x for x in arr if x==pivot]
    
    return quick_sort(left)+mid+quick_sort(right)
    

def calc_time(algo, size):
    arr = [random.randint(1,1000) for i in range(size)]
    st = time.time()
    algo(arr)
    end = time.time()
    return end-st

input_sizes = [100,1000,10000,10000]

for i in input_sizes:
    m = calc_time(merge_sort, i);
    q = calc_time(quick_sort, i)
    print(f"\n\nInput size : {i}\nMerge sort : {m}\nQuick sort : {q}")