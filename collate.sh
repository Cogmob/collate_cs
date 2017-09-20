#!/bin/zsh

python3 d_collate/_.py
cd after/bank
/cygdrive/c/Program\ Files/Mono/bin/csc /r:'C:\Users\lavery\.babun\cygwin\home\lavery\.useful\net-4.5\nunit.framework.dll' account_test.cs account.cs /target:library |
# /home/lavery/.useful/net-4.5/nunitlite-runner.exe after/bank/account_test.dll
/home/lavery/.useful/net-4.5/nunitlite-runner.exe 'C:\Users\lavery\.babun\cygwin\home\lavery\net\after\bank\account_test.dll' --noh --noresult | python3 ../../d_collate/process.py
