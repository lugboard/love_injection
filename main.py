import random

count = 0
while True:
    which = random.randrange(2) # 0=ドド(0,4,7) 1=スコ
    if which == 0 and (count == 0 or count == 4 or count == 8):
        print("ドド", end ="")
        count += 1
    elif which == 0 and (count != 0 or count != 4 or count != 8):
        print("ドド")
        count = 0
    elif which == 1 and (count == 0 or count == 4 or count == 8):
        print("スコ")
        count = 0
    else:
        if count == 3 or count == 7 or count == 11:
            print("スコ")
            if count == 11:
                break
            count += 1
        else:
            print("スコ", end="")
            count += 1
print("ラブ注入♡")