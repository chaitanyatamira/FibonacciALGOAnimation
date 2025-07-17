# Fibonacci Search Algorithm Animation

A step-by-step visual demonstration of the Fibonacci Search Algorithm implemented in Python using Tkinter GUI framework. This educational tool provides an interactive animation that helps users understand how the Fibonacci search algorithm works through visual representation.

## 🎯 Overview

The Fibonacci Search Algorithm is an efficient searching technique that uses Fibonacci numbers to divide the search space. This project demonstrates the algorithm through an animated interface where users can:

- Input a custom array of integers
- Specify a target element to search for
- Watch the step-by-step execution with visual highlights
- View real-time algorithm state information (Fibonacci values, offset, current index)

## 🚀 Features

- **Interactive GUI**: Easy-to-use interface built with Tkinter
- **Real-time Animation**: Visual representation of each search step
- **Algorithm Visualization**: Display of Fibonacci values, offset, and current search index
- **Educational Tool**: Perfect for learning and teaching search algorithms
- **Customizable Input**: Support for user-defined arrays and target values

## 📋 Requirements

- Python 3.x
- Tkinter (usually included with Python)

## 🔧 Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/chaitanyatamira/FibonacciALGOAnimation.git
   cd FibonacciALGOAnimation
   ```

2. Run the application:

   ```bash
   python cbp.py
   ```

3. Using the application:
   - Enter array elements separated by commas (e.g., `1,5,8,12,20,24,30,43,50,65`)
   - Enter the target element to search for
   - Click "Start Animation" to begin the visualization

## 📚 Algorithm Explanation

The Fibonacci Search Algorithm works by:

1. Finding the smallest Fibonacci number greater than or equal to the array length
2. Using Fibonacci numbers to divide the array into unequal parts
3. Comparing the target with elements at calculated positions
4. Eliminating portions of the array based on comparisons
5. Continuing until the element is found or the search space is exhausted

### Example Walkthrough

Consider an array of size 10: `[1, 5, 8, 12, 20, 24, 30, 43, 50, 65]` and target element `24`.

**Initial Setup:**

- Array size: 10
- Smallest Fibonacci number ≥ 10: 13
- Initial values: Fib = 13, Fib_m1 = 8, Fib_m2 = 5
- Offset = -1

**Step 1:** First Iteration

- Calculate index: min(offset + Fib_m2, n-1) = min(-1 + 5, 9) = min(4, 9) = 4
- Compare array[4] = 20 with target 24
- Since 20 < 24, move to the right portion

![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/bc5dddc3-e62d-4f97-987f-6ae6615cf1f2)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/54305716-d5f4-407e-a396-5bcb25bf9807)

**Step 2:** Second Iteration

- Update offset = 4 (previous index)
- Update Fibonacci values: Fib = 8, Fib_m1 = 5, Fib_m2 = 3
- Calculate index: min(4 + 3, 9) = min(7, 9) = 7
- Compare array[7] = 43 with target 24
- Since 43 > 24, move to the left portion

![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/d5d3062c-8fd0-44ab-afe1-ccc1c60e62a4)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/f87c00ab-3d44-45c6-ba23-f1fa7d473dc8)

**Step 3:** Third Iteration

- Discard elements after index 7
- Update Fibonacci values: Fib = 3, Fib_m1 = 2, Fib_m2 = 1
- Calculate index: min(4 + 1, 6) = min(5, 6) = 5
- Compare array[5] = 24 with target 24
- **Match found!** Element 24 is at index 5

![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/46e62029-7319-4183-9fe6-42f044c9a508)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/2c5a7dd5-cd61-4b43-92cb-e5215c0dcd41)

**Result:**
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/eae2ffe3-dc10-4f6c-a8f7-2994ba81ce1e)
![image](https://github.com/chaitanyatamira/FibonacciALGOAnimation/assets/125778105/e750a7af-dee7-44c4-880b-001b29191672)

## 🎓 Educational Value

This animation helps students and developers understand:

- How Fibonacci numbers are used in searching algorithms
- The divide-and-conquer approach in algorithm design
- Visual representation of algorithm execution steps
- Comparison between different search techniques

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Chaitanya Tamira**

- GitHub: [@chaitanyatamira](https://github.com/chaitanyatamira)

## 🙏 Acknowledgments

- Thanks to the Python community for the excellent Tkinter library
- Inspired by the need for visual learning tools in computer science education
