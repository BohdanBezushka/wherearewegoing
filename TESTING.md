# Testing the Where Are We Going? project.
![testing](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/64a2dfaa-8fc8-4ca8-a012-eacdadbf1427)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [User Stories](#user-stories)
- [Features](#features)
_____

# Code Validation

## HTML
HTML code was tested using the [W3C Validator](https://validator.w3.org/) via text input. Each page's source code was copied and pasted into the validator and checked for errors and warnings.

<details>
<summary>Home</summary>
<br>
  
![HTML Validation for Home Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/fc9afcee-c9a2-467d-9f98-60ebece18e18)

* The <li> error persists but it is inside a <ul>.
* The ID error isn't changed because I need the same code for the mobile version.

These two errors will be present in all tests because they correspond to the header.
</details>

<details>
<summary>Festivals</summary>
<br>

![HTML Validation for Festival Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/85ef424b-323e-4f24-88ba-6003717a7d0f)

The "id="card-border" error is due to the fact that for each festival an equal id is created.
</details>

<details>
<summary>Contact</summary>
<br>

![HTML Validation for Contact Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/37b4a902-02e9-43c1-98c3-f2e5a18465a3)
</details>

<details>
<summary>About us</summary>
<br>
  
![HTML Validation for About us Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/72f537ba-cf9f-468b-83eb-a052247ffd77)
</details>

<details>
<summary>Newsletter</summary>
<br>

![HTML Validation for Newsletter Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/64cf2c87-cc91-431c-a781-8187f061286c)
</details>

<details>
<summary>Festival Detail</summary>
<br>
  
![HTML Validation for Festival Detail Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/ae217d58-a4f8-4517-a05c-22d204e1df9d)
</details>

<details>
<summary>Bag</summary>
<br>
  
![HTML Validation for Bag Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/50e7a794-6f95-47e5-8a5f-7b1eb39e9477)
</details>

<details>
<summary>Bag</summary>
<br>
  
![HTML Validation for Bag Page](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/50e7a794-6f95-47e5-8a5f-7b1eb39e9477)
</details>

[Back To Top](#table-of-contents)
_____

## CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via file input.

<details>
<summary>Screenshot with results for the styles.css files</summary>
<br>

base.css
![CSS Validation for base.css file](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/153dcdb7-c05e-4fa2-962a-1c802bf06122)

profile.css
![CSS Validation for profile.css file](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/a0f4c3a5-da51-4d30-aeb4-179e34ae10ea)

checkout.css
![CSS Validation for checkout.css file](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/056d338d-d6e1-49ad-9a03-d647a9ea6e6a)
</details>

[Back To Top](#table-of-contents)
_____

## Python
Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/). Long lines were deleted using `# noqa`. 

<details>
<summary>Manage.py</summary>
<br>

![Python Validation for manage.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/59c3fdf5-e72f-48c7-a616-8d5a3ae5ce86)
</details>

<details>
<summary>Custom_storages.py</summary>
<br>

![Python Validation for custom_storages.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/1d8172ad-c13a-4467-bd67-7ab55dec8741)
</details>

<details>
<summary>Wherearewegoing</summary>
<br>

asgi.py
![Python Validation for asgi.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/6a24d364-94f2-4b62-8807-6e8b82fc622e)

settings.py
![Python Validation for settings.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c56bebb2-c521-4659-a88a-e0e55e1ed79c)

urls.py
![Python Validation for urls.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/a46ac798-442c-4169-8150-e5d28427a776)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/913ce560-fc2f-418b-81e4-4bc69648814b)

wsgi.py
![Python Validation for wsgi.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/e9042763-2956-486d-94bd-55a2f2f2a011)
</details>


<details>
<summary>Profiles</summary>
<br>
  
admin.py
![Python Validation for admin.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4af9a642-8453-4386-85b9-7762466fc773)

apps.py
![Python Validation for apps.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/879deaf8-bd49-4312-be23-2bf00501c080)

forms.py
![Python Validation for forms.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/26ae1a0f-3415-4627-a307-dd5e047b5e73)

models.py
![Python Validation for models.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/d0dd09ec-7662-4e80-9faa-d5cd110a5c82)

tests.py
![Python Validation for tests.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3df4acf9-20ab-47ac-8cd0-ec5b83a93d90)

urls.py
![Python Validation for urls.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/35f03ea6-9440-4576-859d-2169e25dda02)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f683c843-092d-45c5-a3b9-39282de0f190)
</details>


<details>
<summary>Home</summary>
<br>

apps.py
![Python Validation for apps.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f1b093da-9b5d-4275-a40a-b9a8113cc003)

urls.py
![Python Validation for urls.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4983c52f-d160-4577-95c7-4d7b2774aa2f)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/94a1b31e-1048-4f32-a416-6cab531caa06)
</details>


<details>
<summary>Festivals</summary>
<br>
  
admin.py
![Python Validation for admin.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/8684c8bb-7169-487a-a087-64710067dcca)

apps.py
![Python Validation for apps.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/53f25d42-6fdd-453d-b324-de9c4ac33260)

forms.py
![Python Validation for forms.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/a96de8ba-84ce-4ec2-94d2-e55d9f8f12ec)

models.py
![Python Validation for models.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/103872ce-1a3c-4c2b-a106-9015832b9493)

urls.py
![Python Validation for urls.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/d19276b4-0964-4d9e-a4e5-e5423b575425)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/efe91458-ea42-431b-b351-eba27420188d)

