[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mMxhKicI)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21456184&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 2: Character Abilities Showcase

## 🎯 Project Overview

Build a simple character system that demonstrates mastery of object-oriented programming fundamentals: inheritance, method overriding, polymorphism, and composition. This project focuses on core OOP concepts without the complexity of a full game system.

## Bonus Creative Features
### All Player subclasses (Warrior, Mage, Rogue) now gain experience points every time they perform an attack or use a special ability:

- Normal attacks give moderate XP
- Special abilities give extra XP
- Every 100 XP automatically increases the player's level
- Level-ups also print a celebratory message

## Also, Player subclasses now have stamina:

- Players start with 100 stamina.
- Each attack brings the stamina down based on the type of attack and the subclass.
- Once the stamina reaches 0, the player can no longer attack the target.

## Ai Usage

I started off by using chatGPT for my bonus creative feature, stamina. To make sure the stamina doesn't go below 0, I started by using an if statement that sets the stamina to 0 if it goes below it. I used chatGPT to find a more efficient way to do this. The results were using 'max'. I also used chatGPT to find the little mistakes that were causing errors and causing the code to not run.

## How to Run
python project2_starter.py
