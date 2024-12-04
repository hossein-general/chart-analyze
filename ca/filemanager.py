# importings
import os
from typing import List


# The FileManager class is responsible for moving files and renaming them
# the main purpose could be getting the directory where the charts are put by user and creating a copy of them within the resources/photos/charts directory for further analyzes
class FileManager:
    # getting the chart_dir folder directory so it could put picture of file to be converted there
    def __init__(self, charts_dir: str):
        self.charts_dir = charts_dir

    def transfer_files(self, directory: str):
        """
        getting a directory address, and moving all applicable pictures from there to the charts_dir directory
        """

        # a list of supported file extensions
        supported_files = (".png", ".jpg")

        # list of supported file types
        dir_files = os.listdir(directory)

        # listing the files
        for file in reversed(dir_files):
            if not file.endswith(supported_files):
                dir_files.remove(file)

        # getting the list of already used file names to prevent duplication or overwriting
        used_names = self.get_used_names()

        # moving each file included in the valid file list
        for file in enumerate(dir_files):
            os.rename(file, r"resources/Photos/charts/test2.png")

    def get_used_names(self, directory: str, file_extensions: List[str]):
        """
        returning a list of all files with the specified file extension within the directory
        """

        # list of supported file types
        dir_files = os.listdir(directory)

        # matching the file extensions
        for file in reversed(dir_files):
            if not file.endswith(file_extensions):
                dir_files.remove(file)


def main():
    print("program start (for testing)")
    FileManager.transfer_files(r"resources/Photos/charts")


if __name__ == "__main__":
    main()
