#!/bin/zsh
source 'local.zsh'

python3 collate_cs before after 1
cd after

$csc /r:"$nunit_path" /target:library /out:out.dll bank\\account_test.cs bank\\account.cs UnityEngine\\MonoBehaviour.cs | python3 ../e_filter_test_runner_output/_.py

if [ $? -eq 0 ]
then
    # $nunit_runner 'out.dll' --noh --noresult | python3 ../e_filter_test_runner_output/_.py
    if [ $? -eq 0 ]
    then
        print -P '    %F{green}pass%'
    fi
fi
