# CoordRequestResponseLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with &#x60;XML_STOPFINDER_REQUEST&#x60;, or can be used as the origin or destination in an &#x60;XML_TRIP_REQUEST2&#x60; request. The format of a location ID differs greatly, depending on the type of location it is.  | [optional] 
**type** | **str** | This specifies the type of the returned item. If you search with a type of &#x60;GIS_POINT&#x60;, a returned item has a type of &#x60;gisPoint&#x60;.  | [optional] 
**name** | **str** | Contains a human-readable title for the location.  | [optional] 
**disassembled_name** | **str** | This is the short version of the location name, which does not include the suburb or other information.  | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | If available, contains information about this location&#39;s parent location. For example, if the stop has a type of &#x60;platform&#x60;, then this field may contain information about the station in which the platform is located.  | [optional] 
**coord** | **list[float]** | Contains exactly two values: the first value is the latitude, the second value is the longitude.  | [optional] 
**properties** | [**CoordRequestResponseLocationProperties**](CoordRequestResponseLocationProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


