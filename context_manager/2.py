# TODO use a context manager to open log.txt and print only the ERROR lines

with open("log.txt", "w") as log_file:
    log_file.write(
        "2024-03-10 09:12:01 INFO User login: alice\n"
        "2024-03-10 09:13:45 ERROR Failed to read config file\n"
        "2024-03-10 09:14:02 INFO Server started on port 8080\n"
        "2024-03-10 09:15:30 INFO Cache cleared\n"
        "2024-03-10 09:16:11 ERROR Database connection timed out\n"
        "2024-03-10 09:17:05 INFO Backup completed\n"
        "2024-03-10 09:18:42 ERROR Unhandled exception in payment\n"
        "2024-03-10 09:19:00 INFO User login: bob\n"
        "2024-03-10 09:20:15 INFO Scheduled job completed\n"
        "2024-03-10 09:21:33 ERROR Service health check failed\n")

with open("log.txt", "r") as log_file:
    for lines in log_file:
        if "ERROR" in lines:
            print(lines.strip())
