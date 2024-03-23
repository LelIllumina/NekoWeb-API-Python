# Nekoweb API Python Wrapper

Basic API Wrapper for the [Nekoweb API](https://nekoweb.org/api). More functionality to be added.

## Features

- **File Creation**: Create new files or folders on Nekoweb.
- **Site Information**: Retrieve information about a Nekoweb site, including creation and update timestamps.
- **Folder Reading**: Read the contents of a folder on Nekoweb.
- **File Deletion**: Delete files or folders from Nekoweb.

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository:
```shell
git clone https://github.com/LelIllumina/NekoWeb-API-Python.git
```

2. Navigate to the project directory:
```shell
cd Nekoweb-api-python
```

3. Install the required Python libraries:
```shell
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory with your NekoWeb API key:
```env filename=".env"
NEKOWEB_API_KEY=your_api_key_here
```
## Usage

Run main.py and follow the prompts.
```shell
python3 main.py
```

## TODO

- [ ] Add Functionality for all endpoints.
- [ ] Cleaner output and error handling.
- [x] Main.py to access each API endpoint from running one file.
- [ ] Take arguments without running file.

## Contributing

Contributions are welcome! Please fix my awful code if you want :3

## Acknowledgments

- NekoWeb for providing the API.
- [Nekoapi](https://nekoapi.nekoweb.org/) by [Fairfruit](https://fairfruit.nekoweb.org/)
- The Python community for the libraries