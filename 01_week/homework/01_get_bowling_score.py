def get_bowling_score(s):
    result = 0
    count = 0
    frames = list(s)
    print(frames)
    for i in range(len(frames)):
        if frames[i] == 'S':
            result += 10
            next_frame = frames[i+1]
            if next_frame == 'S':
                result += 10
            elif next_frame == '-':
                result += 0
            else:
                result += int(next_frame)
            next_next_frame = frames[i+2]
            if next_next_frame == 'S':
                result += 10
        print(result)






    print(result)
    pass


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300
