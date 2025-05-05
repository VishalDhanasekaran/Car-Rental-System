# openapi_client.CarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_car_cars_post**](CarsApi.md#create_car_cars_post) | **POST** /cars/ | Create Car
[**get_car_cars_car_id_get**](CarsApi.md#get_car_cars_car_id_get) | **GET** /cars/{car_id} | Get Car
[**get_cars_cars_get**](CarsApi.md#get_cars_cars_get) | **GET** /cars/ | Get Cars
[**rent_car_cars_car_id_rent_post**](CarsApi.md#rent_car_cars_car_id_rent_post) | **POST** /cars/{car_id}/rent | Rent Car


# **create_car_cars_post**
> Car create_car_cars_post(car_create)

Create Car

Add a new car to the system

### Example


```python
import openapi_client
from openapi_client.models.car import Car
from openapi_client.models.car_create import CarCreate
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
    api_instance = openapi_client.CarsApi(api_client)
    car_create = openapi_client.CarCreate() # CarCreate | 

    try:
        # Create Car
        api_response = api_instance.create_car_cars_post(car_create)
        print("The response of CarsApi->create_car_cars_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->create_car_cars_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_create** | [**CarCreate**](CarCreate.md)|  | 

### Return type

[**Car**](Car.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_cars_car_id_get**
> Car get_car_cars_car_id_get(car_id)

Get Car

Retrieve details of a specific car

### Example


```python
import openapi_client
from openapi_client.models.car import Car
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
    api_instance = openapi_client.CarsApi(api_client)
    car_id = 56 # int | 

    try:
        # Get Car
        api_response = api_instance.get_car_cars_car_id_get(car_id)
        print("The response of CarsApi->get_car_cars_car_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->get_car_cars_car_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 

### Return type

[**Car**](Car.md)

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

# **get_cars_cars_get**
> List[Car] get_cars_cars_get(available_only=available_only, skip=skip, limit=limit)

Get Cars

Retrieve all cars, with option to filter only available ones

### Example


```python
import openapi_client
from openapi_client.models.car import Car
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
    api_instance = openapi_client.CarsApi(api_client)
    available_only = False # bool |  (optional) (default to False)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Cars
        api_response = api_instance.get_cars_cars_get(available_only=available_only, skip=skip, limit=limit)
        print("The response of CarsApi->get_cars_cars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->get_cars_cars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_only** | **bool**|  | [optional] [default to False]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Car]**](Car.md)

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

# **rent_car_cars_car_id_rent_post**
> RentalResponse rent_car_cars_car_id_rent_post(car_id, rental_create)

Rent Car

Rent a car for a specified period

### Example


```python
import openapi_client
from openapi_client.models.rental_create import RentalCreate
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
    api_instance = openapi_client.CarsApi(api_client)
    car_id = 56 # int | 
    rental_create = openapi_client.RentalCreate() # RentalCreate | 

    try:
        # Rent Car
        api_response = api_instance.rent_car_cars_car_id_rent_post(car_id, rental_create)
        print("The response of CarsApi->rent_car_cars_car_id_rent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->rent_car_cars_car_id_rent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 
 **rental_create** | [**RentalCreate**](RentalCreate.md)|  | 

### Return type

[**RentalResponse**](RentalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

