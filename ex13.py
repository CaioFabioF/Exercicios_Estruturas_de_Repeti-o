termo1 = 0
termo2 = 1
while True :
    termo3 = termo1 + termo2
    if termo3 > 500:
        break
    termo1 = termo2
    termo2 = termo3
    print(termo3)
