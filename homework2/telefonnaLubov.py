def nums_to_text(nums):
    nums.append(1)
    msg = ""
    count = 0
    previous = None

    for elem in nums:
        if previous == elem or previous == None:
            count += 1
        else:
            if previous != -1:
                mod3 = count % 3
                mod4 = count % 4

                match previous:
                    case 2:
                        match mod3:
                            case 1: msg += "a"
                            case 2: msg += "b"
                            case 0: msg += "c"
                    case 3:
                        match mod3:
                            case 1: msg += "d"
                            case 2: msg += "e"
                            case 0: msg += "f"
                    case 4:
                        match mod3:
                            case 1: msg += "g"
                            case 2: msg += "h"
                            case 0: msg += "i"
                    case 5:
                        match mod3:
                            case 1: msg += "j"
                            case 2: msg += "k"
                            case 0: msg += "l"
                    case 6:
                        match mod3:
                            case 1: msg += "m"
                            case 2: msg += "n"
                            case 0: msg += "o"
                    case 7:
                        match mod4:
                            case 1: msg += "p"
                            case 2: msg += "q"
                            case 3: msg += "r"
                            case 0: msg += "s"
                    case 8:
                        match mod3:
                            case 1: msg += "t"
                            case 2: msg += "u"
                            case 0: msg += "v"
                    case 9:
                        match mod4:
                            case 1: msg += "w"
                            case 2: msg += "x"
                            case 3: msg += "y"
                            case 0: msg += "z"
                    case 0:
                        msg += " "
            #     count = 1
            # else:
            count = 1
        previous = elem
    return msg

def text_to_nums(text):
    button_matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
                     ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    nums = []
    prev_letter = None
    lower_text = text.lower()

    for elem in lower_text:
        if elem != " ":
            i = 2  # button digit
            is_found = False

            for button in button_matrix:
                j = 1  # times the digit needs to be pressed
                if not is_found:
                    for letter in button:
                        if letter == elem:
                            for same_button in button:
                                if prev_letter == same_button:
                                    nums.append(-1)
                                    break
                            for times in range(j):
                                nums.append(i)

                            is_found = True
                            break
                        j += 1
                else:
                    break
                i += 1
        else:
            nums.append(0)
        prev_letter = elem
    return nums

def nums_to_angle(nums):
    sum = 0
    for number in nums:
        if number >= 0 and number <= 9 or number < 0 and number >= -9: #cannot have a number thats not on the phone?
            sum += number * 30
    
    if sum > 359 or sum < -359:
        sum =sum % 360
    if (sum < 0):
        sum += 360
    return sum

pivot_angles = []
for x in range(0, 345, 15):
    pivot_angles.append(x)
pivot_angles_size = len(pivot_angles)

def angles_to_nums(angles):
    nums = []
    for elem in angles:
        #normalize
        if elem > 359 or elem < -359:
            elem =elem % 360
        if (elem < 0):
            elem += 360
        #floor or ceil
        i = 0
        while i < pivot_angles_size - 1:
            if elem >= pivot_angles[i] and elem <= pivot_angles[i + 1]:
                if i % 2 == 0:
                    elem = pivot_angles[i]
                else:
                    elem = pivot_angles[i + 1]
            i += 1
        #calculate number
        if elem != 0 and elem < 330:
            if elem == 300:
                nums.append(0)
            else:
                nums.append(int(elem / 30))
    return nums 

def is_phone_tastic(word):
    if word == "":
        return False
    nums = text_to_nums(word)
    angle = nums_to_angle(nums)
    division = angle / len(word)
    return int(division) == division

# print(nums_to_text([2, 2, 1, 2, 0, 6, 6, 2, 0, 6, 6, 2]))
# print(text_to_nums("I nomerut e ei sega da kaja"))
# print(text_to_nums("PiToNa iSkAsH lI dA tI pOkAjA"))
# print(nums_to_text([4, 4, 4, 0, 6, 6, -1, 6, 6, 6, -1, 6, 3, 3, 7, 7,
#                     7, 8, 8, -1, 8, 0, 3, 3, 0, 3, 3, 4, 4, 4, 0, 7, 7, 7, 7, 3, 3, 4, 2, 0, 3, 2, 0, 5, 5, 2, 5, 2]))
# print(text_to_nums("aaaAAab"))
# print(nums_to_text([0, 2, 2, 2, 2, 2, 2, 2, 2, 0]))

# print(nums_to_angle([-12, -6, -6, -2]))
# print(text_to_nums("aa"))
# print(is_phone_tastic("               "))

# kurec = []
# for x in range(0, 360, 15):
#     kurec.append(x)
# print(kurec)
# tashak = angles_to_nums(kurec)
# print(tashak)

# print(angles_to_nums([15.01]))
