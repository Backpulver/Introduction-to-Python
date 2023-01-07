def nums_to_text(nums):
    nums.append(1)
    alphabet_matrix = [[" "], [], ["c", "a", "b"], ["f", "d", "e"], ["i", "g", "h"], ["l", "j", "k"],
                     ["o", "m", "n"], ["s", "p", "q", "r"], ["v", "t", "u"], ["z", "w", "x", "y"]]
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
                
                if previous == 0:
                    msg += alphabet_matrix[previous][0]
                elif previous == 7 or previous == 9:
                    msg += alphabet_matrix[previous][mod4]
                else:
                    msg += alphabet_matrix[previous][mod3]
            count = 1
        previous = elem

        
    return msg

def text_to_nums(text):
    button_matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
                     ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    nums = []
    prev_button = None
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
                            if prev_button == button:
                                nums.append(-1)
                            for times in range(j):
                                nums.append(i)

                            prev_button = button
                            is_found = True
                            break
                        j += 1
                else:
                    break
                i += 1
        else:
            nums.append(0)
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
    division = nums_to_angle(text_to_nums(word)) / len(word)
    return int(division) == division


# print(nums_to_text([7, 7, 7, 7]))
print(nums_to_text(text_to_nums("i nomeRut e  ei sEga da kajA   pitona iskasH li da ti pokaja")))