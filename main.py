import requests as rq

from keys import edamam_id, edamam_key, url


def bmr_calculation():

    weightInKg = int(input("Enter your weight in Kg: \n"))
    heightInCentemeters = int(input("Enter your height in Cm: \n"))
    age = int(input("Enter your age in years: \n"))
    MaleOrFemale = input("Are you a (M)ale or (F)emale? \n").lower()

    # Mifflin St. Jeor Equation
    if MaleOrFemale == "m":
        bmr = 66.5 + (13.75 *
                      weightInKg) + (5 * heightInCentemeters) - (6.755 * age)
        bmr = round(bmr)

    if MaleOrFemale == "f":
        bmr = 655.1 + (9.6 * weightInKg) + (1.8 * heightInCentemeters) - (4.7 *
                                                                          age)
        bmr = round(bmr)
    print(f" Your BMR is : {bmr}kcals")

    return bmr


def daily_caloric_needs(bmr):

    print('''
    1 = Sendentary
    2 = Exercise 1 - 3 times a week
    3 = Exercise 4 - 5 times a week
    4 = Daily Exercise / intensity of exercise 3 - 4 times a week
    5 = Intense Exercise 6 times a week \n''')

    activityLevel = int(input("Select your activity level: "))
    if activityLevel == 1:
        activityLevelIndex = 1.2
    elif activityLevel == 2:
        activityLevelIndex = 1.375
    elif activityLevel == 3:
        activityLevelIndex = 1.46
    elif activityLevel == 4:
        activityLevelIndex = 1.725
    elif activityLevel == 5:
        activityLevelIndex = 1.9
    dailyCaloriesNeeded = int(bmr * activityLevelIndex)

    print(
        f"\nBased you your activity level, to maintain your current body weight you will need {dailyCaloriesNeeded}kcals a day."
    )
    return dailyCaloriesNeeded


def macros_calculation(kcals):
    # Maintenace macro calories
    calories_from_protien = int(.4 * kcals)
    protien_grams = int(calories_from_protien / 4)
    calories_from_carbs = int(.4 * kcals)
    carb_grams = int(calories_from_carbs / 4)
    calories_from_fat = int(.2 * kcals)
    fat_grams = int(calories_from_fat / 9)

    print(
        f"Calories from Protien: {calories_from_protien}kcals from {protien_grams} grams of protien."
    )
    print(
        f"Calories from Carbs: {calories_from_carbs}kcals from {carb_grams} grams of cab."
    )
    print(
        f"Calories from Fat: {calories_from_fat}kcals from {fat_grams} grams of fat.\n"
    )

    LoseOrGain = input(
        "Do you want to (L)ose, (G)ain or (M)aintain body weight? \n").lower()
    if LoseOrGain == 'l':

        # Calculate fat loss
        # .5kg of fat has 3,500 calories -- To lose .25kg a week, we divide 3,500 by 2 then by 7 and subtract from kcals

        LoseQuarterKilo_Calories = int(kcals - int((3500 / 2) / 7))
        print(
            f"To lose .5lb (.25kg) of body weight a week, your daily calories need to drop to {LoseQuarterKilo_Calories}kcals a day."
        )

        calories_from_protien = int(.4 * LoseQuarterKilo_Calories)
        protien_grams = int(calories_from_protien / 4)
        calories_from_carbs = int(.4 * LoseQuarterKilo_Calories)
        carb_grams = int(calories_from_carbs / 4)
        calories_from_fat = int(.2 * LoseQuarterKilo_Calories)
        fat_grams = int(calories_from_fat / 9)

        print(
            f"Calories from Protien: {calories_from_protien}kcals from {protien_grams} grams of protien."
        )
        print(
            f"Calories from Carbs: {calories_from_carbs}kcals from {carb_grams} grams of cab."
        )
        print(
            f"Calories from Fat: {calories_from_fat}kcals from {fat_grams} grams of fat.\n"
        )

    if LoseOrGain == 'g':

        # Calculate fat gain
        # .5kg of fat has 3,500 calories -- To gain .25kg a week, we divide 3,500 by 2 then by 7 and add to kcals

        GainQuarterKilo_Calories = int(kcals + int((3500 / 2) / 7))
        print(
            f"To gain .5lb (.25kg) of body weight a week, your daily calories need to increase to {GainQuarterKilo_Calories}kcal a day."
        )

        calories_from_protien = int(.4 * GainQuarterKilo_Calories)
        protien_grams = int(calories_from_protien / 4)
        calories_from_carbs = int(.4 * GainQuarterKilo_Calories)
        carb_grams = int(calories_from_carbs / 4)
        calories_from_fat = int(.2 * GainQuarterKilo_Calories)
        fat_grams = int(calories_from_fat / 9)

        print(
            f"Calories from Protien: {calories_from_protien}kcals from {protien_grams} grams of protien."
        )
        print(
            f"Calories from Carbs: {calories_from_carbs}kcals from {carb_grams} grams of cab."
        )
        print(
            f"Calories from Fat: {calories_from_fat}kcals from {fat_grams} grams of fat.\n"
        )

    if LoseOrGain == 'm':
        return


def food_calories():

    ingr = []

    while True:
        data = input("Enter your ingredient: ")
        ingr.append(data)

        choice = input("Enter another ingredient? (Y/N) : ")
        if choice.casefold() == 'n':
            break

    for item in ingr:
        options = {'app_id': edamam_id, 'app_key': edamam_key, 'ingr': item}

        print(f'\n{item}')

        req = rq.get(url, options).json()
        calories = round(req['calories'], 2)
        fats = round(req['totalNutrients']['FAT']['quantity'], 2)
        fats_unit = req['totalNutrients']['FAT']['unit']
        fat_cal = round(req['totalNutrientsKCal']['FAT_KCAL']['quantity'], 2)
        fat_cal_units = req['totalNutrientsKCal']['FAT_KCAL']['unit']
        protien = round(req['totalNutrients']['PROCNT']['quantity'], 2)
        protien_units = req['totalNutrients']['PROCNT']['unit']
        protien_cal = round(
            req['totalNutrientsKCal']['PROCNT_KCAL']['quantity'], 2)
        protien_cal_units = req['totalNutrientsKCal']['PROCNT_KCAL']['unit']
        carbs = round(req['totalNutrients']['CHOCDF']['quantity'], 2)
        carb_units = req['totalNutrients']['CHOCDF']['unit']
        carb_cal = round(req['totalNutrientsKCal']['CHOCDF_KCAL']['quantity'],
                         2)
        carb_cal_units = req['totalNutrientsKCal']['CHOCDF_KCAL']['unit']

        print(f'Total Calories:        {calories}kcal')
        print(
            f"Calories from Protien: {protien_cal}{protien_cal_units} from {protien}{protien_units} of Protien."
        )
        print(
            f"Calories from Carbs:   {carb_cal}{carb_cal_units} from {carbs}{carb_units} of Carbs."
        )
        print(
            f"Calories from Fat:     {fat_cal}{fat_cal_units} from {fats}{fats_unit} of Fat.\n"
        )


bmr = bmr_calculation()
dailyCaloriesNeeded = daily_caloric_needs(bmr)
macros_calculation(dailyCaloriesNeeded)
food_calories()
