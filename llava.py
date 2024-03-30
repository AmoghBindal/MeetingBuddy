import replicate
import os 

os.environ["REPLICATE_API_TOKEN"] = "r8_D1drOA4uzBmtzRFdMGJjbbrnGh8ROkV2Q16Vl"

print(os.environ.get("REPLICATE_API_TOKEN"))

#This Function Takes text and image and prints response
def genresponse(text, imgurl):
    output = replicate.run(
        "yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb",
        input={
            "image": imgurl,
            "top_p": 1,
            "prompt": "Help me, I am in a video meeting and the host has asked me something. This is what was said in the meeting previously, "+text+ " what should I respond with",
            "max_tokens": 1024,
            "temperature": 0.2
        }
    )

    # The yorickvp/llava-13b model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    for item in output:
        # https://replicate.com/yorickvp/llava-13b/api#output-schema
        print(item, end="")