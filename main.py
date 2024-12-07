from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pyais.encode import encode_dict

app = FastAPI()

class AISData(BaseModel):
    course: float = Field(..., example=219.3, description="Course over ground in degrees")
    lat: float = Field(..., example=37.802, description="Latitude in decimal degrees")
    lon: float = Field(..., example=-122.341, description="Longitude in decimal degrees")
    mmsi: str = Field(..., example="366053209", description="Maritime Mobile Service Identity (MMSI)")
    type: int = Field(..., example=1, description="AIS message type (e.g., 1 for position reports)")
    radio_channel: str = Field("A", example="A", description="Radio channel (A or B)")
    talker_id: str = Field("AIVDM", example="AIVDM", description="Talker ID (usually 'AIVDM')")

@app.post("/generate_ais/")
async def generate_ais(data: AISData):
    try:
        encoded = encode_dict(
            {
                "course": data.course,
                "lat": data.lat,
                "lon": data.lon,
                "mmsi": data.mmsi,
                "type": data.type,
            },
            radio_channel=data.radio_channel,
            talker_id=data.talker_id,
        )[0]

        return {"ais_message": encoded}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate AIS message: {str(e)}")
