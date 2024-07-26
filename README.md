
# Password Checker

This Python script checks a list of passwords against the Aries Online API to see if they have been pwned. The results are printed to the console with color-coded messages and saved to a text file with the current date.

## Features

- Reads passwords from a text file.
- Checks each password against the Aries Online API.
- Color-coded output for easy readability:
  - Red: Password found and has been used.
  - Yellow: Error in the API response.
  - Green: Password not found in the database.
- Saves the results to `checked.txt` with the current date.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/password-checker.git
    cd password-checker
    ```

2. Install the required libraries:
    ```bash
    pip install requests colorama
    ```

## Usage

1. Create a `passwords.txt` file in the same directory as the script. Add one password per line.

2. Run the script:
    ```bash
    python check_passwords.py
    ```

3. The results will be displayed in the terminal with color-coded messages and saved to `checked.txt` with the current date.

## Example Output

### Terminal Output
```
Password: admin - Found: True - Used Times: 5453
Password: password123 - Not found in database
Password: letmein - Error: No password provided.
```

### `checked.txt` Content
```
2024-07-26 - Password: admin - Found: True - Used Times: 5453
2024-07-26 - Password: password123 - Not found in database
2024-07-26 - Password: letmein - Error: No password provided.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Acknowledgements

- [Aries Online API](https://api.api-aries.online)
- [Colorama Library](https://pypi.org/project/colorama/)

## Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/password-checker](https://github.com/yourusername/password-checker)
