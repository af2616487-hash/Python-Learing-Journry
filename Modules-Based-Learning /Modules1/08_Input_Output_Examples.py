"""
╔═══════════════════════════════════════════════════════════════════════════╗
║         MODULE 8: INPUT AND OUTPUT OPERATIONS IN PYTHON                   ║
║     Different ways to take input and display output effectively           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: Basic Input and Output Operations
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*80)
print("EXAMPLE 1: BASIC INPUT AND OUTPUT")
print("="*80)
print("Description: Taking simple string input and displaying output with f-strings\n")

name = input("➤ Enter your name: ")
print(f"👋 Hello, {name}!")
print(f"✓ Welcome to Python Learning Module!\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: Type Conversion - Taking Integer Input
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 2: TYPE CONVERSION - INTEGER INPUT")
print("="*80)
print("Description: Converting string input to integer for mathematical operations\n")

age = int(input("➤ Enter your age: "))
print(f"📅 Your current age: {age} years")
print(f"🎂 Next year you will be: {age + 1} years")
print(f"🎓 After 10 years you will be: {age + 10} years\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 3: Taking Multiple Inputs Using split()
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 3: MULTIPLE INPUTS WITH split()")
print("="*80)
print("Description: Taking multiple space-separated values in a single line\n")

x, y = input("➤ Enter two numbers (separated by space): ").split()
print(f"📌 First number: {x}")
print(f"📌 Second number: {y}")
print(f"📊 Concatenated: {x}{y}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 4: Float Input and Temperature Conversion
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 4: FLOAT INPUT AND TEMPERATURE CONVERSION")
print("="*80)
print("Description: Converting Celsius to Fahrenheit using float values\n")

celsius = float(input("➤ Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"🌡️  {celsius}°C = {fahrenheit:.2f}°F")
print(f"📈 Formula used: (C × 9/5) + 32\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 5: String Input Operations
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 5: STRING INPUT OPERATIONS")
print("="*80)
print("Description: Various string methods and operations\n")

sentence = input("➤ Enter a sentence: ")
print(f"📝 Original text: {sentence}")
print(f"📊 Length: {len(sentence)} characters")
print(f"🔤 UPPERCASE: {sentence.upper()}")
print(f"🔡 lowercase: {sentence.lower()}")
print(f"🔄 Reversed: {sentence[::-1]}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 6: Processing List of Numbers (Sum, Average, Min, Max)
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 6: PROCESSING LIST OF NUMBERS")
print("="*80)
print("Description: Calculating sum, average, maximum, and minimum values\n")

numbers = list(map(int, input("➤ Enter numbers (separated by space): ").split()))
print(f"\n📋 Numbers entered: {numbers}")
print(f"➕ Sum: {sum(numbers)}")
print(f"📊 Average: {sum(numbers) / len(numbers):.2f}")
print(f"📈 Maximum: {max(numbers)}")
print(f"📉 Minimum: {min(numbers)}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 7: Print with Different Separators (sep parameter)
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 7: PRINT WITH DIFFERENT SEPARATORS")
print("="*80)
print("Description: Using 'sep' parameter to customize output separation\n")

print("Default (space):     ", "A", "B", "C")
print("Dash separator:      ", "A", "B", "C", sep="-")
print("Pipe separator:      ", "Item1", "Item2", "Item3", sep=" | ")
print("Arrow separator:     ", "Start", "End", sep=" ➜ ")
print("Comma separator:     ", "apple", "banana", "orange", sep=", ")
print()


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 8: Print with Different End Parameters
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 8: PRINT WITH DIFFERENT END PARAMETERS")
print("="*80)
print("Description: Using 'end' parameter for custom line endings\n")

print("Default behavior (newline):")
print("Line 1")
print("Line 2")
print("Line 3")

print("\nCustom end parameter (space):")
print("Item1", end=" ")
print("Item2", end=" ")
print("Item3")

print("\nLoading animation:")
print("Loading", end="")
for i in range(4):
    print(".", end="", flush=True)
    # In real execution, this would show animation
print(" Done!")

print("\n")

# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("✨ ALL 8 EXAMPLES COMPLETED SUCCESSFULLY! ✨")
print("="*80)
print("\n📚 Module Summary:")
print("   • Example 1: Basic input/output with f-strings")
print("   • Example 2: Type conversion (int)")
print("   • Example 3: Multiple inputs using split()")
print("   • Example 4: Float conversion and calculations")
print("   • Example 5: String manipulation methods")
print("   • Example 6: List operations (sum, avg, min, max)")
print("   • Example 7: Separator customization")
print("   • Example 8: End parameter customization")
print("="*80 + "\n")
