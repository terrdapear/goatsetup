from random import randint
def main():
    t = 1000
    def out():
        #variables here
        n = 100
        return [ #lines here
            [n],
            [randint(1,n) for i in range(n)]
        ]

    with open("hatdog.txt",'w') as file:
        file.write(f"{t}")
        for _ in range(t):
            for line in out():
                if line:
                    file.write("\n"+" ".join([str(x) for x in line]))

if __name__=="__main__":
    main()
