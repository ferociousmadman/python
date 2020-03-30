from itertools import product

# ----------------------------------------------------------------
# Author: Skipper Davies with credit to
# https://www.geeksforgeeks.org/python-itertools-product/ for
# portions of the original code.
#
# Date: 3-29-20
#
# This program finds the cartesian product of however many sets
# are stored in variables that are passed as arguments to the
# function cartesian_product(). The if statement afterwards sets
# the variables to whatever is in each set, and then calls the
# function and displays the result. The number of tuples in any
# cartesian product are then displayed, followed by how many
# relations are in the cartesian product. The variables x and y
# assist with those calculations. Unfortunately, for the program
# to work properly, this program has to be manually re-written to
# include only the number of variables and arguments for each set
# required. For example: if you want to find the cartesian product
# of two sets, then only two arguments should be passed to the
# function, and only two variables A & B should be set. If you want
# to find the cartesian product of three sets, then three arguments
# should be passed to the function, and three variables A & B, & C
# should be set, etc. Right now this is a manual process.
# ----------------------------------------------------------------


def cartesian_product(A, B):

    # return the list of all the computed tuple
    # using the product() method
    return list(product(A, B))

# Driver Function:


if __name__ == "__main__":
    A = 5, 7, 11
    B = "a", "b", "c"
    print('The cartesian product is: ', cartesian_product(A, B))
    x = len(cartesian_product(A, B))
    print('This many tuples are in the cartesian product: ', x)
    y = 2**x
    print('This many relations are in the cartesian product:', y, 'or 2 to the', str(x) + 'th power')


