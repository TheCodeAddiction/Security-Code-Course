# About
DNS lookup is an important part of passive-recon. It's a great way to enumerate domains that you 
can then dive into later. However, grabbing every DNS record for a domain can be tedious.

To solve this, we will make an automated python tool, that will query every record for a given domain.
We will also create a bunch of files, with different results like, one for all SOA records, which are
interesting when it comes to `DNS Zone Transfers`. 

# Task details:
1. For a given domain, enumerate all of these DNS record types:
`"A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"`
2. Grab the important information and filter into the following text files:
    1. One text file containing all general DNS information, for example `politiet.no. 1954 IN A 195.225.15.101`
    2. One text file containing all SOA records
    3. One text file containing a list of all the domains you have found, and only the domains, so that it can be looped over by a tool.
3. Make the tool be able to enumerate from a file, so that you can grab DNS records from a bunch of domains at once.
# Important notes
1. Your code should use "helper files" to encapsulate generic functions in different
files, this way you don't have one super large file that contains all the code.