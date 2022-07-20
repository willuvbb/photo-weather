# %%
import json

import flickrapi

from settings import FLICKR_API_KEY, FLICKR_SECRET_KEY

api_key = FLICKR_API_KEY
api_secret = FLICKR_SECRET_KEY

USER_ID = "196068418@N02"

# %%
flickr = flickrapi.FlickrAPI(api_key, api_secret)
photos = flickr.photos.search(user_id=USER_ID, per_page="10")
sets = flickr.photosets.getList(user_id=USER_ID)

flickr_json = flickrapi.FlickrAPI(api_key, api_secret, format="json")
photos_json = flickr_json.photos.search(user_id=USER_ID, per_page="10")
sets_json = flickr_json.photosets.getList(user_id=USER_ID)
photos_parsed = json.loads(photos_json)
sets_parsed = json.loads(sets_json)
# %%
exif_j = flickr_json.photos.getExif(photo_id=photos_parsed["photos"]["photo"][0]["id"])
ejp = json.loads(exif_j)
for item in ejp["photo"]["exif"]:
    if item["label"] in ["Date and Time (Original)", "Date and Time (Modified)"]:
        print("item['raw']['_content']:", item["raw"]["_content"])

loc_j = flickr_json.photos.geo.getLocation(
    photo_id=photos_parsed["photos"]["photo"][0]["id"]
)
loc = json.loads(loc_j)
