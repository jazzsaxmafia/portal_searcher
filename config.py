# Social Pick
key_socialpick = '237bc4b34763740433c5c5918703da1a1fb0e64f'
base_url_socialpick = "http://apis.daum.net/socialpick/search"
save_path_socialpick = "/home/ubuntu/web/socialpick/data/socialpick"

# Image (Naver)
key_naver = '5d8f3e56c2afa7ad444d6b53feed0179'
base_url_naver= 'http://openapi.naver.com/search'
save_path_image =  "/home/ubuntu/web/socialpick/data/image"

# Image (Daum)
key_daum = '237bc4b34763740433c5c5918703da1a1fb0e64f'
base_url_daum = 'http://apis.daum.net/search'

import datetime
def get_today():
	return datetime.datetime.today().strftime("%Y%m%d")

