def main():
    number = int(input("Enter a number "))

    if number %2 == 1:
        result = 1
    else:
        result = 0

    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()
