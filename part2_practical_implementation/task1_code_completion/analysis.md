I manually wrote a Python function to sort dictionaries by a key using `sorted()` and a lambda. GitHub Copilot generated a similar function but used `.get()` to avoid key errors. Both are efficient (O(n log n)) due to Python’s Timsort, but the AI’s version is safer.

This shows how AI tools improve code robustness and reduce small errors. However, Copilot didn’t validate data types or check for empty lists, highlighting the need for human review. AI helped optimize a common pattern, saving time while reminding me to stay cautious and critical.
