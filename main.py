def main(num):
    return str(num)

def takenum ():
    return int(input("Enter your num:"))
    



if __name__ == "__main__":
    num = takenum()
    print(f"{type(main(num))} {main(num)}")

