# Import the regular expression library
import re

# String of "dash_str"
dash_str = """COBOL is a compiled English-like computer programming language designed for business use. 122. On 10/10/2015 is a big date unlike 1/11/2010 """

# Find every instance of a date of the specified format occuring in the text
dash_date_finder = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", dash_str)

# Print every date found, line by line
for date in dash_date_finder:
    print(date)


# String of "hyphen_str"
hyphen_str = """COBOL is a compiled English-like computer programming language designed for business use. 122. On 10-10-2015 is a big date unlike 1-11-2010 """

# Find every instance of a date of the specified format occuring in the text
hyphen_date_finder = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", hyphen_str)

# Print every date found, line by line
for date in hyphen_date_finder:
    print(date)

# String of "month_str"
month_str = """COBOL is a compiled English-like computer programming language designed for business use. 122. On 10 MAR 2015 is a big date unlike 1 NOV 2010 """

# Find every instance of a date of the specified format occuring in the text, make it case insenstitive
month_date_finder = re.findall(
    r"([\d]{1,2}\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s[\d]{4})(?i)", month_str)

# Print every date found, line by line
for date in month_date_finder:
    print(date)


# String of "full_str"
full_str = """COBOL is a compiled English-like computer programming language designed for business use. 122. On 10 October 2015 is a big date unlike 1 November 2010 """

# Find every instance of a date of the specified format occuring in the text, make it case insensitive
full_date_finder = re.findall(
    r"([\d]{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s[\d]{4})(?i)", full_str)

# Print every date found, line by line
for date in full_date_finder:
    print(date)
