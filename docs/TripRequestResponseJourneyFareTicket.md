# TripRequestResponseJourneyFareTicket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This ID uniquely identifies the ticket type, based on the of traveller, mode of transport and the time of day.   | [optional] 
**name** | **str** | This describes the type of fare, which will be for Opal card.  | [optional] 
**comment** | **str** | Additional information about the ticket type.  | [optional] 
**currency** | **str** | The currency used for all pricing contained within this ticket. All prices are in Australian dollars (&#x60;AUD&#x60;).  | [optional] 
**price_level** | **str** | XXX | [optional] 
**price_brutto** | **float** | Total tariff amount for this ticket (i.e. not including extra charges such as station access fee). &#39;Brutto&#39; means &#39;Gross&#39; in German.  | [optional] 
**price_netto** | **float** | The net tariff amount for this ticket. This is currently at 0 as it related to the tax percentage.  | [optional] 
**tax_percent** | **int** | This is the amount of tax applied to the fare. Currently this will be 0 in all cases.  | [optional] 
**from_leg** | **int** | This value contains a 0-based index of the starting leg for this fare. For example, if there are 3 legs and the first two are covered by a single fare and the final by another, there will be one ticket with a &#x60;fromLeg&#x60; of &#x60;0&#x60; and a &#x60;toLeg&#x60; of &#x60;1&#x60;, and the second will have a value of &#x60;2&#x60; for both &#x60;fromLeg&#x60; and &#x60;toLeg&#x60;.   | [optional] 
**to_leg** | **int** | This value contains a 0-based index of the starting leg for this fare. For example, if there are 3 legs and the first two are covered by a single fare and the final by another, there will be one ticket with a &#x60;fromLeg&#x60; of &#x60;0&#x60; and a &#x60;toLeg&#x60; of &#x60;1&#x60;, and the second will have a value of &#x60;2&#x60; for both &#x60;fromLeg&#x60; and &#x60;toLeg&#x60;.   | [optional] 
**net** | **str** | XXX | [optional] 
**person** | **str** | This is the type of traveller the ticket applies to. | [optional] 
**traveller_class** | **str** | This indicates the class (e.g. first class, second class), but is not currently used.  | [optional] 
**time_validity** | **str** | This describes how long the ticket is valid for. Not currently used. | [optional] 
**valid_minutes** | **int** | This describes how long in minutes the ticket is valid for. Not currently used. | [optional] 
**is_short_haul** | **str** | Whether or not the trip is short haul. Not currently used. | [optional] 
**returns_allowed** | **str** | Whether or not the ticket allows you to make the return journey also. Not currently used. | [optional] 
**valid_for_one_journey_only** | **str** | Whether or not the ticket is a single journey ticket only. Not currently used. | [optional] 
**valid_for_one_operator_only** | **str** | Whether or not the ticket will only work for a single operator. Not currently used. | [optional] 
**number_of_changes** | **int** | The number of transfers allowed with this ticket. Not currently used. | [optional] 
**name_validity_area** | **str** | Not currently used. | [optional] 
**properties** | [**TripRequestResponseJourneyFareTicketProperties**](TripRequestResponseJourneyFareTicketProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


