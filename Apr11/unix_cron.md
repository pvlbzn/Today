####cron

Cron is a time-based job scheduler utility in Unix-like OS.

**Configuration syntax**:

```
0-59	0-23	1-31	1-12	0-6				command
min		hour	day		month	day of week		command to execute
```

Run once a day at midnight: `0 0 * * *`

**Schedule**:
Most convinient way for me was to create a `.crontab` dotfile, and give it to the cron.

```
crontab ~/.crontab
crontab -l
> list of crons
```

Simple and handy!
