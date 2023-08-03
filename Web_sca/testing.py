import re

# Function to filter "Important information" using regex
def filter_important_information(text):
    pattern = r'''
        (?i)  # Case-insensitive matching
        \b    # Word boundary
        (?:   # Non-capturing group for URL parts
            https?://             # Match http:// or https://
            |                     # or
            www\.                 # Match www.
        )
        \S+   # Match one or more non-space characters (the domain)
        (?:   # Non-capturing group for optional path and query string
            /  # Match the / symbol
            \S* # Match zero or more non-space characters (the path)
        )?
        (?:   # Non-capturing group for optional query string
            \? # Match the ? symbol
            \S* # Match zero or more non-space characters (the query string)
        )?
        \b    # Word boundary
    '''
    return [line for line in text.split('\n') if re.search(pattern, line,re.VERBOSE)]

# Read contents from the file
with open(r'D:\python\jupyter\Web_sca\eduman.txt', 'r') as file:
    original_text = file.read()
filtered_lines = filter_important_information(original_text)
filtered_text = '\n'.join(filtered_lines)

# Write the filtered content file
with open(r'D:\python\jupyter\Web_sca\filtered.txt', 'w') as file:
    file.write(filtered_text)

print("Filtered content has been written to 'filtered.txt'.")