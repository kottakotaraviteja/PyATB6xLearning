import random
attempt = 1
max_attempts = 3

response_code = 0

while attempt <= max_attempts:
    # Simulate an API call using a random response (replace this with real API code)
    response_code = random.choice([200, 500, 404, 503])

    print(f"Attempt {attempt}: Response {response_code}")

    if response_code == 200:
        print("✅ Test Passed")
        break  # Exit loop if success

    attempt += 1  # Try again if not success

# After 3 attempts, if still not 200:
if response_code != 200:
    print("❌ Test Failed after 3 attempts")