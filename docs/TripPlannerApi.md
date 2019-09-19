# swagger_client.TripPlannerApi

All URIs are relative to *https://api.transport.nsw.gov.au/v1/tp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tfnsw_addinfo_request**](TripPlannerApi.md#tfnsw_addinfo_request) | **GET** /add_info | Provides capability to display all public transport service status and incident information (as published from the Incident Capture System).
[**tfnsw_coord_request**](TripPlannerApi.md#tfnsw_coord_request) | **GET** /coord | When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.
[**tfnsw_dm_request**](TripPlannerApi.md#tfnsw_dm_request) | **GET** /departure_mon | Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.
[**tfnsw_stopfinder_request**](TripPlannerApi.md#tfnsw_stopfinder_request) | **GET** /stop_finder | Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).
[**tfnsw_trip_request2**](TripPlannerApi.md#tfnsw_trip_request2) | **GET** /trip | Provides capability to provide NSW public transport trip plan options, including walking and driving legs, real-time and Opal fare information.


# **tfnsw_addinfo_request**
> AdditionalInfoResponse tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid, filter_mot_type=filter_mot_type, filter_publication_status=filter_publication_status, itd_l_pxx_sel_stop=itd_l_pxx_sel_stop, itd_l_pxx_sel_line=itd_l_pxx_sel_line, itd_l_pxx_sel_operator=itd_l_pxx_sel_operator, filter_pn_line_dir=filter_pn_line_dir, filter_pn_line_sub=filter_pn_line_sub, version=version)

Provides capability to display all public transport service status and incident information (as published from the Incident Capture System).

This endpoint returns a list of service alerts or additional information about travelling on the public transport network. This list can be filtered by date, route type, route, operator or stop. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: tfsnwAccessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TripPlannerApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
filter_date_valid = '01-10-2016' # str | This parameter allows you to filter the returned items that are only valid on the specified date. The format of this field is `DD-MM-YYYY`. For example, 12 September 2016 would be represented by `12-09-2016`.  (optional) (default to 01-10-2016)
filter_mot_type = 56 # int | This parameter allows you to filter the returned items by the modes of transport they affected. Available modes include:  * `1`: Train * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus  (optional)
filter_publication_status = 'filter_publication_status_example' # str | This field can be used so only current alerts are returned, and not historic alerts.  (optional)
itd_l_pxx_sel_stop = 'itd_l_pxx_sel_stop_example' # str | This parameter allows you to filter the returned items by its stop ID. For example, to retrieve items that are only relevant to Central Station, you would set this value to `10111010`. You can use the XML_STOPFINDER_REQUEST to determine the ID for a particular stop.  (optional)
itd_l_pxx_sel_line = 'itd_l_pxx_sel_line_example' # str | This parameter allows you to filter the returned items by line number. For example, `020T1`.  (optional)
itd_l_pxx_sel_operator = 'itd_l_pxx_sel_operator_example' # str | This parameter allows you to filter the returned items by operator ID.   (optional)
filter_pn_line_dir = 'filter_pn_line_dir_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:D`, (NNN: subnet, LLLLL: Route number, D: direction `H`/`R`).  (optional)
filter_pn_line_sub = 'filter_pn_line_sub_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:E:D`, (NNN: subnet, LLLLL: Route number, D: direction `H`/`R`).  (optional)
version = '10.2.1.15' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.15)

try:
    # Provides capability to display all public transport service status and incident information (as published from the Incident Capture System).
    api_response = api_instance.tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid, filter_mot_type=filter_mot_type, filter_publication_status=filter_publication_status, itd_l_pxx_sel_stop=itd_l_pxx_sel_stop, itd_l_pxx_sel_line=itd_l_pxx_sel_line, itd_l_pxx_sel_operator=itd_l_pxx_sel_operator, filter_pn_line_dir=filter_pn_line_dir, filter_pn_line_sub=filter_pn_line_sub, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripPlannerApi->tfnsw_addinfo_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **filter_date_valid** | **str**| This parameter allows you to filter the returned items that are only valid on the specified date. The format of this field is &#x60;DD-MM-YYYY&#x60;. For example, 12 September 2016 would be represented by &#x60;12-09-2016&#x60;.  | [optional] [default to 01-10-2016]
 **filter_mot_type** | **int**| This parameter allows you to filter the returned items by the modes of transport they affected. Available modes include:  * &#x60;1&#x60;: Train * &#x60;4&#x60;: Light Rail * &#x60;5&#x60;: Bus * &#x60;7&#x60;: Coach * &#x60;9&#x60;: Ferry * &#x60;11&#x60;: School Bus  | [optional] 
 **filter_publication_status** | **str**| This field can be used so only current alerts are returned, and not historic alerts.  | [optional] 
 **itd_l_pxx_sel_stop** | **str**| This parameter allows you to filter the returned items by its stop ID. For example, to retrieve items that are only relevant to Central Station, you would set this value to &#x60;10111010&#x60;. You can use the XML_STOPFINDER_REQUEST to determine the ID for a particular stop.  | [optional] 
 **itd_l_pxx_sel_line** | **str**| This parameter allows you to filter the returned items by line number. For example, &#x60;020T1&#x60;.  | [optional] 
 **itd_l_pxx_sel_operator** | **str**| This parameter allows you to filter the returned items by operator ID.   | [optional] 
 **filter_pn_line_dir** | **str**| This parameter allows you to filter the returned items by specific routes. The route is provided in the format &#x60;NNN:LLLLL:D&#x60;, (NNN: subnet, LLLLL: Route number, D: direction &#x60;H&#x60;/&#x60;R&#x60;).  | [optional] 
 **filter_pn_line_sub** | **str**| This parameter allows you to filter the returned items by specific routes. The route is provided in the format &#x60;NNN:LLLLL:E:D&#x60;, (NNN: subnet, LLLLL: Route number, D: direction &#x60;H&#x60;/&#x60;R&#x60;).  | [optional] 
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.15]

### Return type

[**AdditionalInfoResponse**](AdditionalInfoResponse.md)

### Authorization

[tfsnwAccessCode](../README.md#tfsnwAccessCode)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_coord_request**
> CoordRequestResponse tfnsw_coord_request(output_format, coord, coord_output_format, incl_filter, type_1, radius_1, incl_draw_classes_1=incl_draw_classes_1, type_2=type_2, radius_2=radius_2, incl_draw_classes_2=incl_draw_classes_2, type_3=type_3, radius_3=radius_3, incl_draw_classes_3=incl_draw_classes_3, purpose=purpose, version=version)

When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.

This endpoint returns places of interest based on the given coordinate and a radius. The types of POIs can be controlled, so if, for example, you only want Opal resellers returned, you can do so. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: tfsnwAccessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TripPlannerApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord = '151.206290:-33.884080:EPSG:4326' # str | The coordinate is in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first). For example, the following `coord` value can be used to search around Central Station: `151.206290:-33.884080:EPSG:4326`.  (default to 151.206290:-33.884080:EPSG:4326)
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format. 
incl_filter = 1 # int | This enables \"advanced filter mode\" on the server, which is required to enable searching using coordinates.   (default to 1)
type_1 = 'GIS_POINT' # str | This specifies the type of items to return.  * `GIS_POINT`: GIS points, including Opal resellers (see `inclDrawClasses_1`) * `BUS_POINT`: Stops/stations * `POI_POINT`: Places of interest  (default to GIS_POINT)
radius_1 = 1000 # int | This indicates the maximum number of metres to search in all directions from the location specified in `coord`. For example, if you use a value of `500` and a `type_1` value of `GIS_POINT`, all Opal resellers within 500 metres will be returned.  (default to 1000)
incl_draw_classes_1 = 56 # int | This flag changes the list of POIs that are returned. To return Opal resellers, set this value to `74` and `type_1` to `GIS_POINT`.  (optional)
type_2 = 'BUS_POINT' # str | This specifies the type of items to return.  * `GIS_POINT`: GIS points, including Opal resellers (see `inclDrawClasses_2`) * `BUS_POINT`: Stops/stations * `POI_POINT`: Places of interest  (optional) (default to BUS_POINT)
radius_2 = 1000 # int | This indicates the maximum number of metres to search in all directions from the location specified in `coord`. For example, if you use a value of `500` and a `type_2` value of `GIS_POINT`, all Opal resellers within 500 metres will be returned.  (optional) (default to 1000)
incl_draw_classes_2 = 56 # int | This flag changes the list of POIs that are returned. To return Opal resellers, set this value to `74` and `type_2` to `GIS_POINT`.  (optional)
type_3 = 'POI_POINT' # str | This specifies the type of items to return.  * `GIS_POINT`: GIS points, including Opal resellers (see `inclDrawClasses_3`) * `BUS_POINT`: Stops/stations * `POI_POINT`: Places of interest  (optional) (default to POI_POINT)
radius_3 = 1000 # int | This indicates the maximum number of metres to search in all directions from the location specified in `coord`. For example, if you use a value of `500` and a `type_3` value of `GIS_POINT`, all Opal resellers within 500 metres will be returned.  (optional) (default to 1000)
incl_draw_classes_3 = 56 # int | This flag changes the list of POIs that are returned. To return Opal resellers, set this value to `74` and `type_3` to `GIS_POINT`.  (optional)
purpose = 'purpose_example' # str | This field indicates how the returned data is to be used, which in turn impacts whether or not certain locations are returned.  (optional)
version = '10.2.1.15' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.15)

try:
    # When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.
    api_response = api_instance.tfnsw_coord_request(output_format, coord, coord_output_format, incl_filter, type_1, radius_1, incl_draw_classes_1=incl_draw_classes_1, type_2=type_2, radius_2=radius_2, incl_draw_classes_2=incl_draw_classes_2, type_3=type_3, radius_3=radius_3, incl_draw_classes_3=incl_draw_classes_3, purpose=purpose, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripPlannerApi->tfnsw_coord_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord** | **str**| The coordinate is in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first). For example, the following &#x60;coord&#x60; value can be used to search around Central Station: &#x60;151.206290:-33.884080:EPSG:4326&#x60;.  | [default to 151.206290:-33.884080:EPSG:4326]
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format.  | 
 **incl_filter** | **int**| This enables \&quot;advanced filter mode\&quot; on the server, which is required to enable searching using coordinates.   | [default to 1]
 **type_1** | **str**| This specifies the type of items to return.  * &#x60;GIS_POINT&#x60;: GIS points, including Opal resellers (see &#x60;inclDrawClasses_1&#x60;) * &#x60;BUS_POINT&#x60;: Stops/stations * &#x60;POI_POINT&#x60;: Places of interest  | [default to GIS_POINT]
 **radius_1** | **int**| This indicates the maximum number of metres to search in all directions from the location specified in &#x60;coord&#x60;. For example, if you use a value of &#x60;500&#x60; and a &#x60;type_1&#x60; value of &#x60;GIS_POINT&#x60;, all Opal resellers within 500 metres will be returned.  | [default to 1000]
 **incl_draw_classes_1** | **int**| This flag changes the list of POIs that are returned. To return Opal resellers, set this value to &#x60;74&#x60; and &#x60;type_1&#x60; to &#x60;GIS_POINT&#x60;.  | [optional] 
 **type_2** | **str**| This specifies the type of items to return.  * &#x60;GIS_POINT&#x60;: GIS points, including Opal resellers (see &#x60;inclDrawClasses_2&#x60;) * &#x60;BUS_POINT&#x60;: Stops/stations * &#x60;POI_POINT&#x60;: Places of interest  | [optional] [default to BUS_POINT]
 **radius_2** | **int**| This indicates the maximum number of metres to search in all directions from the location specified in &#x60;coord&#x60;. For example, if you use a value of &#x60;500&#x60; and a &#x60;type_2&#x60; value of &#x60;GIS_POINT&#x60;, all Opal resellers within 500 metres will be returned.  | [optional] [default to 1000]
 **incl_draw_classes_2** | **int**| This flag changes the list of POIs that are returned. To return Opal resellers, set this value to &#x60;74&#x60; and &#x60;type_2&#x60; to &#x60;GIS_POINT&#x60;.  | [optional] 
 **type_3** | **str**| This specifies the type of items to return.  * &#x60;GIS_POINT&#x60;: GIS points, including Opal resellers (see &#x60;inclDrawClasses_3&#x60;) * &#x60;BUS_POINT&#x60;: Stops/stations * &#x60;POI_POINT&#x60;: Places of interest  | [optional] [default to POI_POINT]
 **radius_3** | **int**| This indicates the maximum number of metres to search in all directions from the location specified in &#x60;coord&#x60;. For example, if you use a value of &#x60;500&#x60; and a &#x60;type_3&#x60; value of &#x60;GIS_POINT&#x60;, all Opal resellers within 500 metres will be returned.  | [optional] [default to 1000]
 **incl_draw_classes_3** | **int**| This flag changes the list of POIs that are returned. To return Opal resellers, set this value to &#x60;74&#x60; and &#x60;type_3&#x60; to &#x60;GIS_POINT&#x60;.  | [optional] 
 **purpose** | **str**| This field indicates how the returned data is to be used, which in turn impacts whether or not certain locations are returned.  | [optional] 
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.15]

