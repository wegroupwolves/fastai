import torch
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms
solar_panel_model = torch.load("/home/lander/Documents/Work/WeGroup/wg-be-api-house-properties/wg_be_api_house_properties/ml_models/pytorch_model_solar_panels", map_location="cpu")
