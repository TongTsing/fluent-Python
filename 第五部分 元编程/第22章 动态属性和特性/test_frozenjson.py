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

    assert frozen.class_ == 'Math'

    print("All tests passed.")

if __name__ == "__main__":
    test_frozen_json()