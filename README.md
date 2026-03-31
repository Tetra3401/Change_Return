# Change Return Program

A simple Python program that calculates and displays the correct change owed to a customer after a purchase.

## Overview

The program generates a random item cost (up to $200), prompts the user to enter a payment amount, and then breaks down the change into the appropriate denominations: dollars, quarters, dimes, nickels, and pennies.

## Requirements

- Python 3.x
- No external dependencies

## Usage

Run the script from the command line:

```bash
python change_return.py
```

You will see a randomly generated item cost and be prompted to enter a payment amount:

```
Your item costs $47.83
Type out an amount to pay: $50
```

The program will then display the change breakdown:

```
You receive:
2 dollars
0 quarters
1 dimes
1 nickels
2 pennies.
```

## How It Works

1. A random cost between $0.00 and $200.00 is generated.
2. The user inputs a payment amount.
3. The difference (change) is converted to **integer cents** to avoid floating point precision errors.
4. Floor division (`//`) and modulo (`%`) are used to calculate the number of each coin denomination cleanly and efficiently.

## Notes

- The payment amount is rounded to the nearest cent.
- If the payment entered is less than the item cost, the change values will be negative. input validation is not currently implemented.
- Floating point arithmetic (e.g. repeated subtraction of `0.10`) is intentionally avoided by working in whole cents internally.
