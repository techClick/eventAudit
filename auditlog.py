import json
from datetime import datetime
import files.database

class AuditLog:
    def __init__(self,newEvent):
        newEvent = json.loads(newEvent)
        time = datetime.now().strftime('%d %B, %Y %I:%M %p')
        events = files.database.getData('auditlogevents.txt')

        if newEvent and len(newEvent) > 0:
            newEvent.update({"time":time})
            if newEvent["details"] == None or newEvent["details"] == "":
                newEvent["details"] = "Empty"
            events.append(newEvent)
            saveData = json.dumps(events)
            files.database.saveData( 'auditlogevents.txt',saveData )

        self.events = list(reversed(events))

