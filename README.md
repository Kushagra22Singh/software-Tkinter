# SOFTWARE

This repository contains a Python application developed using various libraries for graphical user interfaces, data visualization, and database interactions. The project includes functionalities such as admin settings, user authentication, order reviews, and graphical analytics.

## Features

- User-friendly GUI created with Tkinter.
- Admin functionalities for reviewing ratings, order history, and payment details.
- Visualization of ratings and order analytics using Matplotlib.
- Integration with MySQL for data storage and retrieval.
- Support for various payment methods (UPI, Card, and Cash on Delivery).
- Discount and promotional code application for payments.
- Order tracking with a visual map simulation.

## Installation and Setup

### Prerequisites

Ensure the following are installed on your system:

1. Python 3.x
2. MySQL Server
3. Required Python libraries (listed in `requirements.txt`).

### Installation Steps

1. **Fork and Clone the Repository**  
   Fork this repository to your GitHub account, then clone it to your local machine:
   ```bash
   git clone https://github.com/<your-username>/SOFTWARE.git
   cd SOFTWARE
   ```

2. **Install Dependencies**  
   Use `pip` to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**  
   - Create a MySQL database named `trial`.
   - Import the provided database schema (if available in the repository) to set up necessary tables:
     ```sql
     mysql -u root -p trial < schema.sql
     ```
   - Update the database connection parameters in the script (`host`, `user`, `passwd`, and `database`) if they differ from the default.

4. **Run the Application**  
   Execute the Python script to start the application:
   ```bash
   python SOFTWARE.py
   ```

### Directory Structure

```
SOFTWARE/
├── SOFTWARE.py            # Main application script
├── requirements.txt       # List of dependencies
├── schema.sql             # Database schema (if provided)
├── README.md              # Project documentation
└── assets/                # Images and resources for the GUI
```

### Requirements File Example

Ensure the following dependencies are listed in your `requirements.txt`:

```
pygame
pillow
geopy
mysql-connector-python
prettytable
numpy
matplotlib
```

## Usage

1. Launch the application and follow the GUI prompts.
2. Use the "Admin Settings" section for administrative tasks like reviewing ratings and order history.
3. To track orders, ensure that the map resources are correctly placed in the `assets/` directory.

## Notes

- Ensure all image paths in the script are updated to reflect the correct location in the `assets/` directory.
- If errors occur during database operations, check the database schema and the connection credentials.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
