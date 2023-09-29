# InGamePanel

The aim of this project is to streamline the creation of InGamePanels for Microsoft Flight Simulator 2020. After modifying the 'Scripts.py' file with the project's Name, Creator, and the title of the window to be displayed, the project will automatically incorporate this information and launch Microsoft Flight Simulator 2020 to build the project, generating the '.spb' file. The project will be ready for export to Microsoft Flight Simulator 2020.

# Requirements

* [NodeJS](https://nodejs.org/dist/v20.7.0/node-v20.7.0-x64.msi)
* [Python](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)

# How to use

1. Open the `Scripts.py` file and modify the following information: `{project-name}`, `{project-creator}`, and `{project-title}` where:
   - `{project-name}`: Name of the package to be exported to Microsoft Flight Simulator (e.g. `toolbar-pushback`)
   - `{project-creator}`: Developer/company name (e.g. `Helbert`, `SkyX Simulations`)
   - `{project-title}`: Title of the addon window (e.g. `Toolbar Pushback`)
2. Save the file.
3. Double-click to execute the script.
4. If the script does not execute upon double-clicking, open the Windows terminal (e.g. `CMD`) and enter the following command:
```python
python Scripts.py
```
5. You just need to change the `MyPanel.html`, `MyPanel.css` and, `MyPanel.js` on the `Community/html_ui/InGamePanels/` folder

# How to test

1. Copy the folder inside `Community` folder to the `Community` folder from `Microsoft Flight Simulator 2020`
2. Open the `Microsoft Flight Simulator 2020`.