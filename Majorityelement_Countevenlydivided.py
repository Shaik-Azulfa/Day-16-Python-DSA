#Majority Element
def majorityElement(nums):
    n = len(nums)
    count = {} # count store karne ke liye

    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n // 2:
            return num
          #Count evenly divided  digits
def countDigits(n):
    temp = n
    count = 0
    while temp != 0:
        digit = temp % 10 # last digit nikali
        # Mistake 1: if digit==0 and digit%n==0 ❌
        # Sahi: digit 0 na ho AUR n % digit == 0 ho
        if digit != 0 and n % digit == 0:
            count += 1
        temp = temp // 10 # Mistake 2: temp//10 likha tha, store nahi kiya ❌
    return count

# Example: n = 12
# digit=2: 2!=0 aur 12%2==0 → count=1
# digit=1: 1!=0 aur 12%1==0 → count=2
# Answer = 2
