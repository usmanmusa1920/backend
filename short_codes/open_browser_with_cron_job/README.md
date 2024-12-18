# Cron-Job to open web-browser

Now, set up your cron job by running:

```sh
crontab -e
```

Add the cron job, that will run at 8am of everyday:

```sh
0 8 * * * /home/usman/Desktop/open_browser_with_cron_job/open_browser.sh >> /path/to/logfile.log 2>&1
```

The `>> /path/to/logfile.log 2>&1` will log the output and any errors, which can help with debugging. You can check this log file later to see if there are any errors during execution.

Ensure the bash script is executable:

```sh
chmod +x /home/usman/Desktop/open_browser_with_cron_job/open_browser.sh
```

You can test the script manually first by running:

```sh
/home/usman/Desktop/open_browser_with_cron_job/open_browser.sh
```

If this works manually but fails in cron, then the issue is likely with the environment settings in cron, which the display setting should fix.

For debugging Cron Jobs. If it still doesn't work, check the cron job logs for any errors:

```sh
grep CRON /var/log/syslog
```

This will show any captured errors.


```sh
#!/bin/bash

echo "How to chnage the mode of everything within the `.ssh` directory"

#            ┌───────────── u (owner)
#            │ ┌───────────── g (group)
#            │ │ ┌───────────── o (other)
#            │ │ │
#            │ │ │
# sudo chmod 7 7 7 ~/.ssh/


###### How to apply file permission

#            ┌───────────── r (read)
#            │ ┌───────────── w (write)
#            │ │ ┌───────────── x (execute)
#            │ │ │
#            │ │ │
#            4 2 1 ~/.ssh/


#      4 + 2   ────────   6   r + w (read + write)
#      4 + 1   ────────   5   r + e (read + execute)
#      2 + 1   ────────   3   w + e (write + execute)


echo "How to set cronjob task"

# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                       7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command_to_execute


###### Sample crontab ######

# Empty temp folder every Friday at 5pm
0 5 * * 5 rm -rf /tmp/*

# Backup images to Google Drive every night at midnight
0 0 * * * rsync -a ~/Pictures/ ~/Google\ Drive/Pictures/
```
