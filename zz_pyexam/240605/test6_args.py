def attach_custom_dict(**kwargs):
    default_dict = {
        'address': 'tokyo',
    }

    for key, value in kwargs.items():
        default_dict[key] = value
    
    return default_dict

user = { 'name': 'taro', 'age': 20 }

def test1():
    print(attach_custom_dict(**user))
    # print(attach_custom_dict(user))
    # print(attach_custom_dict(*user))
    # print(attach_custom_dict(+user))

def test2():
    def age_check(age, skip, /):
        if skip:
            return True

        if age < 20:
            raise ValueError('未成年です')
    # TypeError: test2.<locals>.age_check() got some positional-only arguments passed as keyword arguments: 'skip'
    # print(age_check(19, skip=False))
    # print(age_check(age=20, True))
    print(age_check(20, True))

"""
https://www.self-study-blog.com/dokugaku/python-function-args-parameter-option/
「/」の前が位置専用
「/」と「*」の間が位置またはキーワード
「*」の後ろがキーワード専用
"""


if __name__ == '__main__':
    test2()