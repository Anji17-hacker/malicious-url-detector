import re
import socket
import whois
import tldextract
from urllib.parse import urlparse
from datetime import datetime

def extract_features(url):
    features = {}
    
    parsed = urlparse(url)
    ext = tldextract.extract(url)
    domain = parsed.netloc if parsed.netloc else parsed.path

    # --- Basic Features ---
    features['url_length'] = len(url)
    features['dot_count'] = url.count('.')
    features['hyphen_count'] = url.count('-')
    features['slash_count'] = url.count('/')
    features['has_https'] = int(parsed.scheme == 'https')

    # --- Suspicious Signs ---
    features['at_symbol'] = int('@' in url)
    features['double_slash'] = int('//' in url[7:])
    features['digit_count'] = sum(c.isdigit() for c in url)

    # --- Domain Features ---
    features['domain_length'] = len(domain)
    features['subdomain_count'] = len(ext.subdomain.split('.')) if ext.subdomain else 0

    # --- Keywords ---
    keywords = ['login', 'secure', 'account', 'update', 'free', 'verify']
    features['suspicious_keywords'] = sum(word in url.lower() for word in keywords)

    # --- IP address check ---
    features['ip_address'] = int(bool(re.match(r'^\d+\.\d+\.\d+\.\d+', domain)))

    # --- DNS check ---
    try:
        socket.gethostbyname(domain)
        features['dns'] = 1
    except:
        features['dns'] = 0

    return features
