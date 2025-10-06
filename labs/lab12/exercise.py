# Counter-controlled approach - must know count first
num_count = int(input("How many numbers? "))
total = 0

for i in range(num_count):
    number = int(input(f"Enter number {i + 1}: "))
    total += number

print(f"Total: {total}")

# Sentinel-controlled approach - stop when ready
total = 0
count = 0

number = int(input("Enter number (0 to stop): "))  # Prime input

while number != 0:  # Condition
    total += number
    count += 1
    number = int(input("Enter number (0 to stop): "))  # Update

print(f"Total of {count} numbers: {total}")