# Bhoite's Cafe Website
## ☕ An E-commerce Café Platform
This project is a comprehensive full-stack e-commerce website designed for a cafe, allowing customers to browse a menu, add items to a shopping cart, place orders, and generate bills. It also includes an analytics dashboard to track top-selling items.

✨ **_Features:_**<br>
**Interactive Menu Display:** Browse food and drink items categorized for easy navigation.

**Customer Authentication:** Secure user login functionality using a custom Customer model.

**Dynamic Shopping Cart:** Add multiple items and specify quantities. Cart details (item name, quantity, price, item total) are managed in the user's session.

**Seamless Order Placement:** Finalize and place orders, with all selected items and their details saved into Order and OrderItem database tables for persistent record-keeping.

**PDF Bill Generation:** Customers can generate and download a detailed PDF bill for their placed order, including order ID, customer details, and item-wise breakdown.

**Sales Data Visualization:** An integrated analytics dashboard displays interactive horizontal bar charts (using Plotly) to visualize key sales metrics, such as the "Top N Most Sold Items."

**Robust Session Management:** Ensures continuity of cart data across different pages.

**Database Integration:** Utilizes Django's powerful ORM for efficient interaction with a relational database, ensuring reliable storage and retrieval of menu, order, and customer data.

**Error Handling & Data Integrity:** Includes server-side checks (e.g., for empty carts, missing menu items) and database transactions for data consistency.

🛠️ **_Technologies Used:_**
**Backend:**<br>
Python 3.12<br>
Django Framework<br>

**Frontend:**<br>
HTML5<br>
CSS3

**Database:**<br>
SQLite

**Libraries / APIs:**<br>
plotly: For creating interactive data visualizations.<br>
fpdf: For generating PDF bills.<br>
Django's ORM: For database interactions.

[Click here](https://www.linkedin.com/posts/sailesh-bhoite_django-python-webdevelopment-activity-7339626412946919425-2C94?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4) for Demo Video.

## Authors

- [@Sailesh Bhoite](https://github.com/Sailesh-Bhoite)