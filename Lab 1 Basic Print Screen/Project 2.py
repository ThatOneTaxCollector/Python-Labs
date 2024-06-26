# Lab 2
# Partners: Braden Gerlach
# Comments: Takes in user input and,
#   performs number crunching to produce an output,
#   and it prints it to the terminal

import datetime


def main():
    # Accept numeric and string inputs from the user
    numeric_input = float(input("Enter a numeric value: "))
    string_input = input("Enter a string value: ")

    # Whack calc pipeline to mangle the inputs
    calculation_result = numeric_input * 3.14535
    calculation_result += 42 * len(string_input)

    # Formatting
    formatted_result = round(calculation_result, 2)

    # DateTime
    current_datetime = datetime.datetime.now()

    # Sloppy concatenation has been used to make the output look nice
    output_message = ("~~=====================================~\n" +
                      "The current date and time is:\n"

                      "{}").format(current_datetime) + ("\n"

                      "\nThe result of the calculation is:"
                      " {}").format(formatted_result) + "\n" + (
                      "~~=====================================~")

    # Print the final output
    print(output_message)


main()