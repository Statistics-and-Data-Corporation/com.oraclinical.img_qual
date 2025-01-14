import torch
from torchvision.transforms import functional as F
from PIL import Image
from scipy import ndimage
import numpy as np
import pathlib
import logging
import io

logger = logging.getLogger(__name__)


def load_model(model_path, device="cpu"):
    model = torch.load(model_path, map_location=torch.device(device))
    model.eval()
    return model


def estimate_blur(image):
    if image.mode != "L":
        image = image.convert("L")

    image = np.array(image).astype(float)
    blur_map = ndimage.laplace(image)
    score = np.var(blur_map)
    return score


def get_bounding_boxes(image, model, threshold=0.8):
    # Transform the image
    image_tensor = F.to_tensor(image).unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        predictions = model(image_tensor)

    # Extract bounding boxes and scores
    bounding_boxes = []
    scores = []

    for box, score in zip(predictions[0]["boxes"], predictions[0]["scores"]):
        if score >= threshold:
            bounding_boxes.append(box.tolist())
            scores.append(score.item())

    return bounding_boxes, scores


def crop_roi(image, bounding_box):
    bbx = tuple(int(x) for x in bounding_box[0])
    img = image.crop(bbx)
    return img


def process_image(file: bytes) -> tuple:
    cpath = pathlib.Path(__file__).parent.resolve()
    model_name = "eye_detector.pt"
    logger.info(f"Loading model from {cpath / model_name}")
    logger.info(f"Is CUDA Available: {torch.cuda.is_available()}")
    logger.info(f"Device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    model = load_model(
        cpath / model_name, "cuda" if torch.cuda.is_available() else "cpu"
    )

    image = Image.open(io.BytesIO(file)).convert("RGB")

    bounding_boxes, _ = get_bounding_boxes(image, model, threshold=0.8)
    if bounding_boxes == []:
        return 0, False

    img = crop_roi(image, bounding_boxes)

    score = estimate_blur(img)

    quality = True if score > 100 else False
    return score, quality