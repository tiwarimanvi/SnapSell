# SnapSell

SnapSell is an online marketplace built on Django, providing a platform for users to buy and sell products. The project includes both frontend and backend components, all developed using the Django web framework.

## Features

- **Buy and Sell Products:** Users can browse a variety of products listed on the platform. Sellers can upload details about their products, including images, descriptions, and prices.

- **Conversation Feature:** Buyers and sellers can engage in conversations about products. This allows for better communication and negotiation before a purchase is made.

- **Seller Dashboard:** Sellers have access to a personalized dashboard where they can view and manage the items they have uploaded. This includes the ability to edit details or delete items.

- **User Authentication:** The application supports user authentication with login and signup functionalities. This ensures a secure and personalized experience for users.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tiwarimanvi/SnapSell.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000/`.

## Usage

1. Visit the site: `http://localhost:8000/`

2. Sign up for a new account or log in if you already have one.

3. Explore the marketplace, buy and sell products, and engage in conversations with other users.

4. Sellers can access their dashboard to manage their listed items.

## Contributing

If you'd like to contribute to SnapSell, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

