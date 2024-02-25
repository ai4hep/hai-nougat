import sys,torch
from pathlib import Path
here = Path(__file__).parent.absolute()
sys.path.append(f'{here.parent.parent}')
from HaiNougat.apis import markdown_compatible, close_envs
from tqdm import tqdm

def inference_stream(dataloader, nougat_model, pages, compute_pages, batch):            
    
    predictions = [""] * len(pages)
    with torch.no_grad():
        for idx, sample in tqdm(enumerate(dataloader), total=len(dataloader)):
            if sample is None:
                continue
            model_output = nougat_model.inference(image_tensors=sample)
            
            for j, output in enumerate(model_output["predictions"]):
                if model_output["repeats"][j] is not None:
                    if model_output["repeats"][j] > 0:
                        disclaimer = "\n\n+++ ==WARNING: Truncated because of repetitions==\n%s\n+++\n\n"
                    else:
                        disclaimer = (
                            "\n\n+++ ==ERROR: No output for this page==\n%s\n+++\n\n"
                        )
                    rest = close_envs(model_output["repetitions"][j]).strip()
                    if len(rest) > 0:
                        disclaimer = disclaimer % rest
                    else:
                        disclaimer = ""
                else:
                    disclaimer = ""
                
                predictions[pages.index(compute_pages[idx * batch + j])] = (
                    markdown_compatible(output) + disclaimer
                )
            
            yield "".join(predictions).strip()
            predictions = [""] * len(pages)
        torch.cuda.empty_cache()

def inference_no_stream(dataloader, nougat_model, pages, compute_pages, batch):            
    predictions = [""] * len(pages)
    with torch.no_grad():
        for idx, sample in tqdm(enumerate(dataloader), total=len(dataloader)):
            if sample is None:
                continue
            model_output = nougat_model.inference(image_tensors=sample)
            
            for j, output in enumerate(model_output["predictions"]):
                if model_output["repeats"][j] is not None:
                    if model_output["repeats"][j] > 0:
                        disclaimer = "\n\n+++ ==WARNING: Truncated because of repetitions==\n%s\n+++\n\n"
                    else:
                        disclaimer = (
                            "\n\n+++ ==ERROR: No output for this page==\n%s\n+++\n\n"
                        )
                    rest = close_envs(model_output["repetitions"][j]).strip()
                    if len(rest) > 0:
                        disclaimer = disclaimer % rest
                    else:
                        disclaimer = ""
                else:
                    disclaimer = ""
                
                predictions[pages.index(compute_pages[idx * batch + j])] = (
                    markdown_compatible(output) + disclaimer
                )
        
    final = "".join(predictions).strip()
    torch.cuda.empty_cache()
    return final