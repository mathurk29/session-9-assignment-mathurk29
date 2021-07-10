import session9
from  session9 import random_profiles
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