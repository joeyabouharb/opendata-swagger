# StopFinderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the &#x60;version&#x60; request parameter.   | [optional] 
**error** | [**ErrorResponse**](ErrorResponse.md) | If an error has occurred, this element contains information about the error.  | [optional] 
**locations** | [**list[StopFinderLocation]**](StopFinderLocation.md) | An array of all locations that were found using the specified search input. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


