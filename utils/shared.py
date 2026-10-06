# SPDX-License-Identifier: GPL-2.0
#
# vim: set ts=8 sw=8 noet tw=80 cc=80 fo+=t :

import os

PROJECT_NAME = "jupiter"
DEBUG_MODE = os.environ.get("DEBUG", "0") == "1"
CONFIG_DIR = os.environ.get("CONFIG_DIR", "./configs/")

# =====================
# DIRECTORIES AND FILES
# =====================

# jupiter init file
# TODO: /var/log/jupiter.log
CONFIG_FILE_INIT = CONFIG_DIR + "jupiter.ini"

# =======
# LOGGING
# =======
DEFAULT_CONSOLE_LOG_LEVEL = "INFO"
DEFAULT_CONSOLE_LOG_COLORED_OUT = True
DEFAULT_CONSOLE_LOG_TIMESTAMP = False
DEFAULT_FILE_LOG_LEVEL = "INFO"
DEFAULT_LOG_FILE_PATHNAME = PROJECT_NAME + ".log"
DEFAULT_FILE_LOG_TIMESTAMP = True
FORMAT_OUTPUT_BOLD = False

# ====
# USER
# ====
# Informational messages
INFO_OUTPUT_COLOR = "cyan"
INFO_ENABLE_NL = False  # new line after each message print
INFO_OUTPUT_BOLD = False
INFO_PREFIX = "---| "
# Errors messages
ERROR_OUTPUT_COLOR = "red"
ERROR_ENABLE_NL = False
ERROR_OUTPUT_BOLD = False
ERROR_PREFIX = "[ ERROR ] "
