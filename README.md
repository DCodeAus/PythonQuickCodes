# Python Quick Codes

A collection of small Python programs I wrote while learning: QR code makers, a web scraper, simple data programs and a few with windows (GUIs). Each one is short and commented, so they're good for reading and tweaking.

## What you need

- **Python 3.** On a Mac it's usually already there; check with `python3 --version`. Otherwise get it from [python.org](https://www.python.org/downloads/).
- **Some programs need extra packages**, listed in the table. Install them with `pip`, Python's package installer, for example `python3 -m pip install qrcode pillow`. (If you use [uv](https://docs.astral.sh/uv/), `uv run --with qrcode --with pillow python pictureQRCodeGenerator.py` installs and runs in one step.)

## How to run a program

1. Download this repository (green **Code** button › **Download ZIP**) and unzip it.
2. Open Terminal **in the `PythonQuickCodes` folder**. The programs read and write files next to themselves, so they need to be run from here:
   ```bash
   cd path/to/PythonQuickCodes
   ```
3. Run one with `python3` and its file name:
   ```bash
   python3 US_population_program.py
   ```

## The programs

| File | What it does | Extra packages |
|---|---|---|
| `QRCodeGenerator.py` | Makes a QR code for a web address and saves it as `myqr.png` and `myqr.svg`. Change the address on the `S = "www.google.com"` line. | `pyqrcode pypng` |
| `pictureQRCodeGenerator.py` | Makes a coloured QR code with a logo in the middle (`googlelogo.jpg`) and saves it as `QRCodeName.png`. Change the address with `url = ...` and the colour with `QRcolor = ...`. | `qrcode pillow` |
| `Webscraper.py` | Downloads a practice jobs page ([Real Python's fake jobs site](https://realpython.github.io/fake-jobs/)) and prints each job title, company and location. | `requests beautifulsoup4` |
| `US_population_program.py` | Reads US population figures from `USPopulation.txt` (one number per year, 1950 onwards) and prints the average yearly change and the years with the biggest and smallest increase. | none |
| `US_population_program_GUI.py` | The same, in a window. | none |
| `SalesTracker.py` | Asks how many staff there are and each person's sales, saves them to `sales_report.txt`, then reads them back with a total. | none |
| `SalesTrackerGUI.py` | The same, in a window. | none |
| `vehicle_console.py` | A menu for looking up, adding, changing and deleting cars, saved in `vehicles.dat`. | none |
| `vehicle_GUI.py` | The same, in a window. | none |
| `vehicle.py` | Not run directly: it defines the `Automobile` class (make, model ID, mileage, price) that the two vehicle programs use. | none |
| `PythonTurtleStopSign` | Draws stop-sign shapes with Python's built-in turtle graphics. It has no `.py` ending, so run it with `python3 PythonTurtleStopSign`. | none |

### Example: the population program

```
$ python3 US_population_program.py
The average annual change in population during the time period is 2,443.88
The year with the greatest increase in population was 1955
The year with the smallest increase in population was 1967
```

The figures in `USPopulation.txt` are in thousands.

## Notes

- The window programs use **tkinter**, which comes with Python. If you get `No module named '_tkinter'` on a Mac with Homebrew Python, install it with `brew install python-tk`.
- The vehicle programs save with Python's `pickle` format. Only open `.dat` files you made yourself: a pickle file from someone else can run code on your computer.
