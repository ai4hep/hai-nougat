import os
import hai
hai.api_key = os.getenv("HEPAI_API_KEY")

ret = hai.Model.inference(
    model='meta/nougat-test',
    input='hello',
    file='xxx/ddd.pdf',
    xxx='xx',
    )

print(ret)