### Return type

[**CoordRequestResponse**](CoordRequestResponse.md)

### Authorization

[tfsnwAccessCode](../README.md#tfsnwAccessCode)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_dm_request**
> DepartureMonitorResponse tfnsw_dm_request(output_format, coord_output_format, type_dm, name_dm, dep_arr_macro, itd_date, itd_time, mode=mode, name_key_dm=name_key_dm, tf_nswdm=tf_nswdm, version=version)

Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.

This endpoint returns a list of departures/arrivals for a given location based on the date and time specified. This data can be used to display a \"upcoming departures\" board for a stop. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: tfsnwAccessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TripPlannerApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
type_dm = 'stop' # str | This specifies the type of results expected based on the search input in `name_dm`. By specifying `any`, locations of all types can be returned. Typically, this API call is used for a specific stop, so `stop` should be used along with a stop ID in `name_dm`.  (default to stop)
name_dm = '10111010' # str | This is the search term that will be used to find locations. If the combination of this value and `type_dm` results in more than one location found - or `mode` is not set to `direct`, then a list of stops and no departures will be returned.  (default to 10111010)
dep_arr_macro = 'dep' # str | This value anchors the requested date time to the departure time.  (default to dep)
itd_date = '20161001' # str | The reference date used when searching trips, in `YYYYMMDD` format. For instance, 20160901 refers to 1 September 2016. Works in conjunction with the `itdTime` and `depArrMacro` values.  (default to 20161001)
itd_time = '1200' # str | The reference time used when searching trips, in `HHMM` 24-hour format. For instance, 2215 refers to 10:15 PM. | Works in conjunction with the `itdDate` and `depArrMacro` values.  (default to 1200)
mode = 'direct' # str | This allows the departure board to display directly without going through the stop verification process. Use this when the stop is known. This relies on the given combination of `type_dm` and `name_dm` returning only a single result, otherwise a list of stops and no departures shall be returned.  (optional) (default to direct)
name_key_dm = 'name_key_dm_example' # str | Setting this parameter to `$USEPOINT$` enables you to request departures for a specific platform within a station. If this isn't used, then departures for all platforms at the stop specified in `name_dm` are returned.  (optional)
tf_nswdm = 'true' # str | Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. (optional) (default to true)
version = '10.2.1.15' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.15)

