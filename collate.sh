#!/bin/zsh

python3 d_collate/_.py
cd after/bank
/cygdrive/c/Program\ Files/Mono/bin/csc account_test.csh /target:library
# cs account_test.csh /target:library

