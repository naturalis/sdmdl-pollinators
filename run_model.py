from sdmdl.sdmdl_main import sdmdl

new_model = sdmdl('/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl')
new_model.prep()

new_model.train()

new_model.predict()

new_model.clean()