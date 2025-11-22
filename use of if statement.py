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