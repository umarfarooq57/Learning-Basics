#include <iostream>
using namespace std;

int main()
{
    // Step 1: Ask the user to enter a paragraph
    cout << "Enter a paragraph: "; // Print a message to the user
    string paragraph;              // Create a variable to store the paragraph
    getline(cin, paragraph);       // Read the entire paragraph (including spaces) and store it in the variable

    // Step 2: Ask the user to enter the word they want to count
    cout << "Enter a word to count the frequency of: "; // Print a message to the user
    string word;                                        // Create a variable to store the word
    cin >> word;                                        // Read the word and store it in the variable

    // Step 3: Count how many times the word appears in the paragraph
    int count = 0;      // Create a variable to keep track of the count (start at 0)
    string currentWord; // Create a variable to store each word as we read it from the paragraph

    // Loop through each character in the paragraph
    for (auto && ch : paragraph)
    {
        // If the character is a space or the end of the paragraph, it means we've reached the end of a word:
        if (ch == ' ' || ch == '\0')
        {
            // Check if the current word matches the word we're counting
            if (currentWord == word)
            {
                count++; // If it matches, increase the count by 1
            }
            currentWord = ""; // Reset the current word to start building the next word
        }
        else
        {
            // If the character is not a space, it's part of a word
            currentWord += ch; // Add the character to the current word
        }
    }

    // Check the last word in the paragraph (since it might not end with a space)
    if (currentWord == word)
    {
        count++; // If it matches, increase the count by 1
    }

    // Step 4: Print the result
    cout << "The word '" << word << "' appears " << count << " in the paragraph";

    return 0; // End the program
}