try:
    # Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.
    api_response = api_instance.tfnsw_dm_request(output_format, coord_output_format, type_dm, name_dm, dep_arr_macro, itd_date, itd_time, mode=mode, name_key_dm=name_key_dm, tf_nswdm=tf_nswdm, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripPlannerApi->tfnsw_dm_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **type_dm** | **str**| This specifies the type of results expected based on the search input in &#x60;name_dm&#x60;. By specifying &#x60;any&#x60;, locations of all types can be returned. Typically, this API call is used for a specific stop, so &#x60;stop&#x60; should be used along with a stop ID in &#x60;name_dm&#x60;.  | [default to stop]
 **name_dm** | **str**| This is the search term that will be used to find locations. If the combination of this value and &#x60;type_dm&#x60; results in more than one location found - or &#x60;mode&#x60; is not set to &#x60;direct&#x60;, then a list of stops and no departures will be returned.  | [default to 10111010]
 **dep_arr_macro** | **str**| This value anchors the requested date time to the departure time.  | [default to dep]
 **itd_date** | **str**| The reference date used when searching trips, in &#x60;YYYYMMDD&#x60; format. For instance, 20160901 refers to 1 September 2016. Works in conjunction with the &#x60;itdTime&#x60; and &#x60;depArrMacro&#x60; values.  | [default to 20161001]
 **itd_time** | **str**| The reference time used when searching trips, in &#x60;HHMM&#x60; 24-hour format. For instance, 2215 refers to 10:15 PM. | Works in conjunction with the &#x60;itdDate&#x60; and &#x60;depArrMacro&#x60; values.  | [default to 1200]
 **mode** | **str**| This allows the departure board to display directly without going through the stop verification process. Use this when the stop is known. This relies on the given combination of &#x60;type_dm&#x60; and &#x60;name_dm&#x60; returning only a single result, otherwise a list of stops and no departures shall be returned.  | [optional] [default to direct]
 **name_key_dm** | **str**| Setting this parameter to &#x60;$USEPOINT$&#x60; enables you to request departures for a specific platform within a station. If this isn&#39;t used, then departures for all platforms at the stop specified in &#x60;name_dm&#x60; are returned.  | [optional] 
 **tf_nswdm** | **str**| Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.15]

