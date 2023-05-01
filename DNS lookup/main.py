import dns.resolver
from helper import file_helper as fh

dns_record_types = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]



valid_dns_records = []
def create_list_of_all_dns_records(domain):
    for record in dns_record_types:
        dns_record = get_dns_record(domain, record)
        if dns_record is not None:
            valid_dns_records.append(dns_record)



def get_dns_record(domain, record_type):
    try:
        result = dns.resolver.resolve(domain, record_type)
        return result.response.answer[0].to_text()
    except dns.exception.DNSException:
        pass

def main():
    print("━━━ writing DNS records ━━━")
    with open("Input/domains.txt", 'r') as file:
        for record in file:
            domain = record.strip()
            create_list_of_all_dns_records(domain)
    fh.write_all_dns_records_to_file(valid_dns_records)
    fh.write_all_soa_records_to_file(valid_dns_records)
    fh.write_all_domain_names_to_file(valid_dns_records)
    print("Done!╰(*°▽°*)╯")

main()