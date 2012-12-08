#!/bin/sh
# -*- Mode: shell-script -*-
# Copyright (C) 2000 by Chmouel Boudjnah <chmouel@mandrakesoft.com>
# Redistribution of this file is permitted under the terms of the GNU 
# Public License (GPL)
## description: 

VERSION=$(sed -n 's/#define.*UTS_RELEASE.*\"\(.*mdk\)\"/\1/p' /usr/src/linux/include/linux/version.h)
[[ -z $VERSION ]] && VERSION=$(uname -r|sed 's/mdk.*$/mdk/')
echo $VERSION