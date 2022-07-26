# Copyright 2022 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dataclasses
import json


@dataclasses.dataclass
class CPRConfig(object):
    """Configure the build process by editing the default values here.

    config_file: File path used to save values in this config. (Some
      values, such as the model name, are generated at build time and
      depended on by future steps, so saving it allows this script to
      deploy the model without re-uploading it, for example.)

    base_image: Base Docker image on top of which the model server will
      be built. By default, a Debian-based Python 3 image without GPU
      support will be used.

    image: Name and tag assigned to the built model server image.

    artifact_local_dir: Local directory where a copy of the pretrained model weights
      will be saved.

    region: Google Cloud Region where the model will be uploaded during the
      build process.

    project_id: Google Cloud project ID.

    repository: Name of the Artifact Registry repository where the container
      will be uploaded.

    artifact_gcs_dir: Location on GCS where a copy of the pretrained model
      weights will be uploaded.

    model_name: Full resource path of the uploaded model. This is a write-only
      field, the value is generated by Vertex AI when the model is uploaded.

    endpoint_name: Full resource path of the created endpoint. This is a
      write-only field, the value is generated by Vertex AI when the model is
      deployed to an endpoint.

    machine_type: Machine type to use when deploying the model.
    """

    config_file: str = "config.json"
    base_image: str = "python:3.10-bullseye"
    image: str = "timm_predictor:latest"
    artifact_local_dir: str = ""
    region: str = "us-central1"
    project_id: str = "samthrasher-experimental"
    repository: str = "cpr-images"
    artifact_gcs_dir: str = "gs://samthrasher-cpr-example/timm-vit224/"
    model_name: str = ""
    endpoint_name: str = ""
    machine_type: str = "n1-standard-2"

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(dataclasses.asdict(self), f, indent=2)

    def load(self):
        with open(self.config_file) as f:
            self.__init__(**json.load(f))