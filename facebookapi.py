import requests

# Your Facebook Graph API Token
access_token = 'your_access_token_here'

def get_fb_photos(page_id):
    url = f'https://graph.facebook.com/v12.0/{page_id}/photos?type=uploaded&access_token={access_token}'
    response = requests.get(url)
    photos = response.json()
    
    for photo in photos['data']:
        photo_url = f"https://graph.facebook.com/v12.0/{photo['id']}/picture?access_token={access_token}"
        img_data = requests.get(photo_url).content
        with open(f"{photo['id']}.jpg", 'wb') as handler:
            handler.write(img_data)
            print(f"Downloaded {photo['id']}.jpg")

# Replace 'your_page_id' with a valid Facebook page ID.
get_fb_photos('your_page_id')
