# TripRequestResponseJourneyFareTicketProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rider_category_name** | **str** | A human-readable title for this ticket type. | [optional] 
**price_station_access_fee** | **str** | If part of the fare includes a station access fee (for example, when travelling to the airport), this field contains how much of the fare is made up of the station access fee. Note that this value is a string in the format of dollars and cents, in the currency described in &#x60;currency&#x60;. An example value is &#x60;3.50&#x60;.  | [optional] 
**price_total_fare** | **str** | This is the total cost of the fare, which combines the station access fee (if present) with the tariff for the particular trip. Note that this value is a string in the format of dollars and cents, in the currency described in &#x60;currency&#x60;. An example value is &#x60;3.50&#x60;.   | [optional] 
**evaluation_ticket** | **str** | If this value is set, then this particular ticket entry contains the total journey information for the given category of traveller. For example, for an &#x60;ADULT&#x60; traveller, there may be a ticket entry for each mode of travel, as well as a single entry for the entire trip which accumulates the various leg costs together.  Depending on the modes of travel, it&#39;s possible that the API is unable to determine the precise cost. For example, if a private ferry operator is included in a trip plan, then their cost is likely not included.  The possible values for this field are:  * &#x60;nswFareEnabled&#x60;: The entire cost of the trip was able to be calculated. * &#x60;nswFarePartiallyEnabled&#x60;: The cost of some - but not all - of the legs could be calculated. * &#x60;nswFareNotEnabled&#x60;: Opal is not available for this journey. * &#x60;nswFareNotAvailable&#x60;: The API was unable to determine any of the cost of the journey.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


