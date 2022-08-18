import run
from io import StringIO
from unittest.mock import patch

def test_is_prime():
    numbers = {2:True,3:True,4:False,5:True,6:False,7:True,8:False,9:False,10:False,11:True}
    for number in numbers.keys():
        isPrime = numbers[number]
        assert run.is_prime(number) == isPrime

def test_get_multiplys_until_they_are_all_prime():
    for x in range(4,1000):
        multipliers = run.get_multiplys_until_they_are_all_prime([x])

def test_simplify():
    assert run.simplify(98) == 9.899494936611665
    assert round(run.simplify(502),5) == 22.40536
    assert round(run.simplify(54),5) == 7.34847
    assert round(run.simplify(752),5) == 27.42262
    assert round(run.simplify(259),5) == 16.09348
    with patch('sys.stdout', new = StringIO()) as fake_out:
        run.simplify(97) #Is prime
        assert fake_out.getvalue() == "√ 97\nNumber is prime, can't be simplified\n" 


def test_main():
    with patch('sys.stdout', new = StringIO()) as fake_out:
        run.main()
        assert fake_out.getvalue() == "Please specifiy a number to simplify\n" 
