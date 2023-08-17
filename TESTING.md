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
- [Features Testing](#features-testing)
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

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO.  This was run in Chrome DevTools in incognito mode.

The following are the results for all pages:

| Page | Device | Performance | Accessibility | Best Practice | SEO |
| ---- | ------ | ----------- | ------------- | ------------- | --- |
| Home | desktop  |  72 | 86 | 100 |  100 |
|                               | desktop | 73 | 86 | 100 | 100 |
| Festivals | desktop  |  96 | 83 | 100 |  90 |
|                          | mobile | 73 | 83 | 92 | 92 |
| Festival detail  | desktop  |  75 | 72 | 92 |  100 |
|                          | mobile | 70 | 72 | 92 | 100 |
| Bag    | desktop  |  97 | 71 |  100 |  90 |
|                          | mobile | 80 | 71 |  100 | 89 |
| Checkout       | desktop |  69 | 87 | 100 |  100 |
|                          | mobile |  74 | 87 | 100 | 100 |
| Checkout success     | desktop  |  95 | 83 | 100 | 100 |
|                          | mobile | 77 | 83 | 100 | 100 |
| Contact      | desktop  |  95 | 78 | 100 |  100 |
|                          | mobile |  72 | 86 | 100 | 100 |
| About us       | desktop  |  92 | 78 | 100 |  100 |
|                          | mobile |  81 | 86 | 100 | 100 |
| Newsletter      | desktop  |  93 | 76 | 100 |  100 |
|                          | mobile |  65 | 85 | 100 | 100 |
| Sign in       | desktop  |  96 | 78 | 100 |  100 |
|                          | mobile |  81 | 84 | 92 | 100 |
| Sign up    | desktop  |  98 | 76 | 100 |  100 |
|                          | mobile |  80 | 84 | 100 | 100 |
| Forgot Password?     | desktop |  79 | 84 | 92 |  100 |
|                          | mobile |  99 | 95 | 92 | 100 |
| Sign out      | desktop  |  98 | 76 | 100 |  90 |
|                          | mobile |  86 | 83 | 92 | 92 |
| My Profile       | desktop  |  97 | 77 | 100 | 90 |
|                          | mobile |  75 | 85 | 100 | 92 |
| Management    | desktop  |  96 | 71 | 100 |  90 |
|                          | mobile |  80 | 79 | 100 | 92 |
| Edit Festival      | desktop  |  97 | 60 | 100 |  80 |
|                          | mobile |  76 | 68 | 100 | 83 |

Comments on the results:
* The negative performance results are due to Stripe files and the use of AWS storage.
* As for the negative data on accessibility, I would like to improve it when I have time, using the indications and suggestions of Lighthouse.

[Back To Top](#table-of-contents)
_____

# Responsiveness

The website was tested extensively on Chrome dev tools for responsiveness.  All pages are fully responsive on screens with widths between 320px and 2560px. Friends and family tested the website on their devices and all reported no issues with responsiveness.


<details>

<summary>Screenshots of the website at different screen sizes.</summary>

**Home**

        Mobile 320px
 ![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/9f0eb830-882b-4a46-928f-23d39527e9e1)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/2ee38b03-11c3-46e6-b5c9-eb01b3c230ef)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f053ea50-ff10-4998-8fd7-0255542cbe51)

**Festivals**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/21ef3dec-9c80-4b22-88d6-85f5010cb0e8)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/44d3d335-8fb7-46c6-88fd-31b465b8a41c)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/4512dc26-31fb-4e6c-a004-6fec1b440b71)


**Festival detail**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c54c5ca7-40a6-4a4e-896f-d9975939a6cb)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3323e719-4d4e-4c16-b6da-70c544646a56)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/52e9caeb-c92a-48a1-abea-2492534a0af1)

**Bag**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/5e9adb71-fe1d-440b-9b05-4c3ea022eaed)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/62d2c434-eaf8-4f47-8e81-1f8a523b8ca3)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b3cbafbb-7988-4bc8-9110-fb6d623f75ee)


