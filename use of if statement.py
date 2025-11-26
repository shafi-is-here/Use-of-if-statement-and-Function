is_male = False
is_tall = True

if is_male and is_tall:
    print("Your are both male and tall.")
elif is_male and not(is_tall):
    print("You are male but not tall.")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:

    print("you are neither male or tall")
      def max_num(num1, num2, num3):
        if num1>=num2 and num1>=num3 :
         return num1
        elif num2>=num1 and num2>=num3 :
            return num2
        else :
            return num3
print(max_num(20, 30, 10))
