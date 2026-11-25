
def check_eligibility(name, age, citizen):

    if age < 18 and citizen != "Y":
        print(f"{name} is not eligible to vote.")
        print("Reasons:")
        print("- Age is below 18.")
        print("- Not an Indian citizen.")

    elif age < 18:
        print(f"{name} is not eligible to vote.")
        print("Reason: Age is below 18.")

    elif citizen != "Y":
        print(f"{name} is not eligible to vote.")
        print("Reason: Not an Indian citizen.")

    else:
        print(f"{name} is eligible to vote.")


def main():

    while True:

        print("\n--- Voting Eligibility System ---")

        name = input("Enter your name: ")

        # Age validation
        while True:
            try:
                age = int(input("Enter your age: "))

                if age < 0 or age > 120:
                    print("Invalid age. Enter age between 0 and 120.")
                else:
                    break

            except ValueError:
                print("Invalid input. Enter a whole number for age.")

        # Citizenship validation
        while True:
            citizen = input(
                "Are you an Indian citizen? (Y/N): "
            ).strip().upper()

            if citizen in ("Y", "N"):
                break
            else:
                print("Invalid input. Enter Y or N.")

        # Check eligibility
        check_eligibility(name, age, citizen)

        # Ask whether to continue
        while True:
            again = input(
                "\nDo you want to check another person? (Y/N): "
            ).strip().upper()

            if again == "Y":
                break
            elif again == "N":
                print("\nThank you for using the Voting Eligibility System!")
                return
            else:
                print("Invalid input. Enter Y or N.")


if __name__ == "__main__":
    main()
