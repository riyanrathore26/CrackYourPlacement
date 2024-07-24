class Solution():
    def multiply(first,second):
        num1,num2 = 0,0
        while first or second:
            if first:
                num1 = num1*10+first.val
                first = first.next
            if second:
                num2 = num2*10+second.val
                second = second.next
            return num1*num2