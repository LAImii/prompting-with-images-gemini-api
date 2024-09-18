import os
import json
import PIL.Image
import google.generativeai as genai

HOME = os.getcwd()
images_folder_path = HOME + '\images'

# add google api key
GOOGLE_API_KEY = 'AIzaSyDGzVGPsZfiCdUDwrghl4mWiNllEcVi7Vw'
genai.configure(api_key=GOOGLE_API_KEY)

# Prompting with images
def genAIImages(prompts):
    images = []
    questions = []
    answers = []
    for i in os.listdir(images_folder_path):
        sample_image = PIL.Image.open(images_folder_path + '\\' + i)
        images.append(i)

        for p in prompts:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content([p, sample_image])
            questions.append(p)
            answers.append(response.text)
    
    return images, questions, answers


# Export as text file
def exportTextFile() :
    prompts = [
        "What type of restroom is in this image?",
        "Describe in detail this type of restroom."
        ]
    images, questions, answers = genAIImages(prompts)

    with open("my_file.txt", "w") as file:
        for i in images:
            file.write("\n" + i + "\n")

            for p in range(len(prompts)):
                result = "- " + questions[0] + "\n" + answers[0] + "\n"
                file.write(result)
                del questions[0]
                del answers[0]

# Export as json file
def exportJSONFile():
    prompts = [
        "What type of restroom is in this image?",
        "Describe in detail this type of restroom."
        ]
    images, questions, answers = genAIImages(prompts)
    
    results = []
    for i in range(len(images)):
        data = {}
        data['image'] = images[i]
        result = []

        for p in range(len(prompts)):
            x = {}
            x['prompt'] = questions[0]
            x['response'] = answers[0]
            result.append(x)
            del questions[0]
            del answers[0]
        
        data['result'] = result
        results.append(data)

    with open('my_file.json', 'w') as file:
        json.dump(results, file, indent=4)


exportTextFile()
# exportJSONFile()