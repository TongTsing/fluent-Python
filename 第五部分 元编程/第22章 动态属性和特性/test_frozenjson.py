from FrozenJson import FrozenJSON

def test_frozen_json():
    data = {
        'class': 'Math',
        'name': 'Alice',
        'age': 30,
        'address': {
            'city': 'Wonderland',
            'zip': '12345'
        },
        'hobbies': ['reading', 'chess', 'hiking']
    }

    frozen = FrozenJSON(data)

    assert frozen.name == 'Alice'
    assert frozen.age == 30
    assert frozen.address.city == 'Wonderland'
    assert frozen.address.zip == '12345'
    assert frozen.hobbies[0] == 'reading'
    assert frozen.hobbies[1] == 'chess'
    assert frozen.hobbies[2] == 'hiking'

    print("All tests passed.")

if __name__ == "__main__":
    test_frozen_json()