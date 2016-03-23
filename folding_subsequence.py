input_sequence = [3, 6, 1, 2, 4, 3, 5, 6, 1, 8, 3]
output_sequence = []
sequence_length = len(input_sequence) - 1

for count, item in enumerate(input_sequence):
    if count == 0:
        output_sequence.append(item)
    elif count == 1:
        if input_sequence[count] < output_sequence[-1]:
            if count != sequence_length and input_sequence[count+1] < input_sequence[count]:
                continue
            check = 'CHECK_GREATER'
            output_sequence.append(item)
        elif input_sequence[count] > output_sequence[-1]:
            if count != sequence_length and input_sequence[count+1] > input_sequence[count]:
                continue
            check = 'CHECK_LESSER'
            output_sequence.append(item)
        else:
            continue
    else:
        if check == 'CHECK_GREATER' and input_sequence[count] > output_sequence[-1]:
            if count != sequence_length and input_sequence[count+1] > input_sequence[count]:
                continue
            check = 'CHECK_LESSER'
            output_sequence.append(item)
        elif check == 'CHECK_LESSER' and input_sequence[count] < output_sequence[-1]:
            if count != sequence_length and input_sequence[count+1] < input_sequence[count]:
                continue
            check = 'CHECK_GREATER'
            output_sequence.append(item)
        else:
            continue

print output_sequence
