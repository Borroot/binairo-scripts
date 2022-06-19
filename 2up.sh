#!/usr/bin/env bash
# AUTHOR: Borroot

# Provide a pdf file which should be turned into a booklet
pdfjam --a4paper --booklet true --suffix final --landscape "$1"
