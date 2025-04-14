def main():

    slide1 = float(input("Enter the length of side1: "))
    slide2 = float(input("Enter the length of slide2: "))
    slide3 = float(input("Enter the length of slide3: "))

    perimeter = slide1 + slide2 + slide3

    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()