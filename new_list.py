class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "The object Node"

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        if self.data < other.data:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.data <= other.data

    def __gt__(self, other):
        """greater than"""
        if not isinstance(other, Node):
            raise TypeError
        return self.data > other.data

    def __ge__(self, other):
        """greater or equal"""
        if not isinstance(other, Node):
            raise TypeError
        return not self < other


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        return "object MyLinkedList"

    def __str__(self):
        if self.head is None:
            res = '<>'
            return res
        res = '<'
        res += str(self.head.data)
        cur = self.head.next
        while cur is not None:
            res += ", " + str(cur.data)
            cur = cur.next
        res += '>'
        return res

    def __len__(self):
        if not self.head:
            return 0
        return self.length

    def append(self, val):
        """Adding a new element to the list"""
        if not isinstance(val, Node):
            raise TypeError
        if self.head is None:
            self.head = val
            self.length += 1
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = val
        self.length += 1

    def __copy__(self):
        new_ll = MyLinkedList
        if self.head is None:
            new_ll.head = None
            return
        cur = self.head
        new_ll.head = cur
        while cur.next is not None:
            new_ll.append(cur.next, )
            cur = cur.next
        return new_ll

    def __eq__(self, other):
        """is equal to"""
        if not isinstance(other, MyLinkedList):
            raise TypeError
        if self.head is None and other.head is None:
            return True
        cur1, cur2 = self.head, other.head
        while cur1 is not None or cur2 is not None:
            if cur1.data != cur2.data:
                return False
            cur1, cur2 = cur1.next, cur2.next
            if cur1 is None and cur2 is not None or cur1 is not None and cur2 is None:
                return False
        return True

    def __neg__(self, other):
        """is not equal to"""
        return not self == other

    def __iadd__(self, other):
        if not isinstance(other, MyLinkedList):
            raise TypeError
        if self.head is None and other.head is None:
            return self
        if self.head is None and other.head is not None:
            self.head = other.head
            cur1 = self.head
            cur2 = other.head.next
            while cur2 is not None:
                cur1.next = cur2
                cur2 = cur2.next
            return self
        if self.head is not None and other.head is None:
            return self
        if self.head is not None and other.head is not None:
            cur1 = self.head
            while cur1.next is not None:
                cur1 = cur1.next
            cur2 = other.head
            cur1.next = cur2
            while cur2.next is not None:
                cur1.next = cur2
                cur1 = cur1.next
                cur2 = cur2.next
        return self

    def __add__(self, other):
        """addition with assignment"""
        if not isinstance(other, MyLinkedList):
            raise TypeError
        ll = MyLinkedList()
        if self.head is None and other.head is None:
            return ll
        if self.head is None and other.head is not None:
            ll = other
            return ll
        if self.head is not None and other.head is None:
            ll = self
            return ll
        if self.head is not None and other.head is not None:
            ll.head = self.head
            cur = ll.head
            cur1 = self.head.next
            while cur1 is not None:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            cur2 = other.head
            while cur2 is not None:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        return ll

    def __lt__(self, other):
        """less than"""
        if not isinstance(other, MyLinkedList):
            raise TypeError
        if (self.head is None and other.head is None or
                self.head is not None and other.head is None):
            return False
        if self.head is None and other.head is not None:
            return True
        cur1, cur2 = self.head, other.head
        while cur1 is not None and cur2 is not None:
            if cur1 < cur2:
                return True
            elif cur1 > cur2:
                return False
            cur1, cur2 = cur1.next, cur2.next
        return False

    def __le__(self, other):
        """less or equal"""
        if self < other or self == other:
            return True
        return False

    def __gt__(self, other):
        """greater than"""
        return not self <= other

    def __ge__(self, other):
        """greater or equal"""
        if not isinstance(other, MyLinkedList):
            raise TypeError
        return not self < other

    def merge(self, other):
        """merges two linked lists"""
        if not isinstance(other, MyLinkedList):
            raise TypeError
        return self + other

    def front(self):
        """returns the first node of a linked list"""
        if self.head is None:
            return None
        return self.head

    def pop(self):
        """deletes the last value"""
        if self.head is None:
            return
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        copy_cur = cur.next
        cur.next = None
        return copy_cur

    def reverse(self):
        """returns a reversed linked list"""
        if self.length <= 1:
            return self
        reversed_ll = MyLinkedList()
        reversed_ll.head = self.pop()
        cur = reversed_ll.head
        while self.head.next is not None:
            cur.next = self.pop()
            cur = cur.next
        cur.next = self.head
        return reversed_ll

    def empty(self):
        """clears the list"""
        if self.head is None:
            return self
        while self.head.next is not None:
            self.pop()
        self.head = None
        return self

    def is_in(self, val):
        """indicates whether the specified value exists in the linked list"""
        if not isinstance(val, Node):
            raise TypeError
        if self.head is None:
            return False
        if self.length == 1:
            return val.data == self.head.data
        cur = self.head
        while cur is not None:
            if cur.data == val.data:
                return True
            cur = cur.next
        return False

    def remove(self, val):
        """Removes existing value from the linked list"""
        if not isinstance(val, Node):
            raise TypeError
        if self.length == 0:
            raise ValueError("The value is not in the linked list")
        if not self.is_in(val):
            raise ValueError("The value is not in the linked list")
        if self.length == 1:
            self.head = None
            return self
        if self.head == val:
            self.head = self.head.next
            return self
        cur = self.head
        while cur.next is not None:
            if cur.next == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self

    def remove_if(self, func):
        """removes all elements from the linked list that satisfy the function conditions"""
        if self.head is None:
            return
        while func(self.head) and self.head.next is not None:
            self.head = self.head.next
        if self.head.next is None:
            if func(self.head):
                self.head = None
            return self
        if self.head is not None:
            cur = self.head
            while cur.next is not None:
                if func(cur.next):
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            if cur.next is not None:
                if func(cur.next):
                    cur.next = None
        return self

    def sort(self):
        """sorted the linked list"""
        if self.head is None or self.head.next is None:
            return self
        lst = []
        while self.head is not None:
            min_el = self.get_min()
            lst.append(min_el)
            self.remove(min_el)
        self.head = lst[0]
        cur = self.head
        for each in lst[1:]:
            cur.next = each
            cur = cur.next
        return self

    def push_front(self, val):
        """Adding a new element to the beginning of the list"""
        if not isinstance(val, Node):
            raise TypeError
        if self.head is None:
            self.head = val
            self.length += 1
            return
        self.head, self.head.next = val, self.head
        self.length += 1
        return self

    def get_min(self):
        """returns the smallest element in a linked list"""
        if self.head is None:
            return
        if self.head.next is None:
            return self.head
        cur = self.head
        min_el = cur
        while cur.next is not None:
            cur = cur.next
            if cur.data < min_el.data:
                min_el = cur
        return min_el

    def insert(self, val, ind):
        """adds the specified value at the specified index in the linked list"""
        if not isinstance(val, Node):
            raise TypeError
        if ind < 0:
            return
        if self.head is None and ind == 0:
            self.head = val
        elif self.head is None and ind > 0:
            return
        elif self.head is not None and ind == 0:
            self.push_front(val)
            return self
        if self.length == ind:
            self.append(val)
            return self
        cur_ind = 1
        cur = self.head
        while cur.next is not None:
            if cur_ind == ind:
                tmp = cur.next
                cur.next = val
                cur.next.next = tmp
            cur = cur.next
            cur_ind += 1
        return self

    def pop_front(self):
        """removes the first element of the linked list and returns it"""
        if self.head is None:
            return
        if self.length == 1:
            self.head = None
        removed = self.head
        self.head = self.head.next
        return removed

    def clear(self):
        """Clears the linked list"""
        if self.head is None:
            return self
        while self.head.next is not None:
            self.pop()
        self.head = None

    def emplace(self, pos, *args):
        """adds one or more values at the specified index in the linked list"""
        for each in args:
            if not isinstance(each, Node):
                raise TypeError
        if pos == 0:
            for each in args[::-1]:
                self.push_front(each)
        cur_pos = 1
        cur = self.head
        while cur.next is not None:
            if cur_pos == pos:
                for each in args[::-1]:
                    self.insert(each, cur_pos)
            cur = cur.next
            cur_pos += 1
        return self

    def erase(self, *args):
        for each in args:
            if not isinstance(each, Node):
                raise TypeError
        for each in args:
            if self.is_in(each):
                self.remove(each)
        return self


