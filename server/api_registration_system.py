from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .storage import read_data, write_data, log_audit

app = FastAPI()
class Registration(BaseModel):
    member_id: str
    event_id: str

@app.post("/")
def register(r: Registration):
    members = read_data("members")
    events = read_data("events")
    regs = read_data("registrations")

    if not any(m['id'] == r.member_id for m in members):
        raise HTTPException(status_code=404, detail="Member not found")
    
    event = next((e for e in events if e['id'] == r.event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    count = sum(1 for reg in regs if reg['event_id'] == r.event_id)
    if count >= event['capacity']:
        raise HTTPException(status_code=400, detail="Event is full")

    max_id = 0
    for reg in regs:
        try:
            curr_num = int(reg['id'].split('-')[1])
            if curr_num > max_id:
                max_id = curr_num
        except:
            continue
            
    new_id = f"R-{max_id + 1}"

    new_reg = {"id": new_id, "member_id": r.member_id, "event_id": r.event_id}
    regs.append(new_reg)
    write_data("registrations", regs)
    log_audit(f"REGISTERED: {r.member_id} -> {r.event_id}")
    return {"msg": "Success", "reg_id": new_reg['id']}

@app.get("/")
def list_registrations():
    return read_data("registrations")