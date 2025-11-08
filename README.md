
# Mood Checker Application Documentation

This document provides a comprehensive overview of the Mood Checker application's source code. The application consists of two main files: `main.py` and `mood_analyzer.py`.

## 1. `main.py`: The User Interface

This file is responsible for creating the graphical user interface (GUI) of the application using the `tkinter` library.

### 1.1. Key Components

*   **`tkinter`:** The standard Python interface to the Tcl/Tk GUI toolkit. It is used to create the main window, widgets, and handle user interactions.
*   **`ttk`:** The themed widget set for `tkinter`, which provides more modern and customizable widgets.
*   **`mood_analyzer`:** A custom module that contains the logic for analyzing the user's mood based on their input.

### 1.2. Constants

*   **Fonts:** A set of professional fonts are defined for different text elements in the GUI, ensuring a consistent and clean look.
*   **Themes:** The application supports both "dark" and "light" themes. Each theme is a dictionary of color codes for various GUI elements.

### 1.3. Functions

*   **`apply_theme(theme_name)`:** Applies the selected theme to all widgets in the application.
*   **`toggle_theme()`:** Toggles between the "dark" and "light" themes.
*   **`check_mood(event=None)`:** Retrieves the user's input, calls the `analyze_mood` function from the `mood_analyzer` module, and updates the GUI with the detected mood and a corresponding message.
*   **`show_exit_screen()`:** Displays a thank you message and closes the application.
*   **`custom_ask_name()`:** Creates a custom dialog to ask for the user's name at the beginning of the application.

### 1.4. GUI Setup

*   **Main Window:** The main window is created using `tk.Tk()` and configured with a title, initial size, and minimum size.
*   **Window Centering and Maximizing:** The window is centered on the screen and maximized using a combination of `root.state('zoomed')` and `root.eval('tk::PlaceWindow . center')`.
*   **Widgets:** The GUI is built with various widgets, including labels, a text input area, buttons, and a main frame to hold them all.
*   **Styling:** The `ttk.Style` class is used to configure the appearance of the widgets.

## 2. `mood_analyzer.py`: The Mood Analysis Logic

This file contains the core logic for analyzing the user's mood from a given text.

### 2.1. Key Components

*   **`re`:** The regular expression module, used for finding whole word matches in the text.

### 2.2. `analyze_mood(text)` Function

This is the main function of the module. It takes a string of text as input and returns a tuple containing the detected mood and a motivational message.

#### 2.2.1. Keyword Lists

*   **`positive_keywords`:** A list of words that indicate a positive mood.
*   **`negative_keywords`:** A list of words that indicate a negative mood.
*   **`motivational_keywords`:** A list of words that indicate a motivational mood.
*   **`negations`:** A list of words that can negate the meaning of a sentence (e.g., "not", "don't").

#### 2.2.2. Analysis Process

1.  **Text Normalization:** The input text is converted to lowercase.
2.  **Negation Check:** The function checks if any negation words are present in the text.
3.  **Scoring:** The function counts the number of positive and negative keywords in the text and calculates a score.
4.  **Score Adjustment:** If a negation is found, the score is flipped (positive becomes negative).
5.  **Mood Determination:** The mood is determined based on the final score:
    *   `score > 0`: "positive"
    *   `score < 0`: "negative"
    *   `score == 0`: "neutral"
6.  **Motivational Check:** If the mood is "neutral", the function checks for motivational keywords to see if the mood should be "motivational".
7.  **Return Value:** The function returns the detected mood and a corresponding message.
