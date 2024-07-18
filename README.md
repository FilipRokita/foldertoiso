# FolderToISO

This Python script `foldertoiso.py` converts a specified folder into an ISO file using the `shutil` library. Here's a brief overview of its functionality and usage:

## Usage

To convert a folder to an ISO file, run the script with two command-line arguments:

1. `<path to folder>`: Path to the folder you want to convert.
2. `<path to iso>`: Desired path and filename of the resulting ISO file (without the .iso extension).

## Example

```
python3 foldertoiso.py example_folder/ example_iso
```

## Requirements

- Python 3.x
- `shutil` library (standard library in Python)

## How It Works

1. The script compresses the specified folder into a ZIP archive using shutil.make_archive.
2. It then renames the ZIP archive with a .iso extension to simulate an ISO file.
3. Finally, it notifies the user of the successful conversion or prints an error message if any issues occur.

## Notes

- Ensure that the folder you specify exists and the paths are correct.
- The resulting file is a ZIP archive renamed with a .iso extension, not a true ISO 9660 image.

## Legal

This program is provided as-is, without warranties or conditions of any kind, either express or implied. By using this program, you agree that the author is not responsible for any damage that may occur as a result of its use.

## License

This script is released under the MIT License. See [LICENSE](./LICENSE) file for more details.

## Author

Filip Rokita  
Website: [www.filiprokita.com](https://www.filiprokita.com/)
