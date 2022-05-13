# secret --> gizli sayı, guess --> tahmin
import random


def verify(guess, secret):
    if guess > secret:
        return -1
    elif guess == secret:
        return 0
    else:
        return 1


def guess_a_number(secret_num):
    i = 0
    upper_bound = 1000000
    lower_bound = 1
    guess = (lower_bound + upper_bound) // 2
    while i < 50:
        print("Gizli Sayı -> " + str(secret_num))
        print("Denenen Sayı -> " + str(guess))
        result = verify(guess, secret_num)
        if result == 1:
            print("Eşleşmiyor.Kalan hakkınız: " + str(49 - i))
            print("Dönen değer -> " + str(result))
            lower_bound = guess + 1
            guess = (lower_bound + upper_bound) // 2
        elif result == 0:
            print("Kazandın!")
            break
        else:
            print("Eşleşmiyor.Kalan hakkınız: " + str(49 - i))
            print("Dönen değer -> " + str(result))
            upper_bound = guess - 1
            guess = (upper_bound + lower_bound) // 2

        print()
        i += 1
    else:
        print("Hak Bitti")


secret_num = random.randint(1, 1000000)
guess_a_number(secret_num)
