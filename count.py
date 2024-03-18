def count_inputs():
    count = 0

    while True:
        user_input = input("Enter a value (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            break

        count += 1
        data_type = type(user_input).__name__
        print(f"Input {count}: {user_input} ({data_type})")

    print(f"\nTotal inputs: {count}")

# Run the counter
count_inputs()