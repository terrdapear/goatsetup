from random import randint
def main():
    t = 1000
    out = [
        [randint(1,2*10**5),randint(3,10**3)]
        for _ in range(t)
    ]

    with open("hatdog.txt",'w') as file:
        file.write(f"{t}")
        for line in out:
            if line:
                file.write("\n"+" ".join([str(x) for x in line]))

if __name__=="__main__":
    main()
