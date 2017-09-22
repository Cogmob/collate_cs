#!/bin/zsh

python3 d_collate/_.py
cd after/bank
/cygdrive/c/Program\ Files/Mono/bin/csc /r:'C:\Users\lavery\.babun\cygwin\home\lavery\.useful\net-4.5\nunit.framework.dll' account_test.cs account.cs /target:library /out:out.dll | python3 ../../e_filter_test_runner_output/_.py
if [ $? -eq 0 ]
then
    /home/lavery/.useful/net-4.5/nunitlite-runner.exe 'out.dll' --noh --noresult | python3 ../../e_filter_test_runner_output/_.py
    if [ $? -eq 0 ]
    then
        print -P '    %F{green}pass%'
    fi
fi