### Return type

[**DepartureMonitorResponse**](DepartureMonitorResponse.md)

### Authorization

[tfsnwAccessCode](../README.md#tfsnwAccessCode)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_stopfinder_request**
> StopFinderResponse tfnsw_stopfinder_request(output_format, type_sf, name_sf, coord_output_format, any_max_size_hit_list=any_max_size_hit_list, tf_nswsf=tf_nswsf, version=version)

Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).

This endpoint returns info about stops that match the search criteria. Matches can be sorted on `matchQuality` to determine the best matches for the given input. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: tfsnwAccessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TripPlannerApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
type_sf = 'type_sf_example' # str | This specifies the type of results expected in the list of returned stops. By specifying `any`, locations of all types can be returned. If you specifically know that you're searching using a coord, specify `coord`. Likewise, if you're using a stop ID as an input, use `stop` for more accurate results. 
name_sf = 'Circular Quay' # str | This is the search term that will be used to find locations. To lookup a coordinate, set `type_sf` to `coord`, and use the following format: `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first). For example, `151.206290:-33.884080:EPSG:4326`.  (default to Circular Quay)
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
any_max_size_hit_list = 10 # int | The maximum number of results to return in the request. (optional) (default to 10)
tf_nswsf = 'true' # str | Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site. (optional) (default to true)
version = '10.2.1.15' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.15)

