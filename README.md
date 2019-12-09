# Introduce
OCR server power by concr [https://github.com/breezedeus/cnocr](https://github.com/breezedeus/cnocr).
# Required
 - python3
 - cnocr (https://github.com/breezedeus/cnocr)
# Start
Start the service:
```python
python ocr_server.py
```

Request:
```curl
curl http://127.0.0.1:8888 -X POST -H "Content-Type:application/json" -d "{\"filePath\":\"D:\\opencv-test\\8.jpg\"}"
```

Response:
```json
{
    "code": 0,
    "message": "OK",
    "data": [
        [
            "嗯",
            "嗯"
        ]
    ]
}
```
