# SPDX-License-Identifier: GPL-2.0
#
# vim: set ts=8 sw=8 noet tw=80 cc=80 fo+=t :

import logging
import jupiter.core.logging as logg
from modules.credentials.module import cred
from jupiter.core.module import cli

logger = logging.getLogger(__name__)


def main():
    # init the logging feature
    logg.init_logging()

    # ----------- REGISTERING SUB-COMMANDS/GROUPS ---------

    # launch the command line
    cli()


if __name__ == "__main__":
    main()
