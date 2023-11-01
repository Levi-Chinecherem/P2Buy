# P2Buy - Community E-Commerce Platform

P2Buy is a unique community-based e-commerce platform where consumers come together to purchase products in bulk, enabling cost savings and convenient delivery. This README provides an overview of the project structure and key features.

## Table of Contents

- [Screenshots](#screenshots)
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Screenshots

Here are some sample screenshots of the application:

![Screenshot 1](https://github.com/Levi-Chinecherem/Fitness-and-Health-Tip-Tutoring/blob/main/sample%20outputs/p1.png)

![Screenshot 2](https://github.com/Levi-Chinecherem/Fitness-and-Health-Tip-Tutoring/blob/main/sample%20outputs/p4.png)

![Screenshot 3](https://github.com/Levi-Chinecherem/Fitness-and-Health-Tip-Tutoring/blob/main/sample%20outputs/p3.png)

## Project Description

P2Buy is designed to bring everyday consumers together for collective product purchases. The platform offers a wide range of features to enhance the shopping experience, including product group management, favorites, purchase tracking, user feedback, notifications, and product recommendations.

## Features

### Accounts

- User registration, login, and profile management.
- Password reset and change functionality.
- User-specific forms for updating profiles.

### Dashboard

- Product tracking from grouping to delivery.
- Favorites management.
- Purchase group monitoring with completion status.
- Detailed purchase history with group information.
- Group status transitions: open, order_processing, closed, received.

### Products

- View product listings and categories.
- Add products to purchase groups.
- Add products to favorites.
- Update products within groups.
- Checkout and payment for grouped products.

### Notifications

- Email notifications for order updates.
- Notify users about group changes and relevant updates.

### Payments

- Secure and reliable payment gateway integration.
- Facilitate payments for grouped products.

### Feedback

- User feedback collection through contact and feedback forms.
- Report issues for continuous improvement.

### Recommendations

- Product recommendation system based on user preferences and purchase history.

## Installation

1. Clone the project repository:
   ```shell
   git clone https://github.com/Levi-Chinecherem/p2buy.git

2. Navigate to the project directory:

   ```shell
   cd p2buy
   ```
3. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```
4. Configure your project settings, including database and email settings.
5. Run migrations to create the database schema:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser account for admin access:

   ```shell
   python manage.py createsuperuser
   ```
7. Start the development server:

   ```shell
   python manage.py runserver
   ```
8. Access the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage project data.

## Usage

- Navigate to [http://localhost:8000/](http://localhost:8000/) to access the P2Buy platform.
- Use the navigation links in the header to explore different features:
  - Product List
  - Favorites
  - Profile (if authenticated)
- Add products to groups, manage favorites, and make payments for grouped products.
- Use the dashboard to track purchases and view product recommendations.

## Contributing

Contributions to P2Buy are welcome! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that tests pass.
4. Commit your changes and push them to your fork.
5. Create a pull request in the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
