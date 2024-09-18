instruction:
1) create a specific folder
2) open terminal in a specific folder
3) paste "git clone https://github.com/LAImii/prompting-with-images-gemini-api.git" on terminal
4) cd .\prompting-with-images-gemini-api\
5) Open an editor such as Visual Studio Code (or typing "code ." in terminal), then open a terminal in that editor.
6) activate virtual environment:
   6.1) typing "py -m venv env" (window) or "python3 -m venv env" (MAC) in terminal
   6.2) "env\Scripts\activate" (window) or "source env/bin/activate" (MAC) for activate env and using library
   **NOTE: If you get a warning that the library cannot be imported, Install the following libraries:
   - pip install pillow
   - pip install -q -U google-generativeai.
8) run api-script.py file