try:
    # Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).
    api_response = api_instance.tfnsw_stopfinder_request(output_format, type_sf, name_sf, coord_output_format, any_max_size_hit_list=any_max_size_hit_list, tf_nswsf=tf_nswsf, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripPlannerApi->tfnsw_stopfinder_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **type_sf** | **str**| This specifies the type of results expected in the list of returned stops. By specifying &#x60;any&#x60;, locations of all types can be returned. If you specifically know that you&#39;re searching using a coord, specify &#x60;coord&#x60;. Likewise, if you&#39;re using a stop ID as an input, use &#x60;stop&#x60; for more accurate results.  | 
 **name_sf** | **str**| This is the search term that will be used to find locations. To lookup a coordinate, set &#x60;type_sf&#x60; to &#x60;coord&#x60;, and use the following format: &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first). For example, &#x60;151.206290:-33.884080:EPSG:4326&#x60;.  | [default to Circular Quay]
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **any_max_size_hit_list** | **int**| The maximum number of results to return in the request. | [optional] [default to 10]
 **tf_nswsf** | **str**| Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site. | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.15]

### Return type

[**StopFinderResponse**](StopFinderResponse.md)

### Authorization

[tfsnwAccessCode](../README.md#tfsnwAccessCode)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_trip_request2**
> TripRequestResponse tfnsw_trip_request2(output_format, coord_output_format, dep_arr_macro, itd_date, itd_time, type_origin, name_origin, type_destination, name_destination, calc_number_of_trips=calc_number_of_trips, wheelchair=wheelchair, tf_nswtr=tf_nswtr, version=version)

Provides capability to provide NSW public transport trip plan options, including walking and driving legs, real-time and Opal fare information.

This endpoint is used to find a list of journeys between two locations at the specified date and time. For example, if the user is at the Airport and wants to get to Manly using public transport but isn't sure how exactly, this call will tell them exactly which train, bus, ferry or light rail to catch, and between which stops. It is extremely detailed, and includes fare/ticketing information, as well as the the specific path the vehicle(s) will take. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: tfsnwAccessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TripPlannerApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
dep_arr_macro = 'dep_arr_macro_example' # str | This value anchors the requested date time. If set to `dep`, then trips *departing after* the specified date/time *at the specified location* are included. If set to `arr`, then trips *arriving before* the specified time *at its destination stop* are included. Works in conjunctions with the `itdDate` and `itdTime` values. 
itd_date = '20161001' # str | The reference date used when searching trips, in `YYYYMMDD` format. For instance, `20160901` refers to 1 September 2016. Works in conjunction with the `itdTime` and `depArrMacro` values.  (default to 20161001)
itd_time = '1200' # str | The reference time used when searching trips, in `HHMM` 24-hour format. For instance, `2215` refers to 10:15 PM. | Works in conjunction with the `itdDate` and `depArrMacro` values.  (default to 1200)
type_origin = 'any' # str | This is the type of data specified in the `name_origin` field. The origin indicates the starting point when searching for journeys.  The best way to use the trip planner is to use use `any` for this field then specify a valid location ID in `type_origin`, or to use `coord` in this field and a correctly formatted coordinate in `type_origin`.   (default to any)
name_origin = '10101331' # str | This value should contain a valid location/stop ID (for example, `10101100` indicates Central Station - this can be determined using `XML_STOPFINDER_REQUEST`). It is used to indicate the starting point when searching for journeys. Alternatively, you can use a coordinate in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first).  (default to 10101331)
type_destination = 'any' # str | This is the type of data specified in the `name_destination` field. The origin indicates the finishing point when searching for journeys. The best way to use the trip planner is to use use `any` for this field then specify a valid location ID in `type_destination`, or to use `coord` in this field and a correctly formatted coordinate in `type_destination`.   (default to any)
name_destination = '10102027' # str | This value should contain a valid location/stop ID (for example, `10101100` indicates Central Station - this can be determined using `XML_STOPFINDER_REQUEST`). It is used to indicate the finishing point when searching for journeys. Alternatively, you can use a coordinate in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first).  (default to 10102027)
calc_number_of_trips = 6 # int | This parameter indicates the maximum number of trips to returned. Fewer trips may be returned anyway, depending on the available public transport services.  (optional) (default to 6)
wheelchair = 'wheelchair_example' # str | Setting this value to `on` ensures that only wheelchair-accessible options are returned.  (optional)
tf_nswtr = 'true' # str | Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. (optional) (default to true)
version = '10.2.1.15' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.15)

