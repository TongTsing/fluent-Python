from FrozenJson_new import FrozenJSON

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
    # import os
    # print(os.getcwd())
    # with open('第五部分 元编程/第22章 动态属性和特性/osconfeed.json', 'r', encoding='utf-8') as f:
    #     import json
    #     data = json.load(f)

    frozen = FrozenJSON(data)

    print(getattr(frozen, 'class'))


if __name__ == "__main__":
    test_frozen_json()