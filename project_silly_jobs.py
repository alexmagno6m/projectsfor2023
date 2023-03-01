from silly_jobs import work1, work2
import random

while True:
    first_work = random.choice(work1)
    second_work = random.choice(work2)
    print("\n")
    print("{} {}".format(first_work, second_work))
    print("\n")
    try_again = input("intentar de nuevo? (presione Enter o sino n para salir)")
    if try_again.lower()=="n":
        break
        input("\nPresione Enter para salir")