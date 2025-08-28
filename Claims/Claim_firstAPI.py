import requests

# Base URL and endpoint
base_url = "https://devapi.rajyasabha.digital/ms/api/v1/common/"
end_point = "get-states/Active"
url = base_url + end_point

# Your token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiNjUzMDU2MTNhYmFmZGNiZWE1M2MxZTUxNWVhOGVkZmIyNjI0NjU2ZDgxNWJlMmNmNDJmNWI5YjU0NWUwYzFjZGY3NTdjYjc0OTA5ZjAxYmMiLCJpYXQiOjE3NDk0NjE3NzUuNDQ1MjY0LCJuYmYiOjE3NDk0NjE3NzUuNDQ1MjY3LCJleHAiOjE3ODA5OTc3NzUuNDI3NTgyLCJzdWIiOiIzMCIsInNjb3BlcyI6W119.TEM6Y-we-5jhoFI1vzYM3wBgrHZahZ5KBbGvJi7uEcfR9F233-QCqiZ7W8iIunceX_CpmOJAWS46s9OzG3yEFdFnGaRxPYP-gysVZjr9Pd8c_5foo1nE_NDuneyW38iCT5n_3CfFg-XJPHiCB5HbiZwKmTzJLTWi7JXiB0udsoIqB8oy0ndCWA3fYMvgTMMUh0JoNo-ZyT5bARPr8GUJX8elxMX_aCeAx5GLuPGlOCxE_I4I7n72TMvg_ibkOjAQs04uMC-8B0YiHD_Nq_OZPJC8AhUs0TQRwc9x0aH6kMIilx3dAHxd8cdmF6i5VcOCbBfzuQlKUUevYFfK_0o3jWntiVf5mMpB0jqtXXHIl76c4J1oRJsGNNKKMhK3xn1q5Fd-kU7yeivUJSsI0E-8OYoJSjhyso9AN7veKAwxiEPB_l4Zl-DXaYzUReQ9uzS457IpGUVPvWYkgT7cUjf8a7qqp18xXMO6RBmnsl1qeytDruwNVqZjBe8PB1fwedO6McekjQmdZv9Nggia2A6CxM5rCkA29TJsmZ-lErDNL2YeWhSUBu3tPi44kHymvztjP_RUaQuV5-fQnGz-7u8yCrQHK5bLSG2e3uVnxqxXkrg4EclnrLLotlQ5WqcZHNDvGcOn3YBr4wItUwZ2EF_13ImKNse9e2daDFI_v-yFu2k"

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json" ,
    "Accept" : "application/json"
}

# GET request with headers
response = requests.get(url, headers=headers)

# Output
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Error parsing JSON:", e)
    print("Raw Response:", response.text)
