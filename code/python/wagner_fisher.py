def wagner_fisher(str1, str2):
    """
    Compute the edit distance (Levenshtein distance) between two strings using the Wagner-Fisher algorithm.

    Parameters:
    - str1 (str): The first input string.
    - str2 (str): The second input string.

    Returns:
    int: The edit distance between the two input strings.
    """

    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]

    # Fill the matrix with initial values
    for i in range(len_str1):
        matrix[i][0] = i

    for j in range(len_str2):
        matrix[0][j] = j

    # Fill in the matrix based on Wagner-Fisher algorithm
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    # The bottom-right cell contains the final edit distance
    return matrix[-1][-1]


def main():
    # Example usage
    titles = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye"]

    user_input = input("Enter a book title: ")

    matches = [(title, wagner_fisher(user_input, title)) for title in titles]
    matches.sort(key=lambda x: x[1])

    print("Best Matches:")
    for match, distance in matches[:5]:
        print(f"Title: {match}, Distance: {distance}")
    

if __name__ == '__main__':
    main()
    
