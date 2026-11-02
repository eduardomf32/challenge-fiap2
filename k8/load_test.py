import urllib.request
import urllib.error
import concurrent.futures
import os
import sys
import time

api_key = os.environ.get("API_KEY")
if not api_key:
    api_key = "tm_key_b08277a34f830661e27885e2611d65382b5cb31bb9347cb65ed587435e28b18e"

url = "http://localhost:8080/evaluation/evaluate?flag_name=nova-interface-checkout&user_id=teste-hpa"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

total_requests = 20000
concurrency = 50

def send_request(_):
    req = urllib.request.Request(url, data=b"", headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception:
        return False

print(f"Disparando {total_requests} requisições com concorrência {concurrency}...")
start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
    results = list(executor.map(send_request, range(total_requests)))

success = results.count(True)
errors = results.count(False)
elapsed = time.time() - start_time

print(f"\n--- Resultado do Teste de Carga ---")
print(f"Tempo total: {elapsed:.2f}s")
print(f"RPS: {total_requests / elapsed:.2f}")
print(f"Respostas 200 OK: {success}")
print(f"Falhas: {errors}")