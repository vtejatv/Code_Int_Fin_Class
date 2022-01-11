import shutil
import CONSTANTS


tmp_path = CONSTANTS.DROPBOX_PATH + 'tmp'
output_path = CONSTANTS.DROPBOX_PATH + 'output'

shutil.rmtree(tmp_path)
shutil.rmtree(output_path)