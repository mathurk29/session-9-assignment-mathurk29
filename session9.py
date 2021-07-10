from datetime import date
import datetime
from collections import namedtuple
from collections import defaultdict
from faker import Faker
from collections import Counter
from time import perf_counter
fake = Faker()

random_profiles = [fake.profile() for _ in range(10_00)]


def calculate_age(birthdate):
    age = date.today() - birthdate  # gives instance of time_detla class
    return age.days


ProfileTtuple = namedtuple('ProfileTtuple', fake.profile().keys())
ProfileTtuple.__doc__ = "A namedTuple with fields generated from keys present in a faker.profile"
ProfileTtuple.current_location.__doc__ = "Gives the x and y co-ordinates of the person's location"
ProfileTtuple.blood_group.__doc__ = "Tells the blood group of the fake person from faker.profile"
ProfileTtuple.birthdate.__doc__ = "Gives the birthdate of the fake person from faker.profile"


def profile_with_tuples(random_profiles: list) -> tuple: 
    ''' A function which processes 10_000 faker profiles (by converting them to tuple for faster access) to print largest blood type, mean-current_location, oldest_person_age, and average age 

        Returns a tuple: 
            -   time taken to access the dictionary.
            -   most common blood type among the dataset
            -   average of the locations of the people
            -   olderst person in the dataset
            -   average age of the people in dataset
    '''
    total_time = 0

    blood_types = list()
    sum_current_location_x = 0
    sum_current_location_y = 0
    oldest_person_age = 0
    sum_age = 0

    for profile in random_profiles:
        temp = ProfileTtuple(**profile)

        # calculate time only for statements accessing tuple
        start = perf_counter()
        blood_types.append(temp.blood_group)
        sum_current_location_x += temp.current_location[0]
        sum_current_location_y += temp.current_location[1]
        birthday = temp.birthdate
        end = perf_counter()
        total_time += end - start

        # calculate required values
        sum_age += calculate_age(birthday)
        oldest_person_age = max(
            oldest_person_age, calculate_age(temp.birthdate))

    mean_current_location_x = sum_current_location_x / len(random_profiles)
    mean_current_location_y = sum_current_location_y / len(random_profiles)
    average_age = (sum_age / len(random_profiles)) // 365
    most_common_blood_type, count_mostcommon_blood_type = Counter(
        blood_types).most_common(1)[0]
    oldest_person_age = oldest_person_age // 365

    result = namedtuple(
        'result', 'time_taken largest_blood_type, mean_current_location, oldest_person_age,  average_age')

    re = result(total_time, most_common_blood_type, (mean_current_location_x,
                mean_current_location_y), oldest_person_age, average_age)

    return re


# 2

def profile_without_tuples(random_profiles: list) -> tuple:
    ''' A function which processes 10_000 faker profiles (in dictionary format) to print largest blood type, mean-current_location, oldest_person_age, and average age 

        Returns a tuple: 
            -   time taken to access the dictionary.
            -   most common blood type among the dataset
            -   average of the locations of the people
            -   olderst person in the dataset
            -   average age of the people in dataset
    '''

    total_time = 0

    blood_types = list()
    sum_current_location_x = 0
    sum_current_location_y = 0
    oldest_person_age = 0
    sum_age = 0

    for profile in random_profiles:

        # calculate time only for statements accessing tuple
        start = perf_counter()
        blood_types.append(profile['blood_group'])
        sum_current_location_x += profile['current_location'][0]
        sum_current_location_y += profile['current_location'][1]
        birthday = profile['birthdate']
        end = perf_counter()

        # calculate required values
        sum_age += calculate_age(birthday)
        oldest_person_age = max(
            oldest_person_age, calculate_age(profile['birthdate']))

        total_time += end - start

    mean_current_location_x = sum_current_location_x / len(random_profiles)
    mean_current_location_y = sum_current_location_y / len(random_profiles)
    average_age = (sum_age / len(random_profiles)) // 365
    most_common_blood_type, count_mostcommon_blood_type = Counter(
        blood_types).most_common(1)[0]

    result = dict(time_taken=total_time, largest_blood_type=most_common_blood_type, mean_current_location=(
        mean_current_location_x, mean_current_location_y), oldest_person_age=oldest_person_age, aveage_age=average_age)

    return result


#3