**Checkout**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/ba116c8e-241b-409b-942b-77035ba05814)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/28b6ce46-1193-45fa-8400-955af16a7972)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/7317b585-8e97-4d47-9ed4-f0dacbf9e1c0)


**Checkout success**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/46906b48-671c-4dde-8ad5-831e74a0f150)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/880b5633-50b3-4c46-a8c1-a5810d56b347)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/03290988-6e25-4784-a884-60bdd6239cd0)


**Contact**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/77e49781-649c-48c1-b639-8eba3fe595b2)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/1fa47eff-1bb9-4f71-bea0-5b7535a9269f)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/dbbdbcb4-f2c7-4e32-bf37-f88d6992a1dd)


**About us**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f3d05d37-cf10-48ae-ab6a-96476ea6d815)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/32b15075-cbdb-42c5-b94a-5402456d5c75)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/9c4a37bc-5729-4ce8-b661-593c5f988ccc)


**Newsletter**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/1fbc45c6-2f72-47a4-9f1e-6aea720f2433)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/657cd76b-1e21-409d-baa6-8eb3a29b3a07)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/b538e046-e51a-454d-83d9-965fd7ca704d)


**Login**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/64967fbd-9e78-4fd8-86a9-10c5a2bec557)


        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f53ed6d5-58ec-4661-9be6-bbfcdcd9b39f)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c780c5ff-0c8f-4574-8c6b-9c71c77231b5)


**Sign up**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/98edd135-0769-4f4f-8d45-fb52ab58853f)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/297af31b-eea3-4532-98b2-6cc089bcfd6d)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/8ad3fab0-dad7-4174-9b7a-252a04c42cbb)


**Forgot password**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/521eb76e-a205-4186-a4e1-9c78d872519b)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/751aafce-ba21-4c7a-8b9d-6fec7726c4ba)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/dc55a045-bd13-4103-b36b-c1bade1a3d2f)

**Sign out**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/34a82c06-4e35-4f02-8e4c-9d9246ab0fb4)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/6cacffad-be8b-4894-8a37-f96e50dc61c6)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/c0170e3b-b855-4249-9ed9-5473790c66b2)

**My profile**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/857e0db0-cdd8-4368-8d61-4de9dd57e7e7)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/58ecf67a-2e17-4a08-a32b-a260312b7397)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/23cf24bf-f937-49a1-8472-1718e0f469d1)


**Management**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/6661b264-500a-4c4b-be53-fcd1e245ebc1)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/d28739d7-d9a4-4013-a314-7e781f7ecf7d)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/3f9f947f-29e9-4f7e-982b-21d8a83b21df)


**Edit festival**

        Mobile 320px
![Mobile 320px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/39ca67bc-2fb3-4ee1-a9b3-cffdd73f0e37)

        Tablet 768px
![Tablet 768px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/f2ebffd7-058f-43e9-a0f8-ed599b021348)

        Desktop 1200px
