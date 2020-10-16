class Array(object):

    def __init__(self, *elmnts) -> None:
        self._data = elmnts

    def __len__(self) -> int:
        return len(self._data)

    def append(self, elmnt) -> None:
        self._data += (elmnt,)

    def remove(self, key) -> None:
        temp = ()
        for elmnt in self._data:
            if elmnt != key:
                temp += (elmnt,)
        self._data = temp

    def pop(self, index: int) -> None:
        self._data = self._data[:index] + self._data[(index + 1):]

    def __add__(self, other):
        return Array(*(self._data + other.get_data()))

    def index(self, key) -> int:
        for index, char in enumerate(self._data):
            if key == char:
                return index
        return -1

    def __getitem__(self, index):
        return self._data[index]

    def get_data(self):
        return self._data
