#!/bin/bash

# run as root

if [[ $1 == "-add" ]]; then
    for user in $(cut -f1 -d: /etc/passwd); do
        mkdir /tmp/$user
        crontab -l -u $user >/tmp/$user/cron_export
        awk '$0="#"$0' /tmp/$user/cron_export >/tmp/$user/cron_comment
        crontab -r -u $user
        crontab -u $user /tmp/$user/cron_comment
        rm -rf /tmp/$user
    done
elif [[ $1 == "-remove" ]]; then
    for user in $(cut -f1 -d: /etc/passwd); do
        mkdir /tmp/$user
        crontab -l -u $user >/tmp/$user/cron_export
        awk '{ print substr($0,2) }' /tmp/$user/cron_export >/tmp/$user/cront_uncomment
        crontab -r -u $user
        crontab -u $user /tmp/$user/cront_uncomment
        rm -rf /tmp/$user
    done
else
    echo "no option was selected. Please use -add to add comments or -remove to remove comments"
fi
