import sys

BUFFER_SIZE = 2 ** 20
FROM = "From ".encode()

users_file = {}


def process(filename):
    current_user = None
    fld = "users/"

    for b_line in open(filename, "rb", buffering=BUFFER_SIZE):
        if b_line.startswith(FROM):
            users_email = b_line.split(b" ")[1]
            current_user = users_email

            if current_user not in users_file:
                users_file[current_user] = open(fld + current_user.decode(),
                                                "wb",
                                                buffering=BUFFER_SIZE)

        if current_user:
            users_file[current_user].write(b_line)

    for file in users_file.values():
        file.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("filename is not define")
        exit(1)
    process(sys.argv[1])
