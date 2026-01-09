import base64
import os
from hepai import HepAI, RemoteModel

# model: RemoteModel = HepAI(base_url="http://localhost:42600/apiv2"
#                            ).connect_to("hepai/custom-model")

model: RemoteModel = HepAI(base_url="https://aiapi.ihep.ac.cn/apiv2").connect_to("hepai/hainougat")

print(model.worker_info)  # Get worker info.
print(model.functions)  # Get all remote callable functions.
print(model.function_details)  # Get all remote callable function details.

# Call the `custom_method` of the remote model.
with open("/aifs/user/home/tangzihan/project/hai-nougat/Long_Progressive_Focused_Transformer_for_Single_Image_Super-Resolution_CVPR_2025_paper.pdf", "rb") as f:
    bytes_ = f.read()
pdfbin = base64.b64encode(bytes_).decode()
output = model.inference(api_key = os.getenv("HEPAI_API_KEY"),
        stream =False,
        timeout =60,
        pdfbin = pdfbin,
        )
print(f"output: {output}")

# call the `get_stream` of the remote model.
# stream = model.get_stream(stream=True)  # Note: You should set `stream=True` additionally.
# print(f"Output of get_stream:")
# for x in stream:
#     print(f"{x}, type: {type(x)}", flush=True)



