# RentalCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**car_id** | **int** |  | 
**user_name** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 

## Example

```python
from openapi_client.models.rental_create import RentalCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RentalCreate from a JSON string
rental_create_instance = RentalCreate.from_json(json)
# print the JSON string representation of the object
print(RentalCreate.to_json())

# convert the object into a dict
rental_create_dict = rental_create_instance.to_dict()
# create an instance of RentalCreate from a dict
rental_create_from_dict = RentalCreate.from_dict(rental_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


