#!/usr/bin/env python3

import datetime
import glob
import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s %(message)s")
cur_dir = "/home/srijan/Downloads"

movies_dir = cur_dir + "/movies"
music_dir = cur_dir + "/music"
document_dir = cur_dir + "/documents"
image_dir = cur_dir + "/images"
code_dir = cur_dir + "/code"
zip_dir = cur_dir + "/zip"

dir_map = {
    movies_dir: ["./*.avi", "./*.m4v", "./*3gp", "./*mpeg-2", "./*mpeg4"],
    music_dir: ["./*.mp3", "./*.wav"],
    image_dir: ["*.jpeg", "*.jpg", "*.gif"],
    document_dir: ["*.pdf", "*.doc", "*.docx", "*.PDF", "*.xlsx"],
    code_dir: ["*.py", "*.java", "*.sh", "*.c", "*.js", "*.csv", "*.html"],
    zip_dir: ["*.zip", "*.rar", "*.gz", "*.7z"]
}


def create_required_directory():
    print("Hello")
    logging.debug("Current Directory is: {} ".format(os.getcwd()))
    os.chdir(cur_dir)
    logging.debug("Current Directory is: {} ".format(os.getcwd()))

    for dir_name in dir_map:
        logging.debug(dir_name)

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            logging.debug("Created Music Directory")


def dest_file_name(file, dest_dir):
    file_name = file.replace(cur_dir, "")
    logging.debug("Only File Name: {} ".format(file_name))

    dest_file_name = dest_dir + file_name
    if not os.path.isfile(dest_file_name):
        return ""

    counter = 0

    while os.path.isfile(dest_file_name):
        logging.debug("Am i here")
        index = file_name.rfind(".")
        name = file_name[:index]
        extension = file_name[index:]
        new_file_name = name + "(" + str(counter) + ")" + extension
        dest_file_name = dest_dir + new_file_name

    logging.debug("Your File Name is {} ".format(new_file_name))
    return new_file_name


def move_all_files():
    for dest_dir, extensions in dir_map.items():
        for extension in extensions:
            files = glob.iglob(os.path.join(cur_dir, extension))

            for file in files:
                if os.path.isfile(file):
                    try:
                        dest_filename = dest_file_name(file, dest_dir)
                        actual_dest_dir = ""

                        if not dest_filename == "":
                            actual_dest_dir = dest_dir + "/" + dest_filename
                        else:
                            actual_dest_dir = dest_dir

                        logging.debug("Copying {} to {}".format(file, actual_dest_dir))
                        shutil.move(file, actual_dest_dir)
                    except shutil.Error:
                        logging.debug("There is already a file with the filename {}".format(file))


def move_files():
    logging.debug("Start of Move file on {} ".format(datetime.datetime.now()))
    create_required_directory()
    move_all_files()


move_files()
