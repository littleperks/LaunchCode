def is_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Give me a year and I will return \"True\" if leap year and \"False\" otherwise: "))

    print(is_leap(year))


if __name__ == "__main__":
    main()