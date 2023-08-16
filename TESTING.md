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


