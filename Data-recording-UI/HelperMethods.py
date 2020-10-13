#region Min-Max values
MIN_AGE = 18
MAX_AGE = 100

MIN_WEIGHT = 0
MAX_WEIGHT = 500

# For now the concept of height is 5'10" = 5.10. Another example 6'01" = 6.01
# ************************** CAUTION WITH 5.1 AND 5.01 may have to think of a different way ****************************
MIN_HEIGHT = 1.00
MAX_HEIGHT = 8.00

DEFAULT_SCROLLDOWNMENU_OPTION = "Select an option"

Ethnicity = ["Select an option",
             "American Indian",
             "Asian",
             "African American",
             "Native Hawaiian or Other Pacific Islander",
             "White",
             "Hispanic or Latino"]

Race = ["Select an option",
        "African",
        "Asian",
        "European",
        "Native American",
        "Oceanic"]
#endregion

def isAgeValid(age):
    return MIN_AGE < age < MAX_AGE


def isWeightValid(weight):
    return MIN_WEIGHT < weight < MAX_WEIGHT


def isScrollDownMenuWrong(option):
    return option == DEFAULT_SCROLLDOWNMENU_OPTION


# may not be used
def isEmpty(field):
    return len(field) == 0


def isHeightValid(height):
    return MIN_HEIGHT < height < MAX_HEIGHT