try:
    # Provides capability to provide NSW public transport trip plan options, including walking and driving legs, real-time and Opal fare information.
    api_response = api_instance.tfnsw_trip_request2(output_format, coord_output_format, dep_arr_macro, itd_date, itd_time, type_origin, name_origin, type_destination, name_destination, calc_number_of_trips=calc_number_of_trips, wheelchair=wheelchair, tf_nswtr=tf_nswtr, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripPlannerApi->tfnsw_trip_request2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **dep_arr_macro** | **str**| This value anchors the requested date time. If set to &#x60;dep&#x60;, then trips *departing after* the specified date/time *at the specified location* are included. If set to &#x60;arr&#x60;, then trips *arriving before* the specified time *at its destination stop* are included. Works in conjunctions with the &#x60;itdDate&#x60; and &#x60;itdTime&#x60; values.  | 
 **itd_date** | **str**| The reference date used when searching trips, in &#x60;YYYYMMDD&#x60; format. For instance, &#x60;20160901&#x60; refers to 1 September 2016. Works in conjunction with the &#x60;itdTime&#x60; and &#x60;depArrMacro&#x60; values.  | [default to 20161001]
 **itd_time** | **str**| The reference time used when searching trips, in &#x60;HHMM&#x60; 24-hour format. For instance, &#x60;2215&#x60; refers to 10:15 PM. | Works in conjunction with the &#x60;itdDate&#x60; and &#x60;depArrMacro&#x60; values.  | [default to 1200]
 **type_origin** | **str**| This is the type of data specified in the &#x60;name_origin&#x60; field. The origin indicates the starting point when searching for journeys.  The best way to use the trip planner is to use use &#x60;any&#x60; for this field then specify a valid location ID in &#x60;type_origin&#x60;, or to use &#x60;coord&#x60; in this field and a correctly formatted coordinate in &#x60;type_origin&#x60;.   | [default to any]
 **name_origin** | **str**| This value should contain a valid location/stop ID (for example, &#x60;10101100&#x60; indicates Central Station - this can be determined using &#x60;XML_STOPFINDER_REQUEST&#x60;). It is used to indicate the starting point when searching for journeys. Alternatively, you can use a coordinate in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first).  | [default to 10101331]
 **type_destination** | **str**| This is the type of data specified in the &#x60;name_destination&#x60; field. The origin indicates the finishing point when searching for journeys. The best way to use the trip planner is to use use &#x60;any&#x60; for this field then specify a valid location ID in &#x60;type_destination&#x60;, or to use &#x60;coord&#x60; in this field and a correctly formatted coordinate in &#x60;type_destination&#x60;.   | [default to any]
 **name_destination** | **str**| This value should contain a valid location/stop ID (for example, &#x60;10101100&#x60; indicates Central Station - this can be determined using &#x60;XML_STOPFINDER_REQUEST&#x60;). It is used to indicate the finishing point when searching for journeys. Alternatively, you can use a coordinate in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first).  | [default to 10102027]
 **calc_number_of_trips** | **int**| This parameter indicates the maximum number of trips to returned. Fewer trips may be returned anyway, depending on the available public transport services.  | [optional] [default to 6]
 **wheelchair** | **str**| Setting this value to &#x60;on&#x60; ensures that only wheelchair-accessible options are returned.  | [optional] 
 **tf_nswtr** | **str**| Including parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.15]

### Return type

[**TripRequestResponse**](TripRequestResponse.md)

### Authorization

[tfsnwAccessCode](../README.md#tfsnwAccessCode)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

