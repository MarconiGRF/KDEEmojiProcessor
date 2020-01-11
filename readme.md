# KDE Emoticon to Emoji Processor

## Overview
This is Python 3 a script to enable Emoji support on KDE Plasma < 5.17 desktop environment.

Based on [Unicode's Full Emoji List page](http://www.unicode.org/emoji/charts/full-emoji-list.html), it will generate the PNGs and correct names for the full list of emojis using the Emoji's name and Base64 Hash to generate every file and place them into correct KDE Emoticon path.

## Usage
- ### 1 - Clone this repository to **your home path**:
    ```
    git clone https://github.com/MarconiGRF/KDEEmojiProcessor
    ```

- ### 2 - Make sure that you have Python 3 installed on your linux distribution:    
    ```
    python3 -V
    ```
    If your output was Python 3.7  or higher, you're good to go.

- ### 3 - Install pathlib through pip:
    ```
    pip3 install pathlib
    ```

- ### 4 - Get Unicode Data
    - #### 4.1 - Access the [Unicode's Full Emoji List page](http://www.unicode.org/emoji/charts/full-emoji-list.html), load the entire page (it takes a while, there are around 1700 emoji rows and the HTML file has ~27MB).
    - #### 4.2 - When finished loading the page, open the HTML source code, copy the entire `<table>` element, save into the repo's directory as `unicodeEmojis.html`

- ### 5 - Run the script and watch magic happen.
    ```
    python3 KDEEmojiProcessor.py
    ```

- ### 6 - Select Emoji theme on KDE's Emoticons Application
    - #### 6.1 - If everything runs OK, open KDE's Emoticon Theme Chooser
    - #### 6.2 - From the shown list, select iOS theme, apply then click OK to close.
    - #### 6.3 - Reboot your system and now it will have support to Emoticons to be shown Emojis.
