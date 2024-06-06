def join_char(*args):
    word = ""
    for i in args:
        word += i
    return word

t_word = ("a", "b", "c")

print(*t_word)
# buf = *t_word
# print(type(*t_word))
print(join_char(*t_word))
# https://qiita.com/wwacky/items/02d99948e86541d1d84a
# import unzip
# print(unzip())

# print(join_char(+t_word))
# print(join_char(**t_word))
# print(join_char(t_word))