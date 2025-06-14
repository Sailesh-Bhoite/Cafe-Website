Bhoite's Cafe Website
☕ An E-commerce Platform for Cafes
This project is a comprehensive full-stack e-commerce website designed for a cafe, allowing customers to browse a menu, add items to a shopping cart, place orders, and generate bills. It also includes an analytics dashboard to track top-selling items.

✨ Features
Interactive Menu Display: Browse food and drink items categorized for easy navigation.

Customer Authentication: Secure user login functionality using a custom Customer model.

Dynamic Shopping Cart: Add multiple items and specify quantities. Cart details (item name, quantity, price, item total) are managed in the user's session.

Seamless Order Placement: Finalize and place orders, with all selected items and their details saved into Order and OrderItem database tables for persistent record-keeping.

PDF Bill Generation: Customers can generate and download a detailed PDF bill for their placed order, including order ID, customer details, and item-wise breakdown.

Sales Data Visualization: An integrated analytics dashboard displays interactive horizontal bar charts (using Plotly) to visualize key sales metrics, such as the "Top N Most Sold Items."

Robust Session Management: Ensures continuity of cart data across different pages.

Database Integration: Utilizes Django's powerful ORM for efficient interaction with a relational database, ensuring reliable storage and retrieval of menu, order, and customer data.

Error Handling & Data Integrity: Includes server-side checks (e.g., for empty carts, missing menu items) and database transactions for data consistency.

🛠️ Technologies Used
Backend:

Python 3.12

Django Framework

Frontend:

HTML5

CSS3

Database:

SQLite (default for development, easily configurable for PostgreSQL/MySQL)

Libraries / APIs:

plotly: For creating interactive data visualizations.

fpdf: For generating PDF bills.

Django's ORM: For database interactions.

🚀 Installation & Setup
Follow these steps to get a local copy of the project up and running on your machine.

Prerequisites
Python 3.12

pip (Python package installer)

git

Steps
Clone the repository:

git clone [YOUR_REPOSITORY_URL_HERE]
cd BhoitesCafeWebsite # Replace with your actual project folder name


Create and activate a virtual environment:

python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate


Install project dependencies:

pip install -r requirements.txt


Note: If you haven't created requirements.txt yet, you can do so by running pip freeze > requirements.txt after installing Django, plotly, fpdf, etc.

Apply database migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (optional, but recommended for admin access):

python manage.py createsuperuser


Follow the prompts to create your admin user.

Run the development server:

python manage.py runserver


The application will be accessible at http://127.0.0.1:8000/.

💡 Usage
Navigate to the Home Page: Open http://127.0.0.1:8000/ in your browser.

Register/Login: Create a new customer account or log in if you already have one.

Browse Menu: Explore the categorized menu items.

Add to Cart: Specify quantities for desired items and click the "Cart" button in the header to add them.

View Cart: Review your selected items and make any final quantity adjustments.

Place Order: Proceed to place your order.

Generate Bill: After placing an order, download a PDF bill for your records.

Analytics: Visit the analytics page (e.g., /analytics/ or as per your urls.py) to see visualizations of best-selling products.
