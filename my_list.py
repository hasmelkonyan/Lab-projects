class MyList(list):
    def __init__(self, iterable=None):
        if iterable is None:
            super().__init__()
        else:
            super().__init__([i for i in iterable if isinstance(i, (int, tuple, str))])

    def __copy__(self):
        """copy and move"""
        other = MyList()
        for each in self:
            other.append(each)
        return other

    def __add__(self, other):
        """addition"""
        if not isinstance(other, MyList):
            raise TypeError
        res = []
        for i in range(len(self)):
            res.append(self[i])
        for i in range(len(other)):
            res.append(other[i])
        return res

    def __iadd__(self, other):
        """addition with assignment"""
        if not isinstance(other, MyList):
            raise TypeError
        for i in range(len(other)):
            self.append(other[i])
        return self

    def __eq__(self, other):
        """is equal to"""
        if not isinstance(other, MyList):
            raise TypeError
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __neg__(self, other):
        """not equal to"""
        if not isinstance(other, MyList):
            raise TypeError
        if len(self) != len(other):
            return True
        for i in range(len(self)):
            if self[i] != other[i]:
                return True
        return False

    def __it__(self, other):
        """less than"""
        if not isinstance(other, MyList):
            raise TypeError
        for i in range(len(self)):
            if self[i] == other[i] and self[i] is not self[-1]:
                continue
            elif self[i] < other[i]:
                return True
            else:
                return False

    def __le__(self, other):
        """less or equal"""
        if not isinstance(other, MyList):
            raise TypeError
        for i in range(len(self)):
            if self[i] != other[i] and self[i] > other[i]:
                return False
        return True

    def __gt__(self, other):
        """greater than"""
        if not isinstance(other, MyList):
            raise TypeError
        for i in range(len(self)):
            if self[i] == other[i] and self[i] is not self[-1]:
                continue
            elif self[i] > other[i]:
                return True
            else:
                return False

    def __ge__(self, other):
        """greater or equal"""
        if not isinstance(other, MyList):
            raise TypeError
        for i in range(len(self)):
            if self[i] != other[i] and self[i] < other[i]:
                return False
        return True

    def merge(self, arr):
        return self.extend(arr)

    def front(self):
        return self[0]

    def reverse(self):
        return self[::-1]

    def empty(self):
        return list()

    def remove(self, val):
        ind = self.index(val)
        return self[0:ind] + self[ind + 1:]

    def remove_if(self, func):
        return [i for i in self if func(i)]

    def my_sort(self):
        return self.sort()

    def erase(self, erasable):
        def is_sublist(lst):
            for i in range(len(self)):
                if self[i: i + len(lst)] == lst:
                    return True
            return False

        if not is_sublist(erasable):
            return
        for i in range(len(self)):
            if self[i: i + len(erasable)] == erasable:
                return self[: i] + self[i + len(erasable):]

    def insert(self, index, val):
        if index > len(self):
            return
        return self[: index] + [val] + self[index:]

    def push_front(self, val):
        return [val] + self

    def pop_front(self):
        return self[1:]

    def clear(self):
        return []

    def emplace(self, pos, *args):
        return self[:pos] + [each for each in args] + self[pos:]


l = MyList([1, 2, 3])
l = l.emplace(2, 100, 200, 300)
print(l)

