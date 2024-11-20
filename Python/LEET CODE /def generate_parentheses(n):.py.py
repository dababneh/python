

def generate_parentheses(n):
    result = []

    # Helper function for backtracking
    def backtrack(s='', open_count=0, close_count=0):
        # Base case: If the string has reached the maximum length
        if len(s) == 2 * n:
            result.append(s)
            return
        
        # Add an opening parenthesis if we can
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        
        # Add a closing parenthesis if it's valid
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)

    # Start backtracking from an empty string
    backtrack()
    
    return result

# Example usage
n = 2
combinations = generate_parentheses(n)
print("All combinations of well-formed parentheses for n =", n)
for combo in combinations:
    print(combo)
