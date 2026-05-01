"""
PROBLEM STATEMENT: Gaussian Distribution Analyzer

TASK:
Write a function `analyze_gaussian(a, lmbda)` that computes key statistical
properties of the Gaussian probability density function:
ρ(x) = A * exp(-λ * (x - a)^2)

REQUIREMENTS:
1. Calculate the Normalization Constant (A):
   Formula: A = sqrt(λ / π)

2. Calculate the Expectation Value of x squared (<x^2>):
   Formula: <x^2> = (1 / (2 * λ)) + a^2

3. Input Validation:
   - λ (lmbda) must be a real positive constant.
   - If λ <= 0, the function should return the string:
     "Error: lambda must be a positive constant."

4. Formatting:
   - Return the results as a tuple: (A, expectation_x_sq)
   - Round both values to 4 decimal places using the round() function.

5.Vizulaisation:
  - Use matplotlib to draw the electron probability density graph

"""
import math
import matplotlib.pyplot as plt
import numpy as np

def analyze_gaussian(a, ld):
    A = math.sqrt(ld/math.pi)
    expectation_x_sq = (1/(2*ld)) + a**2

    return round(A , 4), round(expectation_x_sq , 4)


def plot_gaussian(a, ld, A):
    sigma = math.sqrt(1 / (2 * ld))
    x = np.linspace(a - 4 * sigma, a + 4 * sigma, 500)
    y = A * np.exp(-ld * (x - a) ** 2)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=(f'λ={ld}, a={a}'), color='blue', linewidth=2)
    plt.fill_between(x, y, color='blue', alpha=0.1)

    plt.axvline(a, color='red', linestyle='--', label=f'Center (a={a})')
    plt.title("Gaussian Probability Distribution")
    plt.xlabel("x")
    plt.ylabel("ρ(x)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

def main():
    while True:
        print("Welcome to Gaussian Distribution Analyzer")
        try:
          ld = float(input("Please enter the value of λ:"))
          if ld<=0:
              print("Please enter a positive integer")
              continue
          a = float(input("Please enter the value of a:"))
        except ValueError:
            print("please enter valid numbers!")
            continue

        r1, r2 = analyze_gaussian(a, ld)
        print(f"The value of Normalisation Constant is : {r1} ")
        print(f"The value of Expectation Value is : {r2} ")
        plot_gaussian(a , ld , r1)
        query = input("Would you like to use the program again?\n"
                      "Press 'y' to continue or press any other key to exit.").lower()
        if query == 'y':
            continue
        else:
            break

main()
