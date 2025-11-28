Create a frequency dictionary using a single loop

Input:

nums = [1, 1, 2, 3, 3, 3]


Output:

{1:2, 2:1, 3:3}


But you cannot use if key not in dict directly.
Try .get(key, default).