from multiprocessing import Pool
import time
import sys
import bcrypt


def hash_password(password):
    print(password, bcrypt.hashpw(password, bcrypt.gensalt()))


if __name__ == '__main__':
    parallelism = sys.argv[1:2] == ['-p']
    passwords = [b'password1', b'password2', b'password3', b'password4', b'password5',
                 b'password6', b'password7', b'password8', b'password9', b'password10',
                 b'password11', b'password12', b'password13', b'password14', b'password15',
                 b'password16', b'password17', b'password18', b'password19', b'password20']
    start_time = time.time()
    if parallelism:
        p = Pool()
        p.map(hash_password, passwords)
    else:
        for password in passwords:
            hash_password(password)

    end_time = time.time()

    print('-' * 90)
    print(f"Results(parallelism is {'on' if parallelism else 'off'}): {end_time-start_time}s")
