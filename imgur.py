from imgur_python import Imgur

username = 'azart2288'
client_id = '1091e7c26797a5a'
client_secret = 'с5896d4792a72bb93059b6a11f2f21da7b11b39d'
imgur_client = Imgur({'client_id': client_id, 'access_token': client_secret})
gallery_profile = imgur_client.gallery_profile(username)
print(gallery_profile)