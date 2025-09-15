def sort(width, height, length, mass):
    """
    Sort packages into stacks based on volume and mass criteria.
    
    Args:
        width (float): Width in centimeters
        height (float): Height in centimeters  
        length (float): Length in centimeters
        mass (float): Mass in kilograms
        
    Returns:
        str: Stack name - 'STANDARD', 'SPECIAL', or 'REJECTED'
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = volume >= 1000000 or max(width, height, length) >= 150
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Determine stack using ternary operators
    return 'REJECTED' if (is_heavy and is_bulky) else ('SPECIAL' if (is_heavy or is_bulky) else 'STANDARD')


def test_sorting_function():
    """Test the sort function with various package configurations."""
    print("Testing Package Sorting Function")
    print("=" * 40)
    
    # Test cases: (width, height, length, mass, expected_result)
    test_cases = [
        # Standard packages
        (10, 10, 10, 5, "STANDARD"),         # Small, light
        (50, 50, 50, 10, "STANDARD"),        # Medium, light
        
        # Heavy packages (SPECIAL)
        (10, 10, 10, 25, "SPECIAL"),         # Small but heavy
        (100, 100, 100, 20, "REJECTED"),     # Heavy at threshold + bulky volume
        
        # Bulky packages (SPECIAL) 
        (150, 10, 10, 5, "SPECIAL"),         # One dimension >= 150cm
        (100, 100, 100, 5, "SPECIAL"),       # Volume = 1,000,000 cm³ (at threshold)
        (101, 100, 100, 5, "SPECIAL"),       # Volume > 1,000,000 cm³
        
        # Rejected packages (both heavy AND bulky)
        (150, 10, 10, 20, "REJECTED"),       # Heavy + dimension >= 150cm
        (100, 100, 100, 25, "REJECTED"),     # Heavy + volume >= 1,000,000 cm³
        (200, 200, 200, 30, "REJECTED"),     # Very heavy and very bulky
    ]
    
    all_passed = True
    for i, (w, h, l, m, expected) in enumerate(test_cases, 1):
        result = sort(w, h, l, m)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result != expected:
            all_passed = False
            
        volume = w * h * l
        is_bulky = volume >= 1000000 or max(w, h, l) >= 150
        is_heavy = m >= 20
        
        print(f"Test {i:2d}: {w:3}×{h:3}×{l:3}cm, {m:4}kg → {result:8} {status}")
        print(f"         Volume: {volume:,} cm³, Heavy: {is_heavy}, Bulky: {is_bulky}")
        print()
    
    print("=" * 40)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    
    return all_passed


if __name__ == "__main__":
    # Run the test suite
    test_sorting_function()
    
    print("\nInteractive Testing:")
    print("Enter package dimensions and mass to test sorting:")
    print("(Press Ctrl+C to exit)")
    
    try:
        while True:
            try:
                print("\nEnter package details:")
                width = float(input("Width (cm): "))
                height = float(input("Height (cm): "))
                length = float(input("Length (cm): "))
                mass = float(input("Mass (kg): "))
                
                result = sort(width, height, length, mass)
                volume = width * height * length
                is_bulky = volume >= 1000000 or max(width, height, length) >= 150
                is_heavy = mass >= 20
                
                print(f"\nPackage Analysis:")
                print(f"Dimensions: {width}×{height}×{length} cm")
                print(f"Volume: {volume:,} cm³")
                print(f"Mass: {mass} kg")
                print(f"Is Heavy: {is_heavy} (>= 20 kg)")
                print(f"Is Bulky: {is_bulky} (volume >= 1,000,000 cm³ or dimension >= 150 cm)")
                print(f"Stack Assignment: {result}")
                
            except ValueError:
                print("Please enter valid numbers.")
            except KeyboardInterrupt:
                break
                
    except KeyboardInterrupt:
        print("\n\nExiting package sorter. Goodbye!")