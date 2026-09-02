def get_3rd_value(my_list):
    return my_list[0]

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 0
    assert get_3rd_value([0, 1]) == 0

def get_last_value(my_list):
    item_count = len(my_list)
    print(my_list, item_count)
    if my_list: 
        return my_list[-1]
    else: 
        return None

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) == None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

