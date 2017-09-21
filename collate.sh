#!/bin/zsh

python3 d_collate/_.py
cd after/bank
/cygdrive/c/Program\ Files/Mono/bin/csc /r:'C:\Users\lavery\.babun\cygwin\home\lavery\.useful\net-4.5\nunit.framework.dll' account_test.cs account.cs /target:library | python3 ../../e_filter_test_runner_output/_.py
if [ $? -eq 0 ]
then
    echo "it worked"
else
    echo "it failed"
fi
# /home/lavery/.useful/net-4.5/nunitlite-runner.exe after/bank/account_test.dll
# /home/lavery/.useful/net-4.5/nunitlite-runner.exe 'C:\Users\lavery\.babun\cygwin\home\lavery\net\after\bank\account_test.dll' --noh --noresult | python3 ../../e_filter_test_runner_output/_.py
