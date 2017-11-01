#!/bin/zsh

python3 d_collate/_.py
cd after

/cygdrive/c/Windows/Microsoft.NET/Framework64/v3.5/csc.exe /r:'C:\Users\lukea\.babun\cygwin\home\.useful\net-3.5\nunit.framework.dll' /target:library /out:out.dll bank\\account_test.cs bank\\account.cs UnityEngine\\MonoBehaviour.cs | python3 ../e_filter_test_runner_output/_.py

if [ $? -eq 0 ]
then
    /home/.useful/net-3.5/nunitlite-runner.exe 'out.dll' --noh --noresult | python3 ../e_filter_test_runner_output/_.py
    if [ $? -eq 0 ]
    then
        print -P '    %F{green}pass%'
    fi
fi
