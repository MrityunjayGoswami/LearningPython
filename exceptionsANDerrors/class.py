class ValueTooHighError(Exception):
    pass
class ValueTooSmallerError(Exception):
    def __int__(self, message, value):
        self.value = message
        self.value = value

def test_values(x):
    if x >100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallerError('value is too small')

try:
    test_values(101)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallerError as e:
    print(e)
else:
    print('everything looks fine')
finally:
    print('it will run always')