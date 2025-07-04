
import joblib
import os
import numpy as np

# SageMaker will call this to load the model
def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

# Optional: format request input
def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        data = eval(request_body)  # Or use json.loads if input is strictly JSON
        return np.array(data["features"]).reshape(1, -1)
    raise ValueError("Unsupported content type: {}".format(request_content_type))

# Optional: format prediction output
def output_fn(prediction, content_type):
    return str(prediction[0])
