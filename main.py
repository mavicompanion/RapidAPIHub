import os
import requests
import json, io
from PIL import Image
import base64
import matplotlib.pyplot as plt

payload = {
  "modelName": "diffusion1XL", # DO NOT CHANGE THIS VALUE
  "prompt": "", 
  "imageHeight": 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 
  "imageWidth": 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 
  "negativePrompt": None, # Optional, mention aspects (if any) to be ignored in the output image
  "negativePrompt2": None, # Optional, mention aspects (if any) to be ignored in the output image
  "numOutputImages": 1 , # Optiona, Defaults to 1. Max value is 5
  "guidanceScale": 7.5, # Optional, Defaults to 5. Optimal values are < 15. 
  "numInferenceSteps": 10, # Optioanl, Defaults to 50. Max value is 100. 
  "seed": None, # Optional -  Leave it empty to generate a random value. Use the same value if you wish to get the same image. Modify the remaining parameters to get variants of the image
  "outputImgType": "pil" # Optional, Defaults to pil. Supported: pil, latent. 
}

payload['prompt'] = "Elon musk in a hindu temple"

headers = {"content-type": "application/json", "Authorization":""}

url = "https://cloud.olakrutrim.com/v1/images/generations/diffusion"

resp=requests.post(url,headers=headers,json=payload)


if resp.status_code == 200:
    output = resp.json()
    img_datas = output["data"]
    for index,img_data in enumerate(img_datas):
        img_bytes = base64.b64decode(img_data["b64_json"])
        img = Image.open(io.BytesIO(img_bytes))
        plt.imshow(img)
        plt.show()
else:
    print("Failed to get a response from the server. Status code:", resp.status_code)
    print("Response content:", resp.text)
