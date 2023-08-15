# **Where Are We Going?** 🎟️ 

[*Link to the live website.*](https://where-are-we-going-d3621addaf03.herokuapp.com/festivals/)

Welcome to Where Are We Going?, a full-stack e-commerce website built using the Django framework, Bootstrap, HTML, CSS, Python & JavaScript.  It uses Stripe as the payment processor and Amazon Web Services S3 Bucket to store static and media files. The project has been deployed on Heroku and uses a PostgreSQL database instance hosted on ElephantSQL.

This project was created for educational purposes as my fifth and final project for a Diploma in Software Development with Code Institute. Where are we going? is an online shop where the user can buy tickets for the best festivals in the world.

![Where Are We Going](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/e640d22d-3448-4a81-8e19-7c211a56ff85)
_____

## Table of Contents
  - [Introduction](#introduction)
  - [Business Model](#business-model)
    - [Marketing Strategy](#marketing-strategy)
      - [Social Media Marketing](#social-media-marketing)
      - [Email Marketing](#email-marketing)
    - [Search Engine Optimisation](#search-engine-optimisation)
    - [Website Main Goals](#website-main-goals)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Project and Database Structure](#project-and-database-structure)
      - [Data Models](#data-models)
    - [Wireframes and Design Choices](#wireframes-and-design-choices)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks \& Dependencies](#frameworks--dependencies)
    - [Tools](#tools)
  - [Deployment](#deployment)
  - [Validation and Testing](#validation-and-testing)
  - [Bugs](#bugs)
  - [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
[Back to Top](#table-of-contents)
_____
## Introduction
I have come up with an idea to address the growing issue of festival-goers feeling overwhelmed when selecting a festival to attend. With the increasing number of festivals available, people often struggle to determine which event would be the best fit for them. To tackle this problem, I propose the creation of an online platform that serves as a comprehensive hub for the finest festivals worldwide. This platform will simplify the process for users by offering a curated selection of top-tier festivals and facilitating ticket purchases. By centralizing information and ticket sales, attendees can make more informed decisions about their festival choices, enhancing their overall experience.

By following the principles of User Experience Design, Search Engine Optimization and utilizing the Django full-stack framework and Stripe API for secure payments, Where Are We Going? offers its customers an efficient and seamless way to view and purchase its products from anywhere in the world.

You can test the payment functionality by using the following details on the checkout page:

-   Card Number: 4242 4242 4242 4242
-   Expiry Date: Any future date formatted to MM/YY
-   CVN: Any 3-digit number

[Back to Top](#table-of-contents)
_____

## Business Model
"Where Are We Going?" is a business-to-consumer (B2C) e-commerce platform curated for festival enthusiasts. Our platform provides an online marketplace dedicated to procuring tickets for the world's premier festivals, ensuring that users are exclusively presented with the finest events. Users have the option to maintain a connection with us through email or WhatsApp Business, allowing them to offer comments, seek assistance, or share suggestions seamlessly.

### Marketing Strategy
The marketing strategy should focus on establishing the brand as a symbol of transparency, safety, reliability, and the ultimate destination for top-quality festival purchases. Achieving this requires developing a comprehensive content plan tailored to various social networks, as well as implementing a strategic search engine optimization (SEO) approach to secure a prominent position among the top search results. Additionally, it is essential to incorporate a newsletter system to nurture a loyal user base.

The primary objective is to enhance the conversion rate by bridging the gap between site visitors and those who ultimately decide to purchase tickets. This can be achieved by increasing the influx of users to the platform and seamlessly guiding them towards the decision to secure their tickets.

#### Social Media Marketing
To enhance the e-commerce presence, a Facebook page was established to facilitate direct communication between the administrator and the audience. This platform serves as a means to cultivate a follower base by engaging with other accounts, posts, comments, videos, and advertisements. Below, you'll find a screenshot of the business's Facebook page and its inaugural post. Regrettably, a short while later, Facebook unexpectedly shut down the page.

<details>
<summary>Facebook</summary>

    Facebook page
![Facebook-page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/23e417c9-176b-46e6-ad25-9419aec35d2d)

    First post on the Facebook page
![Facebook-page2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/7b4aa440-e970-4587-bac1-22d27b98f10b)

</details>

#### Email Marketing
An email newsletter subscription service will be implemented on the e-commerce website. This service will keep users informed about the latest news, special promotions, and more, while also motivating them to revisit the website.

Displayed below are screenshots of the newsletter subscription form and the inaugural user who has successfully registered.

<details>
<summary>Newsletter</summary>

    Mailchimp
![Mailchimp](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/9a51d34b-8e66-432f-bb2b-460c556b7a0b)

    The first user registered
![The first user registered](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/005150ce-1863-4b36-98d3-80171f0c0797)

</details>

### Search Engine Optimisation
Search engine optimisation (SEO) encompasses a number of techniques aimed at improving the visibility and ranking of web pages in organic search results. In my efforts to increase my website's search engine ranking, I researched keywords.

To do this, I used [Word Tracker](https://www.wordtracker.com/) to select the most relevant keywords. Once the optimal keywords were identified, I strategically integrated them into various elements of the website, such as meta tags, content and alternative image descriptions. This extensive keyword integration helps search engines understand the interconnectedness between the various pages of the website and ultimately improves its visibility in search engines.

Furthermore, I've incorporated a sitemap.xml and a robots.txt file into my project. The sitemap offers a comprehensive list of all website pages, ensuring search engines can efficiently navigate through the content. In parallel, the robots.txt file provides instructions to search engines, outlining which specific pages should not be crawled or indexed. Below are screenshots from both files:

<details>
<summary>SEO Files</summary>

    sitemap.xml
![sitemap.xml](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3060c2d4-273f-4638-ae93-2f64e901b516)

    robots.txt
![robots.txt](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3f32c952-b813-4473-a884-a410a1e7fd11)

</details>

Moreover, each festival name is equipped with a link that, when clicked, opens in a new tab, directing users to the official festival website. This strategic linking fosters a connection between our website and the festivals, contributing to an improved ranking within search engine results.

Additionally, a privacy policy has been seamlessly integrated into the website. Although not a direct SEO ranking determinant, including this policy is advised for search engines like Google to index. Furthermore, it significantly enhances the website's credibility and trustworthiness. This step aligns with compliance efforts related to diverse data protection and privacy laws and regulations.

### Website Main Goals

For the user/customer:

- To give users a responsive and easy-to-navigate website with a clear purpose.
- To provide users with products that meet their expectations.
- To allow users to view details on products and add them to their shopping basket.
- To allow users to purchase products as Made to Order if the stock runs out.
- To allow users to checkout quickly and safely.
- To give users the option to save their information for future visits.
- To give registered users the ability to view their previous orders.
- To give registered users the ability to submit product reviews.
- To give users ways to contact the business owner easily and efficiently.

For the administrator:

- To be able to showcase the best festivals.
- Provide your customers with up-to-date information.
- To have a secure and efficient way to sell tickets.
- To be able to add new festivals through the administration panel.
- To be able to delete festivals via the administration panel.
- The ability to edit festivals via the administration panel.
- To be able to see a history of sales.

[Back to Top](#table-of-contents)
_____

## User Experience
This section aims to determine what a user would expect from interacting with the website. Each User Story was recorded in GitHub Issues. Scenarios of actions each type of user, including the business owner, wishes to take are listed below.

### User Stories

**As a User:**

* As a user, I can register for an account, so that I have access to other features of the website.
* As a user, I can check my emails for a registration confirmation email, so that I can verify that my registration was successful.
* As a Registered User, I can log in and log out from my account, so that I can access my account's information and keep my information secure.
* As a Registered User, I can reset my password, so that I can recover access to my account if I forget my password.
* As a User, I can land on the homepage of the site, so that I can learn more about the business and the types of products they sell.
* As a User, I can view the logo and the links in the navigation bar, so that I can easily navigate to other pages of the site.
* As a User, I can access contact details, social and developer links across all pages, so that I can follow/contact the business owner and the website creator.
* As a User, I can learn more about the business, so that I can decide if I want to purchase from them or not.
* As a User, I can write a message to the business owner using email or WhatsApp Business, so that I can ask questions or give feedback.
* As a User, I can sign up for the newsletter, so that I keep updated on the latest products, offers and pop-up stalls.
* As a User, I can view a list of festivals, so that I can select some to purchase.
* As a User, I can view individual festival details, so that I can identify more information about the product.
* As a User, I can search for a specific festival, so that I can quickly find products I'm interested in.
* As a customer, I can access my basket, so that I can review items before I purchase them.
* As a customer, I can add festivals and identify their total cost in the basket, so that I know how much I'm spending.
* As a Customer, I can update the quantity of each festival in my basket, so that I can easily make changes to my order before checkout.
* As a User, I can see real-time notifications as I interact with the website so that I can have a better experience.
* As a Customer, I can confirm my festivals and total cost on the checkout page, so that I can continue to enter the required information to complete my order.
* As a Customer, I can easily enter my payment information, so that I can check out quickly and efficiently.
* As a Customer, I can view an order confirmation after checkout, so that I can confirm that my order was successful.
* As a Registered Customer, I can have a personal user profile, so that I can save my payment info and view my order history and confirmations.
* As a Registered Customer, I can edit personal information on my profile, so that I can use the correct details when processing future orders.
* As a User, I can navigate to the About page, so that I can learn more about the shop owner.
* As a User, I can easily navigate back to the top of the page with one click, so that I can easily access other parts of the website.
* As a user, I receive the tickets via email, each accompanied by a unique identification code, so that I can have secure access to the event.--- It's not completed
* As a User, I can connect with my social media account, so that I can easily create an account. --- It's not completed

**As a Business Owner:**
* As a Business Owner, I can have a banner with a CTA clearly visible on the landing page, so that users are encouraged to access the shop and view/buy festivals.
* As a Business Owner, I can use the Admin interface to add, update, view and delete festivals so that I can populate the online shop.
* As a Business Owner, I can add a festival via the UI, so that I can add new items to my store.
* As a Business Owner, I can edit/update a festival via the UI, so that I can change the festival price, description, image and other festival criteria.
* As a Business Owner, I can delete a festival via the UI, so that remove festivals that are no longer on sale.
* As a Business Owner, I can access and review the complete sales history within the Django admin panel, ensuring a comprehensive overview of all past transactions and sales activities.
* As a Business Owner, I can view, add, delete, and modify festivals in the Django admin panel.
* As a Business Owner, I can have my Business Facebook page linked with my website, so that I can connect and interact with my customers directly and potentially extend my reach through posts and other content creation.

**As a Developer:**
* As a developer, I can add functionality with the plus (+) and minus (-) buttons to the quantity selector, so that the user has a better experience adding products to their basket on mobile.
* As a developer, I can make sure that customers can confidently provide the information required safely and securely so that they can have a positive experience on the site.
* As a Developer, I can add metadata, a sitemap and robots.txt file, so that the website can be found and ranked by search engines.
* As a Developer, I can build custom error pages, so that the user remains on the site and has a way to get back to the homepage or access navigation.

[Back to Top](#table-of-contents)
_____

### Data Models
Models define the source of the data stored.  Each model contains the essential fields and behaviours of the data being stored. The image below shows this project's Data Schema and the relationships between the models.

<details>
<summary>Database Schema</summary>

![Database Schema](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/acfa6844-454f-426e-9774-3549a8940b05)

</details>

### Design

**Colour Scheme**
Coolors]( https://coolors.co/) was used to generate a colour palette for the website:

![colour-scheme](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/96547f1c-e4a5-4194-8297-a2ac8b8b5870)

* The colour `000000` is used to give it a plain background so that the user can clearly distinguish the content.
* The colour `FF0000` is mainly used on the buttons when the user stops the mouse over them.
* The colour `FF66B2` is mainly used on the footer buttons to differentiate them from the others.

**Typography**
The typography used throughout the project is ['Geologica'](https://fonts.google.com/specimen/Geologica?query=GEOLOGICA) because it is a versatile typeface that works well for both display and body text. Different weights and styles of 'Geologica' are used in the project to distinguish more important parts from others or to highlight specific text.

![Google Fonts](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/479a3dc1-3ee2-4e73-adff-c5e01c2ef6d7)

**Icons**
[Font Awesome](https://fontawesome.com/) social media icons were used for the Footer. They are used as interactive links and have an aria-label which gives the relevant information to screen readers to read out to the users. 

**Wireframes**
Wireframes are made in Canva. Below you can see the design of the different parts of the project. But I have not been able to develop the project as I wanted due to lack of time because I am working in a company since June and I have practically no time to dedicate to the project. That's why you can see that the final design of my project doesn't look like the wireframes.

<details>
<summary>Main Menu</summary>
  
    Part 1
![Main Menu 1](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4b953172-51d9-4082-88d4-948486a63a87)

    Part 2
![Main Menu 2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/84f47743-bead-4b88-ad35-e2a328018430)

    Part 3
![Main Menu 3](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c53f52c2-9553-40a4-b524-535a3fc059fb)

    Part 4
![Main Menu 4](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/577a953b-ae28-4820-b148-a3ab201f7e8b)
</details>

<details>
<summary>Checkout</summary>
  
    Checkout
![Checkout](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f55e8c35-1089-4a1d-a034-423e3d9370ab)
</details>

<details>
<summary>Shopping bag</summary>
  
    Shopping bag
![shopping bag](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b5e6390e-50d4-4e84-9819-649f19598707)
</details>
