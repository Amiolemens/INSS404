def request():
    num1=input('Enter variable num1')
    num2=input('Enter variable num2')
    print(addition(num1,num2))
    print(substraction(num1,num2))
    print(multiplication(num1,num2))
    print(division(num1,num2))
    print(maximum(num1,num2))
    print(minimum(num1,num2))

    def addition(num1, num2):
        sum = int(num1) + int(num2)
        return sum

num=int(input('Enter a positive integer:'))
if num%2==0:
    print(num,'even number')
else:
    print('num,odd number')