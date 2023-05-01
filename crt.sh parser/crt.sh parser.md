# About
https://crt.sh/ is a website used to search for certificates assigned to a given domain
. However, when you search for a domain, you will get a lot of records, including
a lot of duplicates. On top of that, you might get a huge list of domains, which
you will have to send to a tool, meaning you need to manually put them into a file.
Doing this by hand, will take ages, so, instead we will write a python program that
does it for us.

# Task details:
1. Your program should take input from user, for what domain they want to search.
2. The program will take the domain, and search it up on crt.sh
3. Your program will parse the response and grab all unique domains and put them into a
file called "<domain name>_results.txt"

# Important notes
1. Your code should use "helper files" to encapsulate generic functions in different
files, this way you don't have one super large file that contains all the code.
2. Remember the crt.sh has rate limiting, which you should check for.