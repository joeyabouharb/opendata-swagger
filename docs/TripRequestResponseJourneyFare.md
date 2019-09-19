# TripRequestResponseJourneyFare

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickets** | [**list[TripRequestResponseJourneyFareTicket]**](TripRequestResponseJourneyFareTicket.md) | Contains a list of the available ticket types for the given trip. given a single type of traveller (e.g. Adult), there may be multiple records in this array that applies to that single traveller. This is because fares are broken down depending on which modes of travel there are.  Please take note of the documentation for &#x60;evaluationTicket&#x60;, as this value is used to determine the cost of an entire journey.   | [optional] 
**zones** | [**list[TripRequestResponseJourneyFareZone]**](TripRequestResponseJourneyFareZone.md) | This data is not used at this time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


