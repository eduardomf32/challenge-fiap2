import boto3
import json
import time
import uuid

SQS_URL = "https://sqs.us-east-1.amazonaws.com/710818030245/evaluation-events-queue"
REGION = "us-east-1"

sqs = boto3.client("sqs", region_name=REGION)

TOTAL_MESSAGES = 15000
BATCH_SIZE = 10

print(f"Enviando {TOTAL_MESSAGES} mensagens com timestamp como String para {SQS_URL}...")
start = time.time()

for i in range(0, TOTAL_MESSAGES, BATCH_SIZE):
    entries = []
    for j in range(BATCH_SIZE):
        idx = i + j
        event_id = str(uuid.uuid4())
        body = {
            "id": event_id,
            "flag_name": "nova-interface-checkout",
            "user_id": f"sqs-cliente-{idx}",
            "result": True,
            "timestamp": str(int(time.time())),
            "source": "teste-carga-analytics"
        }
        entries.append({
            "Id": f"msg_{idx}",
            "MessageBody": json.dumps(body)
        })
    try:
        sqs.send_message_batch(QueueUrl=SQS_URL, Entries=entries)
    except Exception as e:
        print(f"Falha no envio do lote {i}: {e}")

print(f"Envio concluído em {time.time() - start:.2f}s!")