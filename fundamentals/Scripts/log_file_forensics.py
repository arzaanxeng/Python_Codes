"""
NetGuard — Log File Forensics
You've been handed a simulated server log file (as a Python string). Your job is to parse it like a forensics tool.
Your mock_log should look like:
2024-01-15 08:23:11 INFO  Request from 192.168.1.10 user=alice@corp.com GET /dashboard 200
2024-01-15 08:24:05 WARN  Request from 203.0.113.42 user=bob@external.net GET /admin 403
2024-01-15 08:25:33 ERROR Request from 203.0.113.42 user=bob@external.net POST /login 500
2024-01-15 08:26:01 INFO  Request from 10.0.0.5 user=carol@corp.com GET /home 200
2024-01-15 08:27:44 ERROR Request from 45.33.32.156 user=unknown POST /login 500

Tasks:
Extract all unique IPs, emails, HTTP status codes, and log levels using Regex
Flag any IP that appears more than once as SUSPICIOUS
Flag any request hitting /admin or /login as a HIGH-RISK endpoint
Build a threat_score() function — each ERROR adds 2 points, each WARN adds 1, each 403/500 adds 1. Print a ranked threat table
Port scan the Ips

"""

import re
import socket

mock_log = """
2024-01-15 08:23:11 INFO  Request from 192.168.1.10 user=alice@corp.com GET /dashboard 200
2024-01-15 08:24:05 WARN  Request from 203.0.113.42 user=bob@external.net GET /admin 403
2024-01-15 08:25:33 ERROR Request from 203.0.113.42 user=bob@external.net POST /login 500
2024-01-15 08:26:01 INFO  Request from 10.0.0.5 user=carol@corp.com GET /home 200
2024-01-15 08:27:44 ERROR Request from 45.33.32.156 user=unknown POST /login 500
"""

# 1. EXTRACT DATA
def extraction_data(log):
    log_pattern = re.compile(
        r".*?\s+"                      # Skip date/time
        r"(INFO|WARN|ERROR)\s+"        # Group 1: Log Level
        r"Request from ([\d.]+)\s+"    # Group 2: IP
        r"user=(\S+)\s+"               # Group 3: Email/user
        r"[A-Z]+\s+(\S+)\s+"           # Group 4: Request Path
        r"(\d{3})"                     # Group 5: HTTP Code
    )
    matches = log_pattern.findall(log)
    data = [(m[1], m[0], m[4], m[3]) for m in matches]
    # data tuple → (ip, level, http_code, path)

    emails = list({m[2] for m in matches if "@" in m[2]})
    return data, emails


# 2. FORENSICS REPORT
def forensics_report(data, emails):
    ip_counts = {}
    high_risk_paths = set()

    for ip, _, _, path in data:
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        if path in ["/admin", "/login"]:
            high_risk_paths.add(path)

    suspicious = [ip for ip, count in ip_counts.items() if count > 1]

    print("===== NETGUARD FORENSICS REPORT =====")
    print(f"  Emails Found     : {', '.join(emails) or 'None'}")
    print(f"  Suspicious IPs   : {', '.join(suspicious) or 'None'}")
    print(f"  High-Risk Hits   : {', '.join(high_risk_paths) or 'None'}")
    print("=" * 38)

    return suspicious


# 3. THREAT SCORING
def ip_threat(data):
    ip_scores = {}
    for ip, level, http, _ in data:
        if ip not in ip_scores:
            ip_scores[ip] = 0
        if level == "ERROR":
            ip_scores[ip] += 2
        elif level == "WARN":
            ip_scores[ip] += 1
        if http in ["403", "500"]:
            ip_scores[ip] += 1
    return ip_scores


def get_level(ip_scores):
    print("\n=== THREAT SCORES (RANKED) ===")
    print(f"{'IP Address':<16} | {'Score':<6} | {'Status':<10}")
    print("=" * 38)

    ranked = sorted(ip_scores.items(), key=lambda x: x[1], reverse=True)
    for ip, score in ranked:
        if score >= 4:
            status = "CRITICAL"
        elif score >= 2:
            status = "MODERATE"
        else:
            status = "CLEAN"
        print(f"{ip:<16} | {score:<6} | {status:<10}")


# 4. PORT SCANNER
def audit_network(ips):
    print("\n=== PORT AUDIT — SUSPICIOUS IPs ONLY (PORT 80) ===")
    print(f"{'IP Address':<16} | {'Status':<20}")
    print("=" * 38)
    for ip in ips:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((ip, 80))
        s.close()
        status = "ACTIVE" if result == 0 else "INACTIVE/FILTERED"
        print(f"{ip:<16} | {status:<20}")


data, emails       = extraction_data(mock_log)
suspicious_ips     = forensics_report(data, emails)
scores             = ip_threat(data)
get_level(scores)
audit_network(suspicious_ips)
















