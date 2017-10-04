def validPhoneNumber(phoneNumber):

    if ' ' not in phoneNumber:
        return False
    elif '-' not in phoneNumber:
        return False
    elif len(phoneNumber) > 14:
        return False
    return True

phoneNumber = "(323) 456-7890"
print(validPhoneNumber(phoneNumber))
