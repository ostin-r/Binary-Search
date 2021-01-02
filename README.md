# Binary-Search
Trying out my first search algorithm.

I've done some reading on the binary search algorithm to discover how similar it is to different numerical methods that I learned in engineering school.  Instead of using mathematical functions, these sorting algorithms are concerned with more general forms of information such as strings.

My plan for this project is to:
- learn what I can about the binary search algorithm
- implement a binary search function for ordered lists
- compare my solution to solutions offered by professionals on the interwebs

So far I have learned about "time complexity" which is a comparison of rates of input & computations required by the algorithm.  This is represented by an "O" followed by the n-complexity relationship.  A linear relationship between input and time complexity is O(n).  In addition, it seems natural that sorting algorithms would be the next thing that I should study.  Maybe I'll add a solution for one of those to this project.

Update 12/30/20:

I've finished the algorithm and I got my function working with sorted lists.  Unsurprisingly, my solution is complicated compared to professional solutions... (https://www.geeksforgeeks.org/python-program-for-binary-search/)  The main difference is that my code slices the array, whereas the solution simply changes the index.  This is where I added a lot of complexity.  In order to deal with slicing the array, I had to add another array that was sliced in the same place that preserved the location data.  Slicing the data that I am searching proved to be problematic.  I plan on reading through the professional solution and trying to implement it myself (whithout checking it too much).

1/2/21 project notes:

I successfully implemented my own binary search without looking at any online solutions.  Being a beginner programmer, the 40 or so lines of code that make up the function were pretty difficult for me to implement.  Comparing my function to the geekstogeeks solution, there were a few differences.  The major difference I noticed is that their solution is simpler in that it changes the search index rather than 'slicing' the array as I did in search_numb.  My only gripe with this solution is that it contains a seemingly passive way of breaking the loop if the searched value is not present in the array.  This feature wasn't clear until I ran through an actual scenario on paper.

Overall, I really enjoyed this project.  I am calling this project 'finished' but I may continue to add a few more features or functions to it: a sorting algorithm, a binary search for strings, etc.
