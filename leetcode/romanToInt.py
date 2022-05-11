str = "MCMXCIV"


def romanToInt(inputString: str) -> int:
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000,
             'IV': 4,
             'IX': 9,
             'XL': 40,
             'XC': 90,
             'CD': 400,
             'CM': 900}
    specialCase = ["IV", "IX", "XL", "XC", "CD", "CM"]

    specialList = []

    # special char
    for item in specialCase:
        if item in inputString:
            specialList.append(item)
            # remove the special char in s
            inputString = inputString.replace(item, '')
    # print(specialList);
    total = 0
    for item in specialList:
        total += roman[item]

    for item in inputString:
        total += roman[item]

    return total


print(romanToInt(str))
