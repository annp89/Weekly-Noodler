input_sequence = [3, 6, 1, 2, 4, 5, 5, 6, 1, 8, 3]
output_sequence = []

for count, item in enumerate(input_sequence):
    if count == 0:
        output_sequence.append(item)
    elif count == 1:
        if input_sequence[count] < output_sequence[-1]:
            check = 'CHECK_GREATER'
            output_sequence.append(item)
        elif input_sequence[count] > output_sequence[-1]:
            check = 'CHECK_LESSER'
            output_sequence.append(item)
        else:
            continue
    else:
        if check == 'CHECK_GREATER' and input_sequence[count] > output_sequence[-1]:
            output_sequence.append(item)
            check = 'CHECK_LESSER'
        elif check == 'CHECK_LESSER' and input_sequence[count] < output_sequence[-1]:
            output_sequence.append(item)
            check = 'CHECK_GREATER'
        else:
            continue

print output_sequence
