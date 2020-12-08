import math

'''
Prompts the user for a String and returns whatever was entered.
@param prompt - the prompt text for the user
@return - the String entered by the user
'''
def getString(prompt):
    return input(prompt + " ").strip()

# Tests for getString
# print(getString("What's your name?")) # Expected: exactly what was entered

'''
Converts a list of strings to a list of lowercase strings
@param list - a list of strings
@return - the list of lowercase strings
'''
def listToLowercase(list):
  for i in range(len(list)):
    list[i] = list[i].lower()
  return list

# Tests
# print(listToLowercase(["Yes", "Y", "No", "N"])) # Expected: ["yes", "y", "no", "n"]

'''
Converts a list of strings to a string with commas separating each
@param list - a list of strings
@return - the list converted to a string with commas separating each
'''
def listToString(list):
    result = " ["
    count = 0
    for item in list:
        count += 1
        if(count == len(list)):
            result += "or " + str(item)
        elif(count == len(list) - 1):
            result += str(item) + " "
        else:
            result += str(item) + ", "
    result += "]:"
    return result

# Tests
# nums = [1, 2, 3, 4, 5]
# print(listToString(nums))
# pets = ["Velcro", "Zipper", "Waffles"]
# print(listToString(pets))
# random = ["Marc", 39, 192.5, True]
# print(listToString(random))
# yesOrNo = ["Yes", "No"]
# print(listToString(yesOrNo))

'''
Validates that the user's input is included in a list of possible values
@param prompt - the prompt text for the user
@param possibleValues - a list of strings
@param totalAttempts - the maximum number of attempts allowed. Default value is infinity.
@return - the user's input if it was valid
@return - None if input wasn't valid within a number of attempts
'''
def validateUserString(prompt, possibleValues, displayPossibleValues = True, totalAttempts = float("inf"), invalidMsg = "Invalid input."):
  attempts = 0
  possibleValuesString = listToString(possibleValues)
  possibleValuesLowercase = listToLowercase(possibleValues)
  while (True):
    newPrompt = prompt
    invalidInputMsg = ""
    if(totalAttempts == float("inf") and attempts > 0):
      invalidInputMsg = "\n" + invalidMsg + " Try again...\n"
    elif(totalAttempts < float("inf") and attempts > 0):
      invalidInputMsg = "\n" + invalidMsg + " You have " + str(totalAttempts - attempts) + " attempt(s) remaining. Try again...\n"
    newPrompt = invalidInputMsg + newPrompt
    if(displayPossibleValues):
      newPrompt = newPrompt + possibleValuesString
    userInput = getString(newPrompt)
    inputLowercase = userInput.lower()
    if(inputLowercase in possibleValuesLowercase):
      return userInput
    attempts += 1
    if(attempts == totalAttempts):
      return None

# Tests
# print(validateUserString("Are you a student?", ["Yes", "No"]))
# print(validateUserString("Are you a student?", ["Yes", "No"], True, 3))
# print(validateUserString("Are you a student?", ["Yes", "No"], True, 3, "Incorrect Y/N value."))
# print(validateUserString("Are you a student?", ["Yes", "No"], True, float("inf"), "Incorrect Y/N value."))
# print(validateUserString("What is your account number?", ["9999"], False, 3, "That account number was not found."))

'''
Prompts the user to enter an integer. If the value is not an integer, it prints an invalid input message and tries again.  Otherwise, it returns the integer that was entered.
@param prompt - the prompt text for the user
@return the integer entered
'''
def getInt(prompt):
  invalidAttempt = False
  while(True):
    newPrompt = prompt
    if(invalidAttempt):
      newPrompt = "\nInvalid input. Try again...\n" + newPrompt
    try:
      userInput = getString(newPrompt + " [Enter a number without decimals]")
      userInputInt = int(userInput)
      return userInputInt
    except ValueError:
      invalidAttempt = True

# Tests
# print(getInt("What's your age?"))

'''
Prompts the user to enter a number. If the value is not a number, it prints an invalid input message and tries again.  Otherwise, it returns the value that was entered.
@param prompt - the prompt text for the user
@param convertToInt - a boolean value. If true the function will convert a whole number (example: 10.0) to its integer representation (example: 10)
@return the number entered
'''
def getFloat(prompt, convertToInt = False):
  invalidAttempt = False
  while(True):
    newPrompt = prompt
    if(invalidAttempt):
      newPrompt = "\nInvalid input. Try again...\n" + newPrompt
    try:
      userInput = getString(newPrompt + " [Enter a number]")
      userInputNum = float(userInput)
      if(convertToInt and userInputNum % 1 == 0):
        userInputNum = int(userInputNum)
      return userInputNum
    except ValueError:
      invalidAttempt = True

# Tests
# print(getFloat("What's your weight?"))
# print(getFloat("What's your weight?", True))

'''
Prompts the user to enter a whole number.  If the value is not a whole
number, prints the notIntMessage and tries again.  Otherwise, returns the
int that was entered.
@param prompt - the prompt text for the user
@param convertToInt - a boolean to determine if the input needs to be an int (True) or float (False)
@param notIntMessage the error message for not an int
@return the int entered
'''
def getNum(prompt, minValue = -float("inf"), maxValue = float("inf"), totalAttempts = float("inf"), convertToInt = False, invalidMsg = "Invalid number."):
  attempts = 0
  while(True):
    newPrompt = prompt
    if(minValue > -float("inf") and maxValue < float("inf")):
      newPrompt = prompt + " [Enter a number between " + str(minValue) + " and " + str(maxValue) + "]:"
    elif(minValue > -float("inf") and maxValue == float("inf")):
      newPrompt = prompt + " [Enter a number greater than or equal to " + str(minValue) + "]:"
    else:
      newPrompt = prompt + " [Enter a number]:"
    invalidInputMsg = ""
    if(totalAttempts == float("inf") and attempts > 0):
      invalidInputMsg = "\n" + invalidMsg + " Try again...\n"
    elif(totalAttempts < float("inf") and attempts > 0):
      invalidInputMsg = "\n" + invalidMsg + " You have " + str(totalAttempts - attempts) + " attempt(s) remaining. Try again...\n"
    newPrompt = invalidInputMsg + newPrompt
    userInput = getString(newPrompt)
    try:
      inputNum = float(userInput)
      if(convertToInt):
        inputNum = math.floor(inputNum)
      if(inputNum >= minValue and inputNum <= maxValue):
        return inputNum
      attempts += 1
      if(attempts == totalAttempts):
        return None
    except ValueError:
      attempts += 1
      if(attempts == totalAttempts):
        return None

# Tests
# print(getNum("How much do you weigh?"))
# print(getNum("How much do you weigh?", 0))
# print(getNum("How much do you weigh?", 0, 1000))
# print(getNum("How much do you weigh?", 0, 1000, 3))
# print(getNum("How much do you weigh?", 0, 1000, 3, True))