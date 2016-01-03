def flatten(dictionary):
    print("started with param:\n", dictionary)
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            print("current k,v pair:", k, " || ", v)
            if isinstance(v, dict):
                if v=={}:
                    print("value is empty dict: ",v)
                    result["/".join((path + (k,)))] = "" # added this case myself
                else:
                    print("value is non empty dict: ", v)
                    stack.append((path + (k,), v))
            else:
                print("value is not a dict: ", v)
                result["/".join((path + (k,)))] = v
    print("finished! return value is:\n", result,"\n\n")
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}