# Testing
nd1 = Node(1)
nd2 = Node(2)
nd3 = Node(1)
nd4 = Node(3)
ll1 = MyLinkedList()
ll2 = MyLinkedList()
ll1.append(nd1)
ll1.append(nd2)
ll2.append(nd3)
ll2.append(nd4)
nd5 = Node(10)
ll3 = MyLinkedList()
ll3.append(nd5)
nd6 = Node(1)
nd7 = Node(2)
nd8 = Node(11)
nd9 = Node(6)
ll4 = MyLinkedList()
ll4.append(nd6)
ll4.append(nd7)
ll4.append(nd8)
ll4.append(nd9)
print("ll1")
print(ll1)
print("ll2")
print(ll2)
print("ll3")
print(ll3)
print("ll4")
print(ll4)
print("***********************")


# Copy operator assignment =
def copy_test():
    ll = ll2
    print(ll)


def print_test():
    print(ll1)


# Operator is equal to ==
def is_equal_test():
    print(ll1 == ll2)


# Operator not equal to !=
def is_not_equal_test():
    print(ll1 != ll2)


# Operator +
def plus_test():
    ll = ll1 + ll2
    print(ll)


# operator +=
def plus_eq_test():
    nd = Node(8)
    ll = MyLinkedList()
    ll.append(nd)
    ll += ll1
    print(ll)


# Operator <=
def less_or_equal_test():
    print(ll1 <= ll2)
    print(ll3 <= ll1)


# operator <
def less_than_test():
    print(ll1 < ll2)
    print(ll3 < ll1)


# operator >
def more_than_test():
    print(ll2 > ll1)
    print(ll2 > ll3)


# operator >=
def more_or_equal_test():
    print(ll2 > ll1)
    print(ll2 > ll3)
    print(ll1 >= ll4)


def merge_test():
    ll1.merge(ll2)
    print(ll1)


def front_test():
    print(ll1.front().data)
    print(ll3.front().data)


def reverse_test():
    print(ll1.reverse())
    print("-----")
    print(ll4.reverse())


def empty_test():
    print(ll2.empty())


def remove_test():
    print(ll4.remove(nd8))


def remove_if_test():
    def is_even(n):
        if not isinstance(n, Node):
            raise TypeError
        return n.data % 2 == 0

    print(ll4.remove_if(is_even))


def sort_test():
    print(ll4.sort())


def insert_test():
    nd = Node(120)
    print(ll4.insert(nd, 3))


def push_front_test():
    nd = Node("front")
    print(ll4.push_front(nd))


def pop_front_test():
    print(ll4.pop_front().data)
    print("------")
    print(ll4)


def clear_test():
    print(ll1.clear())


def emplace_test():
    nd = Node("New")
    ndd = Node("Mew")
    print(ll1.emplace(1, nd, ndd))


def erase_test():
    print(ll4.erase(nd7, nd9))
