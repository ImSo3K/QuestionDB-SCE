# QuestionDB-SCE
College Project

# How to install pdf2image
```
pip install pdf2image
```
1. change the following line in pdf2image.py file in your site-packages
```fmt="ppm"``` to ```fmt="png"``` so it will convert to .png file

2. change change the following line in generators.py file in your site-packages
```yield str(uuid4())``` to ```yield str('Question')```

# how to install image2docx

```
pip install python-docx
```
