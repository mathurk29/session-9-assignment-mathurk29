import pytest
import session9
from  session9 import market_close, random_profiles, wrapper_3
from session9 import Stock_with_weight
import inspect


def test_is_using_tuples():
    assert 'namedtuple' in inspect.getsource(
        session9.profile_with_tuples), 'You have not used namedtuples!'


def test_tuples_doc_check():
    assert session9.ProfileTtuple.__doc__ is not '', 'Please define proper docstring for namedtuple fields.'
    assert session9.ProfileTtuple.current_location.__doc__ is not '', 'Please define proper docstring for namedtuple fields.'
    assert session9.ProfileTtuple.blood_group.__doc__ is not '', 'Please define proper docstring for namedtuple fields.'
    assert session9.ProfileTtuple.birthdate.__doc__ is not '', 'Please define proper docstring for namedtuple fields.'
    assert session9.profile_with_tuples.__doc__ is not '', 'Please define proper docstring for namedtuple fields.'


def test_who_is_faster():
    assert session9.profile_with_tuples(random_profiles).time_taken < session9.profile_without_tuples(random_profiles)[
        'time_taken'], 'Oops! Your tuples got mutilated by the "Dict"ator'


def test_check_annotations():
    assert session9.profile_with_tuples.__annotations__ , 'Annotations not provided'
    assert session9.profile_without_tuples.__annotations__ , 'Annotations not provided'

def test_init3():


    bse1000 = session9.init_3()
    for company in bse1000:
        assert isinstance(company.name,str), 'Error in generating stock values of the comapny' 
        assert isinstance(company.symbol,str) , 'Error in generating stock values of the comapny'
        assert isinstance(company.open, float) or isinstance(company.open,int), 'Error in generating stock values of the comapny'
        assert isinstance(company.high, float) or isinstance(company.high,int), 'Error in generating stock values of the comapny'
        assert isinstance(company.close,float) or isinstance(company.close,int) , 'Error in generating stock values of the comapny'

def test_market_close():
    from faker import Faker
    fake = Faker()
    name1 = fake.company()
    name2= fake.company()
    company1 = session9.Stock_with_weight(name1,name1[0:3],1000,1500,1250,1000/(1000+800))
    company2 = session9.Stock_with_weight(name2,name2[0:3],800,1200,1100,800/(1000+800))
    assert round(market_close(1800,[company1,company2])) == 272, 'What?'


def test_2_market_close():
    from faker import Faker
    fake = Faker()
    name1 = fake.company()
    company1 = session9.Stock_with_weight(name1,name1[0:3],1000,1500,1800,1000/(1000+800))
    with pytest.raises(ValueError, match=r'High lesser than close'):
        market_close(1800,[company1])


def test_sanity_wrapper():
    for _ in range(3):
        wrapper_3()