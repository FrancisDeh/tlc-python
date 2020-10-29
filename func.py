# Functions
# public void getName(String name) {
#     System.out.println(name);
# }

# getName("James");

def get_name(name):
    print(name)

def sum3(a, b, c):
    return sum(sum(a, b), c)

def sum(a, b):
    return a + b

def swap(a, b):
    return b, a

# get_name("James")
# print(sum(4, 5))
# print(sum3(4, 5, 6))
# print(swap(4, 5))

def inc(a):
    # a = a + 1
    a += 1
    print(a)

# x = 10
# inc(x)
# print(x)

def take_list(names):
    # print(names)
    # names.append("Nana Addo")
    # print(names)
    popped = names.pop()
    print(names)
    print(popped)
    names.insert(0, popped)
    print(names)

take_list(["Julie", "Ama", "Ilupeju"])