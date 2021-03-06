#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# This file is part of CoTeTo - a code generation tool
# 20170602 Joerg Raedler jraedler@udk-berlin.de
#

import os
import sys

# check if we are running in the development folder
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if os.path.isfile(os.path.join(parent, 'setup.py')):
    sys.path.insert(0, parent)

from CoTeTo.GUI import main
sys.exit(main())
