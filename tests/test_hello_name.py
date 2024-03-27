from src.hello import say_hello


def test_hello_name():
    input_list = ["Maximillian", "Uwe"]
    want_list = ["Hallo Maximillian", "Hallo Uwe"]

    got_list = say_hello(input_list)
    assert got_list == want_list
