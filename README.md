# Thunderbird Index CSV Formatter

This simple python program formats exported CSV index files from Thunderbird to include only the email name and email address of the sender in the correct format for importing it into another program, like a email campaign service.

## Installation Instructions

### Step 1: Install ImportExportTools NG in Thunderbird

- Open Thunderbird, then click on the settings icon in the bottom left.
- Click on "Add-ons and Themes" next to the settings icon.
- In the search bar near the top middle of your screen, type "ImportExportTools NG".
- Click on the green icon next to ImportExportTools NG that says "+ Add to Thunderbird".
- Click "Add" to install your ImportExportTools.

### Step 2: Download the Formatting Program

- Download the program from [this link](https://github.com/Odus007/thunderbird-index-formatter/archive/refs/heads/main.zip).
- Unzip the file and remember where you placed it for later use.

## Usage Instructions

Ensure you have exported a CSV index file from your email before running this program.

### Exporting Index Using ImportExportTools NG in Thunderbird

- Select the email(s) you want the index of. Use `Ctrl + A` to select all. Another way is `Ctrl + Click` to select one, and then `Ctrl + Shift + Click` to select a range.
- Right-click on any selected email to bring up a menu.
- Click "Export Message As..." at the bottom of the menu, then select "Message Index".
- Choose between HTML and CSV formats. Select "CSV format".
- Choose a location to save the exported index and remember it.

### Formatting the CSV with Thunderbird Index Formatter

- Place the CSV file from ImportExportTools into the `place_csv_files_here` folder in the thunderbird-index-formatter folder you unzipped.
- Run `run-index-formatter.exe` (not the `index_formatter.py` file).
- Your CSV file is now correctly formatted and ready to be moved to a different folder if desired. <br>
<b> Happy email spamming :) </b>
