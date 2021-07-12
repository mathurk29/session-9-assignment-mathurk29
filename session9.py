from datetime import date
import datetime
from collections import namedtuple
from collections import defaultdict
from faker import Faker
from collections import Counter
from time import perf_counter
import random
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

# namedtuple to describes a single company in stock market
Stock = namedtuple('Stock','name symbol open high close')
Stock_with_weight = namedtuple('Stock_with_weight', Stock._fields + ('weight',))

def init_3() -> tuple :
    ''' Returns a list of 1000 random companies and it\'s stock details for one day. '''


    #initializing stock market with 1000 companies
    stock_market = list()
    for _ in range(10_000):
        name = fake.company()
        symbol = name[0:5]
        open = random.randint(10_000,11_000)
        high = open* random.uniform(1,1.5)
        close = random.uniform(open*0.8,high)
        stock_market.append(Stock(name,symbol,open,high,close))
    return stock_market


def extend_weight(stock_market:list) -> tuple:
    ''' Extends Stock namedtuple with relative weight.\n
        Returns sum total of open and the extended stock martket
    '''

    # Adding weights to comapnies of the stock_market. Let's call our market as BSE
    sum_open = sum([company.open for company in stock_market ])
    bse = list()
    for company in stock_market:
        weight = company.open/sum_open
        temp = Stock_with_weight(*company,weight)
        print(temp)
        bse.append(temp)

    return sum_open, bse
    
    
def market_close(sum_open: int,bse: list) -> float:

    ''' 
        Calculate the no. of points by which market closes based on individual stocks.
    '''

    #Validations
    for company in bse:
        if company.close > company.high:
            raise ValueError('High lesser than close')


    delta = 0.0
    for company in bse:
        change = company.close - company.open
        delta += change * company.weight


    if delta > 0:
        print(f'Market opened at {sum_open} and went up by whopping {delta} points. 21 din me paisa double - a scheme for rich by Laxmi Chit fund!!!! ')
    else:
        print(f'Market opened at {sum_open} and fell down by whopping {abs(delta)} points. Golmaal hai bhai sab golmaal hai!!!!')

    return delta


def wrapper_3():
    stock_market = init_3()
    sum_open, bse = extend_weight(stock_market)
    _ = market_close(sum_open,bse)