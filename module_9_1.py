def test_list(int_list):
    for i in int_list:
        if not isinstance(i, int or float):
            return False
    return True


def apply_all_func(int_list, *functions):
    if test_list(int_list):
        results={}
        for function in functions:
            results[function.__name__] = function(int_list)
        return results
    else:
        return 'Список должен состоять из чисел!'

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, '15', 9], min, sum, max))

