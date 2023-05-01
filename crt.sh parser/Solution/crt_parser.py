from crt import crt

def main():
    target_list = input("Give me a list of domains name:\n")
    target_domains = target_list.split(",")
    for domain in target_domains:
        crt.get_all_domains(crt.create_url(domain),domain)



if __name__ == '__main__':
    main()
