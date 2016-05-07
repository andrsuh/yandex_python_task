import sys
import os


def func(filename):
    BUFFER_SIZE = 1024 * 1024

    FROM = "From ".encode()
    # BUFFER_SIZE = 65536 * 2
    users_file = {None: open(os.devnull, 'wb', buffering=BUFFER_SIZE)}

    current_user = None

    for b_line in open(filename, "rb", buffering=BUFFER_SIZE):
        if b_line.startswith(FROM):
            users_email = b_line.split(b" ")[1]
            current_user = users_email

            if current_user not in users_file:
                users_file[current_user] = open(
                                            "users/" + current_user.decode(),
                                            "wb",
                                             buffering=BUFFER_SIZE
                                            )

        # if current_user:
        users_file[current_user].write(b_line)

    for file in users_file.values():
        file.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    func(sys.argv[1])

    # def func_1():
    #     for line in open("maxtest.mailbox", errors="ignore", buffering=BUFFER_SIZE):
    #         if line.startswith("From "):
    #             users_email = line.split(" ")[1]
    #             current_user = users_email
    #             # print(current_user)
    #
    #             if current_user not in users_file:
    #                 users_file[current_user] = open("users/" + current_user, "w", buffering=BUFFER_SIZE)
    #
    #         if current_user:
    #             users_file[current_user].write(line)
    #
    #     for file in users_file.values():
    #         file.close()
