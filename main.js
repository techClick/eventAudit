function addServiceEvent(eventName, eventId ){
    eventDetails = document.getElementById("inputDetail"+eventId).value
    serviceEvent = {name:eventName,id:+eventId+1,details:eventDetails}
    urlData = JSON.stringify(serviceEvent)
    window.location.href = "home?newevent="+urlData
}
function addService(){
    newService = document.getElementById("serviceInput").value
    if (newService == "" || newService == ""){
        alert("Please, fill in the service to add.")
        return
    }
    window.location.href = "home?newservice="+newService
}
