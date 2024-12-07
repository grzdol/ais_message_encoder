### Quick tutorial
#### Install dependecies
```
pip install fastapi uvicorn pyais
```
#### Run server
```
uvicorn main:app --reload
```
#### Example request with curl
```
curl -X POST "http://127.0.0.1:8000/generate_ais/" \
     -H "Content-Type: application/json" \
     -d '{
         "course": 219.3,
         "lat": 37.802,
         "lon": -122.341,
         "mmsi": "366053209",
         "type": 1,
         "radio_channel": "B",
         "talker_id": "AIVDM"
     }'
```