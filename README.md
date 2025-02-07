s# **📌 FreeCell Card Game – Python Implementation**  

## **📄 Project Overview**  
This project implements the **FreeCell solitaire card game** in Python. The goal of the game is to move all 52 cards to the **four foundation piles** in ascending order, following standard FreeCell rules. The game logic enforces valid moves, detects winning conditions, and provides a **command-based user interface**.  

## **📁 Project Structure**  
```
📂 /                     → Root directory  
│-- 📜 cards.py          → Provided Card & Deck classes (unchanged)  
│-- 📜 freecellStart.py  → Initial game framework (optional)  
│-- 📜 cards.pyc         → Cached compiled file (auto-generated)  
│-- 📜 Project08.backup.pdf → Backup project documentation  
│-- 📜 project08_2.pdf   → Project specification document  
```

## **🛠 Requirements**  
To run this project, you need:  
- **Python 3.x**  
- **A terminal/command prompt** to interact with the game  

## **🚀 How to Play**  
1. Run the game script:  
   ```bash
   python freecellStart.py
   ```  
2. Use the following commands to play:  
   ```
   t2f T F   → Move from Tableau (T) to Foundation (F)  
   t2c T C   → Move from Tableau (T) to Free Cell (C)  
   t2t T1 T2 → Move from Tableau (T1) to Tableau (T2)  
   c2t C T   → Move from Free Cell (C) to Tableau (T)  
   c2f C F   → Move from Free Cell (C) to Foundation (F)  
   h         → Show help menu  
   q         → Quit game  
   ```
3. The game will display the **current board state** after each move.  
4. The game ends when **all 52 cards are moved to the foundations (win)** or **no more moves are possible (lose)**.  

## **📌 Features**  
✔ Implements **valid FreeCell moves** following game rules  
✔ Detects **winning conditions** and displays appropriate messages  
✔ Includes **error handling** for invalid moves and inputs  
✔ Provides **formatted board display** for better readability  

## **📌 Future Improvements**  
- Implement **graphical user interface (GUI)** using **Tkinter or PyGame**  
- Allow **drag-and-drop functionality** instead of text commands  
- Add **AI suggestions** for possible moves  