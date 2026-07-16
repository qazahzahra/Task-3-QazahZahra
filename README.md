# Project 3: Random Password Generator

Part of the **DecodeLabs Industrial Training Kit** (Batch 2026).

Problem Statement

Write a tool that asks the user for a password length (e.g., 8 characters) and generates a random, complex password using letters and numbers.

Key Skill: Importing Modules (`import random`) & String manipulation.

How It Works

1. The user is asked to enter the desired password length.
2. The input is validated — the program keeps asking until a positive number greater than 0 is entered (no zero or negative lengths allowed).
3. A character pool is built by combining `string.ascii_letters` (a–z, A–Z) and `string.digits` (0–9).
4. A loop runs `length` times, using `random.choice()` to pick a random character from the pool each time and build the password.
5. The final password is printed to the console.

