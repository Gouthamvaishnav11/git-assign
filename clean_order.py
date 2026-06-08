print("Cleaning invalid orders...")

# Cleaning Logic
# Remove rows where amount <= 0
# Example:
# 1002,502,-50,completed
# This record should be removed because amount is invalid.