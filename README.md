# Epic Merch  

Step into the ultimate gaming haven with **Epic Merch** – your go-to destination for high-quality gaming goods and merchandise! Our platform is designed to provide an effortless shopping experience, allowing you to discover and purchase the coolest gaming gear with ease.  

Whether you're a hardcore gamer or a casual enthusiast, **Epic Merch** has something for everyone. Browse through our extensive collection of gaming products, filter items based on your preferences, and explore detailed product descriptions to find exactly what you need.  

With a seamless checkout process powered by **Stripe**, adding your favorite items to the cart and completing your purchase has never been easier. Plus, track your order history and update your profile information effortlessly. If you're a **superuser**, you can even manage products directly from the website!  

Join the **Epic Merch** community today and level up your gaming setup with the best gear available. Ready to explore? Dive in and experience the ultimate gaming shopping adventure!  

![Epic Merch Screenshot](/media/readme/responsive.png)  

[Visit Epic Merch Live](https://epic-merch-565735eb773a.herokuapp.com/)

---

## Table of Contents

### [User Experience](#user-experience-ux)

- [Project Goals](#project-goals)
- [Agile Methodology](#agile-methodology)
- [Target Audience](#target-audience)
- [First time user](#first-time-user)
- [Registered user](#registered-user)
- [Admin user](#admin-user)

### [SEO and Marketing](#seo-and-marketing-1)

### [Design](#design-1)

- [Color Scheme](#color-scheme)
- [Product Images](#product-images)
- [Wireframes](#wireframes)
- [Database Scheme](#database-scheme)
- [Data Model](#data-models)
- [User Journey](#user-journey)

### [Security Features](#security-features-1)

- [User Authentication](#user-authentication)
- [Login Required](#login-required)
- [CSRF Protection](#csrf-protection)
- [Custom Views Security Measures](#custom-views-security-measures)
- [Form Validation](#form-validation)

### [Features](#features-1)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

### [Technologies Used](#technologies-used-1)

- [Languages Used](#languages-used)
- [Databases Used](#databases-used)
- [Frameworks Used](#frameworks-used)
- [Payment Systyem](#payment-system)
- [Programs Used](#programs-used)
- [Emails and Newsletter](#emails-and-newsletter)
- [SEO and Marketing](#seo-and-marketing-2)

### [Deployment and Local development](#deployment-and-local-development-1)

- [Local Development](#local-development)
- [ElephantSQL Database](#elephantsql-database)
- [AWS Amazon](#aws-amazon)
- [Heroku Deployment](#heroku-deployment)

### [Testing](#testing-1)

### [References](#references-1)

- [Docs](#docs)
- [Content](#content)
- [Acknowledgements](#acknowledgements)

---


## User Experience (UX)  

Step into the ultimate gaming universe with **Epic Merch’s E-commerce Platform**, where the world of gaming goods and merchandise awaits. Our platform is designed to provide a seamless and immersive shopping experience, ensuring effortless browsing, purchasing, and engagement with your favorite gaming gear. Every click brings you closer to leveling up your setup with high-quality products tailored for gamers.  

**Epic Merch** is meticulously crafted with user-friendly navigation, featuring a visually captivating interface that enhances your shopping experience. Whether you’re searching for the latest gaming accessories or exclusive collectibles, our personalized recommendations and detailed product information ensure you find exactly what you need.  

Browse through a curated selection of gaming merchandise, conveniently categorized for easy navigation. With our mobile-friendly design, access your wishlist and cart from any device, ensuring a seamless shopping experience wherever you go.  

Experience the excitement of securing the perfect gaming gear, knowing that every purchase enhances your passion for gaming. Enjoy special promotions, including **free shipping on orders over $200**, so you can get your gaming essentials delivered hassle-free.  

**Epic Merch’s E-commerce Platform** is more than just a store; it's a **gaming paradise** where your love for gaming merchandise thrives. Join us in celebrating gaming culture and indulge in the joy of discovering the best gaming gear available. **Game on!** 🎮  

![Epic Merch Screenshot](/media/screenshots_webp/epic_merch_responsive.webp)  

[Visit Epic Merch Live](#) 🚀  

---  

## Project Goals  

Epic Merch is dedicated to creating a comprehensive and user-friendly e-commerce platform tailored for gaming enthusiasts. The project focuses on:  

- **Enhanced User Experience:** Provide a seamless and intuitive interface for browsing, purchasing, and engaging with a diverse selection of gaming products.  

- **Streamlined Shopping Experience:** Simplify the process of finding and purchasing gaming merchandise by offering personalized recommendations and hassle-free checkout.  

- **Promote Gaming Culture:** Encourage users to discover new gaming gear, accessories, and collectibles through curated collections and featured releases.  

- **Accessibility and Convenience:** Prioritize accessibility by ensuring the platform is optimized for mobile devices, allowing users to browse, shop, and manage their accounts on the go.  

By focusing on these project goals, **Epic Merch** aims to create a seamless and engaging shopping experience for gamers looking for top-quality merchandise.  


## Agile Methodology  

Agile methodology was the core framework for organizing and managing the development of **Epic Merch**. The workflow involved:  

- **User Story Creation:** User stories were carefully crafted following Agile principles, ensuring clear definitions of project goals and user needs.  

- **Epics Development:** Broad epics were defined, each encompassing potential user stories, serving as the foundation for structured development.  

- **Iterative Development:** By breaking down epics into actionable user stories, the project progressed in iterative cycles, refining features and improving functionality.  

- **Github Project Board:** A public project board on GitHub was used to track tasks, organized into columns such as *Todo, In Progress, and Done* for real-time progress visualization.  

- **Task Prioritization:** Issues were labeled based on priority, allowing for structured task management and ensuring that critical functionalities were addressed efficiently.  

By leveraging Agile methodology, **Epic Merch** maintained flexibility, adaptability, and continuous improvement, resulting in a dynamic and efficient development process.  


<details>
<summary> User Stories Template
</summary>

![User Stories, Template](/media/readme/u_s_template.png)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](/media/readme/u_s.png)
</details>

<details>
<summary> Project Milestones
</summary>

![Project Milestones](/media/readme/milstones.png)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](/media/readme/p_board.png)

- <a href="https://github.com/users/ObiOne84/projects/5" target="_blank">Visit project GitHub page here.</a>

- <a href="https://github.com/users/ObiOne84/projects/5/views/1?layout=roadmap" target="_blank">Visit project GitHub roadmap here.</a>

</details>

#### Epics

- Project Setup & Deployment
- Milestone 2: Product & Shopping Cart Functionality
- Milestone 3: Checkout, Payments & Order Management
- Milestone 4: Admin Panel & Product Management

#### User Stories

1. View Homepage
**As a user, I want to view the homepage so that I can see an overview of the store and featured products.**

✅ **Acceptance Criteria:**
- The homepage should display featured products, promotions, and navigation links.
- The user should be able to navigate to other pages from the homepage.

2. Browse Products
**As a user, I want to navigate to the products page so that I can browse available products easily.**

✅ **Acceptance Criteria:**
- The products page should list all available products.
- Clicking on a product should take the user to the product details page.

3. Sort Products
**As a user, I want to sort products by price, popularity, or category so that I can quickly find what I am looking for.**

✅ **Acceptance Criteria:**
- Sorting options should be available on the products page.
- The selected sorting method should update the product display accordingly.

4. View Product Details
**As a user, I want to view product details so that I can see product descriptions, images, and pricing before making a purchase.**

✅ **Acceptance Criteria:**
- Clicking a product should open a detailed product page.
- The page should display the product’s name, price, description, and images.

5. Select Product Quantity
**As a user, I want to choose the quantity of a product so that I can buy multiple units if needed.**

✅ **Acceptance Criteria:**
- A quantity selector should be available on the product page.
- The total price should update based on the selected quantity.

6. Add Products to Basket
**As a user, I want to add products to my shopping basket so that I can purchase them later.**

✅ **Acceptance Criteria:**
- Clicking "Add to Cart" should add the product to the basket.
- A confirmation message should be displayed.

7. View Shopping Cart
**As a user, I want to view my cart page so that I can see the products I have added and their total cost.**

✅ **Acceptance Criteria:**
- The cart should display added products, their quantities, and the total price.
- The user should be able to proceed to checkout from the cart page.

8. Modify Cart Items
**As a user, I want to modify the quantity of items in my cart so that I can adjust my order before checkout.**

✅ **Acceptance Criteria:**
- Users should be able to increase or decrease the quantity of products.
- The total cost should update accordingly.

9. Remove Items from Cart
**As a user, I want to delete products from my cart so that I can remove items I no longer want to purchase.**

✅ **Acceptance Criteria:**
- A "Remove" button should be available for each product in the cart.
- Clicking the button should remove the item and update the total price.

10. Proceed to Payment
**As a user, I want to proceed to the payment page so that I can complete my order securely.**

✅ **Acceptance Criteria:**
- Clicking "Checkout" should take the user to the payment page.
- The page should display the order summary before payment.

11. Make Payment Using Stripe
**As a user, I want to pay using Stripe so that my payment is processed safely.**

✅ **Acceptance Criteria:**
- The payment page should integrate Stripe for payment processing.
- A successful payment should redirect the user to the order confirmation page.

12. Receive Order Confirmation Email
**As a user, I want to receive an order confirmation email so that I have proof of my purchase.**

✅ **Acceptance Criteria:**
- After a successful order, an email should be sent to the user.
- The email should contain the order number, product details, and total cost.

13. View Order History
**As a user, I want to view my order history on my profile page so that I can track my past purchases.**

✅ **Acceptance Criteria:**
- The profile page should display past orders with details.
- Clicking on an order should show the full order information.

14. Update Profile Information
**As a user, I want to update my default information on my profile page so that my details are saved for future orders.**

✅ **Acceptance Criteria:**
- Users should be able to update their address, phone number, and email.
- Changes should be saved and reflected in future orders.

15. Register an Account
**As a user, I want to register on the website so that I can place orders and track my purchase history.**

✅ **Acceptance Criteria:**
- A registration form should be available for new users.
- Users should receive a confirmation email after signing up.

16. Add to Wishlist
**As a user, I want to add products to my wishlist so that I can save them for future purchases.**

✅ **Acceptance Criteria:**
- An "Add to Wishlist" button should be available on product pages.
- Users should be able to access and manage their wishlist from their profile.

17. View Related Products
**As a user, I want to see related products on product pages so that I can explore similar or complementary items.**

✅ **Acceptance Criteria:**
- The product page should display related products.
- Clicking a related product should navigate to its details page.

## User Stories for Admin (Superuser)

18. Add New Products
**As a superuser, I want to add new products from the website so that I can update the store’s inventory easily.**

✅ **Acceptance Criteria:**
- A form should be available for adding new products.
- New products should appear in the product listings after saving.

19. Edit Existing Products
**As a superuser, I want to edit existing product details so that I can keep product information up to date.**

✅ **Acceptance Criteria:**
- An "Edit" button should be available for each product.
- Changes should be saved and reflected on the product page.

20. Delete Products
**As a superuser, I want to delete products from the store so that I can remove outdated or unavailable items.**

✅ **Acceptance Criteria:**
- A "Delete" button should be available for each product.
- Deleted products should no longer appear in product listings.

## Target Audience

- **Gaming Enthusiasts & Collectors**: Individuals passionate about gaming culture, seeking exclusive merchandise and high-quality gaming gear.
- **Tech-Savvy Shoppers**: Users who prefer a seamless, intuitive, and efficient online shopping experience.
- **Mobile Gamers & Users**: Customers who shop on the go and require a fully optimized mobile experience.
- **Community-Driven Gamers**: Those who engage with fellow gamers, share reviews, and participate in gaming discussions.
- **Content Creators & Streamers**: Influencers looking for the best gaming accessories to enhance their streaming setups.
- **Gift Shoppers**: People searching for the perfect gaming-related gifts for friends and family.

Epic Merch provides a dynamic e-commerce experience tailored for gamers, offering a curated selection of products, seamless shopping, and a thriving community of gaming enthusiasts.

## First Time User

- Simple and intuitive website navigation for easy exploration and discovery.
- Engaging visuals showcasing available products.
- Informative content providing an overview of the platform’s functionality and upcoming updates.
- Search bar to help users find their favorite gaming merchandise.
- Easy registration process for a hassle-free shopping experience.
- Secure and seamless checkout process.

## Registered User

- Quick and secure login with a personalized user account.
- Ability to browse and review products.
- Faster checkout process with stored payment and shipping details.
- User profile management for updating personal information.
- Wishlist and order tracking for a convenient shopping experience.

## Admin User

- Secure login with admin access control.
- Dashboard for managing products, reviews, and users.
- Ability to add, edit, or remove products and categories.
- User account management, including editing or deleting user profiles and orders.

## SEO and Marketing

Please see [SEO and Marketing](SEO_MARKETING.md) for a detailed analysis of the marketing strategy for Epic Merch.

## Design

The **Epic Merch E-commerce Platform** is crafted to deliver a visually captivating and user-friendly experience, inspired by the dynamic world of gaming.

- **Dark Theme**: The interface features a sleek dark mode for an immersive, high-contrast look that enhances product visibility.
- **Neon Accents**: Neon highlights at the background are used to emphasize key elements, such as call-to-action buttons and important sections.
- **Grid-Based Layout**: Clean and spacious grid-based design ensures smooth navigation and easy product browsing.
- **Interactive Elements**: Hover effects and animations enhance engagement, making the shopping experience more interactive and enjoyable.
- **Mobile-Optimized**: Fully responsive design for seamless shopping across all devices.


