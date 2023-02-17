"""
Challenge 4: List of Products of all Elements
Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

We'll cover the following

Problem Statement
Input:
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:
A list of numbers (could be floating points or integers)

Output:
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input
arr = [1,2,3,4]
Sample Output
arr = [24,12,8,6]

"""

begin
    function find_product(array_list :: Array{T,N}) where {T, N}

        """
        In this example, the myfunction function takes an array arr of type Array{T, N},
        where T is any type and N is any number of dimensions. The where clause is used
        to specify the type and number of dimensions of the array.
        """

        new_array_list = []
        iteration = 2
        for value in eachindex(array_list)
            println(array_list[iteration:end])
            
        end

        return 1
    end

    @assert([24, 12, 8, 6] == find_product([1, 2, 3, 4]))
end
