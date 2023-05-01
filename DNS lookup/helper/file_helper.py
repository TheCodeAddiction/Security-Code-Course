import os
import re


def write_list_to_file(filename, list):
    file_path = os.path.join("Output", filename)
    with open(file_path, "w") as f:
        for data in list:
            f.write(str(data) + "\n")
    f.close()


def write_all_dns_records_to_file(dns_records):
    write_list_to_file("valid_dns_records.txt", dns_records)


def write_all_soa_records_to_file(dns_records):
    soa_regex = r'^([\w\.-]+)\s+\d+\s+IN\s+SOA\s+(.+)$'
    soa_records = []
    for record in dns_records:
        match = re.match(soa_regex, record)
        if match:
            soa_records.append(match.groups())

    print(soa_records)
    write_list_to_file("soa_dns_records.txt", soa_records)


def write_all_domain_names_to_file(dns_records):
    unique_domains = []
    domain_pattern = r'\b(?:[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}\b'
    for record in dns_records:
        domains = re.findall(domain_pattern, record)
        for domain in domains:
            if domain not in unique_domains:
                unique_domains.append(domain)
    write_list_to_file("all_domains.txt", unique_domains)
