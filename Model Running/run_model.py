from sdmdl.sdmdl_main import sdmdl
# Import the SDMDL python package

# Create a new Model (Enter the root to your repository here)
new_model = sdmdl('/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl')

# Model preparation
new_model.prep()

# Model training
new_model.train()

# Model testing
new_model.predict()

# Cleaning up unnecessary data
new_model.clean()
