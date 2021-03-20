import files.database
import json

# Services include
# CUSTOMER_CREATED
# CORRELATION_OF_RECORD_DONE
# CUSTOMER_BILLED
# CUSTOMER_DEACTIVATED
# etc

class Service:
    def __init__(self,newService):
        name = files.database.getData('services.txt')

        if newService and newService != "" :
            newService=newService.replace(" ","_")
            newService=newService.upper()
            name.append(newService)
            saveData = json.dumps(name)
            files.database.saveData( 'services.txt',saveData )

        self.name = list(reversed(name))
