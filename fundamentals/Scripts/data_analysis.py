import re

def harvest_security_data(url):
    """
    Extracts IPv4 addresses, email addresses, and CVE IDs from a mock HTML string.
    Ignores the 'url' parameter; uses the global mock_html variable as per exercise.

    Returns:
        tuple: (list_of_unique_ips, list_of_unique_emails, list_of_unique_cves)
    """

    mock_html = """
    Critical vulnerability CVE-2025-4782 discovered in web servers.
    Contact admin@threat.org immediately for assistance.
    Attacker IP: 192.168.1.100 was observed scanning the network.
    Email support@security.com for patch details.
    Multiple issues reported: CVE-2024-9999 and CVE-2025-4782 again.
    Internal server IP: 10.0.0.50 requires immediate attention.
    Reach out to analyst@netguard.local for more information.
    """
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    cve_pattern = r'\bCVE-\d{4}-\d{4}\b'

    raw_ips = re.findall(ip_pattern, mock_html)
    raw_emails = re.findall(email_pattern, mock_html)
    raw_cves = re.findall(cve_pattern, mock_html)

    def is_valid_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if not p.isdigit():
                return False
            num = int(p)
            if num < 0 or num > 255:
                return False
        return True

    def unique_preserve_order(iterable, validator=None):
        seen = set()
        unique = []
        for item in iterable:
            if validator and not validator(item):
                continue
            if item not in seen:
                seen.add(item)
                unique.append(item)
        return unique

    unique_ips = unique_preserve_order(raw_ips, validator=is_valid_ip)
    unique_emails = unique_preserve_order(raw_emails)
    unique_cves = unique_preserve_order(raw_cves)
    return unique_ips, unique_emails, unique_cves


if __name__ == "__main__":

    ips, emails, cves = harvest_security_data("dummy_url")

    print(f"Emails Found: {', '.join(emails)}")
    print(f"IPs Found: {', '.join(ips)}")
    print(f"CVEs Found: {', '.join(cves)}")