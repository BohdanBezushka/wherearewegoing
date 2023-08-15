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
![Coolors]( https://coolors.co/) was used to generate a colour palette for the website:

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

<details>
<summary>Checkout details</summary>
  
    Checkout details
![Checkout details](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/689d1796-059c-49bf-911b-f13fdd775744)
</details>

<details>
<summary>Festivals</summary>
  
    Festivals
![Festivals](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/afce84d0-3184-4126-ad10-023326d8427c)
</details>

<details>
<summary>About</summary>
  
    Part 1
![Part 1](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/55c3ef4d-f2a5-4f46-b016-d79decad0c0b)

    Part 2
![Part 2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/900e51a2-c163-4159-b9ec-7904db36a3fe)

    Part 3
![Part 3](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/1ef19679-18d8-4d4c-9725-7aaaaeca15fc)
</details>

<details>
<summary>Sign in</summary>
  
    Sign in
![Sign in](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b686cff3-fc7e-4fc0-a96e-40c8fb832dd4)
</details>

<details>
<summary>Sign up</summary>
  
    Sign up
![Sign up](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/0309d144-a17b-414f-b0a9-300b8c96cdf2)
</details>

<details>
<summary>Footer</summary>
  
    Footer
![Footer](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c7ce55ba-fa9b-493e-854d-d4b20662298c)
</details>



[Back to Top](#table-of-contents)
_____

## Agile Methodology
The plan for this project was carried out using the Agile Methodology. GitHub issues, which can be found [here](https://github.com/BohdanBezushka/wherearewegoing/issues), were used to record user stories, bugs and developer tasks. These were categorised into 4 Epics/Milestones and organised into 1 Project/Sprint. Each User Story includes Acceptance Criteria and Tasks that are necessary for a clear and effective approach to the project, ensuring that the minimum project requirements are met. The MoSCoW Method of Prioritisation was also used, classifying each User Story as a "Must Have", "Should Have", "Could Have" and "Won't have". Also, the labels "Fix bug" and "Project Task" were added for better organisation.

"USER HISTORY: Different ways to create an account" and "USER STORY: Tickets by email" I have not been able to implement them due to lack of time.

<details>
<summary>Screenshots of the Issues section of Github</summary>

        Open Issues
![Open Issues](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c325f4f2-d68a-4238-a5ec-ca9a3ccd81a9)

        Closed Issues
![Closed Issues](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/8eaea7eb-e886-48a6-8ec9-01d7db4de985)

        Labels
![Labels](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/d98ad5f7-3e27-487b-9780-686d06a4b31b)

        Open Epics
![Open Epics](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/ca5833f6-50c4-41b1-8b51-b81438a2a5d1)

        Closed Epics
![Closed Epics](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/e4889cca-534c-41fe-9e4a-574fec84a31c)

        Add Issue
![Add Issue](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/786ce2e0-c236-4d1b-8008-245bd2f9cf86)

        Sprint
![Sprint](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/ef3d7806-00a5-4532-8697-74a5e67cebec)
</details>

In order to develop an MVP (Minimum Viable Product), I employed the issues section of GitHub along with Trello, allowing me to meticulously plan and create a streamlined timeline for the project's progression.

[Back to Top](#table-of-contents)
_____

## Features
  
### Favicon 
Our favicon works to visually identify the webpage and help the user recognize it more easily when they have multiple tabs open in the browser. Additionally, it improves the image and branding of a webpage.

<details>
<summary>Where Are We Going? Favicon</summary>

        Favicon
![Favicon](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/636f2e67-6113-4508-bdf3-b7a6a6f0a487)
</details>

### Introduction page
All parts of the project have a header and footer so that the user can easily move between different sections.

<details>
<summary>Home</summary>

![Home](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/173c4194-c52c-42cc-a1e6-08bf9f43b04e)
</details>

### Festivals
In this section, the user can see a list of all festivals.

<details>
<summary>Festivals</summary>

![Festivals](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/04885491-93b2-4a6d-8f6e-44c5adb2d7da)
</details>

### Festival details
In this section, the user has a description of the festival and can add tickets to the shopping bag.

<details>
<summary>Festival details</summary>
  
    Festival details
![Festival details](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/a78c1de7-99b5-4a9c-9775-9d92b123f128)

    Add a festival to the shopping cart
![Add a festival to the shopping cart](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/320c75c4-4995-49f5-9a9c-aabd07b78485)

    Add more tickets for same festival
![Add more tickets of same festival](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/735d8b02-525d-4810-b7f7-9e37b215312e)
</details>

### Shopping bag
In this section, the user can see his shopping cart, modify the festival tickets, delete the festival and see the total price. They can also continue shopping or make a payment.

<details>
<summary>Shopping bag</summary>
  
    Shopping bag
![Shopping bag](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/cecfce11-490c-4698-b42d-5ffddef84e16)

    Update festival
![Update festival](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3cfffcb8-52dc-4cf3-9431-9e387a442499)

    Delete festival
![Delete festival](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/970a8664-18d1-4a03-b5f0-2ba9f46b6848)
</details>

### Checkout
In this section, the user can fill in the form and add their card to complete the purchase. When the payment is completed the user can see a summary of the purchase.

<details>
<summary>Checkout</summary>
  
    Checkout
![Checkout](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/51bc6bfb-fdcc-4748-8642-0c9d9af750b2)

    Order information
![Order information](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/5efb9e84-2891-4b14-8fdf-f9169f08702f)
</details>

### Contact
In this section, the user has at his disposal an e-mail address and a telephone number to ask for help, suggestions and opinions.

<details>
<summary>Contact</summary>
  
    Contact
![Contact](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/9b0db390-b7ce-4cfc-8ffa-952adc82b12f)
</details>

### More
In this section, the user can click on the "about us" button and get to know us. He can also go to the newsletter section to sign up. 

<details>
<summary>More</summary>
  
    About us
![About us](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/726eeb62-8ef6-40b9-af0a-a18c48acbf35)

    Newsletter
![Newsletter](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b5d12f32-95e0-484f-8adf-2e5ec7a0ec1e)
</details>

### Sign in and sign up
In this section, the user can log in with his e-mail address and password. It also has a link to the user registration section and another link in case the user has forgotten the password.

<details>
<summary>Login, log out and registration</summary>
  
    Sign in
![Sign in](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/0cb9b7ee-accb-4a33-b462-0446c31cd401)

    Sign up
![Sign up](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/1da50ca5-e7ee-4c9a-a2d4-a48eededacde)

    Forgot Password?
![Forgot Password](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4cf56c23-2cb8-487b-b70d-c110ff917ab5)

    Verify your e-mail address
![Verify your e-mail address](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/5f901e55-8e1f-492b-998a-72282dc2f359)

    E-mail
![E-mail](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/557d3280-2f9e-49f2-99cb-9f6f718dde8c)

    E-mail confirmation
![E-mail confirmation](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/ae0883db-faba-4631-a031-062abc7b4228)

    Confirmed
![Confirmed](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/aa2458c3-74bb-461e-9700-14f06f33adf1)

    Signed
![Signed](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/eac8ea6c-6602-4adc-b24f-0a1dc11f3579)

    Log out part 1
![Log out part 1](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/5bf3d894-303c-4be2-99ee-e2a281587a01)

    Log out part 2
![Log out part 2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/86dc2518-098f-4810-a7e4-075521b116ab)
</details>

### Regular user
In this section, the user can fill in the default information when making a purchase and can also view the purchase history.

<details>
<summary>My profile</summary>
  
    My profile
![My profile](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/d5a33763-e205-4499-a447-0f9f67038d23)
</details>

### Admin
In this part, we show how the administrator can add new festivals, update festivals and delete festivals.

<details>
<summary>Admin sections</summary>
  
    Festival management
![Festival management](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/fcf897eb-9303-4fc2-b63c-12181d2fc70b)

    Added festival
![Added festival](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/a49dbee2-610e-4a9c-95a1-bc045d6c7593)

    Edit part 1
![Edit part 1](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/99dabcab-a046-4e1a-bc96-419ef6fb0821)

    Edit part 2
![Edit part 2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/2244dd23-5cab-4650-8aa1-dec917246e87)

    Edit part 3
![Edit part 3](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/8b61c6cf-4c6c-43cd-b0d0-223ca011d393)

    Deleted
![Deleted](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/6e2624e3-a257-4f06-88d5-7be36a5459e9)
</details>

### Django Administration
In this section, the administrator can view, update, delete and add users, festivals and orders.

<details>
<summary>Sections</summary>
  
    Users
![Users](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/0b591abc-d17a-43c9-8840-a1eaed74da6a)

    Orders
![Orders](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/e6b1bc7c-5444-4caf-8b71-46ba755653e8)

    Festivals
![Festivals](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3423e547-07bf-442c-99b8-63fd9d0e113b)
</details>

[Back To Top](#table-of-contents)
___

## Future Features
When I have time, I would like to continue working on the following features:

* Implement a ticket delivery (with a unique code to avoid scams) to the user's email address and phone number when the user completes the purchase.
* Implement a blog in order to attract more users to the website.
* I would like to add the option for users to register using Google or Facebook because it makes accessing the application faster. The registration process will be implemented using Django Allauth to integrate with the authentication APIs of these platforms.

[Back To Top](#table-of-contents)
___

## Technologies Used
This project was developed using the following languages, frameworks, libraries and dependencies:

### Languages
- [HTML5](https://www.w3schools.com/html/)
- [CSS3](https://www.w3schools.com/css/css_intro.asp)
- [Python 3.8.12](https://www.python.org/downloads/release/python-3812/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Frameworks & Dependencies
- [Django 3.2.18](https://www.djangoproject.com/) - Free and open source Python Web Framework
- [Gunicorn 20.1.0](https://gunicorn.org/) - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
- [PostgreSQL 0.5.0](https://www.postgresql.org/) - A powerful, open-source object-relational database system
- [Pyscopg2 2.9.5](https://www.psycopg.org/docs/) - A PostgreSQL database adapter for Python
- [Stripe](https://stripe.com/) - Provides a secure and convenient way to handle online payments
- [Amazon Web Services S3 Bucket](https://aws.amazon.com/s3/) - A cloud storage service which provides object storage, built for storing and recovering any amount of information or data from anywhere over the internet through a web services interface
- [Heroku](https://www.heroku.com) - A cloud platform as a service
- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - The database provided by Django
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication and registration
- [Bootstrap 4.6.2](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A Framework for building responsive, mobile-first sites
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Provides a |crispy filter and {% crispy %} tag that helps control the rendering behaviour of Django forms in a very elegant and DRY way
- [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library adds image processing capabilities to your Python interpreter
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) - Allows connection to S3 bucket

### Tools
- [Cloud Anywhere](https://codeanywhere.com/solutions/collaborate) - Online Cloud Editor Used
- [GitHub](https://github.com/) - Cloud-based git repository used
- [W3C Validator](https://validator.w3.org/) - A validator which checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, etc.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - A validator which checks the validity of CSS code
- [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) - Highlights syntactical and stylistic problems in Python source code
- [JShint](https://jshint.com/) - A JavaScript code quality tool
- [Chrome DevTools and Lighthouse](https://developer.chrome.com/docs/devtools/) - Web Developer Tools
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) - A box shadow generating tool
- [Am I responsive](https://ui.dev/amiresponsive) - For responsive visuals of the website
- [CanIUse](https://caniuse.com/) - Browser support tables for modern web technologies
- [Compress or Die](https://compress-or-die.com) - Webp compression
- [TinyPNG](https://tinypng.com/) - Compresses images to reduce the file size
- [TinyURL](https://tinyurl.com/app/) - Shortens links
- [Coolors](https://coolors.co/) - Colour Palette Generator
- [Google Fonts](https://fonts.google.com/) - Fonts
- [Font Awesome](https://fontawesome.com/) - Icons
- [Balsamiq](https://balsamiq.com/wireframes/) - Low Fidelity Wireframes
- [Google Drawings](https://docs.google.com/drawings) - Data Schema Tables
- [XML Sitemaps](https://www.xml-sitemaps.com/) - Sitemap Generator
- [Word Tracker](https://www.wordtracker.com/) - Keyword Research
- [Privacy Policy](https://www.privacypolicygenerator.info/) - Privacy Policy Generator
- [BrowserStack](https://www.browserstack.com/) - App and Browser Testing

[Back to Top](#table-of-contents)
_____

## Deployment
All deployment information can be found in [DEPLOYMENT.md](DEPLOYMENT.md)

[Back to Top](#table-of-contents)
_____

## Validation and Testing
All validation & testing information can be found in [TESTING.md](TESTING.md).

[Back to Top](#table-of-contents)
_____

## Bugs
**🐛**
<details>
<summary>Festivals weren't loaded:</summary>
  
Problem: When I passed all the data to ElephantSQL and had to load all the festivals I got the following error:
![problem1](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c06f30f2-b53d-4d1a-8042-18a25270e6db)

Solution: Create a JSON file for uploading festivals.
![solution](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/98d3c399-74c0-4a80-a687-6eb7e10fd9b6)
</details>

**🐛🐛**
<details>
<summary>Heroku login in Terminal:</summary>

Problem: When I logged into Heroku through the terminal I got the following error:
![problem2](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/46e4a988-405e-4cae-9c5b-239621935959)

Solution: The error is due to the fact that in my Heroku account, I have Multi-Factor Authentication enabled. So I have to use the command "heroku login -i" put my email and when it asks for the password, enter the API Key.
</details>

**🐛🐛🐛**
<details>
<summary>It does not send email confirmation messages when a user registers:</summary>

Problem: When a new user registers on the website, the page keeps refreshing constantly until it displays the following error:
![problem3](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3c24caa0-8b46-4d16-b092-8bb434b9b8b7)

Solution: The solution is to add again a new application with a password through Google security settings and modify in Heroku settings in your project the EMAIL_HOST_PASS.
</details>

[Back to Top](#table-of-contents)
_____

## Credits

### Information Resources
The following walkthroughs helped me get my project in shape. I have adapted the code in these walkthroughs for the needs of my project:
* Code Institute's "Project - Boutique Ado " which is found in the CI's LMS for the Diploma in Software Development.
* [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)
* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Stripe Documentation](https://stripe.com/docs)

### Content
* [Gmail Help](https://support.google.com/mail?sjid=2849961795253290086-EU#topic=7065107)
* [Django Sending Email To Gmail Account | Python Send Email](https://www.youtube.com/watch?v=UH8oHNDfTyQ)

### Acknowledgements
I would like to thank the following people who inspired, motivated, guided, helped and supported me along this Portfolio Project 5 journey:

- All the people on Slack who have helped me and answered my questions, especially the group that started the course in August 2022.
- The tutors who helped me quickly with the bugs I encountered were invaluable; without them, I think it would have taken me twice as long to complete the project.

![Code Institute](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/966af479-d432-44ec-b25b-0acab0915f5c)

[Back to Top](#table-of-contents)
_____
