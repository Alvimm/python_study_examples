print('BMI module imported')


def calculate_bmi(weight, height):
    print(f'Weight: {weight}')
    print(f'Height: {height}')
    bmi = float(weight) / float(height) ** 2
    return bmi


def bmi_rating(index):
    if index < 18.5:
        return 'Low weight'
    elif index < 25:
        return 'Suitable weight'
    elif index < 30:
        return 'Overweight'
    else:
        return 'Obese'
