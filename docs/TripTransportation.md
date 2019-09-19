# TripTransportation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is an ID that uniquely identifies this route.  | [optional] 
**name** | **str** | This contains the full name of the route.  | [optional] 
**disassembled_name** | **str** | Contains a very short name for the route.  | [optional] 
**number** | **str** | Contains a short name for the route.  | [optional] 
**icon_id** | **int** | Contains an ID for the icon that can be used for this route. Different values here are used to differentiate differents types of the same route type. For example, private ferries have a different wayfinding icon to ferries operated by Sydney Ferries.  | [optional] 
**description** | **str** | Contains a description of this route.  | [optional] 
**product** | [**RouteProduct**](RouteProduct.md) | This element contains additional properties about the route. | [optional] 
**operator** | [**TripTransportationOperator**](TripTransportationOperator.md) |  | [optional] 
**destination** | [**TripTransportationDestination**](TripTransportationDestination.md) |  | [optional] 
**properties** | [**TripTransportationProperties**](TripTransportationProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


