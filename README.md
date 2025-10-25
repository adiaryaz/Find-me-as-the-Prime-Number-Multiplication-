# Find me as the Prime Number (Multiplication)

A program to find and calculate the product of all prime numbers from a series of user inputs.

## 📝 Description

This program repeatedly asks the user if they want to enter a number. If the user agrees (by entering 'y'), they provide an integer. The program must check if this integer is a prime number. When the user decides to stop (by entering 'n'), the program calculates and displays the total product (multiplication) of all the prime numbers that were entered.

-----

## 🎯 Problem Statement

### Input:

  * A sequence of 'y' (yes) or 'n' (no) prompts to control the loop.
  * An integer input from the user following each 'y' prompt.

### Output:

  * The total product of all entered numbers that are identified as prime.
  * "NoProceed" if an invalid input (like a negative number) is entered.

### Rules:

1.  The program runs in a loop, asking for input. 'y' continues the loop, 'n' stops it.
2.  A **prime number** is a natural number **greater than 1** (e.g., 2, 3, 5, 7...).
3.  **Multiplication Logic:** The program should multiply all found prime numbers together.
4.  If **no prime numbers** are found (or no numbers are entered), the result must be **1** (the multiplicative identity).
5.  Non-prime positive numbers (like 1, 4, 8, 10) are ignored.
6.  Entering a **negative number** is invalid and should output "NoProceed".

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
y
2
y
10
n
```

**Output:**

```
2
```

**Explanation:** `2` is a prime number. `10` is not prime and is ignored. The total product is **2**.

### Example 2 (Sample 2)

**Input:**

```
y
2
y
3
y
5
n
```

**Output:**

```
30
```

**Explanation:** `2`, `3`, and `5` are all prime numbers. The product is `2 * 3 * 5 = 30`.

### Example 3 (Sample 3)

**Input:**

```
y
4
y
8
n
```

**Output:**

```
1
```

**Explanation:** Neither `4` nor `8` is a prime number. No primes were found, so the result is **1**.

### Example 4 (Sample 4)

**Input:**

```
n
```

**Output:**

```
1
```

**Explanation:** No numbers were entered, and no primes were found. The result is **1**.

### Example 5 (Sample 5)

**Input:**

```
y
3
y
-5
```

**Output:**

```
NoProceed
```

**Explanation:** The input `-5` is a negative number, which is not a valid input.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/multiply-primes.git
    cd multiply-primes
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Follow the 'y/n' prompts to enter numbers and see the result.
