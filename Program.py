def process_list(input_list):
    # Checking if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("🔴 Error: The length of the list must be a multiple of 10")

    # Removing items at positions which are multiples of 2 or 3
    filtered_list = [item for index, item in enumerate(input_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]

    return filtered_list


if __name__ == '__main__':
    try:
      UserInput = input("Enter Numbers, Separated with spaces: ")
      InputList = list(map(int, UserInput.split()))
      result = process_list(InputList)
      print("Input List:", InputList)
      print("Output List:", result)
    except ValueError as e:
      print(e)
    except Exception as e:
      print("Unexpected Error Occured 😑")
    finally:
      print("Program Complete ")
