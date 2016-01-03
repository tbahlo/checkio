class Friends:
    connections = []
    
    def are_equal(self, first_pair, second_pair):
        if (list(first_pair)[0] == list(second_pair)[0] and list(first_pair)[1] == list(second_pair)[1]) \
                or (list(first_pair)[0] == list(second_pair)[1] and list(first_pair)[1] == list(second_pair)[0]):
                return True
        else:
            return False

    def add(self, connection):
        for pair in self.connections:
            if self.are_equal(pair, connection):
                return False
        self.connections.append(connection)
        return True

    def __init__(self, connections):
        for pair in connections:
            self.add(pair)

    def remove(self, connection):
        for pair in self.connections:
            if self.are_equal(pair, connection):
                self.connections.remove(connection)
                return True
        return False

    def names(self):
        connected_names = set()
        for pair in self.connections:
            connected_names.add(list(pair)[0])
            connected_names.add(list(pair)[1])
        return connected_names

    def connected(self, name):
        friends = set()
        for pair in self.connections:
            if(list(pair)[0] == name):
                friends.add(list(pair)[1])
            if(list(pair)[1] == name):
                friends.add(list(pair)[0])
        return friends

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
