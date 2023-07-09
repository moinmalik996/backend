# Ads System

Ads management based on locations/regions.

## Models
Resides in models package in ads app (ads_system/ads/models/*)
* Ad 
* Location
* AdsLocation

Ad and Location have m2m relation through an intermediate model AdsLocation. 
AdsLocation is the main model which act as a running ad with its data like date expiry, max visits etc.

## APIs / Views
Resides in api package in ads app(ads_system/ads/api/*)
* AdViewSet: Api for Ad
* LocationViewSet: Api for Location
* AdsLocationViewset: Api for AdsLocation
* RunningAdsViewSet: Api for running Ads filtered by location

## Urls
These are just api endpoints.

### Ads
Get all ads (content) or Post a new one

```http
  GET, POST /api/ad/
```

Get Single item

```http
  GET, DELETE, UPDATE /api/ad/${id}
````
  
### Locations
Get all location (content) or Post a new one

```http
  GET, POST /api/location/
```

Get Single item

```http
  GET, DELETE, UPDATE /api/location/${id}
```

### AdsLocations
 Get all actual ads that were created and started for a particular location till now or Post a new one

```http
  GET, POST /api/adslocation/
```

Get Single item

```http
  GET, DELETE, UPDATE /api/adslocation/${id}
```
> **_NOTE:_**  Update will only update the visits data field with the data coming from request.



### RunningAds
 Get all running ads based on particular location

```http
  GET /api/adslocation/
```

Get Single item

```http
  GET /api/adslocation/${id}
```


## Background Task

Each time an adslocation is created, a celery task will be created through post_save signal which will run after 24 hours for that particular ad and set its no. of visits to 0.

ads_system/ads/tasks.py

