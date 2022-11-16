# Shellbie

![image](https://user-images.githubusercontent.com/35274771/202136039-a02ce76e-7172-4548-a1e1-6ade58f63736.png)

**Shellbie** is a small program meant to help you get small tasks done quickly and helpfully. It is also meant to be light and easy to run on all major GNU/Linux distributions.

It is a **proof-of-concept** that will serve as the base for a bigger GNU/Linux FOSS assistant I am working on in the background, so expect more basic functionality from this one. 

This is a Python program that can currently: 

- Pull up the news for you from a few different sources that you can select. 
- Pull up the weather for your locale. 

Shellbie aims to be a fun little friend that helps you get stuff done!

> *More functionality will be coming to Shellbie over time.*

### Using Shellbie

When you first download Shellbie, make sure you have everything you need to properly run it by installing its dependencies - and handily, there is a **installer.sh** file right here waiting for you.

Hold up, though, Mr. ExcitedFace - you'll have to make it executable first to be able to run it: 

`chmod +x installer.sh`

Once that's done, just run the new executable script: 

`./installer.sh`

Now that you have all of the dependencies installed, you're ready to run your new assistant. To start the setup process, run: 

`python3 setup.py`

You will be asked a few questions to get setup, including your name, what you'd like to name your assistant, and your location (this is only asked to serve you weather and *is not* saved anywhere outside of your own local machine). 

Once this is done, you're ready to use your new assistant! Jump into the main menu at any time and launch tasks by running: 

`python3 mainMenu.py`

**Enjoy**! Remember, Shellbie is a work in progress, and will see periodic updates with new functionalities.

### Developing For Shellbie

Shellbie is meant to be **extensible**, and it should be simple to add more functionality to our Assistant.

To make it easy to bring extended functionality to some assistant operations, we have created **Libraries** that are imported and used when needed. You can find them in the **/library** folder in the repo. 

If you're wondering how variables saved in the setup are handled, it's pretty simple, too - they get saved into a **variables.py** file that lives in two locations: 

- One in the document root. 
- One in the **/library** folder.

This is to make it simple for the program to be able to reference the variables file no matter which scope it is in - and all of this is done automatically as you answer questions in the **setup.py** process. You don't ever have to touch the **variables.py** file unless you want to edit it. 

### Contributing to Shellbie

Got ideas you'd like to add to Shellbie? Pull requests are always welcome!
