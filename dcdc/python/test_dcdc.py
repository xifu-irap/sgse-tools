# ------------------------------------------------------------------------------------------------------------
#                            Copyright (C) 2024-2030 Ken-ji de la ROSA, IRAP Toulouse.
# ------------------------------------------------------------------------------------------------------------
#                            This file is part of the ATHENA X-IFU DRE Telemetry and Telecommand Firmware.
#
#                            dcdc-hk-fw is free software: you can redistribute it and/or modify
#                            it under the terms of the GNU General Public License as published by
#                            the Free Software Foundation, either version 3 of the License, or
#                            (at your option) any later version.
#
#                            This program is distributed in the hope that it will be useful,
#                            but WITHOUT ANY WARRANTY; without even the implied warranty of
#                            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#                            GNU General Public License for more details.
#
#                            You should have received a copy of the GNU General Public License
#                            along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------------------------------------
#    email                   kenji.delarosa@alten.com
#    @file                   test_dcdc.py
# -------------------------------------------------------------------------------------------------------------
#    Automatic Generation    No
#    Code Rules Reference    N/A
# -------------------------------------------------------------------------------------------------------------
#   @details
#
#   test: check the loading of the FPGA firmware.
#
# ------------------------------------------------------------------------------------------------------------

# Standard library
import sys
from pathlib import Path
import time
import argparse
import os

# get the script base path
script_base_path = str(Path(__file__).parents[0])

# custom library
from driver import DCDC


if __name__ == '__main__':

    ###########################################
    # parse command line
    ###########################################
    # user-defined: default firmware filepath (relative to this script path)
    default_firmware_filpath = "..\\..\\dcdc-fw_002.bit"

    parser = argparse.ArgumentParser(description='Define command line arguments')
    # add an optional argument with limited choices
    parser.add_argument('--firmware_filepath', '-f', default=default_firmware_filpath,
                        help='The firmware filepath can be absolute or relative to this script path.')

    args_known = parser. parse_known_args()
    # get arguments defined in this file.
    args = args_known[0]
    # get arguments not defined in this file in order to pass them to the called script.
    args_unknown = args_known[1]

    ###########################################
    # User-defined parameters
    ###########################################
    # path to the firmware
    firmware_filepath = args.firmware_filepath

    if os.path.isabs(firmware_filepath):
        # absolute path
        # print("absolute path: ",firmware_filepath)
        firmware_filepath = firmware_filepath
    else:
        # compute the absolute path relative to this script path
        # print("relative_path: ",firmware_filepath)
        firmware_filepath = str(Path(script_base_path,firmware_filepath).resolve())

    # level of verbosity
    verbosity = 2


    ###########################################
    # Start script
    ###########################################

    # Program the FPGA
    board = DCDC()
    board.open(firmware_filepath_p=firmware_filepath)

    board.set_verbosity(verbosity)

    # check internal error
    ###########################################
    board.display_subtitle("Check internal errors")
    error_internal_cnt = board.check_internal_errors()
    board.display("")
    ###########################################
    # summary
    ###########################################
    board.display_title("SUMMARY")

    # get HARDWARE_ID
    reg_name = 'HARDWARE_ID'
    msg = "DCDC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_hardware_id()

    msg = ""
    board.display(msg)

    # get the FIRMWARE_NAME
    reg_name = 'FIRMWARE_NAME'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_firmware_name()


    msg = " "
    board.display(msg)

    # get FIRMWARE_ID
    reg_name = 'FIRMWARE_ID'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_firmware_id()

    msg = " "
    board.display(msg)
