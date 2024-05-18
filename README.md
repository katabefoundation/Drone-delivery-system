# Drone-delivery-system
The Drone project that integrate the drone and the web application to enhance the delivery of  product from one place to another also to help health service for emergence cases

## Installing the project to your machine you have to configure the following
### 1. Configure Django and the following dependencies
  ## i. Install Python or Python 3 to your machine
       $ sudo apt install python3
 ###  ii. Install Django in your machine
       $ python -m pip install Django
  ### iii. install django rest_framework
       $ pip install djangorestframework
  ### iv.  install Django Corsheaders
       $ pip install django-cors-headers
  ### v.   install djoser
       $ pip install djoser
       
## 2. Install Quasar and configure as follows
  ### download or install node in your machine
      $ sudo apt install node
  ### Navigate to drone_frontend folder
      $ cd drone_frontend
  ### start configuring quasar cli for your project you don't need to configure it globally. Just run the following command to your terminal
  #### Install the dependencies
```bash
yarn
# or
npm install
```

#### Start the app in development mode (hot-code reloading, error reporting, etc.)
    ```bash
    $ quasar dev
    ```


#### Lint the files
    ```bash
    $ yarn lint
    # or
    $ npm run lint
    ```


#### Format the files
    ```bash
    $ yarn format
    # or
    $ npm run format
    ```



### Build the app for production
    ```bash
    $ quasar build
    ```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).
  
