import os
import site


MODULE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
source_dir = os.path.join(MODULE_DIR_PATH, "..", "src")
site.addsitedir(source_dir)