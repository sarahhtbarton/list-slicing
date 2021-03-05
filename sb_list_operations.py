"""Utilities for manipulating lists."""


def head(input_list):
    """Return the first item of the input list."""
    first_item = input_list[0]
    return first_item
head(['Jan', 'Feb', 'Mar'])


def tail(input_list):
    """Return a new list of all items, excluding the first item."""
    tail_list = input_list[1:]
    return tail_list
tail(['Jan', 'Feb', 'Mar'])


def last(input_list):
    """Return the last item of the input list."""
    last_item = input_list[-1]
    return last_item
last(['Jan', 'Feb', 'Mar'])


def top(input_list):
    """Return all elements of the input list except the last."""
    top_list = input_list[:-1]
    return top_list
top(['Jan', 'Feb', 'Mar'])


def first_three(input_list):
    """Return the first three elements of the input list."""
    first_three_list = input_list[:3]
    return first_three_list
first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])


def last_five(input_list):
    """Return the last five elements of the input list. """
    last_five_list = input_list[-5:]
    return last_five_list
last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def middle(input_list):
    """Return all elements of input_list except the first two and the last two."""
    middle_list = input_list[2:-2]
    return middle_list
middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of input_list."""
    inner_four_list = input_list[2:6]
    return inner_four_list
inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def inner_four_end(input_list):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list. """
    inner_four_end_list = input_list[-6:-2]
    return inner_four_end_list
inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing."""
    input_list[0] == 42
    #return input_list
replace_head([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def replace_third_and_last(input_list):
    """Replace third and last elements of input_list with 37 and return nothing."""
    input_list[2] == 37
    input_list[-1] == 37
    #return input_list
replace_third_and_last([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def replace_middle(input_list):
    """Replace all elements of a list but the first two and last two with 42 and 37."""
    input_list[2:-2] == [42, 37]
    #return input_list
replace_middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])


def delete_third_and_seventh(input_list):
    """Remove third and seventh elements of input_list and return nothing."""

    input_list[2] == []
    input_list[5] == []
    # can i do these both at the same time???
    #return input_list
delete_third_and_seventh(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
# should return ['Do', 'Re', 'Fa', 'So', 'La', 'Do']


def delete_middle(input_list):
    """Remove all elements from input_list except the first two and last two."""
    input_list[2:-2] == 0
    #return input_list
delete_middle(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
# should return['Do', 'Re', 'Ti', 'Do']