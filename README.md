
# Covid-19 Informer

**Covid-19 Informer** is a simple and interactive Python application that provides real-time statistics about Covid-19 cases from around the world using a graphical user interface (GUI). It fetches data from [Worldometers](https://www.worldometers.info/coronavirus/) and displays total cases, deaths, recoveries, and country-specific stats.

## Features

- Displays global Covid-19 statistics, including total cases, deaths, and recoveries.
- Provides country-specific statistics based on user input.
- Offers a help section for troubleshooting.
- Menu for additional information (e.g., available countries, app details, and help).
- Offline error handling for no internet connection.

## Requirements

- Python 3.x
- Tkinter library for the GUI.
- BeautifulSoup for web scraping.
- Requests for HTTP requests.
- Tkhtmlview for rendering HTML.

### Install Dependencies

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 tk html5lib tkhtmlview lxml
```

## How to Run

1. Download the project files and ensure that all dependencies are installed.
2. Place the following in the project directory:
   - **c19_app.py** (Main app file)
   - **/pics** (picture files for apps, like icons)
3. Run the main app file using the command:
   ```bash
   python c19_app.py
   ```
4. The GUI window will pop up, and you can start checking Covid-19 stats.

## Application Overview

### Main Features:

- **Check Stats by Country:**  
   Enter the name of any country, and the app will display the number of cases, recoveries, and deaths specific to that country.

- **Menu Bar Options:**
   - **Total Cases:** Provides global statistics on total cases, deaths, and recoveries.
   - **Information:** Includes details about the app, available countries, and a help section.
   - **Help:** Provides guidance for troubleshooting if issues arise, such as incorrect country names or lack of internet connection.

### Error Handling:
- **No Internet Connection:** If no internet connection is found, the app will alert the user and automatically close the window.
- **Incorrect Country Name:** If a country name is entered incorrectly, the app will notify the user.

## File Details

- **c19_app.py**: The main application file where the GUI and web scraping functionalities reside.
- **/pics** (picture files for apps, like icons)
- **bin directory**: contains files like help.txt and uninstall.txt to help with certain things.

### Debugging "Incorrect country name entered!":

If you are unable to find stats for some countries, check the "countries available" option under the information menu to get detailed info about the countries you could input. If the app doesn't work due to not having internet connection, make sure your device is connected to the internet.

For any other issues, feel free to contact us.

### Uninstall instructions:

To uninstall the app, simply delete the folder in which the app is stored.

## Contact
Author: [Mohammed Abdullah Amaan](mailto:abdullah@abdullahamaan.com)