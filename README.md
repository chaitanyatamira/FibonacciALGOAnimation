# FibonacciALGOAnimation
This is an step by step animation of Fibonacci Search Algorithm  using the Tkinter and Turtle graphics 
libraries in Python.The purpose of the project is to demonstrate the Fibonacci search algorithm, a search 
technique based on the Fibonacci sequence, through an animated representation. The user can input an array size, 
elements for the array, and a target element to be searched.

Here is the working of the Animation with an Example:
Size of the input array is 10. The smallest Fibonacci number greater than 10 is 13.Therefore, Fib = 13, Fib_m1 = 8, Fib_m2 = 5.We initialize offset = -1
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/bc5dddc3-e62d-4f97-987f-6ae6615cf1f2)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/54305716-d5f4-407e-a396-5bcb25bf9807)

In the first iteration, compare it with the element at index = minimum (offset + Fib_m2, n – 1) = minimum (-1 + 5, 9) = minimum (4, 9) = 4.
The fourth element in the array is 20, which is not a match and is less than the key element.
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/d5d3062c-8fd0-44ab-afe1-ccc1c60e62a4)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/f87c00ab-3d44-45c6-ba23-f1fa7d473dc8)
In the second iteration, update the offset value and the Fibonacci numbers.Since the key is greater, the offset value will become 
the index of the element, i.e. 4. Fibonacci numbers are updated as Fib= Fib_m1 = 8,Fib_m1 = 5, Fib_m2 = 3.
Now, compare it with the element at index = minimum (offset + Fib_m2, n – 1) = minimum (4 + 3, 9) = minimum (7, 9) = 7.
Element at the 7th index of the array is 43, which is not a match and is also lesser than the key.
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/46e62029-7319-4183-9fe6-42f044c9a508)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/2c5a7dd5-cd61-4b43-92cb-e5215c0dcd41)
We discard the elements after the 7th index, so n = 7 and offset value remains 4.
Fibonacci numbers are pushed two steps backward, i.e. Fib = Fib_m1 = 3.
Fib_m1= 2, Fib_m2= 1.
Now, compare it with the element at index = minimum (offset + Fib_m2, n – 1) = minimum (4 + 1, 6) = minimum (5, 7) = 5.
The element at index 5 in the array is 24, which is our key element. 5th index is returned as the output for this example array.
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/eae2ffe3-dc10-4f6c-a8f7-2994ba81ce1e)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/e750a7af-dee7-44c4-880b-001b29191672)


