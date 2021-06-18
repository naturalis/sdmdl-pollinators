# Model running
This folder contains Python scripts that were used to run the [SDMDL](https://github.com/naturalis/sdmdl)
python 
package. The SHAP.py script was created to bypass an error that occurred with 
the SHAP version used in SDMDL, where features contributed equally to the
model outcome. SHAP.py is a temporary workaround. We are working to resolve this
issue in the SDMDL package itself.

* [SHAP.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Model%20Running/SHAP.py) - Creates SHAP feature importance figures that were saved in numpy files after running the model in SDMDL
* [config_names.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Model%20Running/config_names.py) - Formats the species names and pathways to the occurrence data, so it fits the format needed in the SDMDL config.yml
* [run_model.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Model%20Running/run_model.py) - Creates a new deep learning model and runs the SDMDL package