![Desktop 1200px](https://github.com/BohdanBezushka/wherearewegoing/assets/94321555/89f53b94-e1eb-400e-a7d6-717fb593a5e1)
</details>

[Back To Top](#table-of-contents)

_____

# Browser Compatibility

The website was tested on current Chrome, Firefox, Edge and Brave for compatibility.

| Intended      | Chrome    | Firefox   | Edge  | Brave     |
|---------------|-----------|-----------|-------|-----------|
| Appearance    | Good      | Good      | Good  | Good      |
| Responsiveness| Good      | Good      | Good  | Good      |

[Back To Top](#table-of-contents)

_____

# User Stories

Each [User Story](https://github.com/BohdanBezushka/wherearewegoing/issues) has been manually tested and the results have been collected in the tables below.

<details>
<summary>User Story:</summary>

* USER STORY: View a list of festivals [#2](https://github.com/BohdanBezushka/wherearewegoing/issues/2)

As a user, I can view a list of all available festivals for purchase so that I can explore and choose the ones that interest me.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| View a list of all festivals. | Achieved | |
| View festival name. | Achieved | |
| View price. | Achieved | |
| View dates. | Achieved | |

* USER STORY: View individual festivals [#3](https://github.com/BohdanBezushka/wherearewegoing/issues/3)

As a user, I can view individual information for each festival so that I can access detailed information about each event.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Each festival has its own webpage with informative content. | Achieved | |
| Each festival has its link to the official festival website. | Achieved | |

* USER STORY: Buy tickets [#4](https://github.com/BohdanBezushka/wherearewegoing/issues/4)

As a user, I can purchase tickets for any desired festival so that I can attend the festival of my choice.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can see the tickets in the shopping bag. | Achieved | |

* USER STORY: Preferences [#5](https://github.com/BohdanBezushka/wherearewegoing/issues/5)

As a user, I can sort festivals by date, country, and price so that I can easily find and select festivals based on my preferences.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can view festivals according to date.| Achieved | |
| The user can view festivals according to country. | Achieved | | 
| The user can view festivals according to price. | Achieved | | 
 
* USER STORY: Search bar. [#6](https://github.com/BohdanBezushka/wherearewegoing/issues/6)

As a user, I can search for a specific festival using the search bar so that I can quickly find and access the desired festival.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The search bar functions properly, providing optimal results to the user.| Achieved | |
 
* USER STORY: Add a form prior to purchasing. [#7](https://github.com/BohdanBezushka/wherearewegoing/issues/7)

As a user, I can enter my first name, last name, phone number, ID, and email address so that I have my tickets assigned to my account, providing the benefit of personalized ticket management.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user must provide their personal information before purchasing the tickets.| Achieved | |
 
* USER STORY: Stripe payment [#8](https://github.com/BohdanBezushka/wherearewegoing/issues/8)

As a user, I can add my credit card to purchase the tickets so that I can securely and conveniently complete the transaction.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Stripe payment works correctly.| Achieved | |

 * USER STORY: History orders [#9](https://github.com/BohdanBezushka/wherearewegoing/issues/9)

As a user, I can view a record of my purchases so that I can keep track of my transactions and have a history of my past orders.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User views history orders.| Achieved | |
| User views total expenses.| Achieved | |

 * USER STORY: Tickets by email [#10](https://github.com/BohdanBezushka/wherearewegoing/issues/10)

As a user, I receive a message with the tickets to download so that I can have a digital copy of my tickets for easy access.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| When the customer has made a payment, they receive a message with the purchased tickets.|No Achieved | |

 * USER STORY: Responsive design  [#11](https://github.com/BohdanBezushka/wherearewegoing/issues/11)

As a user, I can use the application on any device so that I can access it from anywhere.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The application functions properly on any device.| Achieved | |

 * USER STORY: Idea of the website #12  [#12](https://github.com/BohdanBezushka/wherearewegoing/issues/12)

As a user, I can get an idea of the website's layout and design so that I can have a visual understanding of how the website looks and functions.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The website has a simple and descriptive style.| Achieved | |


 * USER STORY: Easy registration  [#13](https://github.com/BohdanBezushka/wherearewegoing/issues/13)

As a user, I can create a personal account to view my profile so that I can access personalized features and manage my information effectively.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can easily create an account.| Achieved | |


 * USER STORY: Easy login and out [#14](https://github.com/BohdanBezushka/wherearewegoing/issues/14)

As a user, I can easily log in and log out so that I can access my account securely and manage my personal information effectively

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can log in and log out easily.| Achieved | |


 * USER STORY: Recover password [#15](https://github.com/BohdanBezushka/wherearewegoing/issues/15)

As a user, I can recover my password in case I forget it so that I can regain access to my account and continue using the platform without any interruptions.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user recovers their account via email.| Achieved | |
| The user can enter a new password.| Achieved | |

 * USER STORY: Verify email [#16](https://github.com/BohdanBezushka/wherearewegoing/issues/16)

As a user, I want to receive an email to verify my new account so that I can ensure the security and legitimacy of my account registration.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user receives a registration verification email.| Achieved | |
| The user can use the account after verifying it through email.| Achieved | |


 * USER STORY: Different ways to create an account [#17](https://github.com/BohdanBezushka/wherearewegoing/issues/17)

As a user, I want to be able to register in different ways so that I can have flexibility and convenience in creating my account.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can register using their Google account or phone number.| No achieved | |

 * USER STORY: Customer support [#18](https://github.com/BohdanBezushka/wherearewegoing/issues/18)

As a user, I have a dedicated section where I can communicate with customer support for any issues or questions so that I can receive timely assistance and have my concerns addressed effectively.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The user can communicate with the support team at any time.| Achieved | |


 * USER STORY: Admin panel [#19](https://github.com/BohdanBezushka/wherearewegoing/issues/19)

As an owner, I can view all available events from the admin panel so that I can effectively manage and monitor the event listings.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The owner can view a list of all festivals.| Achieved | |

 * USER STORY: Add, delete and modify event [#20](https://github.com/BohdanBezushka/wherearewegoing/issues/19)

As an owner, I can add, modify, and delete an event from the admin panel so that I can effectively manage and update the event information as needed, ensuring accurate and up-to-date listings.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The owner can add a festival.| Achieved | |
| The owner can modify a festival.| Achieved | |
| The owner can delete a festival.| Achieved | |


 * DEVELOPER TASK: Marketing [#21](https://github.com/BohdanBezushka/wherearewegoing/issues/21)

Create the files and meta tags to improve the website's search engine optimization (SEO)

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I have the robots.txt file.| Achieved | |
| I have the sitemap.xml file.| Achieved | |
| I have the meta tags.| Achieved | |


 * USER STORY: Social Media [#22](https://github.com/BohdanBezushka/wherearewegoing/issues/22)

As an owner, I can leverage my social media presence to create a strong brand in the market so that I can increase brand visibility, engage with customers, and ultimately grow my business.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The website has an Instagram account.| Achieved | |
| The website has a Facebook account.|No achieved | I didn't have enough time |


 * DEVELOPER TASK: 404 error page. [#23](https://github.com/BohdanBezushka/wherearewegoing/issues/23)

Create a custom 404 error page.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| When an error occurs, the 404 error page appears.| Achieved | |


 * DEVELOPER TASK: README.md [#24](https://github.com/BohdanBezushka/wherearewegoing/issues/24)

Write the README file with all the project details.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The README file includes all the sections from the previous project and a new section on Marketing.| Achieved | |

</details>

[Back To Top](#table-of-contents)
_____

## Features Testing

Each feature listed in the [README.md](README.md) file has been manually tested on the browsers listed in [Browser Compatibility Testing](#browser-compatibility) and the results are listed in the tables below.

<details>
<summary>Header & Navigation</summary>
<br>

**Top Navigation**

*Unregistered / Not logged in user*

| Feature | Action | Effect |
|------------|----------|---------|
| Logo	| hover over	 | address shows as home 	|
|	| click/tap	 | directs to Home |
| Search icon on mobile	 | tap		|  colour changes, search field opens below |
| Search bar	| click/tap  text input	| gets focus and prompt for text |
|		| type & enter		| directs to Shop Page with query |
|		| enter only		| directs to Shop Page all festivals |
| Search icon on desktop| click		| directs to Shop Page all festivals |
| Account icon|click/tap	| drops down Register, Login links |
| Register link	| click / tap	| directs to Registration Page |
| Login link| click / tap	| directs to Login Page |
|Basket Icon on mobile | tap 	| drops down basket total link |
|Basket total link	|tap	| directs to Shopping Basket |
|Basket Icon on desktop | hover over | address changes to basket |
|			| click / tap    | directs to Shopping Basket Page |

All Tests Passed

<br>

*Registered / Logged in user*

| Feature | Action | Effect |
|------------|----------|---------|
| My Profile link	| hover over	|  address shows as profile |
|		| click / tap	| directs to user’s Profile Page |
| Logout link	| hover over 	| address shows as logout |
|		| click / tap	| directs to Log Out Page |

All Tests Passed

<br>

**Main Navigation**

| Feature | Action | Effect |
|------------|----------|---------|
| Hamburger button on mobile | tap | toggles down menu |
| Home link	| hover over	| address shows as home |
|		| click / tap 	| directs to Home|
|Festivals link	|hover over	| address shows # |
|		| click / tap	| drops down menu with more links |
| Contact link	| hover over	| address shows contact |
|		| click / tap	| directs to Contact Page |
| More link	| hover over	| address shows more |
|		| click / tap	| drops down menu with more links |

All Tests Passed

<br>
</details>

<details>
<summary>Footer</summary>
<br>

| Feature | Action | Effect |
|------------|----------|---------|
| Website logo	            | hover over                | address shows home |
|		                    | click / tap               | directs to Home |
| Festival link            | hover over                | displays a button and changes colour of the letters, address shows festival |
|		                    | click / tap               | directs to Festivals|
| About us link            | hover over                |displays a button and changes the colour of the letters, address shows About us |
|		                    | click / tap               | directs to About us|
| Newsletter us link            | hover over                |displays a button and changes colour of the letters, address shows Newsletter |
|		                    | click / tap               | directs to Newsletter|
| Contact us link            | hover over                |displays a button and changes colour of the letters, address shows Contact |
|		                    | click / tap               | directs to Contact|
| Privacy Policy link            | hover over                |displays a button and changes colour of the letters, address shows Privacy Policy |
|		                    | click / tap               | a new page opens with the privacy policy|
| Facebook link            | hover over                |displays a button and changes colour of the letters, address shows url |
|		                    | click / tap               | a new page opens with the Facebook page|
| Instagram link            | hover over                |displays a button and changes colour of the letters, address shows url |
|		                    | click / tap               | a new page opens with the Instagram page|
| Twitter link            | hover over                |displays a button and changes colour of the letters, address shows url |
|		                    | click / tap               | a new page opens with the Twitter page|
| Github link            | hover over                |displays a button and changes colour of the letters, address shows url |
|		                    | click / tap               | a new page opens with the Github page|
| Linkedin link            | hover over                |displays a button and changes colour of the letters, address shows url |
|		                    | click / tap               | a new page opens with the Linkedin page|

All Tests Passed

<br>
</details>

<details>
<summary>Home Content</summary>
<br>

| Feature | Action | Effect |
|------------|----------|---------|
| Festival Ticktes button 	| hover over	| changes colour of border, address shows festivals |
|			| click / tap	| directs to Festivals Page |

All Tests Passed

<br>
</details>


<details>
<summary>All Festivals</summary>
<br>

<br>

**Sort-Selector**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Sort-selector box	| click / tap 	| drops down a list of sort choices |
| Name (A – Z)		| click / tap / enter |Sorts festivals by name alphabetical order |
| Name (Z – A)		| click / tap / enter |Sorts festivals by name reverse alphabetical |
| Date (Soon – Late)		| click / tap / enter |Sorts festivals by soon order |
| Date (Late – Soon)		| click / tap / enter |Sorts festivals by late order |
| Location	(A – Z)	| click / tap / enter |Sorts festivals by location alphabetical order |
| Location	(Z – A)	| click / tap / enter |Sorts festivals by location reverse alphabetical |
| Price (low to high)	| click / tap / enter |Sorts festivals by price ascending |
| Price (high to low) 	| click / tap / enter |Sorts festivals by price descending |

<br>

**Festival Cards**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Festival image	| hover over	| address shows shop/festival id |
|			| click / tap	| directs to Festival Detail Page |
|Name			| view		| displays festival name	|
|Date		| view		| displays festival date	|
|Location		| view		| displays festival location	|
|Price			| view		| displays festival price		|
|Button up		| click / tap		| goes up		|

All Tests Passed

<br>
</details> 


<details>
<summary>Festival Detail</summary>
<br>

**Festival Detail Section**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Product image 	| hover over 	| address shows s3.amazonaws.com/media/<image file name>.jpg |
| 	| click / tap	| directs to full page image file |
| Festival name link 	| hover over 	| address shows url |
| 	| click / tap	| a new page opens with the url page |
| Festival info | view	| shows description, date, location and price |
| Quantity Selector (-) 	| default view	| lighter in colour than the (+) selector |
|			| hover over | colour changes, tooltip “Decrease Quantity” |
|	| click / tap	| no effect |
| Quantity Selector (+) 	| default view	| darker in colour than the (-) selector |
|			| hover over | colour changes, tooltip “Increase Quantity” |
|	| click / tap	| quantity in input box is incremented |
| Input field	| type non digits	| no effect |
|		| type digits		| displays digits |
|		| leave blank		| no effect |
| Add to Bag button	| hover over 	| change colour border |
|	| click / tap	| if quantity is valid, success message is triggered and festival + quantity are added to bag|
|	|		|if quantity is invalid, error message is triggered | 
| Keep shopping button	| hover over 	| changes colour border, address shows festivals url |
|	| click / tap	| directs back to festivals page |

All Tests Passed

<br>
</details> 

<details>
<summary>Bag</summary>
<br>

The Basket Page can be accessed via the basket icon on the top navigation bar as well as by the button that appears in the toast after adding a product to the bag.

**Empty Bag** 

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Text	| view	| Your bag is empty. |
| Keep shopping button	| hover over 	| changes colour border, address shows festivals url |

All Tests Passed

<br>

**Festivals in Bag**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| (-) button	| hover over	| changes colour |
|		| click / tap	| decrements quantity in input field |
| (+) button	| hover over 	| changes colour |
|		| click / tap	| increments quantity in input field |
| Update button | hover over 	| changes colour border |
| 		| click / tap	| festival quantity updated, totals change depending on the quantity, success toast displays updated festival & bag summary |
| Remove button | hover over	| changes colour border |
| 		| click / tap 	| festival removed, totals change, success toast displays updated festival & bag summary |
| Keep Shopping button | hover over | changes colour border, address shows shop |
|			| click / tap | directs to Shop / All Festivals Page |
| Secure Checkout button | hover over | changes colour border, address shows checkout |
|		| click / tap | directs to Checkout Page |

All Tests Passed
<br>
</details>

<details>
<summary>Checkout</summary>
<br>

**Checkout Page**

*Registered / Logged in Users*

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Form Validation | submit form with required fields left blank | tooltip directs user to fill in required field |
| Save info box 	| Tick and check profile info after checkout | profile details populated with correct info |
| Payment field | Enter invalid card no | text goes red, error message below “x your card number is invalid” | 
| Adjust Bag button | hover over | changes colour border, address shows basket |
|	| click / tap	| directs to Bag Page |
| Complete Order button | hover over | changes colour border |
|			| click / tap | if form is valid  directs to black overlay with white spinner then Checkout Success Page |  

All Tests Passed

<br>

*Unregistered / Not logged in Users*

This table tests two links that are available for unregistered guests instead of the Save Info box in the previous table.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Create an account link | hover over | gets underline, address shows accounts/signup |
|			| click / tap | directs to Register Page |
| Login to save information link | hover over | gets underline, address shows accounts/login |
|			| click / tap | directs to Login Page |

All Tests Passed

<br>

**Checkout Success Page**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
|Success Toast 	| View		| displays just below the navbar, including order no. & email address|
|Order Confirmation Information | view | displays festival names, quantity, totals, delivery info & email address | 
| Keep watching festivals! button | hover over | changes colour border |
|		| click / tap | directs to Festival Shop Page |

All Tests Passed

<br>
</details>


<details>
<summary>Profile</summary>
<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Form 		| Fill in | Form is filled in with user’s default delivery info |
| Update information button | hover over | change colour border |
|			| click / tap | Toast Success Profile updated successfully |
| Order history | hover over | displays full order number |
|	| click / tap | directs to order history detail, toast alert notifies user that this is a past confirmation for order number … |
| Back to Profile button | hover over | changes colour border, address shows profile |
|	| click / tap | directs to Profile Page |

All Tests Passed

<br>
</details>

<details>
<summary>Registration & Authentication</summary>
<br>

**Registration Page**

This page can be accessed by a non-logged in user via the My Account icon on the navbar and the Checkout form on the Checkout Page as well as the Login Page.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| sign link	| hover over	| gets underline, address shows accounts/login |
|		|click / tap	| directs to the Login Page |
| Form validation | submit form with required fields left blank | tooltip directs user to fill in required field |
|Back to Login button | hover over | changes colour border, address shows accounts/login |
|		|click/tap	| directs to the sign Page |
|Sign up button	|hover over	|changes colour border	|
|			|click / tap	| directs to Confirm Email Page, alert toast shows user’s email address |

All Tests Passed

<br>

**Confirm Email Page**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
|Instructs the user to check their email to verify Email address | view | user clicks on the link in the email received |
|Confirm Email Page with email URL | view | instructs user to confirm email and username by clicking the Confirm button |
|Confirm button | hover over | changes colour border |
|		| click / tap | directs to Login Page with success alert |

All Tests Passed

<br>

**Login Page**

The Login Page can be accessed by a registered user straight after registration or via the My Account icon in the Top Navigation bar.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| sinn up link| hover over	| gets underline, address shows accounts/signup|
|		|click / tap	| directs to the Registration Page |
| Form validation | submit form with required fields left blank | tooltip directs user to fill in required field |
|		|submit form with wrong information | error message highlighted at the top of the form |
|Remember me checkbox | click / tap | ticks the checkbox |
|Sign in button	|hover over	|changes colour border	|
|			|click / tap	| directs to Home Page, success toast alerts user that they are successfully logged in |
|Forgot Password? Link |hover over | gets underline, address shows accounts/password/reset|
|		| click / tap | directs to Password Reset Page |
| Home button | hover over	|changes colour border, address shows home |
|		| click / tap 	| directs to the Home Page |

All Tests Passed

<br>

**Logout Page**

The Logout Page can be accessed via the My Account icon dropdown on the Top Navigation bar. 

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Cancel button	| hover over	| changes colour border, address shows home |
|		| click / tap 	| directs to Home Page without logging out |
| Logout button	| hover over	| changes colour border |
|		| click / tap	| directs to Home Page logging out user, success toast message |

All Tests Passed

<br>

</details>


<details>
<summary>Contact</summary>

<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Contact info	| view | display contact info | 	
| Return to shop button | hover over | changes colour border, address shows shop |
|		| click / tap | directs to Festival Shop Page |

All Tests Passed

<br>
</details>

<details>
<summary>About us</summary>

<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| About us info	| view | display about us info | 	
| Return to shop button | hover over | changes colour border, address shows shop |
|		| click / tap | directs to Festival Shop Page |

All Tests Passed

<br>
</details>

<details>
<summary>Newsletter</summary>

<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Newsletter form	| submit form with required fields left blank | tooltip directs user to fill in required field |
| Subscribe button | hover over | changes colour |
|		| click / tap | a message appears saying that you have just subscribed |
| Return to shop button | hover over | changes colour border, address shows shop |
|		| click / tap | directs to Festival Shop Page |

All Tests Passed

<br>
</details>

<details>
<summary>Error 404</summary>
<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| To test Error 404 page | type `/test` at the end of url | directed to Error 404 page |
| Return to shop button | hover over | changes colour border, address shows shop |
|		| click / tap | directs to Festival Shop Page |

All Tests Passed

<br>
</details>

[Back To Top](#table-of-contents)

_____

[Back to README.md](README.md)
