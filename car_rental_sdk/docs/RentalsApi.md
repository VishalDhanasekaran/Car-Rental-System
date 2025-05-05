# openapi_client.RentalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_rental_rentals_rental_id_delete**](RentalsApi.md#cancel_rental_rentals_rental_id_delete) | **DELETE** /rentals/{rental_id} | Cancel Rental
[**get_rental_rentals_rental_id_get**](RentalsApi.md#get_rental_rentals_rental_id_get) | **GET** /rentals/{rental_id} | Get Rental
[**get_rentals_rentals_get**](RentalsApi.md#get_rentals_rentals_get) | **GET** /rentals/ | Get Rentals


# **cancel_rental_rentals_rental_id_delete**
> cancel_rental_rentals_rental_id_delete(rental_id)

Cancel Rental

Cancel an active rental

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RentalsApi(api_client)
    rental_id = 56 # int | 

    try:
        # Cancel Rental
        api_instance.cancel_rental_rentals_rental_id_delete(rental_id)
    except Exception as e:
        print("Exception when calling RentalsApi->cancel_rental_rentals_rental_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rental_rentals_rental_id_get**
> RentalResponse get_rental_rentals_rental_id_get(rental_id)

Get Rental

Retrieve a specific rental

### Example


```python
import openapi_client
from openapi_client.models.rental_response import RentalResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RentalsApi(api_client)
    rental_id = 56 # int | 

    try:
        # Get Rental
        api_response = api_instance.get_rental_rentals_rental_id_get(rental_id)
        print("The response of RentalsApi->get_rental_rentals_rental_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->get_rental_rentals_rental_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_id** | **int**|  | 

### Return type

[**RentalResponse**](RentalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rentals_rentals_get**
> List[RentalResponse] get_rentals_rentals_get(skip=skip, limit=limit)

Get Rentals

Retrieve all rentals

### Example


```python
import openapi_client
from openapi_client.models.rental_response import RentalResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RentalsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Rentals
        api_response = api_instance.get_rentals_rentals_get(skip=skip, limit=limit)
        print("The response of RentalsApi->get_rentals_rentals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->get_rentals_rentals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[RentalResponse]**](RentalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