widgets.py
![Python Validation for widgets.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4e41e10d-5c98-4d05-b9ef-1fe7b0a62dbe)
</details>


<details>
<summary>Checkout</summary>
<br>
  
admin.py
![Python Validation for admin.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c7e5e5ff-ce3b-4af3-8584-f5202ad08e90)


apps.py
![Python Validation for apps.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/db0131d6-4077-46c0-b9c3-fe0814d7d49a)

forms.py
![Python Validation for forms.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b178458e-bcd2-4aa3-8d08-ccab1618d205)

models.py
![Python Validation for models.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/64c59e9d-ae03-4eea-b4d1-5c955bf252b6)

signals.py
![Python Validation for signals.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/23a217be-8228-4a88-839f-26f1f376ec8f)

urls.py
![Python Validation for urls.py)](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/5ad37a0e-5e18-4a44-b38b-c1efac37262b)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/818f20d1-d0c8-4a2f-b1f5-744f6f310a6a)

webhook_handler.py
![Python Validation for webhook_handler.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/2dab7060-8657-40fb-a2d4-b25bf08608fc)

webhookspy
![Python Validation for webhooks.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4fe3ec62-a728-4655-8f0e-dd5dd2e0f2e1)
</details>


<details>
<summary>Bag</summary>
<br>
  
apps.py
![Python Validation for apps.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/aa5da66d-3067-40aa-86d9-50016f0be5c7)

contexts.py
![Python Validation for contexts.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/9115736d-89c0-4770-b67b-875968deccc2)

urls.py
![Python Validation for urls.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/84f8ed1b-1510-4407-aed1-1d4bfa569434)

views.py
![Python Validation for views.py](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f3397628-f5fc-40b2-b0f1-754caebf2fe5)
</details>

[Back To Top](#table-of-contents)
_____

## JavaScript
[JShint](https://jshint.com/) was used to validate customised scripts.

<details>
<summary>Screenshots available here</summary>
<br>

**Script in festivals.html**
![JavaScript Validation for script in festivals.html](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/7ef937d7-ad58-4088-8bd0-cab420360fdc)

**Script in edit_festival.html**
![JavaScript Validation for script in edit_festival.html](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3a4de007-9b86-450a-84f4-bb01318ca0e9)

**Modified quantity_input_script.html**
![JavaScript Validation for script in quantity_input_script.html](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/69e0f5d6-43e9-4a96-b7c0-fdf302cb9675)

**Script in bag.html**
![JavaScript Validation for script in bag.html](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/7ab21a2e-3f8b-4b73-b7c0-752a8c659c69)

**Slightly modified stripe_elements.js file**
![JavaScript Validation for stripe_elements.js](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b5cf05f8-59b9-44e2-8001-85e402a12e1f)
</details>

[Back To Top](#table-of-contents)
_____

# Lighthouse
