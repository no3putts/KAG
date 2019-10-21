# KAG (Kubernetes Adventure Game)
## A text based adventure game written in Python  
  
#### Characters from this game are from https://www.cncf.io/phippy-goes-to-the-zoo-book/  
  
#### (WIP)  
  
#### Intro  
  
A simple adventure based on Kubernetes.  

Purpose: *To help learn the python programming language in a fun way*

Being a kubernetes fan and trying Python for the first time, I wrote this game for an assignment in my graduate class in software development.
  
>"Kubernetes can speed up the development process by making easy, automated deployments,  
>updates (rolling-update) and by managing apps and services with almost zero downtime.  
>Kubernetes is originally developed by Google, it is open-sourced since its launch and  
>managed by a very large community of contributors."  
  
- Game uses pickle.py to serialize/deserialize game data  
- Game Info
  * Options: you can change the frequency of Monsters (0-4)
  * Companions have random HP, attack power, and defense value to compliment the hero's own
  * Monsters have random HP, attack power, and dodge value ( no actual dodge % calculated yet)
  * Game data is saved only for the last adventure
    * Monsters fought
    * Trinkets found
    * Resources found
  * Game allows the use of the previous configured hero and companion
    * companion my get a random value for its stats.  Does not retain old one
    * Hero's HP goes back to 100%
  * Game ends when hero's HP reaches to zero or hero is still alive after 10 iterations
  
#### Future Enhancements

- Allow to move in more direction vs just one direction
  * Give the player control over the diretion (N S E W)
- Add weapons that can be picked up
- Add more Hero attributes that can be trained and learned
- Allow to save more than one hero type 
  * Give a choice to load a hero
  * Allow the deletion of speicfied hero
  * Allow hero to specialize in some class
  * Allow hero leveling
 
  
Copyright (c) 2019 Jeremiah Pineda